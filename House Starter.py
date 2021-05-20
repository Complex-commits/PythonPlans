##Program: House Functions
##Name: Caesar's Cipher
## Date: 3/9/2021
#-------------------------------------------------------------#
#Constants
index = 0
count = 1

##Imports
from graphics import *
from tkinter import *



def main():    
    drawBuild()
    drawWin(1040, 225)
    drawWin(775, 225)
    drawWin(1040, 225)
    drawWin(775, 225)
    drawaDoor()
    drawRooftop()
    drawaChimneyTop()
    drawMoon()
    drawaGarage()
    win.getMouse()#wait for mouse click before closing
    win.close()
 #------------------------------------------------------------------------

 
    root = Tk()
    root.title('Movable Stars')
    root.geometry("800x600")

    w = 600
    h = 400
    x = w//2
    y = h//2

    canvas1 = Canvas(root, width = w, height = h, bg = "black")
    canvas1.pack(pady = 20)
    
    my_circle = canvas1.create_oval(x, y, x+10, y+10, fill = 'white')


    def left(event):
        x = -10
        y = 0
        canvas1.move(my_circle, x, y)

    def right(event):
        x = 10
        y = 0
        canvas1.move(my_circle, x, y)

    def up(event):
        x = 0
        y = -10
        canvas1.move(my_circle, x, y)

    def down(event):
        x = 0
        y = 10
        canvas1.move(my_circle, x, y)


    root.bind("<Left>", left)
    root.bind("<Right>", right)
    root.bind("<Up>", up)
    root.bind("<Down>", down)

    root.mainloop()

win = GraphWin("My Two Story House under the Stars", 1000, 702)
win.setBackground("Black")

def drawBuild():
    #@Drawing the first floor>>>>
    rect1 = Rectangle(Point(700, 700), Point(300, 400))

    #@Drawing the first floor of the house to the screen>>>>
    rect1.draw(win)

    #@Drawing the second floor of the house>>>>
    rect2 = Rectangle(Point(700, 625), Point(300, 400))

    #Drawing the second floor of the house to the screen>>>>>>
    rect2.draw(win)

    #@Moving the first floor of the house to the correct position>>>>
    rect1.move(0, -0)

    #@Moving the second floor of the house to the correct position>>>>>
    rect2.move(0,-200)

    #@Setting the color of the house to Dark Blue>>>>>>>
    rect1.setFill(color_rgb(0, 38, 153))
    rect2.setFill(color_rgb(0, 38, 153))
    

def drawaDoor():
    #@Drawing door on the first floor>>>>
    drawnDoor = Rectangle(Point(771, 327), Point(687, 225))

    #@Setting the door to slate grey color>>>>
    drawnDoor.setFill("Grey")

    #@Moving the door to the middle of the house on the bottom floor>>>>
    drawnDoor.move(-224, 371)

    #@Drawing the door to the screen>>>>>>
    drawnDoor.draw(win)

    
    #@Drawing a circle for the door knob that will connect to the door>>>>
    drawndoorKnob = Circle(Point(675,300), 5)

    #@Moving the doorknob to the correct position where the door is>>>>>>
    drawndoorKnob.move(-145,367)

    #@Setting the doorknob to a white color>>>>
    drawndoorKnob.setFill("White")

    #@Drawing the Doorknob to the screen>>>>>>
    drawndoorKnob.draw(win)

    




def drawWin(x,y, w = 75, h = 150, color= "Black"):

    #@Drawing both windows on the first floor>>>>>>>>
    windowP1 = Rectangle(Point(x, y), Point(x + w, y + h))
    windowP2 = Rectangle(Point(x, y), Point(x + w, y + h))

    #@Drawing lines for the windows on the first floor>>>>
    line1 = Line(Point(x, y + h//2), Point(x + w, y + h//2))
    line2 = Line(Point(x + w//2, y), Point(x + w//2, y + h))

    #@Drawing lines for the windows on the second floor>>>>
    l1 = Line(Point(x, y + h//2), Point(x + w, y + h//2))
    l2 = Line(Point(x + w//2, y), Point(x + w//2, y + h))


    #@Setting the colors of the windows to white>>>>>>
    windowP1.setFill(color_rgb(255,255,255))
    windowP1.setFill(color_rgb(255,255,255))
    windowP2.setFill(color_rgb(255,255,255))


    line1.setFill(color)
    line2.setFill(color)
    l1.setFill(color)
    l2.setFill(color)

    #@Moves the windows to the correct position on the first floor>>>>
    windowP1.move(-440, 300)
    windowP2.move(-440, 10)

    #@Moves the lines of the windows of the first floor to the correct positions>>>>>
    line1.move(-440, 300)
    line2.move(-440, 300)

    #@Moves the lines of the windows of the second floor to the correct position>>>
    l1.move(-440, 10)
    l2.move(-440, 10)

    #@Drawing the windows to the screen>>>>>>>
    windowP1.draw(win)
    windowP2.draw(win)

    #@Drawing the lines of the windows of the first floor to the screen>>>>>>>>
    line1.draw(win)
    line2.draw(win)

    #@Drawing the lines of the windows of second floor to the screen>>> 
    l1.draw(win)
    l2.draw(win)
    





def drawRooftop():
    #@Drawing the polygon for the rooftop of the house>>>>>
    roof = Polygon(Point(575, 200), Point(725, 125), Point(900, 125), Point(999, 200))

    #Setting the color of the Rooftop to grey>>>>>
    roof.setFill("grey")

    #Moving the rooftop the the correct position on the 2D rooftop>>>>>
    roof.move(-285,2)

    #@Drawing the rooftop to the screen>>>>>>>>
    roof.draw(win)
    
def drawaChimneyTop():
    #@Drawing a rectangle to act as a chimneyTop to the house>>>>>
    chi = Rectangle(Point(725, 125), Point(775, 55))

    #@Moving the chimneytop to the correct position to make the roof look 2D>>>>>
    chi.move(-250, 15)

    #@Setting the chimneytop color to white>>>>
    chi.setFill("white")

    #@Drawing the chimneytop to the screen>>>>>>
    chi.draw(win)


def drawaGarage():
    
    #@Drawing the garage door>>>>>
    garagedoor = Rectangle(Point(615, 685), Point(370, 389))
    

    #@Drawing the garage to the screen>>>>
    garagedoor.draw(win)


    #@Moving the garage to the correct position>>>>
    garagedoor.move(329, 80)

    
    #@Setting the color of the garage to Dark Blue>>>>>>>
    garagedoor.setFill(color_rgb(0, 38, 153))




    #@Drawing the inside of the garage door>>>>>
    garagedoordesign = Rectangle(Point(450, 567), Point(315, 389))

    #@Drawing the garage to the screen>>>>
    garagedoordesign.draw(win)

    #@Moving the garage to the correct position>>>>
    garagedoordesign.move(434, 150)

    #@Setting the color of the inside garage to grey>>>>>>>
    garagedoordesign.setFill("grey")

    #@Drawing the polygon for the rooftop>>>>
    garagedoorrooftop = Polygon(Point(200, 325), Point(375, 289), Point(472, 325))
    

    #@Drawing the rooftop for the garage to the screen>>>>
    garagedoorrooftop.draw(win)

    #@Moving the garagerooftop to the correct position>>>>>
    garagedoorrooftop.move(497, 143)

    #@Setting the color of the garagedoorrooftop>>>>>
    garagedoorrooftop.setFill("white")

    




def drawMoon():
    if index <= count:
        #Drawing a circle to act as the moon>>>>>>>
        moon = Circle(Point(175, 75), 25)

        #Setting the fill color of the moon to white>>>>>
        moon.setFill(color_rgb(255, 255, 255))

        #@Drawing a the moon to the screen>>>>>>>>
        moon.draw(win)
        count + 1
    else: 
        return










        

##Call To The Main
main()





