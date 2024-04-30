
stream:
- input/core
- core/output

core:
- channel/clock
- clock/channel

clock:
- global/local
- local/global


channel:
- address/voltage/current
- current/addeess/voltage


copies = Record()

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