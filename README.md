# native
Initial Order

`load_group`
`attach_substrate`
`build_propagator`

**Progression**

- `construction/constructor.py` contains the generic torch module that launches the kernel from task dimensions.

- `device` contains two modules: `observer.py` and `master.py` -- that provides substrate object classes.

- `main.py` runs the standard automorphism search and builds network devices automatically whenever construction task is possible.


## Preparation

Device substrates can be composed in order to represent the task states using available channels and configurable blocks.

All transformations required could be composed using the channels and constructive blocking layer provided by the constructor module generically. This satisfy the resource aspect of which must come from naturally occuring regularities.

For example, one starts with an instance of the **observer** class which configures a block level that covers full or seperable portion of the initial task.

Let a task $T$ of a set ${/{(x_i, x_j), (y_i, y_j)}/}$ mapping input function of $(X_{x}^y, Y_{y}^x)$ to the output function of $(I_{x}^j, J_{y}^i)$.

Construction of $T$ is $\mathbf{C}_{S}(T)$ whose substrate $S$ enables the transformations required by the task.

We can create an instance `constructor = Constructor(*task.shape)`.

For each pass of the input states along the task dimension `0`, the output produced will be of shape `task[0].shape[-1]`.

By calling the method `is_constructor`, the instance will return a boolean variable.

Since the object is linear, we can have an indirect access to the task attributes via setting up an observer system and a master console which measures the observer states and keeps the system properties conserved throughout.

Create a task on the master whose input through running a query at specified observer device, permutes the field properties and returns the state of the device under the induced disturbance.

`injection = torch.rand(512, 2).requires_grad == True`
`
