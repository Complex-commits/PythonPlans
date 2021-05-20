from graphics import *


class Shape():

    def __init__(self,  numSides, shapeName, nameAnchor, messageAnchor):
        """Constructor - give value to all attributes of class"""
        self.__numSides = numSides  # private attribute
        self.__shapeName = shapeName  # private attribute
        self.__nameAnchor = nameAnchor
        self.__messageAnchor = messageAnchor
    # create classes here and their methods
    def displayName(self, win):
        #self.__nameAnchor
        textBox = Text(self.__nameAnchor, self.__shapeName)
        textBox.draw(win)

    def displayNumSides(self, win):
        #textBox = Text(self.__messageAnchor, self.__numSides)

        message = " A " + self.__shapeName + " has " + str(self.__numSides) + " sides."
        textBox = Text(self.__messageAnchor, message)
        textBox.draw(win)

class Square(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        #@ Contructs an Square and draws it to the window.
        numSides = 4
        shapeName = "Square"
        Shape.__init__(self, numSides, shapeName, nameAnchor, messageAnchor)
    def drawShape(self, win):
        coordinate = Rectangle(Point(50, 50), Point(150, 150))
        coordinate.setFill(color_rgb(69, 179, 157))
        coordinate.draw(win)

class Ball(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        #@ Contructs an Ball and draws it to the window.
        numSides = 0
        shapeName = "Circle"
        Shape.__init__(self, numSides, shapeName, nameAnchor, messageAnchor)
    def drawShape(self, win):
        coordinate = Circle(Point(450, 150), 45)
        coordinate.setFill(color_rgb(149, 165, 166))
        coordinate.draw(win)

class Triangle(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        #@ Contructs an Triangle and draws it to the window.
        numSides = 3
        shapeName = "Triangle"
        Shape.__init__(self, numSides, shapeName, nameAnchor, messageAnchor)
    def drawShape(self, win):
        coordinate = Polygon(Point(150, 300), Point(100, 450), Point(200, 450))
        coordinate.setFill(color_rgb(108, 52, 131))
        coordinate.draw(win)

class Octagon(Shape):
    def __init__(self, nameAnchor, messageAnchor):
        #@ Contructs an Octagon and draws it to the window.
        numSides = 8
        shapeName = "Octagon"
        Shape.__init__(self, numSides, shapeName, nameAnchor, messageAnchor)
    def drawShape(self, win):
        coordinate = Polygon(Point(400, 375), Point(450, 400), Point(500, 375), Point(520, 415), Point(500, 450), Point(450, 475), Point(400, 450), Point(380, 415))
        coordinate.setFill(color_rgb(123, 36, 28))
        coordinate.draw(win)

def main():
    #! Main function where the shapes are called.
    win = GraphWin("Shape Shows", 600, 600)
    l1 = Line(Point(300, 0), Point(300, 600))
    l2 = Line(Point(0, 300), Point(600, 300))
    l1.draw(win)
    l2.draw(win)

    shapes = []
    shapes.append(Square(Point(50, 20), Point(100, 280)))
    shapes.append(Ball(Point(350, 20), Point(400, 280)))  
    shapes.append(Triangle(Point(50, 320), Point(100, 570)))  
    shapes.append(Octagon(Point(350, 320), Point(400, 570)))  

    for shape in shapes:
        shape.displayName(win)
        shape.displayNumSides(win)
        shape.drawShape(win)


    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()





