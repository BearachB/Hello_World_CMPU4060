class WholeNumberClass():
# Class object attributes

def __init__(self, x, y):
  if type(x) == int and x > 0 and type(y) == int and y > 0:
    self.x = x
    self.y = y
    print(self.x, "Is the correct type")
  else:
    print("Wrong input type, x must be > 0")

# TWO CASES NOT ALLOWED
# (1) you must not be able to create a WholeNumber that has a negative value;
# (2) an arithmetic operation cannot be allowed to have a negative result.

# Class object methods

def addition(self):
  if type(self.x) == int and type(self.y) == int:
    result = self.x + self.y
  else:
    try:
      result = int(self.x) + int(self.y)
    except ValueError:
      result = print("Wrong input type. Please input a valid integer")
    except TypeError:
      result = print("Wrong input type. Please input a valid integer")
    return result

def subtraction(self):
  if self.x > self.y:
    sub_result = self.x - self.y
    break
  else:
    sub_result = self.y - self.x
  return sub_result

def multiplication(self):
  return self.x * self.y


whole_no_calculator = WholeNumberClass(x=2,y=5)
