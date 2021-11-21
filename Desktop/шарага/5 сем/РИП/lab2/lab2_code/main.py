from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy

def main():
    r = Rectangle("синего", 14, 14)
    c = Circle("зеленого", 14)
    s = Square("красного", 14)
    print(r)
    print(c)
    print(s)

    b = numpy.array([[1.5, 2, 3], [4, 5, 6]])
    print(b)

if __name__ == "__main__":
    main()