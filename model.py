import torch
import json

# model = torch.nn.Transformer(
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
    
"""
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