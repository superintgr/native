import torch
import json

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
    
with open("data.json") as f:
    data = json.load(f)

input = torch.nn.functional.one_hot(data["input"], num_classes=512)
output = torch.nn.functional.one_hot(data["output"], num_classes=512)
