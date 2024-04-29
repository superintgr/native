import torch
import json

"""
model = torch.nn.Transformer(
    d_model=512,
    nhead=8,
    num_encoder_layers=6,
    num_decoder_layers=6,
    dim_feedforward=2048,
    dropout=0.1,
    activation='relu',
    custom_encoder=None,
    custom_decoder=None,
    layer_norm_eps=1e-05,
    batch_first=False,
    norm_first=False,
    bias=True,
    device=None,
    dtype=None)
    
These models would not allow sufficient learning to occur, as their primary focus is on the scalability of the system.

Here are some problems:
-- does not allow any type other than float or complex
-- cannot process integer or long type
-- very large
"""



"""Proposed architecture:

There will be an environment and everything will be modeled after that.

**Environment**

Enables the following features:
[definiteness] every object placed inside the substrate have definite positional properties
[dual] objects have their internal and external attributes
[conservation] an object with a position inside the substrate conserves some special quantity
[modeling] dynamics within the substrate are described geometrically
[dimensionality] environment constructs a three-dimensional structure

Any programmable structure can interact with the environment and their unique properties will be held at the local substrate, where their intrinsic properties are entirely separate from their embedded information.
"""

from reverberation import Reverb

class Environment(object):
    """
    Standard wrapper for environment variables.
    
    Fundamental modules:
    -- reverberation
    -- console
    -- [hidden]
    
    **Reverberation** module is the primary message pathway between network nodes.
    .. The environment always keeps a constant temperature and thermodynamic balance between changing states due to interactions from different regions.
    .. In order to maintain a static state, the reverberation configuration is tuned in a certain direction.
    .. The reflective surfaces are generically shaped so that the normal modes are exposed and thereby allowing interacting instances to occur at normal intervals.
    """
    
    def forward(self, *args, **kwargs):
        """
        Incoming signal causes impulse responses within the substrate regions.
        The responsive regions are defined by the wavelength of comparable dimensions where the natural resonance occurs.
        The room modes determine what specific reverberations are observed.
        
        Messages are transmitted via this dynamical process where the receiver distinguishes the signal using their respective channels.
        The medium keeps a copy of the message and transfers the information to other sites.
        """
        pass
    
    def sample(self, *args, **kwargs):
        """
        Sampling is used to measure states of interest.
        The effectiveness of the analysis depends on the individual who has the proper knowledge to distinguish the expected outcome from the naturally occurring gradient that takes place inside the substrate.
        """
        pass
        
        
"""Pipeline

We have a medium and it covers the following zones:
1. Sender/Transmitter/Receiver
2. Checkpoints/Nodes/Antinodes

There are devices embedded across the network that constitute mediated regions.
Any changes in any part of the medium corresponds to changes reflected at the labeled network regions.
Correspondingly the following is:

tau => {g -> C[tau]} is possible with side effects.
    
if tau is possible at all:
    there exists (h):
        return (h) (tau * {g -> h}) is possible.
"""


Constructor for tau (requires generic resource):
.. construct(tau) from generic {g : !g}


What is generic resource and how is it defined?
.. For task that is defined, its construction is a description of some already defined source transforming into some other possible to be defined source.
.. 