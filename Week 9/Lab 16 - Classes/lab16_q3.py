class Rectangle():

    # CLASS OBJECT ATTRIBUTES

    def __init__(self, length, breadth):
    self.rec_length = length
    self.rec_breadth = breadth

    # METHOD

    def get_rectangle_area(self):
        return self.rec_length * self.rec_breadth

    def get_rectangle_perimeter(self):
        return 2 * (self.rec_length + self.rec_breadth)


my_rectangle = Rectangle(length=10, breadth=20)

print(type(my_rectangle))
print(my_rectangle.get_rectangle_area())
print(my_rectangle.get_rectangle_perimeter())
