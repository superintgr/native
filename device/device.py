import sounddevice as sd
import numpy as np
import argparse


class Standing(Wave):
    """
    Standing wave development.
    - pockets of spatial structures inside a room
    - impose boundaries that dictate wavelength
    - resulting standing wave can only form for boundary condition constructors

    - node positions have the constant zero amplitude
    - confinement causes static pattern to be formed between node/antinode positions
    - resonant frequencies can only effect in those activated regions

    - in guitar strings, the two endpoints excert stabilizing force such that between (min, max), the intermediate positions (fret) have a well defined resonating characteristics

    - incident and reflection
    - causes superposition of the two opposite travelling waves of same frequency to destructively combine at node positions
    - causes superposition of the two opposite oscillating waves of different phase to constructively combine at antinode positions 
    """
    def __init__(self, left, right, spacing):
        self.node = [interval for interval in range(left, right, spacing)]
        self.antinode = [((self.node[i] + self.node[i + 1]) / 2) for i in range(len(self.node) - 1)]
