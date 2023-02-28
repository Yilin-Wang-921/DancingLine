#################################################
# Term Project: Dancing Line
#
# Name: Yilin Wang
# Andrew id: yilinw
#################################################

import math, copy, random, time, numpy
from cmu_112_graphics import *

#################################################
# Helper Functions
#################################################
def roundedRectangle(app, canvas, x0, y0, x1, y1, r, color):
    canvas.create_oval(x0, y0, x0 + 2*r, y0 + 2*r, fill = color, width = 0)
    canvas.create_oval(x1 - 2*r, y0, x1, y0 + 2*r, fill = color, width = 0)
    canvas.create_oval(x0, y1 - 2*r, x0 + 2*r, y1, fill = color, width = 0)
    canvas.create_oval(x1 - 2*r, y1 - 2*r, x1, y1, fill = color, width = 0)
    canvas.create_rectangle(x0 + r, y0, x1 - r, y1, fill = color, width = 0)
    canvas.create_rectangle(x0, y0 + r, x1, y1 - r, fill = color, width = 0)

def getLineCellBound(app, row, col):
    x0 = col * app.lineCellWidth
    y0 = row * app.lineCellHeight
    x1 = (col+1) * app.lineCellWidth
    y1 = (row+1) * app.lineCellHeight
    return x0, y0, x1, y1

def getMapCellBound(app, row, col):
    x0 = col * app.mapCellWidth
    y0 = row* app.mapCellHeight
    x1 = (col+1) * app.mapCellWidth
    y1 = (row+1) * app.mapCellHeight
    return x0, y0, x1, y1

#################################################
# Splash Screen Mode
#################################################

def drawStart(app, canvas):
    #draw background
    canvas.create_rectangle(0,0, app.width, app.height, fill = "light cyan")
    #button for START
    roundedRectangle(app, canvas, app.width/2 - 105, app.height/2 - 125, 
                        app.width/2 + 95, app.height/2 - 65, 20, "turquoise")
    roundedRectangle(app, canvas, app.width/2 - 100, app.height/2 - 130, 
                        app.width/2 + 100, app.height/2 - 70, 20, "cyan")
    #button for TUTORIAL
    roundedRectangle(app, canvas, app.width/2 - 105, app.height/2 + 25, 
                        app.width/2 + 95, app.height/2 + 85, 20, "turquoise")
    roundedRectangle(app, canvas, app.width/2 - 100, app.height/2 + 20, 
                        app.width/2 + 100, app.height/2 + 80, 20, "cyan")
    #text
    font = 'Arial 30 bold italic'
    canvas.create_text(app.width/2 - 3, app.height/2 -101, 
                        text="START", font=font, fill = "light cyan")
    canvas.create_text(app.width/2, app.height/2 - 100, 
                        text="START", font=font, fill = "cyan4")
    canvas.create_text(app.width/2 - 3, app.height/2 + 49, 
                        text="TUTORIAL", font=font, fill = "light cyan")                   
    canvas.create_text(app.width/2, app.height/2 + 50, 
                        text="TUTORIAL", font=font, fill = "cyan4")

def drawLogo(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "turquoise")
    canvas.create_text(app.width/2-5, app.height/2 - 50, 
                        text = "Dancing\nLine - - -",
                        fill = "cyan4", font = 'Arial 80 bold italic')
    canvas.create_text(app.width/2, app.height/2 - 50, 
                        text = "Dancing\nLine - - -",
                        fill = "white", font = 'Arial 80 bold italic')
    canvas.create_text(app.width/2, app.height/2 + 100,
                        text = "click the screen to play", fill = "cyan4",
                        font = 'Arial 18 bold italic')
    canvas.create_text(app.width/2 + 2, app.height/2 + 100,
                        text = "click the screen to play", fill = "white",
                        font = 'Arial 18 bold italic')

# from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
def splashScreenMode_redrawAll(app, canvas): 
    if app.start:
        drawStart(app,canvas)
    else:
        drawLogo(app, canvas)

def splashScreenMode_mousePressed(app, event):
    if event.x:
        app.start = True
        x, y = event.x, event.y
        gameX = [app.width/2 - 105, app.width/2 + 100]
        gameY = [app.height/2 - 130, app.height/2 - 65]
        tutorialX = [app.width/2 - 105, app.width/2 + 100]
        tutorialY = [app.height/2 + 20, app.height/2 + 85]

        if x > gameX[0] and x < gameX[1] and y > gameY[0] and y < gameY[1]:
            app.mode = 'threeDMode'

        elif (x > tutorialX[0] and x < tutorialX[1] and 
                    y > tutorialY[0] and y < tutorialY[1]):
                        app.mode = 'tutorialMode'

#################################################
# Tutorial Screen Mode
#################################################

def loadImage(app):
    app.tutorial1 = app.loadImage('tutorial1.png')
    app.tutorial1 = app.scaleImage(app.tutorial1, 3/14)
    app.tutorial2 = app.loadImage('IMG_2455.JPG')
    app.tutorial2 = app.scaleImage(app.tutorial2, 1/3)

def displayImage(app,canvas):
    canvas.create_image(250, 200, image=ImageTk.PhotoImage(app.tutorial1))
    canvas.create_image(800, 200, image=ImageTk.PhotoImage(app.tutorial2))


def tutorialMode_redrawAll(app, canvas):
    if app.mode == 'tutorialMode':
        #draw background
        canvas.create_rectangle(0,0, app.width, app.height, fill = "light cyan")
        #button for START
        roundedRectangle(app, canvas, app.width/2 - 150, app.height-125, 
                        app.width/2 + 140, app.height- 65, 20, "turquoise")
        roundedRectangle(app, canvas, app.width/2 - 145, app.height- 130, 
                        app.width/2 + 145, app.height- 70, 20, "cyan")
        #text
        font = 'Arial 30 bold italic'
        canvas.create_text(app.width/2 - 3, app.height-101, 
                            text="YES IM READY", font=font, fill = "light cyan")
        canvas.create_text(app.width/2, app.height- 100, 
                            text="YES IM READY", font=font, fill = "cyan4")
        displayImage(app,canvas)
        canvas.create_rectangle(0,0,60,app.height/2 + 100,fill = "light cyan",
                                width = 0)
        canvas.create_text(270, app.height - 250, 
                            text = ("- Use only 'left' and 'right' keys to\n change the direction of the line\n\n- Avoid hitting the WALL!"),
                            font='Arial 20 bold italic', fill = "cyan4")
        canvas.create_text(800, app.height -250, 
                            text = "- Collect coin and ruby along the way",
                            font='Arial 20 bold italic', fill = "cyan4")

def tutorialMode_mousePressed(app, event):
    x, y = event.x, event.y
    gameX = [app.width/2 - 150, app.width/2 + 145]
    gameY = [app.height - 130, app.height - 65]
    if x > gameX[0] and x < gameX[1] and y > gameY[0] and y < gameY[1]:
            app.mode = 'threeDMode'


#################################################
# 3D Game Screen Mode
#################################################


def takeStep(app):
    (drow, dcol) = app.lineDir
    headRow, headCol = app.line[0]
    newRow, newCol = headRow + drow, headCol+dcol
    if len(app.line) <= 10:
        app.line.insert(0,[newRow, newCol])
    else:
        app.line.pop(-1)
        app.line.pop(-2)

#initialize the dancing line
def initLine(app):
    #initiate the dancing line
    app.lineCellHeight = app.height / 25
    app.lineCellWidth = app.width / 30
    app.line = [[0,10]]
    app.lineDir = (app.speed,0)

def drawLine(app,canvas):
    for line in app.line:
        x0,y0,x1,y1 = getLineCellBound(app, line[0],line[1])
        canvas.create_rectangle(x0,y0,x1,y1, fill = app.lineColor, width = 0)

def threeDMode_keyPressed(app,event):
    if app.pause == False and event.key == "Space":
        app.pause = True
    elif app.pause == True and event.key == "Space":
        app.pause = False
    #if the line was moving up originally 
    if app.lineDir == (app.speed,0) and event.key == "Left": 
        app.lineDir = (0, -app.speed)
    elif app.lineDir == (app.speed,0) and event.key == "Right": 
        app.lineDir = (0, +app.speed)
    #if the line was moving to left or right
    elif app.lineDir ==(0, -app.speed) and event.key == "Right":
        app.lineDir = (app.speed, 0)
    elif app.lineDir == (0, +app.speed) and event.key == "Left":
        app.lineDir = (app.speed, 0)
    

#initialize the map
def initMap(app):
    #initiate a map with different values of rows and cols
    app.mapRows = 13
    app.mapCols = 8
    app.map = [ ([0] * app.mapCols) for row in range(app.mapRows) ]
    app.map[12][3] = 1
    app.map[11][3] = 1
    app.map[10][3] = 1
    app.mapCellHeight = app.height / 10
    app.mapCellWidth = app.width / 10
    app.currPath = (10,3)
    app.dir = "up"
    generatePath(app)

#pick a random direction to form the path
def getRandomDirection(app,path):
    r = app.currPath[0]
    c = app.currPath[1]
    #"left" = (0,-1)  "right" = (0, +1)   "up" = (-1,0)
    if c == 5 and app.map[r][c-1] == 0:
        #can go up or left
        directions = [(-1,0),(0,-1)]
        dir = random.randint(0, len(directions)-1)
        return directions[dir]
    if c == 5 and app.map[r][c-1] != 0:
        #can only go up
        return (-1,0)
    if c == 1 and app.map[r][c+1] == 0:
        #can go up or right
        directions = [(-1,0),(0, +1)]
        dir = random.randint(0, len(directions)-1)
        return directions[dir]
    if c == 1 and app.map[r][c+1] != 0:
        #can only go up
        return (-1,0)
    if app.map[r][c+1] != 0:
        #can go up or left
        directions = [(-1,0),(0,-1)]
        dir = random.randint(0, len(directions)-1)
        return directions[dir]
    if app.map[r][c-1] != 0:
        #can go up or right
        directions = [(-1,0),(0, +1)]
        dir = random.randint(0, len(directions)-1)
        return directions[dir]
    else: #can go any directions(left, up, right)
        directions = [(-1,0),(0,-1),(0, +1)]
        dir = random.randint(0, len(directions)-1)
        return directions[dir]

#map generation
def generatePath(app):
    while app.currPath[0] > 0:
        app.dir = getRandomDirection(app, app.currPath)
        newPathRow = app.currPath[0] + app.dir[0]
        newPathCol = app.currPath[1] + app.dir[1]
        app.currPath = (newPathRow, newPathCol)
        r = app.currPath[0]
        c = app.currPath[1]
        app.map[r][c] = 1

def changeMap(app):
    for row in range(len(app.newMap)):
        for col in range(len(app.newMap[0])):
            x0,y0,x1,y1 = getMapCellBound(app,row,col)
            #need to calculate the coordinates for four points of one cell
            vecX0, vecY0 = get2DCoord(app,x0,y0,0)
            vecX1, vecY1 = get2DCoord(app,x1,y1,0)
            vecX2, vecY2 = get2DCoord(app,x0,y1,0)
            vecX3, vecY3 = get2DCoord(app,x1,y0,0)
            #calculate the coordinates in tkinter
            X0, Y0 = getPythonCoord(app,vecX0, vecY0)
            X1, Y1 = getPythonCoord(app,vecX1, vecY1)
            X2, Y2 = getPythonCoord(app,vecX2, vecY2)
            X3, Y3 = getPythonCoord(app,vecX3, vecY3)
            app.newMap[row][col] = (X0, Y0, X1, Y1, X2, Y2, X3, Y3)

def changeLine(app):
    for line in app.line:
        x0,y0,x1,y1 = getLineCellBound(app, line[0], line[1])
        vecX0, vecY0 = get2DCoord(app,x0,y0,0)
        vecX1, vecY1 = get2DCoord(app,x1,y1,0)
        vecX2, vecY2 = get2DCoord(app,x0,y1,0)
        vecX3, vecY3 = get2DCoord(app,x1,y0,0)
        #calculate the coordinates in tkinter
        X0, Y0 = getPythonCoord(app,vecX0, vecY0)
        X1, Y1 = getPythonCoord(app,vecX1, vecY1)
        X2, Y2 = getPythonCoord(app,vecX2, vecY2)
        X3, Y3 = getPythonCoord(app,vecX3, vecY3)
        if (X0,Y0,X1,Y1,X2,Y2,X3,Y3) not in app.newLine:
            if len(app.newLine) <= 10:
                app.newLine.append((X0,Y0,X1,Y1,X2,Y2,X3,Y3))
            else:
                app.newLine.pop(0)
                app.newLine.pop(1)
                app.newLine.append((X0,Y0,X1,Y1,X2,Y2,X3,Y3))


def init3D(app):
    app.origin = 0,app.height
    app.newMap = [ ([0] * app.mapCols) for row in range(app.mapRows) ]
    changeMap(app)
    app.newLine = []
    changeLine(app)

def get2DCoord(app,x,y,z):
    #x axis degree
    theta1 = 360*math.pi/180
    #y axis degree
    theta2 = 60*math.pi/180
    x2D = math.cos(theta1) * x + math.cos(theta2) * y
    y2D = math.sin(theta1) * x + math.sin(theta2) * y + z
    return x2D,y2D
    
def getPythonCoord(app,x2D,y2D):
    ox,oy = app.origin
    x = ox + x2D
    y = oy - y2D
    return x,y

def drawNewMap(app, canvas):
    map = app.newMap[::-1]
    for row in range(len(app.newMap)):
        for col in range(len(app.newMap[0])):
            x0,y0,x1,y1,x2,y2,x3,y3 = map[row][col]
            #draw wall
            if app.map[row][col] == 0:
                canvas.create_polygon(x2,y2,x1,y1,x3,y3,x0,y0,
                                fill = "LightCyan2")
            #draw path
            elif app.map[row][col] == 1:
                canvas.create_polygon(x2,y2,x1,y1,x3,y3,x0,y0,
                                fill = "cyan4")
            else:
                canvas.create_polygon(x2,y2,x1,y1,x3,y3,x0,y0,
                                fill = "gold")

def drawWall(app, canvas):
    map = app.newMap[::-1]
    for row in range(len(app.newMap)):
        for col in range(len(app.newMap[0])):
            x0,y0,x1,y1,x2,y2,x3,y3 = map[row][col]
            if app.map[row][col] == 0:
                for i in range(1,10):
                    canvas.create_polygon(x2,y2-i*2,x1,y1-i*2,x3,y3-i*2,
                                            x0,y0-i*2,fill = "turquoise")
                canvas.create_polygon(x2,y2-20,x1,y1-20,x3,y3-20,x0,y0-20,
                                fill = "LightCyan2")
            elif app.map[row][col] == 2:
                for i in range(1,10):
                    canvas.create_polygon(x2,y2-i*2,x1,y1-i*2,x3,y3-i*2,
                                            x0,y0-i*2,fill = "goldenrod")
                canvas.create_polygon(x2,y2-20,x1,y1-20,x3,y3-20,x0,y0-20,
                                fill = "gold")

def drawNewLineBottom(app, canvas):
     for line in app.newLine:
        X0,Y0,X1,Y1,X2,Y2,X3,Y3 = line
        canvas.create_polygon(X2,Y2,X1,Y1,X3,Y3,X0,Y0,fill = "pink1")
        for i in range(20):
            canvas.create_polygon(X2,Y2-i,X1,Y1-i,X3,Y3-i,X0,Y0-i, fill = "pink3")
        
def drawNewLineTop(app,canvas):
    for line in app.newLine:
        X0,Y0,X1,Y1,X2,Y2,X3,Y3 = line
        canvas.create_polygon(X2,Y2-21,X1,Y1-21,X3,Y3-21,X0,Y0-21,fill = "pink1")

def getScore(app):
    levelScore = (app.level-1)* 20
    row = app.line[0][0]
    app.score = row * 2 + levelScore +app.currSocre

def drawScore(app, canvas):
    canvas.create_text(80, 50, text = f"Score: {int(app.score)}", 
                    font='Arial 30 bold italic', fill = "cyan4")


#if head block overlaps(collides) with the wall, return gameOver
def checkGameOver(app):
    r = app.line[0][0]
    c = app.line[0][1]
    x0,y0,x1,y1 = getLineCellBound(app, r, c)
    map = app.map[::-1]
    #top-left
    mapCellRow = int(y0//app.mapCellHeight)
    mapCellCol = int(x0//app.mapCellWidth)
    print(0, mapCellCol)
    if map[mapCellRow][mapCellCol] != 1:
        app.gameOver = True
    #top-right
    mapCellRow = int(y0//app.mapCellHeight)
    mapCellCol = int(x1//app.mapCellWidth)
    if map[mapCellRow][mapCellCol] != 1:
        app.gameOver = True   
    #bottom-left
    mapCellRow = int(y1//app.mapCellHeight)
    mapCellCol = int(x0//app.mapCellWidth)
    if map[mapCellRow][mapCellCol] != 1:
        app.gameOver = True   
    #bottom-right
    mapCellRow = int(y1//app.mapCellHeight)
    mapCellCol = int(x1//app.mapCellWidth)
    if map[mapCellRow][mapCellCol] != 1:
        app.gameOver = True
    
def drawGameOver(app,canvas):
    canvas.create_text(app.width/2, app.height/2, text = "Game Over!",
    font = 'Arial 90 bold italic', fill = "black")  


def initLevel(app):
    app.rotateCell = []
    app.rotate = False
    app.smallCubes = []
    app.rotateCube = []
    
def checkLevelUp(app):
    r = app.line[0][0]
    c = app.line[0][1]
    x0,y0,x1,y1 = getLineCellBound(app, r, c)
    mapCellRow = int(y0//app.mapCellHeight)
    mapCellCol = int(x0//app.mapCellWidth)
    if mapCellRow == 11:
        app.levelUp = True
        app.level += 1
        app.currScore = app.score
        #keep track of the column position of the line
        app.restartPosition = [int(c),mapCellCol]
        restartGame(app)
        initLevel(app)

def createNewMap(app,position,rows):
    lineCol, mapCol = position
    app.mapRows = rows
    app.mapCols = 8
    app.map = [ ([0] * app.mapCols) for row in range(app.mapRows) ]
    app.map[rows-1][mapCol] = 1
    app.map[rows-2][mapCol] = 1
    app.map[rows-3][mapCol] = 1
    if app.level == 3:
        app.map[1] = [2] * app.mapCols
        app.map[2] = [2] * app.mapCols
        app.map[3] = [2] * app.mapCols
    app.currPath = (rows-3,mapCol)
    app.dir = "up"
    generatePath(app)
    
def createNewLine(app,position):
    lineCol, mapCol = position
    app.lineCellHeight = app.height / 25
    app.lineCellWidth = app.width / 30
    app.line = [[0, lineCol]]
    app.lineDir = (app.speed,0)

def restartGame(app):
    app.newLine = []
    lineCol, mapCol = app.restartPosition
    createNewMap(app,[lineCol, mapCol],13) 
    createNewLine(app,[lineCol, mapCol])
    app.levelUp = False
    app.redCube = []
    app.rotateCoord = []
    

def checkWin(app):
    if app.level == 3:
        r = app.line[0][0]
        c = app.line[0][1]
        x0,y0,x1,y1 = getLineCellBound(app, r, c)
        mapCellRow = int(y0//app.mapCellHeight)
        mapCellCol = int(x0//app.mapCellWidth)
        if mapCellRow == 9:
            app.win = True

def getCells(app,cell):
    row,col = cell
    map = app.map[::-1]
    for i in range(0,col):
        if map[row][i+1] == 1 and map[row][i] != 1:
            if [row,i] not in app.rotateCell:
                app.rotateCell.append([row,i])
    for j in range(col,len(map[0])):
        if map[row][j-1] == 1 and map[row][j] != 1:
            if [row,j] not in app.rotateCell:
                app.rotateCell.append([row,j])
           
def makeSmallCubes(app):
    r = app.line[0][0]
    c = app.line[0][1]
    x0,y0,x1,y1 = getLineCellBound(app, r, c)
    mapCellRow = int(y0//app.mapCellHeight)
    mapCellCol = int(x0//app.mapCellWidth)
    if mapCellRow >= 0 :
        cell = [mapCellRow, mapCellCol]
        getCells(app,cell)

def generateSmallCube(app):
    for cell in app.rotateCell:
        x0, y0, x1, y1 = getMapCellBound(app, cell[0],cell[1])
        cubex0 = x0 + 30
        cubey0 = y0 + 20
        cubex1 = x1 - 30
        cubey1 = y1 - 20
        #need to calculate the coordinates for four points of one cell
        vecX0, vecY0 = get2DCoord(app,cubex0,cubey0,20)
        vecX1, vecY1 = get2DCoord(app,cubex1,cubey1,20)
        vecX2, vecY2 = get2DCoord(app,cubex0,cubey1,20)
        vecX3, vecY3 = get2DCoord(app,cubex1,cubey0,20)
        #calculate the coordinates in tkinter
        X0, Y0 = getPythonCoord(app,vecX0, vecY0)
        X1, Y1 = getPythonCoord(app,vecX1, vecY1)
        X2, Y2 = getPythonCoord(app,vecX2, vecY2)
        X3, Y3 = getPythonCoord(app,vecX3, vecY3)
        if [X0, Y0, X1, Y1, X2, Y2, X3, Y3] not in app.smallCubes:
            app.smallCubes.append([X0, Y0, X1, Y1, X2, Y2, X3, Y3])

########################
# Create Rotating Cube #
########################

def findRedCube(app):
    map = app.map[::-1]
    for row in range(3,len(map)-2):
        for col in range(len(map[0])):
            if map[row][col] == 1:
                app.redCube.append([row,col])
    app.redCube = random.choice(app.redCube)
    x0,y0,x1,y1 = getMapCellBound(app,app.redCube[0],app.redCube[1])
    x0 += 40
    x1 -= 40
    y0 += 20
    y1 -= 20
    app.rotateCube = [x0,y0,x1,y0,x0,y1,x1,y1]
    generateCube(app)


def getRotateCoord(app, x, y, deg, axis):
    x0,y0 = axis
    X = (x-x0)*math.cos(deg*math.pi/180) - (y - y0)*math.sin(deg*math.pi/180)
    Y = (y - y0)*math.cos(deg*math.pi/180) + (x - x0)*math.sin(deg*math.pi/180)
    newX = x0 + X
    newY = y0 + Y
    return newX,newY

def generateCube(app):
    x2,y2,x0,y0,x1,y1,x3,y3 = app.rotateCube
    #need to calculate the coordinates for four points of one cell
    vecX0, vecY0 = get2DCoord(app,x0,y0,0)
    vecX1, vecY1 = get2DCoord(app,x1,y1,0)
    vecX2, vecY2 = get2DCoord(app,x2,y2,0)
    vecX3, vecY3 = get2DCoord(app,x3,y3,0)
    #calculate the coordinates in tkinter
    X0, Y0 = getPythonCoord(app,vecX0, vecY0)
    X1, Y1 = getPythonCoord(app,vecX1, vecY1)
    X2, Y2 = getPythonCoord(app,vecX2, vecY2)
    X3, Y3 = getPythonCoord(app,vecX3, vecY3)
    app.rotateCoord = [X0,Y0,X1,Y1,X2,Y2,X3,Y3]
    

def rotateCubeCoord(app, position):
    x0, y0, x1, y1, x2, y2, x3, y3 = position
    axis = [x2 + (x3-x2)/2, y2 + (y3-y2)/2]
    X0,Y0 = getRotateCoord(app, x0, y0, 36, axis)
    X1,Y1 = getRotateCoord(app, x1, y1, 36, axis)
    X2,Y2 = getRotateCoord(app, x2, y2, 36, axis)
    X3,Y3 = getRotateCoord(app, x3, y3, 36, axis)
    return X0, Y0, X1, Y1, X2, Y2, X3, Y3

def rotateCube(app):
    app.rotateCoord = rotateCubeCoord(app, app.rotateCoord)

def drawRedCube(app,canvas):
    x0,y0,x1,y1,x2,y2,x3,y3 = app.rotateCoord
    for i in range(1,20):
        canvas.create_polygon(x2,y2-i,x1,y1-i,x3,y3-i,x0,y0-i,
                                            fill = "red")
    canvas.create_polygon(x2,y2,x1,y1,x3,y3,x0,y0,
                                            fill = "tomato")

def drawSmallCube(app, canvas):
    for cube in app.smallCubes:
        x0,y0,x1,y1,x2,y2,x3,y3 = cube 
        canvas.create_polygon(x2,y2,x1,y1,x3,y3,x0,y0,
                                    fill = "cyan4")
        for i in range(20):
            canvas.create_polygon(x2,y2-i,x1,y1-i,x3,y3-i,x0,y0-i,
                                    fill = "turquoise")
        canvas.create_polygon(x2,y2-21,x1,y1-21,x3,y3-21,x0,y0-21,
                                    fill = "pink1")

def drawWin(app,canvas):
    canvas.create_text(app.width/2, app.height/2 + 4, text = "YOU WIN!!!",
    font = 'Arial 90 bold italic', fill = "pink1")
    canvas.create_text(app.width/2 + 6, app.height/2, text = "YOU WIN!!!",
    font = 'Arial 90 bold italic', fill = "white")

def checkGetRedCube(app):
    r = app.line[0][0]
    c = app.line[0][1]
    x0,y0,x1,y1 = getLineCellBound(app, r, c)
    mapCellRow = int(y0//app.mapCellHeight)
    mapCellCol = int(x0//app.mapCellWidth)
    redR, redC = app.redCube[0], app.redCube[1]
    if mapCellRow == redR and mapCellCol == redC:
        app.score += 20
        app.redCube = []

def threeDMode_timerFired(app):
    if not app.gameOver and not app.win and not app.pause:
        if round(time.time() - app.startT) % 1 == 0:
            takeStep(app)
            changeLine(app)
            #checkGameOver(app)
            checkLevelUp(app)
            makeSmallCubes(app)
            getScore(app)
            checkWin(app)  
            generateSmallCube(app)
            if app.rotateCube != []:
                rotateCube(app)
            if app.redCube == []:
                findRedCube(app)
            checkGetRedCube(app)

def threeDMode_redrawAll(app, canvas):
    #draw background
    if not app.levelUp:
        canvas.create_rectangle(0,0, app.width, app.height, fill = "light cyan")
        drawNewMap(app,canvas)
        drawNewLineBottom(app,canvas)
        if app.redCube != []:
            drawRedCube(app,canvas)
        drawWall(app,canvas)
        drawNewLineTop(app,canvas)
        drawScore(app, canvas)
        drawSmallCube(app, canvas)
    if app.gameOver:
        drawGameOver(app,canvas)
    if app.win:
        drawWin(app, canvas)


def appStarted(app):
    app.start = False
    app.mode = "splashScreenMode"
    app.speed = 0.5
    initLine(app)
    initMap(app)
    init3D(app)
    app.gameOver = False
    app.startT = time.time()
    app.currT = time.time()
    loadImage(app)
    app.score = 0
    initLevel(app)
    app.win = False
    app.currSocre = 0
    app.pause = False
    app.levelUp = False
    app.level = 1
    app.restartPosition = [0,0]
    app.redCube = []
    app.rotateCoord = []


def playDancingLine():
    runApp(width = 1080, height = 720)

def main():
    playDancingLine()

if __name__ == '__main__':
    main()
