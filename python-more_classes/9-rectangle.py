#!/usr/bin/python3
"""create an empty class called Rectangle"""


"""create the class Rectangle"""


class Rectangle:
    """Class attribute"""
    number_of_instances = 0

    """Class attribute"""
    print_symbol = "#"

    """include class because it cannot be empty"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.width * 2 + self.__height * 2

    """ prints rectangle with # """
    def __str__(self):
        tangleO = []
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    tangleO.append(str(self.print_symbol))
                if i < self.__height - 1:
                    tangleO.append("\n")
        tangleO = "".join(tangleO)
        return tangleO

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    """ returns a Rectangle instance with equal width and height """
    @classmethod
    def square(cls, size=0):
        if width == height == size:
            raise ValueError()
        return cls(width=size, height=size)
