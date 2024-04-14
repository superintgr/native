from metrics import MetricLogger
from wrappers import ResizeObservation, SkipFrame
import torch
import random, numpy as np
from pathlib import Path
from neural import OrioNet
from collections import deque
from scipy.constants import *

"""Geometric Consideration:

Information agent would need to make decisions, take actions, interact with the environment effectively.

- position and velocity of center of mass 
- orientation of the agent
- angular velocity
- external forces
- internal forces

~ state dimensions: position (3) x velocity (3) x orientation (3) x angular velocity (3) --> (12) dimensions 
"""

# Physical Constants
GRAVITY = 9.81  # m/s^2
SPEED_OF_LIGHT = 3.00e8  # m/s
PLANCK_CONSTANT = 6.63e-34  # J*s
AVOGADRO_NUMBER = 6.02e23  # mol^-1

# Mathematical Constants
PI = 3.141592653589793
EULER_NUMBER = 2.718281828459045
GOLDEN_RATIO = 1.618033988749895

# Simulation Parameters
TIME_STEP = 0.01  # s
MAX_SIM_TIME = 1000  # s

# Environment Parameters
ENV_SIZE = (100, 100)  # units
MAX_SPEED = 10  # units/s
TEMPERATURE = 298  # K

# Control Parameters
MAX_THROTTLE = 1.0
MIN_THROTTLE = 0.0
MAX_STEERING_ANGLE = 30  # degrees

class Orio:
    def __init__(self, state_dim, action_dim, save_dir, checkpoint=None):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.memory = deque(maxlen=100000)
        self.batch_size = 32
        self.exploration_rate = 1
        self.exploration_rate_decay = 0.99999975
        self.exploration_rate_min = 0.1
        self.gamma = 0.9
        self.curr_step = 0
        self.burnin = 1e5  # min. experiences before training
        self.learn_every = 3   # no. of experiences between updates to Q_online
        self.sync_every = 1e4   # no. of experiences between Q_target & Q_online sync
        self.save_every = 5e5   # no. of experiences between saving Orio Net
        self.save_dir = save_dir
        self.use_cuda = torch.cuda.is_available()

        # Orio's DNN to predict the most optimal action
        self.net = OrioNet(self.state_dim, self.action_dim).float()
       
        if self.use_cuda:
            self.net = self.net.to(device='cuda')
        else:
            self.net = self.net.to(device='mps')
          
        if checkpoint:
            self.load(checkpoint)

        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=0.00025)
        self.loss_fn = torch.nn.SmoothL1Loss()


    def act(self, state):
        """
        Given a state, choose an epsilon-greedy action and update value of step.

        Inputs:
        - state(LazyFrame): A single observation of the current state, dimension is (state_dim)
        
        Outputs:
        - action_idx (int): An integer representing which action Orio will perform
        """
      
        # EXPLORE
        if np.random.rand() < self.exploration_rate:
            action_idx = np.random.randint(self.action_dim)

        # EXPLOIT
        else:
            state = torch.FloatTensor(state).cuda() if self.use_cuda else torch.FloatTensor(state)
            state = state.unsqueeze(0)
            action_values = self.net(state, model='online')
            action_idx = torch.argmax(action_values, axis=1).item()

        # decrease exploration_rate
        self.exploration_rate *= self.exploration_rate_decay
        self.exploration_rate = max(self.exploration_rate_min, self.exploration_rate)

        # increment step
        self.curr_step += 1
      
        return action_idx

    def cache(self, state, next_state, action, reward, done):
        """
        Store the experience to self.memory (replay buffer)

        Inputs:
        - state (LazyFrame), next_state (LazyFrame), action (int), reward (float), done(bool))
        """
      
        state = torch.FloatTensor(state).cuda() if self.use_cuda else torch.FloatTensor(state)
        next_state = torch.FloatTensor(next_state).cuda() if self.use_cuda else torch.FloatTensor(next_state)
        action = torch.LongTensor([action]).cuda() if self.use_cuda else torch.LongTensor([action])
        reward = torch.DoubleTensor([reward]).cuda() if self.use_cuda else torch.DoubleTensor([reward])
        done = torch.BoolTensor([done]).cuda() if self.use_cuda else torch.BoolTensor([done])
        self.memory.append( (state, next_state, action, reward, done,) )

    def recall(self):
        """
        Retrieve a batch of experiences from memory
        """
        batch = random.sample(self.memory, self.batch_size)
        state, next_state, action, reward, done = map(torch.stack, zip(*batch))
        return state, next_state, action.squeeze(), reward.squeeze(), done.squeeze()

    def td_estimate(self, state, action):
        current_Q = self.net(state, model='online')[np.arange(0, self.batch_size), action] # Q_online(s,a)
        return current_Q

    @torch.no_grad()
    def td_target(self, reward, next_state, done):
        next_state_Q = self.net(next_state, model='online')
        best_action = torch.argmax(next_state_Q, axis=1)
        next_Q = self.net(next_state, model='target')[np.arange(0, self.batch_size), best_action]
        return (reward + (1 - done.float()) * self.gamma * next_Q).float()

    def update_Q_online(self, td_estimate, td_target) :
        loss = self.loss_fn(td_estimate, td_target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()

    def sync_Q_target(self):
        self.net.target.load_state_dict(self.net.online.state_dict())

    def learn(self):
        if self.curr_step % self.sync_every == 0:
            self.sync_Q_target()

        if self.curr_step % self.save_every == 0:
            self.save()

        if self.curr_step < self.burnin:
            return None, None

        if self.curr_step % self.learn_every != 0:
            return None, None

        # Sample from memory
        state, next_state, action, reward, done = self.recall()

        # Get TD Estimate
        td_est = self.td_estimate(state, action)

        # Get TD Target
        td_tgt = self.td_target(reward, next_state, done)

        # Backpropagate loss through Q_online
        loss = self.update_Q_online(td_est, td_tgt)

        return (td_est.mean().item(), loss)

    def save(self):
        save_path = self.save_dir / f"orio_net_{int(self.curr_step // self.save_every)}.chkpt"
        
      torch.save(
            dict(
                model=self.net.state_dict(),
                exploration_rate=self.exploration_rate
            ),
            save_path
        )
        print(f"OrioNet saved to {save_path} at step {self.curr_step}")

    def load(self, load_path):
        if not load_path.exists():
            raise ValueError(f"{load_path} does not exist")

        ckp = torch.load(load_path, map_location=('cuda' if self.use_cuda else 'cpu'))
        exploration_rate = ckp.get('exploration_rate')
        state_dict = ckp.get('model')

        print(f"Loading model at {load_path} with exploration rate {exploration_rate}")
        self.net.load_state_dict(state_dict)
        self.exploration_rate = exploration_rate

env = disk_device.load(version_release)
env = Console(media=env, keys=(["right", ("right", "A")]))
env = SkipFrame(channel=env, skip=4)
env = GrayScaleObservation(channel=env, keep_dim=False)
env = ResizeObservation(channel=env, shape=window_length)
env = TransformObservation(channel=env, f=lambda x: x / 255.)
env = FrameStack(channel=env, num_stack=4)
env.reset()



save_dir = Path('checkpoints') / datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
save_dir.mkdir(parents=True)

checkpoint = Path('checkpoints/2020-10-21T18-25-27/orio.chkpt')
orio = Orio(state_dim=(4, 84, 84), action_dim=env.action_space.n, save_dir=save_dir, checkpoint=checkpoint)
mario.exploration_rate = mario.exploration_rate_min

logger = MetricLogger(save_dir)

episodes = 100

for e in range(episodes):

    state = env.reset()

    while True:

        env.render()

        action = orio.act(state)

        next_state, reward, done, info = env.step(action)

        orio.cache(state, next_state, action, reward, done)

        logger.log_step(reward, None, None)

        state = next_state

        if done or info['flag_get']:
            break

    logger.log_episode()

    if e % 20 == 0:
        logger.record(
            episode=e,
            epsilon=mario.exploration_rate,
            step=orio.curr_step
        )
