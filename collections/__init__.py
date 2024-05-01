# Collection of points, points of points, associations of pairs


one = lambda x, y: x is y and y is x
two = lambda x, y, z: x is y and y is z or z is x
three = lambda a, b: a == b and isinstance(b, type(a))


successor = lambda number, other: successor(number) is successor(other)
natural = lambda number: successor(number) is successor(next(number))
real = lambda number: successor(number) is not natural(number)




#### THE ABOVE CODE ESTABLISHES SOME BASE TRIPLETS WHICH ARE NOT AXIOMS


class Native:
    """Native instance model.
    
    It provides a functional directory for searching and mapping named spaces.
    
    Solvers with their problem contexts:
    
    • describing novel problems in terms of known names and their compositions that reaches a solution space in abstract terms :
    ----- programming languages or custom libraries are fundamentally incapable of meeting novel instances where their necessary connections different from the regular programming has to be directed using limited functionality that it interprets.
    ---- it is possible to make a system more approachable but it is never robust enough to evolve fast and efficiently.
    --- the notion of fundamental objects and maliable entities must not resort to another fundamental host where the host system isn't universal in its entirety.
    -- however a complex where the rest of the space exceeding the repertoire of existing finite elements that covers the whole of spectrum would enable arbitrary improvement with arbitrary possible frequencies.
    - we develop such a complex as substrate that could be generically useful and not special purpose.
    The directory will contain the following programmable objects:
    -- generic constructor
    --- abstract constructor
    ---- graph constructor
    ----- network constructor
          language interface
    
    """
    language : object
    interface : object
    
    def __setattr__(self, *args, **kwargs):
        pass
        
    def __getattr__(self, *args, **kawrgs):
        pass




