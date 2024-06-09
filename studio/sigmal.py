"""
[analog to digital]
- map range (-1, 0, +1) to amplitude levels (-dB, +dB)
- 24 bit signed in register ranges (0x80k, 0x00k, 0x7Fk)


[digital to analog]
- require signal generator for (Hz, volt)
- calibrate oscilloscope to channels
- prepare sampler with (0-order hold, frequency, bit depth)
- get quantizer with dithering if possible
"""

class Process:
    """
    (0) Note: We have to seperate the implementation from preparation.
    Preparation is the phase where the computing environment minimizes the distance between just computed state based on information about that state using knowledge about all possible states.
    Implementation is the phase where static information source is converted into dynamical variables according to the description that would be produced for running operations inside that computing environment.

    (1) Each environment is detached via a vector which turns on certain interactions from node | antinode or antinode | node cycles.
    The nodes for each computing environment is those set of variables that could be directly changed while antinodes are the direct image with respect to the local line cutting-off accessibility to those nodes for equal and opposite amplitude.

    (2) Each local line may only logically seperate the memory registers but the global lines must provide physical seperation between possible parallel lines via a serial line containing the gated regions.
    We can setup an uniform and constant velocity waveform for each variable register locations where the addresses map some position on the curve's linear function (wave vector) as denoting nodes under the propagation rule, such that there are at least one other point of contact between every mixed instances of those node positions followed in non-parallel orientation with each subsequent position marking the anti-node whether realized implicitly or explicitly.
    Explicit realization would require the anti-node to be convergent onto some other named register in count where the propagation yields the function of the node variable in terms of functions of those named pointers. But this would have to be managed in a cyclic fashion keeping in effect the garbage collection phases.
    Implicit realization would be when any subsequent possible anti-node functions would figure large into some convoluted mixture where the decay would balance the input phases with corresponding possible output phases.

    
    """
    registers = [] # hex-valued memory locations
    waves = [] # distributions stored as mono files
    names = [] # aliases for intermediate dense states
    functions = [] # code for measuring the dense snapshots for particular variable named
    positions = [] # locations within the dense picture with vector connecting to the functional images


    def state(cls, name, distribution, functional, pattern, callback):
        """
        Creates a register for the named endpoint.

        Args:
            - name : string valued label
            - distribution : waveform active in the environment
            - functional : object that maps named entities to register values
            - pattern : chunk of framed volume that exists in relation to the process endpoints
            - callback : if backward, calls that function with the image anti-node.
        Returns:
            - register : hex valued object address that is serialized.
        """
        pass

    """
    (0) Creating memory locations.
    Memory addresses can be physical with hardware level descriptions.
    It can also be overlayed (see union) where a set of possible labels occupy one of two more volumes with the highest line containing the named function.

    (1) The difference is in declaring static memory endpoints vs acquiring information from variable linked locations.
    A waveform can be recorded onto a set of linearly connected registered locations.
    Those registers will store the amplitude values and the registers get connected in an ordered pattern.
    Retrieving those amplitude points amount to connecting the GET/READ/TRANSFER/WRITE/SET/FLAG instructions so that for a given map of possible locations, the executed code produces the content as expected.

    """
    

    
