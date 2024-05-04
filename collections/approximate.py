import networkx as nx
import torch

master = nx.Graph()

"""Policy
(1) `master` is an undirected graph object which should be seen as network substrate.
(2) new information is processed by the master node where it compiles the data into 2 dimensional object code.
(3) for information to be new there has to be distinguishable features of the data that constitute extending the population size accordingly.
(4) if information can be present in a state of an object, then that object must have at least two distinguishable states where their attributes can encode information.
(5) if information can be encoded in a pair of states of two objects that each have necessary properties for storing the data, then the two can carry out processing of information too.
(6) if two objects that can process information have unity, then the union of the two states cannot hold information.
"""

def information_state(clone, name):
    state = nx.Graph()
    state.add_node(clone)
    state.add_node(name)
    state.add_edge(name, clone)
    state.add_edge(clone, clone)
    return state

def attach_state(device, attribute):
    master.add_node(attribute)
    master.add_edge(attribute, device)

def approximate_constructor(input_state, output_state, epsilon):
    input_state + ? -> output_state and output_state - ? -> input_state - ? ~ input_state

"""Sofar
(1) Information state requires clonable substrate which we create two instances of for the task of building information substrate that copies the information variable and retransmits the information to other nodes while keeping the copy into the substrate.
(2) name argument is the input arriving at the information substrate via appropriate medium whose computation variable is one of the set of information attributes that are clonable properties of the processing substrate.
(3) To represent information in an object with states of two different levels where each is the function of computing the information variable with the other encoding the substrate attribute.
(4) A constructor is able to be approximated for some input taken from generic resources such that the transformation of cloned attribute and generic attribute pair becomes a pair with two instances of the original cloned parameter.
(5) State is generated with an undirected graph where nodes (x, x0) -> (x, x) and implication is transformation caused through constructor C[X](x0) = Union({[(x, x0), (x, x)]}) with side-effect.
(6) Attach state to the device given an attribute; here the master graph sets the attribute as node (if does not exists yet) whose edge points to the device.
(7) Device containing the cloned attribute as node property which is paired with incoming edge from the master graph applies transformation on the implied property from master to produce the same edge reflected back.
(8) Approximating a constructor is not defined here, although the symbolic expression could work too.
"""
