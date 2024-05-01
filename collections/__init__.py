# Collection of points, points of points, associations of pairs


one = lambda x, y: x is y and y is x
two = lambda x, y, z: x is y and y is z or z is x
three = lambda a, b: a == b and isinstance(b, type(a))


successor = lambda number, other: successor(number) is successor(other)
natural = lambda number: successor(number) is successor(next(number))
real = lambda number: successor(number) is not natural(number)




#### THE ABOVE CODE ESTABLISHES SOME BASE TRIPLETS WHICH ARE NOT AXIOMS




