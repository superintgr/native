import torch
import networkx as nx
from sounddevice import RawStream, RawInputStream, RawOutputStream
import queue
import wave

def trace(function, arguments):
    return torch.jit.trace(function, arguments)

def script(object):
	return torch.jit.script(object)

class Construction:
	def __init__(self, input_shape, output_shape, epsilon=1e-5):
		self.input_shape = input_shape
		self.output_shape = output_shape
		self.transformation = torch.randn(output_shape[1], input_shape[1])
		self.epsilon = epsilon

	def transform(self, input_state):
		output_state = torch.matmul(input_state, self.transformation.T)
		return output_state

	def is_constructor(self, input_state, output_state):
		reconstructed_output = self.transform(input_state)
		difference = torch.abs(reconstructed_output - output_state)
		return torch.all(difference < self.epsilon)
