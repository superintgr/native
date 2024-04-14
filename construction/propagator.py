"""The Propagator Idea

- Independent Stateless Machines
- Connecting Stateful Cells
"""

# Information variable is a function of monotonic process.
core = object
# Cells are independent with respect to only a range that all information variable can take.
flux = object
# Machines are those that compose cells to build computable numbers.
saturation, curve = object, object

class Propagator:
    """All Connections Explicit

    - expression: bottom up tree that meets back at node endpoints (anti-node)
    - monotone: conserved quantities upon instantiation
    """
    base : local
    status : not(Propagator)

# Truth-maintanence system

# Locally consistent window

# Reversible base


"""configuration of static variables (EDSAC?)
# [initial order] (N words)

# declare dependent memory (patterns of bits)

# uniselector, loader, automator, state

# dynamic stack, pointers, levels, state

# prepared for i, loader address, memory at j, assert pointer

# load K to state, assert j from i, compute pointer K in N

# relative addresses, relocation of pointers, bootstrap
"""


# hold a cell for T starting at t
# single core transfer loop
# returned ptr to cell after t at t' < T
# store a cell for X starting at t'
# single core transform loop
# returned ptr to cell after t' at t < X

sequencer = {
    "env" : "assembly",
    "workspace" : "local",
    "field" : "global",
    "project" : "gemini"
}

# using assembly.py as code set workspace to the local path .
# use the global variable to process the buffer
# direct the difference to the host of gemini.py

config = {
    "language" : "C",
    "type" : "propagator",
    "cell" : "compiler",
    "memory" : "disk",
    "static" : "named-other-gradient-name-state",
    "dynamic" : "-name-gradient-other-named--state",
    "state" : "interpreter-core"
}
