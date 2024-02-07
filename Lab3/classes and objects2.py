#ex 1
class MyShape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
# Example
shape1 = MyShape("pink", True)
shape2 = MyShape("green", False)

print("Shape 1 color:", shape1.color)
print("Shape 1 is filled:", shape1.is_filled)
print("Shape 2 color:", shape2.color)
print("Shape 2 is filled:", shape2.is_filled)

#ex 2
class MyShape:
    def __init__(self, color="brown", is_filled=True):
        self.color = color
        self.is_filled = is_filled
# Example
shape1 = MyShape()  
shape2 = MyShape("blue", False) 

print("Shape 1 color:", shape1.color)
print("Shape 1 is filled:", shape1.is_filled)
print("Shape 2 color:", shape2.color)
print("Shape 2 is filled:", shape2.is_filled)

#ex 3
class MyShape:
    def __init__(self, color="brown", is_filled=True):
        self.color = color
        self.is_filled = is_filled
    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"A shape with color {self.color} is {filled_status}."
# Example
shape1 = MyShape()
shape2 = MyShape("black", False)
print(shape1)  
print(shape2) 

#ex 4
class MyShape:
    def __init__(self, color="black", is_filled=True):
        self.color = color
        self.is_filled = is_filled
    def getArea(self):
        return 0
    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"A shape with color {self.color} is {filled_status}."
# Example
shape = MyShape()
print("Area:", shape.getArea())  

#ex 5
class MyShape:
    def __init__(self, color="black", is_filled=True):
        self.color = color
        self.is_filled = is_filled
    def getArea(self):
        return 0
    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"A shape with color {self.color} is {filled_status}."
class Rectangle(MyShape):
    def __init__(self, color="black", is_filled=True, width=0, height=0):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height
class Circle(MyShape):
    def __init__(self, color="black", is_filled=True, radius=0):
        super().__init__(color, is_filled)
        self.radius = radius
    def getArea(self):
        return 3.14 * self.radius ** 2
# Example
rectangle = Rectangle(color="blue", width=5, height=3)
print(rectangle)  
print("Rectangle area:", rectangle.getArea())  
circle = Circle(color="red", radius=4)
print(circle)  
print("Circle area:", circle.getArea()) 

#ex 6
class Rectangle(MyShape):
    def __init__(self, color="black", is_filled=True, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width
    def getArea(self):
        return self.length * self.width
    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"A {filled_status} rectangle with color {self.color}, " \
               f"position ({self.x_top_left}, {self.y_top_left}), " \
               f"length {self.length}, and width {self.width}."
# Example
rectangle = Rectangle(color="blue", x_top_left=2, y_top_left=3, length=5, width=3)
print(rectangle)
print("Rectangle area:", rectangle.getArea())

#ex 7
class Circle(MyShape):
    def __init__(self, color="black", is_filled=True, x_center=0, y_center=0, radius=0):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
    def getArea(self):
        return 3.14 * self.radius ** 2
    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"A {filled_status} circle with color {self.color}, " \
               f"centered at ({self.x_center}, {self.y_center}), " \
               f"and radius {self.radius}."
# Example 
circle = Circle(color="red", x_center=2, y_center=3, radius=4)
print(circle)
print("Circle area:", circle.getArea())

#ex 8
class Rectangle(MyShape):
    def __init__(self, color="black", is_filled=True, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width
    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"A {filled_status} rectangle with color {self.color}, " \
               f"position ({self.x_top_left}, {self.y_top_left}), " \
               f"length {self.length}, and width {self.width}."
class Circle(MyShape):
    def __init__(self, color="black", is_filled=True, x_center=0, y_center=0, radius=0):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
    def getArea(self):
        return 3.14 * self.radius ** 2
    def __str__(self):
        filled_status = "filled" if self.is_filled else "not filled"
        return f"A {filled_status} circle with color {self.color}, " \
               f"centered at ({self.x_center}, {self.y_center}), " \
               f"and radius {self.radius}."
# Example
rectangle = Rectangle(color="blue", x_top_left=2, y_top_left=3, length=5, width=3)
print(rectangle)
print("Rectangle area:", rectangle.getArea())
circle = Circle(color="red", x_center=2, y_center=3, radius=4)
print(circle)
print("Circle area:", circle.getArea())




