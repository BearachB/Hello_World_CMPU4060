class LinearEquations:

  def __init__(self, m, b):
    try:
      self.m = float(m)
      self.b = float(b)
    except TypeError:
      print(" m and b need to be integers or floats")
      self.m = None
      self.b = None

  def __str__(self):
    return "y = {:.2f}x + {:.2f}".format(self.m, self.b)

  def __repr__(self):
    return "({:.2}, {.2f})".format(self.m, self.b)

  def value(self, x):
    return self.m * x + self.b

  def compose(self, other_eqn):
    new_m = self.m * other_eqn.m
    new_b = self.m * other_eqn.b + self.b
    return LinearEquations(new_m, new_b)


  def add(self, other_eqn):
    new_m = self.m + other_eqn.m
    new_b = self.b + other_eqn.b
    return LinearEquations(new_m, new_b)

linear1 = LinearEquations(1, 1)
linear2 = LinearEquations(2, 5)


print(linear1.add(linear2))
