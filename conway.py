"""
conway.py
Author: Eamon
Credit: 
Assignment:conway life game
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
"""
You may use code supplied in the graphics tutorials as a starting point.
Live cells in your program may be represented as rectangles, circles, or any other shape that you would like to use. The example in the video above uses small circles.
The initial state of live cells may be preset or randomized by you, but it must be possible to start the game with a blank screen.
As the Wikipedia article described, your "playing area" may have fixed boundaries, boundaries that wrap around top and bottom, or may be entirely unbounded (in some ways, the easiest approach!).
The user must be able to "turn on" cells by clicking on them with the mouse, or by click-dragging across the window.
If your playing area is unbounded, then the up/down/right/left cursor keys should allow the user to scroll the playing area within the window.
Your live cells should be two different colors: one for its first day of “life”, the second for all subsequent days.
"""
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

#colors
invis = Color(0xffffff,1)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

#list of coords of cells
oldcells = []
newcells = []
oldcellx = []
oldcelly = []

black = Color(0, 1)
noline = LineStyle(0, black)
thinline = LineStyle(1,black)

#cells
#cell on day 1
class Cell1(Sprite):
    cll1 = RectangleAsset(20,20,noline,red)
    def __init__(self,  position):
        super().__init__(Cell1.cll1, position)

#cell after day 1 
class Cell2(Sprite):
    cll2 = RectangleAsset(20,20,noline,blue)
    def __init__(self,  position):
        super().__init__(Cell2.cll2, position)

#when there is no cell
class Cell0(Sprite):
    cll0 = RectangleAsset(20,20,thinline,invis)
    def __init__(self,  position):
        super().__init__(Cell0.cll0, position)



def mouseclick(event):
    global gamebegin, Cell1
    clicky = int((event.y//20)*20)
    print("clicky: " + str(clicky))
    clickx = int((event.x//20)*20)
    if str(clickx) + ", " + str(clicky) not in newcells:
        newcells.append(str(clickx) + ", " + str(clicky))
    #print("clickx: " + str(clickx))
    Cell1((clickx,clicky))
    #print("list: " + str(newcells))
    oldcellx.append(clickx)
    oldcelly.append(clicky)
    print(oldcellx)
    print(oldcelly)


  
nearby = []





#def step(event):
#    print("Hello")
            
            

#dimensions

#Cell1((10, 10))
myapp = App()
myapp.run()
myapp.listenMouseEvent('click',mouseclick)




