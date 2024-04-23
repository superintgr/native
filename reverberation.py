"""Feedback Delay Loop

    input -> {+} --> [delay] ---> (•) ----> output
              ^                    |
              | <-- /decay gain/ --|


**Single Channel Feedback**

- delay (ms)
- decay (gain)

-- delay samples (int)
-- class Delay -> (delay)
       configure(sample rate) -> (void)
       --- delay samples = delay * 0.001 * sample rate
       --- delay.resize(delay samples + 1)
       --- delay.reset() # start with all zeros
    
       process(input) -> (delay)
       --- delayed = delay.read(delay samples)
       --- sum = input + delayed * decay
       --- delay.write(sum)
"""

class Reverb:
    def __init__(self, block_size, sample_rate, module_name):
        self.device = Convolution(block_size, sample_rate, module_name)
    
    def update_parameters(self, dry, wet, ratio):
        self.device.apply_parameters(dry, wet, ratio)

    def forward(self, impulse):
        response = self.device.process_block(impulse)
        return response
