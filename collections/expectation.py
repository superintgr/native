from . import statements, exceptions

class State:
    def __init__(self):
        self.attribute = []
        self.propertie = []
        self.constructor = []

    def forward(self, value):
        substrate = zip(self.propertie, self.attribute, self.constructor)
        
        for state in substrate:
            x, y, z = state
            yield x + y + z is value
    
    def backward(self, value):
        substrate = zip(self.constructor, self.attribute, self.propertie)
        
        for state in substrate:
            theta, phi, rho = state
            yield theta + phi + rho is value
    


# Example
attribute, property, constructor = (error, expression, code)

problem = State()
problem.__setattr__('attribute', attribute)
problem.__setattr__('property', property)
problem..__setattr__('constructor', constructor)

# Expectation preparation
solution = State()
solution.__setattr__('attribute', not(error))
solution.__setattr__('property', 
