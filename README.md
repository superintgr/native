# Different Levels

1. modeling patterns, encoding/decoding, embedding, parsing, vectorizing, read/write/update tasks, os communucations
2. connecting model outputs, conditioning on multipath propagation, closures and constructions, building modules and setting training schedules
3. preparing task managers, setting up construction modules, building models of work repository, pipelining constructions with tasks, externally handling optimization through task registry, supervising construction processes, building direct injection gateway and automatic integration pipeline
4. setting up complete end-to-end modeling, managing whole instances and their substrate support, online and offline communication protocols, resource optimization and linear programming


## Development and Engineering

**Stages**

1.0. Physical layers, conservation of energy, quantum mechanical principles, constructor theory
1.1. Communication, computation, information, channel, fields, storage
1.2. Simulation, model, runtime, network, device, hardware

2.0 Virtual machine, programming model, hardware instructions, compiler design, memory model
2.1 Storage architecture, development pipeline, resource allocation, runtime model, interpreters and assembly

## Protocols

**Programming**

1. All programs are capable of error correction, secures backup policy, online and remote copies of working instances, utility level callables for managing file/code/comm level tasks

```text
program : [super, instance, primary, secondary, copy]
. super is <identity of the master channel driver>
. instance is <group driver module name>
. primary is <path containing source information>
. secondary is <path referred to by source preprocessor>
. copy is <local backup to last secured secondary transfers>

line : [inlet, outlet, sidechain]
. inlet is <path from instance drive>
. outlet is <path to identity drive>
. sidechain is <dictionary mapping of outlet partitions>

callable : [github push/pull/clone, cloud-bucket upload/create/download/readout, google-drive download/upload, hugginface dataset]
. github is <config hidden
. cloud-bucket is <config hidden>
. google-drive is <config hidden>
. hugginface is <config hidden>

pipeline : []
```

**Clocks**

1. Clocks are not used in a traditional sense. Clock functions should be treated as programming tasks.

2. A clock is composed of timed events that depends on time being caused to elapsed at some location within a range definining notion of interval. The interval between any two measurements define a trajectory where certain work has been put in, in order to bring the lowest reading in the range to ultimately sample non-invarient aspects of the time-like procedures.

To define a clock, a program may construct a process which has the responsibility of measuring certain physical properties and upon each successive measuement the process reports backs to an internal function which logs the time differences. Continue the same process with many competing moment carriers where the intervals between the k-fastest and k-slowest could be used to substitute all of the clock related tasks.

For example, the fastest turn-arounds could be used to measure the fastest constructor of some other process that happens in parallel. When there are many possible constructor for a given task, use the timer constructors to filter the constructions that conform to the simulteneous time keeping dynamics.

[David Duetsch][Constructor theory][Philosophy of Constructor theory][3.12][Time]

In both quantum theory and general relativity, time is treated anomalously. The problem in both theories is that time is not among the entities to which the theory attributes objective existence (namely quantum observables and geometrical objects respectively), yet those entities change with time.

So there is widespread agreement that there must be a way of treating time ‘intrinsically’ (i.e. as emerging from the relationships between physical objects such as clocks) rather than ‘extrinsically’ (as an unphysical parameter on which physical quantities somehow depend). But this is difficult to accommodate in the prevailing conception, every part of which (initial state; laws of motion; time-evolution) assumes that extrinsic status.

Attempts have been made to reformulate both theories with intrinsic time (Page & Wootters 1983; Barbour 1999, 2012), but have not yet achieved much generality.

In the constructor- theoretic conception, it is both natural and unavoidable to treat both time and space intrinsically: 

.. they do not appear in the foundations of the theory but are emergent properties of classes of tasks whose substrates include ‘rods’ and ‘timers’.

(That constructor theory allows for serial composition to be noncommutative, and for a task and its transpose to be different, may be considered a built-in direction of time, but not a time parameter.)

Extrinsically, a timer might be defined as a substrate T[l] which, if left isolated in a suitable initial state, emits some information when a time t has passed. But that condition about time ‘passing’ is not constructor-theoretic. 

Some constructor-theoretic content can be added by noting that there is an interoperability law for timers:

.. any timer T[t] is guaranteed to be replaceable, in any construction, by any other timer T[t‘] with the same parameter t, without changing the task that the constructor performs.

A fully intrinsic constructor-theoretic conception of timers would be in terms of tasks that take time.

For example, let R be a non-conducting rod of length l with an additional electron.

Let x and y be states in which the electron is located at either end of R, and let C[1] and C[2] be constructors for the task

T[R] = {x -> y, y -> x}.

Associate them in parallel, with an additional apparatus ensuring that when C[1] halts, it incapacitates C[2].

Define ‘faster’ such that if that composite constructor is capable of performing the task T[R] ⊗ T[R‘], but the same does not hold if C[1] and C[2] are interchanged, then C[2] is faster than C[1].

Then, if C is a constructor for T[R] such that no other constructor for T[R] is faster than it, it can act as a timer.

For instance, if the subsidiary theory was relativity, C would time a period, t = l / c; where c is the speed of light.

```
timer : [T, T‘]
. T is <timer:0)
. T‘ is <timer:1>

state : [x, y]
. x is <state of object>
. y is <state of object>

object : [R[x][y], R‘[y][x]]
.. (R and R‘) are <two instances with fixed length>

task : [x -> y, y -> x]
. x goes <to other>
. y goes <to other>

constructor : [C[1], C[2]]
. C[1] of T[R]
. C[2] of T[R‘]

composition : [*task, **task]
. *task (xor) **task
```
