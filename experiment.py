__permutation__ = [
    {
        "pre/post" : "encoding to serialized binary", "decoding from serialized binary"
]

import pickle

encode = lambda state: pickle.dumps(state)
decode = lambda dump: pickle.loads(dump)

"""
%% TASK %%

Given serialized binaries of fixed length:
. convert to reshapable tensor
. transform tensor to output
. convert output to fixed length binaries

(.) reshaping:
. depends on the models' input shape

(.) transformation:
. requires producing decodable binaries

(.) output:
. depends on reproducible shapes
"""

def state(code, model):
    code = encode(code)
    length = model.input_size
    pad = abs(length - len(code))
    pad = [0] * length
    pad[:length(code)] = code
    return model(pad)

def machine(memory, rule):
    program = lambda symbol: rule[memory[symbol]]
    return program

def computer(input, device):
    memory = {input : not(input)}
    transform = {input : input}
    code = program(memory, transform)
    output = code(input)
    return device(output)

