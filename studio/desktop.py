from functional import compute, construct, prepare, measure
from tools import icons, folders, records

k = icons.get_memory()
j = folders.get_record()
i = records.get_history()

a, b, c, d = compute(k), construct(i), prepare(j), measure(".")

###### INTERFACE ######
last_seen = []
recent_visit = []
all_visits = []
all_scenes = []
###### DASHBOARD ######
phases = []
optimizations = []
loops = []
solved = []


#### MAIN ####
primary = "This is a list of things that will be changed and designed for"
secondary = "This is a list of things that will not be directly addressed here"


### PRIMARY ###
"""
Sending signals from python to room and controlling what gets sent.
Controlling what should be played and how based on some minimum consistency criteria.
Keeping track of what functional effect an event had in order to refine strategies.
Define corner cases and control laws.

tags : control theory, signal generation, policy optimization, constrained optimization, reward maximization and regret minimization.
"""

### Secondary ###
"""
Interfacing with the environment objects and collecting feedbacks.
Connecting external signaling from environment to python in a meaningful way.
Finding strategies for detecting and classifying which latent effect caused current changes.
"""



class Primary:
  modules = {
      buffer : "structure for storing systematic volumes",
      memory : "structure for managing reversible processes",
    }
    """
    **algorithm**
    -1. prepare a buffer for getting new observations
    -0. store observations into memory to create experience replay
    +0. using current state, recall previous experience similar to current observation
    +1. given current state and fetched experience replay, solve for empty buffer or preferred buffer
    
    **buffer**
    - requires type of buffer
    - requires one or more samplers
    - requires fixed length

    Buffer is a list with data points.
    These data points are relative to the environment attached.
    When in that environment, these buffers are selected as possible candidates.
    Candidates are ranked based on some continuity critetia.
    Memories are created!

    **memory**
    - requires a handler
    - requires a pointer
    - must not be independently specifiable

    Memory is what creates actions or changes.
    Given the necessary control endpoints, they have associated memory to their functionals.
    Environment does not directly encode any control behavior.
    Patterns of memory with natural computability of the functions cause actions to be recorded.
    In the process, any functional image is realized and propagated forward with its relative activation impulses.

    Example:

    Load parallel channels.
    Prepare position and control endpoints.
    Process observable and manage memories.
    Dispatch messages across all neighbors.
    Compute all experience-replay profiles.
    """
    checkpoints = []

    def pack(cls, self): pass
    def unpack(self, cls): pass




class Control(Primary):
    """
    Control endpoint.

    **control**
    It is an interface.
    For given set of attributes, the control "controls" some measurable property.
    Measurable property is associated with control policies.

    - send command with valid name
    - include subcommands if serially engaged
    - run command and assert some change
    - measure change given the executive actions.
    - retain names with new controls.

    """
    def __init__(self, name):
        super(Control, self).__init__(name)
        self.commands = [] # value
        self.attributes = [] # query
        self.observables = [] # key
        self.connections = {} # attention

    def set_connection(self, query, key, value):
        # setup attention vector in connections
        left = ((query @ key.T) / len(self.connections)**0.5)
        right = left @ value
        self.connections[left] = right
        self.connections[right] = -left

def softmax(x, k):
    y = [exp(x[i]) / sum([exp(x[j]) for j in range(1, k)])] for i in range(len(x))
    return y


class Policy(Primary):
    """
    What if we serialize the state at a given time and set the code to be key in an attention map?
    From future state, the new deserialized code could be made to query into its past state so that the transformation yields the present state?


    Create a class called Stereo.
    Set static method that packs an instance state into class checkpoints.
    Set instance method that unpacks a checkpoint into instance state.

    Label any two subsequent changes with (left, right) phases.
    """
    class Stereo:
        checkpoints = []

        @classmethod
        def from_left(cls, self):
            # pickle the state into checkpoints.
        def from_right(self, cls):
            # unpickle the checkpoint into state.



functions = []
commands = []
ids = []
flags = []

def create_control(function, number, name, callback):
    functions.append(function)
    ids.append(number)
    commands.append(name)
    flags.append(callback)





class Primary(Primary):
    """
    There are left ~ center and center ~ right in a single cycle.
    System is solved for all center that remain constant throughout cyclic processes.

    (phase -1) : last computed state (center | left -> right | center' | -> left'| right'')
    (phase -0) : local minimum
    (phase +0) : local maximum
    (phase +1) : last measured state (center' | left' -> right | center'' -> left'' | right')
    
    Initialize with random parameters and solve for a central limit.
    From central limit points, prepare left and right tracks.
    For any change in the mid-side matrix, compute the new limit points.
    Create checkpoints if limit points not under the curve so that solution converges to -right distribution of the top-most track or balance the spread around central limits.

    **Gradient**
    (stereo) <left ||.|| right>
    
    (mid) (1/2 * |left>) + (1/2 * |right>)
    (side) (1/2 * |left>) - (1/2 * |right>)

    mid + side ~ |left> + |0>
    mid - side ~ |0> + |right>

    For every iteration in cycle:
    1. Compute mid-side from left-right channels
    2. Measure the gradient of the ms matrix with respect to the lr matrix
    3. Prepare the ms parameters for epsilon in limit
    4. Construct a checkpoint from lr -> ms <- rl

    From checkpoint in current cycle:
    1. Unpack the ms and measure rl dist
    ..
    4. Pack the checkpoint for rl -> ms <- lr
    """
    def prepare_batch(source, length):
        # Create N batches of length from source
        pass

    def embed_sequence(frame, device):
        # take the input dimensions of the device
        # create embedding from current device state
        # return the embedded sequence as query vector

    def get_response(device, query):
        # use the device's attention vector from query
        # store the value with the key set as query
        # set key to be value and value to be linear transform
        # return the linear self-attention

    def build_link(sent, medium, received):
        # query : sent
        # key : medium
        # value : received
        # create an attention register
        
    def solve(solution, epsilon):
        # unpack the solution checkpoint
        # use softmax((query @ key.T) / (len(Q)**0.5)) @ value
        # output is attention scores
        # sum the scores and epsilon
        # update the parameters

"""
Embedding:
- bytes to integers
- integers to amplitudes
- amplitudes to integers
- integers to bytes


"""
