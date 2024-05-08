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


# It is very easy today !! but i shall incentivise a structure first
"""Recently
(1) Substrate object was written with a console object attached to it as device for processing signals.
(2) I will add a method via which a constructor could be approximated from given input/output states.
(3) Fixed point layer is used for first mapping the input state to the intermediate code and then another intermediate code represents the target state.
(4) Translating external states to implicit representations of their causal drives can solve for the mapping task in question.
(5) Object code serialization, layer optimization, testing consistency for approximated constructors and all such utility tasks are going to be defined.
(6) Additionally I have defined a module class which currently is very messy, although provides the general recording, tracing, tracking opportunity when subclassed into tasks.
"""


"""Universal Quantum Computer

(M) two-state observables: {n[i]} (i in Z[:i])
(S) two-state memory elements: {m[i]} (i in Z[:])
(X) pointer on infinite tape: {x[i]} (i in Z[:])

Simultaneous vector <x ~ n ~ m> : <x ~ n[0], n[1], ..., n[M - 1] ~ ..., m[-1], m[0], m[1], ...>

Evolution of the state vector <psi(n++ * T) ~ U[:, n] * psi(0)>
Unitary operator (U) = U * U[~] = 1 = U[~] * U
"""

"""exportation = export + transport
(1) typically import statement brings the referred name to the code environment,
(2) in using external scope the imported names imply features that is composed outside its knowledge,
(3) a function that imports one named instance and uses their namedspaces would export the product
(4) imports are transport - exportation

For programming certain motion where there is a resource which can be harnessed via integration of third party services:
(0) prepare a substrate (slave/master console)
(1) make contact with the provider (slave/slave console)
(2) attach the medium (master/slave console)
(3) transfer assets into channel (right/left console)
(4) transport the product to console (master/left console)
(5) transfer assets into channel (left/right console)
(6) detach the medium (slave/master console)
(7) make contact with the provider (slave/slave console)
(8) destroy a substrate (master/slave console)
"""

changelog = [
    string library design where subtraction is reversible,
    a model of arithmetic operators on their positional equivalence logic,
    levels of neural network probes ranging from hyper level to inner level substrate actions in parallel,
    neural medium and their constructor theoretic implication,
    automatic gradient vs automatic differentiation tools,
    package dependencies expressed in terms of possible imports and exports (new),
    mod script change logs (new),
    gradient computation and reversible properties in simultaneous changes,
    note application regarding .. in change log (new),
    jist on regular network .. in change log (new),
    universals as list (new),
    3b1b ~ tensor exponents .. solution to exponential properties in a system,
    copy is a dangerous thing to forget or not know about,
]


"""importation = computation - transformation

(0) importing something to a computation task
(1) imported products yield the characteristic programs
(2) mutation of imported products is not possible from the computation context
(3) a copy of the product can be mutated as far as the permutation involving the copy allows,
(4) if the information that allows importation is possible, that information does not guarantee the imported knowledge to be usable,
(5) if the transformation on the imported knowledge is not possible, it is possible to copy the object and annotate their impossible mutability condition,
(6) if copying could not be done, then no information can exits

extended discussion:
(0) suppose a superinteger is possible with assertion in a program,
(1) the code is coded in such a way that assertion on that knowledge implies other knowledge,
(2) the implication is programmed to be sought,
(3) the knowledge will be represented via a graph and regular networks of nodes are asserted statements,
(4) programming the network is to program statements whose evaluation establishes connection between two or more nodes,
(5) language used for the graph involves the operation involving reading and writing, checking and modifying, counting and summing, terminating and existing,
"""


image = {
    left : [M + S],
    right : [M - S],
    mid : [L + R],
    side : [L - R],
}

def forward(node, function):
    return function(node)

def backward(antinode, function):
    return function(antinode)

"""Network of Images

(-1) get constructor for left, right task
(-0) set construction task {left -> right} and {right -> left}
(+0) get constructor for mid, side task
(+1) set construction task {mid -> side} and {-side -> mid}

(-1) as left -> right, mid + side -> mid - side
(-0) if left + right is mid possible, set {side -> -side}
(+0) as mid -> side, left - right -> left + right
(+1) if mid - side is right possible, set {-mid -> mid}
"""


taskf(i), a, b) := (0, 1, f(i), f, i, 0)
THIS IMPLIES THAT THE RESULT OF TASK FOR f(i) STORES
THE RESULT IN B FOR f EVALUATED ON a.

reversibility requires that, if b is not initalized with 0, then the results of a should not overwrite b rather combine in some reversible way.
so the function prepared at f(i) whose resulting program processes 'a' with f on some output variable 'b':
-1x modify the function (f) to compute sum and difference for every input
-0x result state corresponds to a pair [left, right] where right contains the updated variable
+0x for left side containing all the recent changes reflected on right, any content of b through computation shifts into some proportion yielding at left
+1x from right side any yield will partially conserved by the left-adjacent node.


"""Q Programs (Generators)

(-1, -0), (+0, +1)
     (-0, +0)
       (0)
       (1)
    (+1, -1)
(+1, +0), (-0, -1)
       

"""
