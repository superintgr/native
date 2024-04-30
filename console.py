import sounddevice as device

config = {"device" : "UMC204HD", "channels" : [2, 4], "samplerate" : 192000, "dtype" : ['int24', 'int24']}

stream = device.RawStream(config)
stream.start()

runtime = {"start" : stream.time, "end" : None}

def send_message(source):
    return stream.write(source)
    
def check_message(counts):
    return stream.read(counts)

def sample_processor(data):
    """Buffer object processor
    
    RawStream would return a plain-python buffer object as contiguous C type array.
    This C struct-type points to some dynamical memory containing the observables, however it gets replaced by the next step.
    The byte-string could be turned into a list containing integers values or processed via custom encoding/decoding schemes.
    
    The data will have the following properties:
    - it has a fixed length
    -- each byte valued sample corresponds to sampler configuration (sample size)
    --- finite number of byte variables tokens
    ---- sequence of the series encodes order of arrival
    
    We would like to accomplish the following:
    ---- have a mechanism for dynamically managing the interpretration algorithm
    --- the chunks shall be defined and labeled in terms of each others information carrying capacity
    -- the energy is preserved throughout so that adjustment at decoding context could retroactively reflect their encoding patterns
    - the multichannel attribute of the data should be taken into consideration in transporting their information contents
    """



with open(address[outer], frequency) as stereo:
    state = stereo.pullback(k)
    
    expectation = calculate_value(last_state, state)
    preparation = forward(expectation)

    with open(address[inner], frequency) as mid:
        side = mid.feedforward(preparation)
        
    master = stereo.feedforward(side)
    copies.push(master)

    
    
From the device channels, we read the state of the specific substrate (channel) with the specified sampling parameters (frequency, resolution)
- With context manager registered for the substrate measurement event, we collect the top-k frames from the associated memory region
-- The address space for the generic device sampling data is defined to have two levels (#outer and #inner) and using the outer level addressing at first
--- From the outer energy state, we calculate the expectation value using the last unity solution
---- The expectation value from the apparent quantity is prepared to be processed further
----- Start a new context manager session with the addressing space attributed to the inner properties
---- Feedforwarding the prepared data through the inner parameters returns an effective side effect
--- Using the side chained state feedforward the information at the outer substrate level
-- Store the returned output as master copy corresponding to the current state vector position
- Finally, store the checkpoints into a disk or equivalent filing system.