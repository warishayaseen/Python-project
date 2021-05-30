
'''The following code is made by taking help for variuos github codes and youtube tutorials.
But some of the code is original and mine'''


import graphics
import random

#Functions to play and draw the game
def playGame(): #Game Start Point
    '''Constructor to choose and select the background and diffculty 
    for gameplay'''
    youWin = graphics.GraphWin("Connect Four Game", 1000, 650)
    youWin.setCoords(0, 0, 1000, 650)
    back = graphics.color_rgb(255,255,224)
    youWin.setBackground(back)
    locationDifficulty =opening(youWin)
    location=locationDifficulty[0]
    difficulty=locationDifficulty[1]
    strategy = ComputerStrategy(difficulty)
    gameBoard = Board()
    gamePlay(youWin,location, gameBoard, difficulty,strategy)
    tryAgain(youWin,gameBoard)

def opening(youWin):
    '''Makes the initial grouping to the game where players pick 

a trouble setting and foundation for playing 

Boundary: 

youWin - window the graphic is brought into'''
    welcome = graphics.Text(graphics.Point(500, 550), 
                            'WELCOME TO CONNECT FOUR!!!')
    welcome.setStyle('bold')
    welcome.setFace('arial')
    welcome.setSize(36)
    welcome.setTextColor('Midnight Blue')
    welcome.draw(youWin)
    choice1 = graphics.Text(graphics.Point(500, 450), 
                            'Select Where You Would Like To Play!')
    choice1.setFace('arial')
    choice1.setSize(20)
    choice1.setTextColor('Midnight Blue')
    choice1.draw(youWin)

    #chooses a place screen
    saylesBack = graphics.Rectangle(graphics.Point(675,100), 
                                    graphics.Point(970, 325))
    saylesBack.setFill('black')
    saylesBack.draw(youWin)
    saylesBox=graphics.Image(graphics.Point(822.5,212.5),"saylesTN.gif")
    saylesBox.draw(youWin)
    saylesText = graphics.Text(graphics.Point(822.5,212.5), 'Sayles')
    saylesText.setFace('arial')
    saylesText.setSize(30)
    saylesText.setStyle("bold")
    saylesText.setTextColor("white")
    saylesText.draw(youWin)

    cmcBack = graphics.Rectangle(graphics.Point(30,100), 
                                 graphics.Point(325, 325))
    cmcBack.setFill('black')
    cmcBack.draw(youWin)
    cmcBox=graphics.Image(graphics.Point(177.5,212.5),"cmcTN.gif")
    cmcBox.draw(youWin)
    cmcText = graphics.Text(graphics.Point(177.5,212.5), 'CMC')
    cmcText.setFace('arial')
    cmcText.setSize(30)
    cmcText.setStyle("bold")
    cmcText.setTextColor("white")
    cmcText.draw(youWin)

    bsBack = graphics.Rectangle(graphics.Point(347.5,100), 
                                graphics.Point(652.5, 325))
    bsBack.setFill('black')
    bsBack.draw(youWin)
    baldBox=graphics.Image(graphics.Point(500,212.5),"baldTN.gif")
    baldBox.draw(youWin)
    baldText = graphics.Text(graphics.Point(500,212.5), 'Bald Spot')
    baldText.setFace('arial')
    baldText.setSize(30)
    baldText.setStyle("bold")
    baldText.setTextColor("white")
    baldText.draw(youWin)

    location=getBackground(youWin)

    baldText.undraw()
    baldBox.undraw()
    bsBack.undraw()
    cmcText.undraw()
    cmcBox.undraw()
    cmcBack.undraw()
    saylesText.undraw()
    saylesBox.undraw()
    saylesBack.undraw()
    choice1.undraw()

    #Chooses a difficulty screen
    choice2 = graphics.Text(graphics.Point(500, 450), 
                            'Select A Difficulty Level! \n \n  Human Player Will Play First')
    choice2.setFace('arial')
    choice2.setSize(18)
    choice2.setTextColor('Midnight Blue')
    choice2.draw(youWin)

    easy = graphics.Rectangle(graphics.Point(250,325),graphics.Point(490,275))
    easy.setFill('green')
    easyText = graphics.Text(graphics.Point(370,300),"EASY")
    easyText.setFace('arial')
    easyText.setSize(24)
    easyText.setTextColor("White")
    easy.draw(youWin)
    easyText.draw(youWin)

    medium = graphics.Rectangle(graphics.Point(510,325),graphics.Point(750,275))
    medium.setFill('gold')
    mediumText = graphics.Text(graphics.Point(630,300),"MEDIUM")
    mediumText.setFace('arial')
    mediumText.setSize(24)
    mediumText.setTextColor("White")
    medium.draw(youWin)
    mediumText.draw(youWin)

    advanced = graphics.Rectangle(graphics.Point(510,265),graphics.Point(750,215))
    advanced.setFill('black')
    advancedText = graphics.Text(graphics.Point(630,240),"ADVANCED")
    advancedText.setFace('arial')
    advancedText.setSize(24)
    advancedText.setTextColor("White")
    advanced.draw(youWin)
    advancedText.draw(youWin)

    hard = graphics.Rectangle(graphics.Point(250,265),graphics.Point(490,215))
    hard.setFill('red')
    hardText = graphics.Text(graphics.Point(370,240),"HARD")
    hardText.setFace('arial')
    hardText.setSize(24)
    hardText.setTextColor("White")
    hard.draw(youWin)
    hardText.draw(youWin)

    difficulty = getDifficulty(youWin)
    return [location,difficulty]

def gamePlay(youWin,location, gameBoard, difficulty,strategy):
    '''Draws the gameBoard for Connect Four the area picked by the player 

Boundary: 

youWin - window the graphic is brought into 

area - picture record of the area picked by the player 

gameBoard - rundown of records containing pieces 

trouble - the snap of the client used to pick procedure 

procedure - the PC's method of picking where to put a piece
    '''
    gamePlace = graphics.Image(graphics.Point(500,325), location)
    gamePlace.draw(youWin)
    grid=graphics.Image(graphics.Point(500,300),"CFBoard.gif")
    grid.draw(youWin)
    getFour=False
    turnCount=0
    while getFour==False:
        if turnCount%2==0:
            playerColor="maize"
            setColumn = getHumanColumn(youWin)
        else:
            playerColor="blue"
            if strategy.strategyReturn() == "easy":
                setColumn = strategy.easy()
            if strategy.strategyReturn() == "medium":
                setColumn = strategy.medium(gameBoard)
            if strategy.strategyReturn() == "hard":
                setColumn = strategy.hard(gameBoard)
            if strategy.strategyReturn() == "advanced":
                setColumn = strategy.advanced(gameBoard)
        filledSpot=gameBoard.getTileCoordinate(setColumn,playerColor)
        gameBoard.playTile(filledSpot,playerColor)
        tileFall(youWin,filledSpot,playerColor)
        end=gameBoard.checkForWin()
        if end=="win":
            drawWin(youWin)
            getFour=True  
        elif end =="loss":
            drawLoss(youWin)
            getFour=True
        elif end == "tie":
            drawTie(youWin)
            getFour = True
        else:
            turnCount+=1
    youWin.getMouse()

def getBackground(youWin):
    """Decides wanted background for game dependent on clicks by client 

Boundary
    youWin - window the graphic is drawn into"""
    back = False
    while back ==False:
        userClick=youWin.getMouse()
        if int(userClick.getX()) in range(675,970) and int(userClick.getY()) in range(100,325):
            image = "sayles.gif"
            back=True
            return image
        elif int(userClick.getX()) in range(30,325) and int(userClick.getY()) in range(100,325):
            image= "cmc.gif"
            back=True
            return image
        elif int(userClick.getX()) in range(348,653) and int(userClick.getY()) in range(100,325):
            image = "bald.gif"
            back=True
            return image      
        
def getDifficulty(youWin):  #Sets the game difficulty
    """Decides wanted difficulty level (hard, easy, medium or advanced) of game, given graphical client input 

Boundary:
    youWin - window the graphic is drawn into
    """
    userClick=youWin.getMouse()
    if int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(275,325):
        difficulty = 1 #makes easy
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(275,325):
        difficulty = 2 #makes medium
    elif int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(215,265):
        difficulty = 3 #makes hard
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(215,265):
        difficulty = 4 #make advanced 
    else:
        difficulty=getDifficulty(youWin)
    return difficulty
        
def getHumanColumn(youWin): # This functions returns the segment chose by the human player through clicks
    
    userClick = youWin.getMouse()
    if int(userClick.getX()) in range(190,265):
        setColumn = 0
    elif int(userClick.getX()) in range(275,355):
        setColumn = 1
    elif int(userClick.getX()) in range(370,445):
        setColumn=2
    elif int(userClick.getX()) in range(455,535):
        setColumn=3
    elif int(userClick.getX()) in range(555,625):
        setColumn=4
    elif int(userClick.getX()) in range(635,715):
        setColumn=5
    elif int(userClick.getX()) in range(725,805):
        setColumn=6
    else:
        setColumn=getHumanColumn(youWin)
    return setColumn

def tileFall(youWin, coordinate, playerColor): # This functions animates/shows the tile fall through the gameBoard

    if int(coordinate[0])==0:
        xCoord=224
    if int(coordinate[0])==1:
        xCoord=314
    if int(coordinate[0])==2:
        xCoord=404
    if int(coordinate[0])==3:
        xCoord=494
    if int(coordinate[0])==4:
        xCoord=586
    if int(coordinate[0])==5:
        xCoord=675
    if int(coordinate[0])==6:
        xCoord=766
    if coordinate[1]==5:
        yCoord=80
    if coordinate[1]==4:
        yCoord=170
    if coordinate[1]==3:
        yCoord=260
    if coordinate[1]==2:
        yCoord=350
    if coordinate[1]==1:
        yCoord=440
    if coordinate[1]==0:
        yCoord=530
    if playerColor=="maize":
        color="gold"
    elif playerColor=="blue":
        color="blue"
    playerPiece = graphics.Circle(graphics.Point(xCoord,600),38)
    i=0
    #makes sure piece begins animating at the top of the gameBoard
    if yCoord < 500: 
        while (600-i) > yCoord +100:
            i += 20 #animates piece
            #playerPiece.undraw()
            playerPiece=graphics.Circle(graphics.Point(xCoord,600-i),38)
            playerPiece.setFill(color)
            playerPiece.draw(youWin)
            playerPiece.undraw()
    playerPiece = graphics.Circle(graphics.Point(xCoord,yCoord),38)
    playerPiece.setFill(color)
    playerPiece.draw(youWin)

def drawWin(youWin): #This function draws stars all over screen if user wins the game
    
    for i in range (0, 1200, 100):
        for j in range(0, 800, 100):
            winStar = graphics.Image(graphics.Point(i, j),"goldstar.gif")
            winStar.draw(youWin)
    finalStar = graphics.Image(graphics.Point(500,325),"goldstar.gif")
    finalStar.draw(youWin)
    winText = graphics.Text(graphics.Point(500, 325), "YOU WIN!")
    winText.setFace("arial")
    winText.setStyle('bold')
    winText.setSize(36)
    winText.draw(youWin)
def drawLoss(youWin): # This function draws sad faces all over screen if human user loses 
    
    for i in range (0, 1200, 100):
         for j in range(0, 800, 100):
            loseFace = graphics.Image(graphics.Point(i, j),"lose.gif")
            loseFace.draw(youWin)
    finalLose = graphics.Circle(graphics.Point(500,325),150)
    finalLose.setFill("blue")
    finalLose.draw(youWin)
    loseText = graphics.Text(graphics.Point(500, 325), "Computer Wins")
    loseText.setFace("arial")
    loseText.setStyle('bold')
    loseText.setSize(36)
    loseText.draw(youWin)

def drawTie(youWin):#This function draws tiles over the screen to indicate a draw/tie game
   
    for i in range (0, 1200, 100):
        for j in range(0, 800, 100):
            tie = graphics.Image(graphics.Point(i, j),"tie.gif")
            tie.draw(youWin)
    finalTie = graphics.Image(graphics.Point(500,325),"finalTie.gif")
    finalTie.draw(youWin)
    tieText = graphics.Text(graphics.Point(500, 250), "It's a tie!")
    tieText.setFace("arial")
    tieText.setStyle('bold')
    tieText.setSize(36)
    tieText.draw(youWin)        

def tryAgain(youWin,gameBoard): # Ask user to startover again
    
    backColor = graphics.color_rgb(255,255,224)
    back = graphics.Rectangle(graphics.Point(0,0),graphics.Point(1000,650))
    back.setFill(backColor)
    back.draw(youWin)
    replay = graphics.Text(graphics.Point(500,550),"Would you like to play again?")
    replay.setStyle('bold')
    replay.setFace('arial')
    replay.setSize(36)
    replay.setTextColor('Midnight Blue')
    replay.draw(youWin)
    yes = graphics.Rectangle(graphics.Point(250,325),graphics.Point(490,275))
    yes.setFill('green')
    yesText = graphics.Text(graphics.Point(370,300),"YES")
    yesText.setFace('arial')
    yesText.setSize(24)
    yesText.setTextColor("White")
    yes.draw(youWin)
    yesText.draw(youWin)
    no = graphics.Rectangle(graphics.Point(510,325),graphics.Point(750,275))
    no.setFill('gray')
    noText = graphics.Text(graphics.Point(630,300),"NO")
    noText.setFace('arial')
    noText.setSize(24)
    noText.setTextColor("White")
    no.draw(youWin)
    noText.draw(youWin)
    userClick=youWin.getMouse()
    if int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(275,325):
        gameBoard.resetBoard()
        playGame()
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(275,325):
        return

'''The following code is made by taking help for variuos github codes and youtube tutorials.
But some of the code is original and mine'''


import graphics
import random

#Functions to play and draw the game
def playGame(): #Game Start Point
    '''Constructor to choose and select the background and diffculty 
    for gameplay'''
    youWin = graphics.GraphWin("Connect Four Game", 1000, 650)
    youWin.setCoords(0, 0, 1000, 650)
    back = graphics.color_rgb(255,255,224)
    youWin.setBackground(back)
    locationDifficulty =opening(youWin)
    location=locationDifficulty[0]
    difficulty=locationDifficulty[1]
    strategy = ComputerStrategy(difficulty)
    gameBoard = Board()
    gamePlay(youWin,location, gameBoard, difficulty,strategy)
    tryAgain(youWin,gameBoard)

def opening(youWin):
    '''Makes the initial grouping to the game where players pick 

a trouble setting and foundation for playing 

Boundary: 

youWin - window the graphic is brought into'''
    welcome = graphics.Text(graphics.Point(500, 550), 
                            'WELCOME TO CONNECT FOUR!!!')
    welcome.setStyle('bold')
    welcome.setFace('arial')
    welcome.setSize(36)
    welcome.setTextColor('Midnight Blue')
    welcome.draw(youWin)
    choice1 = graphics.Text(graphics.Point(500, 450), 
                            'Select Where You Would Like To Play!')
    choice1.setFace('arial')
    choice1.setSize(20)
    choice1.setTextColor('Midnight Blue')
    choice1.draw(youWin)

    #chooses a place screen
    saylesBack = graphics.Rectangle(graphics.Point(675,100), 
                                    graphics.Point(970, 325))
    saylesBack.setFill('black')
    saylesBack.draw(youWin)
    saylesBox=graphics.Image(graphics.Point(822.5,212.5),"saylesTN.gif")
    saylesBox.draw(youWin)
    saylesText = graphics.Text(graphics.Point(822.5,212.5), 'Sayles')
    saylesText.setFace('arial')
    saylesText.setSize(30)
    saylesText.setStyle("bold")
    saylesText.setTextColor("white")
    saylesText.draw(youWin)

    cmcBack = graphics.Rectangle(graphics.Point(30,100), 
                                 graphics.Point(325, 325))
    cmcBack.setFill('black')
    cmcBack.draw(youWin)
    cmcBox=graphics.Image(graphics.Point(177.5,212.5),"cmcTN.gif")
    cmcBox.draw(youWin)
    cmcText = graphics.Text(graphics.Point(177.5,212.5), 'CMC')
    cmcText.setFace('arial')
    cmcText.setSize(30)
    cmcText.setStyle("bold")
    cmcText.setTextColor("white")
    cmcText.draw(youWin)

    bsBack = graphics.Rectangle(graphics.Point(347.5,100), 
                                graphics.Point(652.5, 325))
    bsBack.setFill('black')
    bsBack.draw(youWin)
    baldBox=graphics.Image(graphics.Point(500,212.5),"baldTN.gif")
    baldBox.draw(youWin)
    baldText = graphics.Text(graphics.Point(500,212.5), 'Bald Spot')
    baldText.setFace('arial')
    baldText.setSize(30)
    baldText.setStyle("bold")
    baldText.setTextColor("white")
    baldText.draw(youWin)

    location=getBackground(youWin)

    baldText.undraw()
    baldBox.undraw()
    bsBack.undraw()
    cmcText.undraw()
    cmcBox.undraw()
    cmcBack.undraw()
    saylesText.undraw()
    saylesBox.undraw()
    saylesBack.undraw()
    choice1.undraw()

    #Chooses a difficulty screen
    choice2 = graphics.Text(graphics.Point(500, 450), 
                            'Select A Difficulty Level! \n \n  Human Player Will Play First')
    choice2.setFace('arial')
    choice2.setSize(18)
    choice2.setTextColor('Midnight Blue')
    choice2.draw(youWin)

    easy = graphics.Rectangle(graphics.Point(250,325),graphics.Point(490,275))
    easy.setFill('green')
    easyText = graphics.Text(graphics.Point(370,300),"EASY")
    easyText.setFace('arial')
    easyText.setSize(24)
    easyText.setTextColor("White")
    easy.draw(youWin)
    easyText.draw(youWin)

    medium = graphics.Rectangle(graphics.Point(510,325),graphics.Point(750,275))
    medium.setFill('gold')
    mediumText = graphics.Text(graphics.Point(630,300),"MEDIUM")
    mediumText.setFace('arial')
    mediumText.setSize(24)
    mediumText.setTextColor("White")
    medium.draw(youWin)
    mediumText.draw(youWin)

    advanced = graphics.Rectangle(graphics.Point(510,265),graphics.Point(750,215))
    advanced.setFill('black')
    advancedText = graphics.Text(graphics.Point(630,240),"ADVANCED")
    advancedText.setFace('arial')
    advancedText.setSize(24)
    advancedText.setTextColor("White")
    advanced.draw(youWin)
    advancedText.draw(youWin)

    hard = graphics.Rectangle(graphics.Point(250,265),graphics.Point(490,215))
    hard.setFill('red')
    hardText = graphics.Text(graphics.Point(370,240),"HARD")
    hardText.setFace('arial')
    hardText.setSize(24)
    hardText.setTextColor("White")
    hard.draw(youWin)
    hardText.draw(youWin)

    difficulty = getDifficulty(youWin)
    return [location,difficulty]

def gamePlay(youWin,location, gameBoard, difficulty,strategy):
    '''Draws the gameBoard for Connect Four the area picked by the player 

Boundary: 

youWin - window the graphic is brought into 

area - picture record of the area picked by the player 

gameBoard - rundown of records containing pieces 

trouble - the snap of the client used to pick procedure 

procedure - the PC's method of picking where to put a piece
    '''
    gamePlace = graphics.Image(graphics.Point(500,325), location)
    gamePlace.draw(youWin)
    grid=graphics.Image(graphics.Point(500,300),"CFBoard.gif")
    grid.draw(youWin)
    getFour=False
    turnCount=0
    while getFour==False:
        if turnCount%2==0:
            playerColor="maize"
            setColumn = getHumanColumn(youWin)
        else:
            playerColor="blue"
            if strategy.strategyReturn() == "easy":
                setColumn = strategy.easy()
            if strategy.strategyReturn() == "medium":
                setColumn = strategy.medium(gameBoard)
            if strategy.strategyReturn() == "hard":
                setColumn = strategy.hard(gameBoard)
            if strategy.strategyReturn() == "advanced":
                setColumn = strategy.advanced(gameBoard)
        filledSpot=gameBoard.getTileCoordinate(setColumn,playerColor)
        gameBoard.playTile(filledSpot,playerColor)
        tileFall(youWin,filledSpot,playerColor)
        end=gameBoard.checkForWin()
        if end=="win":
            drawWin(youWin)
            getFour=True  
        elif end =="loss":
            drawLoss(youWin)
            getFour=True
        elif end == "tie":
            drawTie(youWin)
            getFour = True
        else:
            turnCount+=1
    youWin.getMouse()

def getBackground(youWin):
    """Decides wanted background for game dependent on clicks by client 

Boundary
    youWin - window the graphic is drawn into"""
    back = False
    while back ==False:
        userClick=youWin.getMouse()
        if int(userClick.getX()) in range(675,970) and int(userClick.getY()) in range(100,325):
            image = "sayles.gif"
            back=True
            return image
        elif int(userClick.getX()) in range(30,325) and int(userClick.getY()) in range(100,325):
            image= "cmc.gif"
            back=True
            return image
        elif int(userClick.getX()) in range(348,653) and int(userClick.getY()) in range(100,325):
            image = "bald.gif"
            back=True
            return image      
        
def getDifficulty(youWin):  #Sets the game difficulty
    """Decides wanted difficulty level (hard, easy, medium or advanced) of game, given graphical client input 

Boundary:
    youWin - window the graphic is drawn into
    """
    userClick=youWin.getMouse()
    if int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(275,325):
        difficulty = 1 #makes easy
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(275,325):
        difficulty = 2 #makes medium
    elif int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(215,265):
        difficulty = 3 #makes hard
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(215,265):
        difficulty = 4 #make advanced 
    else:
        difficulty=getDifficulty(youWin)
    return difficulty
        
def getHumanColumn(youWin): # This functions returns the segment chose by the human player through clicks
    
    userClick = youWin.getMouse()
    if int(userClick.getX()) in range(190,265):
        setColumn = 0
    elif int(userClick.getX()) in range(275,355):
        setColumn = 1
    elif int(userClick.getX()) in range(370,445):
        setColumn=2
    elif int(userClick.getX()) in range(455,535):
        setColumn=3
    elif int(userClick.getX()) in range(555,625):
        setColumn=4
    elif int(userClick.getX()) in range(635,715):
        setColumn=5
    elif int(userClick.getX()) in range(725,805):
        setColumn=6
    else:
        setColumn=getHumanColumn(youWin)
    return setColumn

def tileFall(youWin, coordinate, playerColor): # This functions animates/shows the tile fall through the gameBoard

    if int(coordinate[0])==0:
        xCoord=224
    if int(coordinate[0])==1:
        xCoord=314
    if int(coordinate[0])==2:
        xCoord=404
    if int(coordinate[0])==3:
        xCoord=494
    if int(coordinate[0])==4:
        xCoord=586
    if int(coordinate[0])==5:
        xCoord=675
    if int(coordinate[0])==6:
        xCoord=766
    if coordinate[1]==5:
        yCoord=80
    if coordinate[1]==4:
        yCoord=170
    if coordinate[1]==3:
        yCoord=260
    if coordinate[1]==2:
        yCoord=350
    if coordinate[1]==1:
        yCoord=440
    if coordinate[1]==0:
        yCoord=530
    if playerColor=="maize":
        color="gold"
    elif playerColor=="blue":
        color="blue"
    playerPiece = graphics.Circle(graphics.Point(xCoord,600),38)
    i=0
    #makes sure piece begins animating at the top of the gameBoard
    if yCoord < 500: 
        while (600-i) > yCoord +100:
            i += 20 #animates piece
            #playerPiece.undraw()
            playerPiece=graphics.Circle(graphics.Point(xCoord,600-i),38)
            playerPiece.setFill(color)
            playerPiece.draw(youWin)
            playerPiece.undraw()
    playerPiece = graphics.Circle(graphics.Point(xCoord,yCoord),38)
    playerPiece.setFill(color)
    playerPiece.draw(youWin)

def drawWin(youWin): #This function draws stars all over screen if user wins the game
    
    for i in range (0, 1200, 100):
        for j in range(0, 800, 100):
            winStar = graphics.Image(graphics.Point(i, j),"goldstar.gif")
            winStar.draw(youWin)
    finalStar = graphics.Image(graphics.Point(500,325),"goldstar.gif")
    finalStar.draw(youWin)
    winText = graphics.Text(graphics.Point(500, 325), "YOU WIN!")
    winText.setFace("arial")
    winText.setStyle('bold')
    winText.setSize(36)
    winText.draw(youWin)
def drawLoss(youWin): # This function draws sad faces all over screen if human user loses 
    
    for i in range (0, 1200, 100):
         for j in range(0, 800, 100):
            loseFace = graphics.Image(graphics.Point(i, j),"lose.gif")
            loseFace.draw(youWin)
    finalLose = graphics.Circle(graphics.Point(500,325),150)
    finalLose.setFill("blue")
    finalLose.draw(youWin)
    loseText = graphics.Text(graphics.Point(500, 325), "Computer Wins")
    loseText.setFace("arial")
    loseText.setStyle('bold')
    loseText.setSize(36)
    loseText.draw(youWin)

def drawTie(youWin):#This function draws tiles over the screen to indicate a draw/tie game
   
    for i in range (0, 1200, 100):
        for j in range(0, 800, 100):
            tie = graphics.Image(graphics.Point(i, j),"tie.gif")
            tie.draw(youWin)
    finalTie = graphics.Image(graphics.Point(500,325),"finalTie.gif")
    finalTie.draw(youWin)
    tieText = graphics.Text(graphics.Point(500, 250), "It's a tie!")
    tieText.setFace("arial")
    tieText.setStyle('bold')
    tieText.setSize(36)
    tieText.draw(youWin)        

def tryAgain(youWin,gameBoard): # Ask user to startover again
    
    backColor = graphics.color_rgb(255,255,224)
    back = graphics.Rectangle(graphics.Point(0,0),graphics.Point(1000,650))
    back.setFill(backColor)
    back.draw(youWin)
    replay = graphics.Text(graphics.Point(500,550),"Would you like to play again?")
    replay.setStyle('bold')
    replay.setFace('arial')
    replay.setSize(36)
    replay.setTextColor('Midnight Blue')
    replay.draw(youWin)
    yes = graphics.Rectangle(graphics.Point(250,325),graphics.Point(490,275))
    yes.setFill('green')
    yesText = graphics.Text(graphics.Point(370,300),"YES")
    yesText.setFace('arial')
    yesText.setSize(24)
    yesText.setTextColor("White")
    yes.draw(youWin)
    yesText.draw(youWin)
    no = graphics.Rectangle(graphics.Point(510,325),graphics.Point(750,275))
    no.setFill('gray')
    noText = graphics.Text(graphics.Point(630,300),"NO")
    noText.setFace('arial')
    noText.setSize(24)
    noText.setTextColor("White")
    no.draw(youWin)
    noText.draw(youWin)
    userClick=youWin.getMouse()
    if int(userClick.getX()) in range(250,490) and int(userClick.getY()) in range(275,325):
        gameBoard.resetBoard()
        playGame()
    elif int(userClick.getX()) in range(510,750) and int(userClick.getY()) in range(275,325):
        return


class Board: #This class will contain the gameBoard for Connect Four and functions that are necessary for game play 
    
    def __init__(self,board=[['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],
                      ['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],
                      ['.','.','.','.','.','.']]):
       
        self.gameBoard = board
    
    def resetBoard(self): #board returning to the initial state
        
        for item in self.getGameBoard():
            for i in range(6):
                item[i] = "."
        
    def getGameBoard(self): #Returns the gameBoard
        
        return self.gameBoard
        
    def getColumn(self, dictionary): #Returns the list of the column
        
        #outer list of the board is columns
        if "." in self.gameBoard[0]:
            dictionary["col0"] = self.gameBoard[0]
        if "." in self.gameBoard[1]:
            dictionary["col1"] = self.gameBoard[1]
        if "." in self.gameBoard[2]:
            dictionary["col2"] = self.gameBoard[2]
        if "." in self.gameBoard[3]:
            dictionary["col3"] = self.gameBoard[3]
        if "." in self.gameBoard[4]:
            dictionary["col4"] = self.gameBoard[4]
        if "." in self.gameBoard[5]:
            dictionary["col5"] = self.gameBoard[5]
        if "." in self.gameBoard[6]:
            dictionary["col6"] = self.gameBoard[6]
    
    def getRow(self, dictionary):  #Returns the list of the row
        
        # inner list of the board is rows
        rowList0 = []
        for i in range(0,7): #makes list for row 0
            rowList0.append(self.gameBoard[i][0])
        dictionary["row0"] = rowList0
        rowList1=[]
        for i in range(0,7): #makes list for row 1
            rowList1.append(self.gameBoard[i][1])
        dictionary["row1"] = rowList1
        rowList2=[]
        for i in range(0,7): #makes list for row 2
            rowList2.append(self.gameBoard[i][2])
        dictionary["row2"] = rowList2
        rowList3=[]
        for i in range(0,7):  #makes list for row 3
            rowList3.append(self.gameBoard[i][3])
        dictionary["row3"] = rowList3
        rowList4=[]
        for i in range(0,7): #makes list for row 4
            rowList4.append(self.gameBoard[i][4])
        dictionary["row4"] = rowList4
        rowList5=[]
        for i in range(0,7): #makes list for row 5
            rowList5.append(self.gameBoard[i][5])
        dictionary["row5"] = rowList5
        
    def getDiagonal(self, dictionary):
        
        # the keys for this are numbers, starting at the bottom left of the gameBoard 
        #row & col numbers begin at top left corner 
        #rows go from 0 to 5
        #cols go from 0 to 6
        acc = 0 # this wil change the diag number each time 
        for i in range(5, -1, -1): #row for loop beginning at 5th row
            currentDiag1 = []
            col = 0
            n = i
            while n < 6 and n >= 0: #n is row beginning at i
                tile = self.gameBoard[col][n]
                currentDiag1.append(tile)
                col+=1 # moves over the columns to the right 
                n+=1 #moves through rows downward
            dictionary["diag"+str(acc)] = currentDiag1  
            acc += 1
            currentDiag2 = []
            col= 0
            m = i
            while m < 6 and m > -1: #m is row beginning at i
                tile = self.gameBoard[col][m]
                currentDiag2.append(tile)
                col+=1 # moves over the columns to the right 
                m-=1 #moves through rows upwards
            dictionary["diag"+str(acc)] = currentDiag2
            acc+=1
        for i in range(0, 7, 1): #col is i, starts at top left moves right 
            currentDiag3 = []
            row = 0 #starts at row 0, top of board
            p = i
            while p < 7 and p > -1 and row < 6: #p is column 
                tile = self.gameBoard[p][row]
                currentDiag3.append(tile)
                row+=1 #moves down the rows
                p+=1 #moves across the columns
            dictionary["diag"+str(acc)] = currentDiag3
            acc+=1
            currentDiag4 = []
            row = 5 # starts at row 5, bottom of board
            q = i
            while q < 7 and q > -1 and row < 6: #q is column
                tile = self.gameBoard[q][row]
                currentDiag4.append(tile)
                row-=1 #moves up the rows
                q+=1 #moves right acorss the columns
            dictionary["diag"+str(acc)] = currentDiag4
            acc += 1
    
    def getTileCoordinate(self, setColumn, playerColor):
        
        originalColumn = setColumn
        for i in range(6):
            #when there is a filled spot in the column
            if self.gameBoard[int(setColumn)][i]=="blue" or self.gameBoard[int(setColumn)][i]=="maize":
                #if there is an empty spot above it
                if (i-1)<0 and playerColor=="maize":
                    while setColumn == originalColumn:
                        setColumn = getHumanColumn(youWin)
                elif (i-1)<0 and playerColor=="blue":
                    while setColumn == originalColumn:
                        for k in range(7):
                            if self.gameBoard[k][0] == '.':
                                setColumn = k      
                #return the coordinate of the first available row in the column
                else:
                    coordinate=(setColumn,i-1)
                    return coordinate
            elif self.gameBoard[setColumn]==[".",".",".",".",".","."]:
                coordinate=(setColumn,5)
                return coordinate
    
    def playTile(self, coordinate, playerColor):
        
        #sets the value at gameBoard in the correct column and row to either
        #"maize" or "blue" according to playerColor
        firstIndex=coordinate[0]
        secondIndex=coordinate[1]
        self.gameBoard[int(firstIndex)][int(secondIndex)]=playerColor
    
    def checkForWin(self): #Winning condition check
        dictionary={}
        self.getRow(dictionary)
        self.getColumn(dictionary)
        self.getDiagonal(dictionary)
        full = 'complete'
        while full == 'complete': #if the game is full, the game is a tie
            for column in self.gameBoard:
                for piece in column:
                    if piece == '.':
                        full = 'notComplete'
            if full == 'complete':
                return "tie" 
        for key in dictionary:
            winList=[]
            if len(dictionary[key])>=4: # if the length of the diagonal is at least four 
                for place in dictionary[key]:
                    if len(winList)==0: #creates list to count up to four of the pieces
                        winList.append(place)
                    else:
                        if winList[0]==place:
                            winList.append(place)
                        elif winList[0]!=place:
                            winList=[]
                            winList.append(place)
                    if len(winList)==4 and winList[0] == 'maize' and winList[3] =="maize":
                        return "win" #user wins the game
                    elif len(winList)==4 and winList[0]=="blue" and winList[3] == 'blue':
                        return "loss" #user loses the game
        return False
    
    
class ComputerStrategy: #Class for computer moves and plans
    
    def __init__(self, difficulty):
        
        if difficulty==1: #easy
            self.strategy = "easy"
        elif difficulty == 2: #medium
            self.strategy = "medium"
        elif difficulty == 3: #hard
            self.strategy  = "hard"
        elif difficulty == 4: #advanced
            self.strategy = "advanced"
    
    def strategyReturn(self):
                return self.strategy

    def easy(self):
        
        setColumn = random.randint(0,6)
        return setColumn
    
    def medium(self, gameBoard):
        
        dictionary ={}
        gameBoard.getRow(dictionary)
        gameBoard.getColumn(dictionary)
        longest = []#longest chain of desired color so far
        setColumn = -1
        for key in dictionary:
            checkList=[]#to build a list of longest of desired color for given key
            for place in dictionary[key]: # place is blue maize or . 
                if place==".":
                    checkList=[]
                elif place=="maize":
                    checkList=[]
                elif len(checkList)==0:
                    checkList.append(place) #place will be blue
                else:
                    if checkList[0]==place:#append to checkList if matching
                        checkList.append(place)
                if len(checkList) > len(longest) and place!=".":
                    longest = checkList[:]#copy checklist to longest
                    desiredKey = key #dict key containing current longest matches
                    index = dictionary[desiredKey].index(place) #the space of first item in list
                    if dictionary[desiredKey][index-1] == ".": #keeps from playing in filled spot
                        if len(longest) == 1 and index-4 >= 0: #keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        elif len(longest) == 2 and index-3 >=0:#keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        elif index-2>=0:#keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
        if setColumn not in range(0,7):# if none of the above conditions were true, play a random place
            setColumn = random.randint(0,6)
        return setColumn 
    
        
    def hard(self, gameBoard):
        
        firstMove = 0
        for item in gameBoard.getGameBoard():#checks items in the list of spaces in the board
            firstMove += item.count("maize") #adds the number of times that maize is present
        if firstMove == 1:#if only one maize on the board
            maize = -1
            while maize == -1:
                for item in gameBoard.getGameBoard():#checks items in the list of spaces in the board
                    if "maize" in item:
                        firstPiece=gameBoard.getGameBoard().index(item)#get the index of maize piece
                        maize = 0
            if firstPiece - 1>=0:#if index of maize is not 0
                setColumn = firstPiece - 1 #place the piece to the left of the maize piece to block row attempt
                return setColumn
        dictionary ={}
        gameBoard.getRow(dictionary)
        gameBoard.getColumn(dictionary)
        longest = []#longest chain of desired color so far
        setColumn = -1
        for key in dictionary:
            checkList=[]#to build a list of longest of desired color for given key
            for place in dictionary[key]: #blue maize or .
                if len(longest) == 3:
                    index = dictionary[desiredKey].index('maize')
                    if index-1>=0:
                        if dictionary[desiredKey][index-1] == ".":
                            setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                elif place==".":
                    checklist=[]
                elif place=="blue":
                    checklist=[]
                elif len(checkList)==0:
                    checkList.append(place)
                else:
                    if checkList[0]==place:#append to checkList if matching
                        checkList.append(place)
                if len(checkList) > len(longest) and place!=".":
                    longest = checkList[:]#copy checklist to longest
                    desiredKey = key#dict key containing current longest matches
                    index = dictionary[desiredKey].index(place)#the space of first item in list
                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                    if dictionary[desiredKey][index-1] == ".": #keeps from playing in filled spot
                        if len(longest) == 1 and index-4 >= 0: #keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        elif len(longest) == 2 and index-3 >=0:#keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        elif index-2>=0:#keeps from playing in useless spot
                                setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                if "maize" in longest and "row" in key:
                    firstMaizeInRow = dictionary[desiredKey].index("maize")
                    numMaizeInRow = len(longest)
                    checkBlue = -1
                    checkBalnk = -1
                    if firstMaizeInRow-1>=0:# makes sure its still in range 
                        checkBlue = dictionary[desiredKey][firstMaizeInRow-1]
                    if firstMaizeInRow +numMaizeInRow <= 6:# makes sure its still in range 
                        checkBlank = dictionary[desiredKey][firstMaizeInRow+numMaizeInRow]
                    if checkBlue == "blue":
                        setColumn = self.getColumnFromDictionary(firstMaizeInRow+numMaizeInRow+1,gameBoard,desiredKey,dictionary)
        if setColumn not in range(0,7):
            setColumn = random.randint(0,6)
        return setColumn 
        
    def advanced(self, gameBoard):
        
        firstMove = 0
        for item in gameBoard.getGameBoard():
            firstMove += item.count("maize")
        if firstMove == 1: # this makes sure it plays a piece next to the user's piece
            maize = False
            while maize == False:
                for item in gameBoard.getGameBoard():
                    if "maize" in item:
                        firstPiece=gameBoard.getGameBoard().index(item)
                        maize = True
            if firstPiece - 1 >= 0: #if there is a column to the left of the user piece 
                setColumn = firstPiece - 1
                return setColumn
        dictionary ={}
        gameBoard.getRow(dictionary)
        gameBoard.getColumn(dictionary)
        #longest chain of desired color so far
        longest = []
        setColumn = -1
        while setColumn ==-1:
            for key in dictionary:
                #to build a list of longest of desired color for given key
                checkList=[]
                #a win could theoretically occur here
                if len(dictionary[key])>=4:
                    for place in dictionary[key]: #blue maize or . i
                        if len(longest) == 3:
                            index = dictionary[desiredKey].index(longest[0])
                            if index-1>=0:
                                if dictionary[desiredKey][index-1] == ".":
                                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        if place==".":
                            checklist=[]
                        elif len(checkList)==0:
                            checkList.append(place)
                        else:
                            #append to checkList if matching
                            if checkList[0]==place:
                                checkList.append(place)
                            if checkList[0]!= place:
                                checkList= []
                                checkList.append(place)
                        if len(checkList) > len(longest):
                            longest = checkList
                            desiredKey = key
                            index = dictionary[desiredKey].index(place)
                            if dictionary[desiredKey][index-1] == ".": #keeps from playing in filled spot
                                if len(longest) == 1 and index-4 >= 0: #keeps from playing in useless spot
                                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                                elif len(longest) == 2 and index-3 >=0:#keeps from playing in useless spot
                                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                                elif index-2>=0:#keeps from playing in useless spot
                                    setColumn = self.getColumnFromDictionary(index, gameBoard, desiredKey, dictionary)
                        if "blue" in longest and len(longest)==3 and "row" in key:
                            firstBlueInRow = dictionary[desiredKey].index("blue")
                            numBlueInRow = len(longest)
                            checkLeft = -1
                            checkRight = -1
                            if firstBlueInRow-1>= 0: #makes sure its still in range 
                                checkLeft = dictionary[desiredKey][firstBlueInRow-1]
                            if firstBlueInRow +numBlueInRow <= 6: #makes sure its still in range 
                                checkRight = dictionary[desiredKey][firstBlueInRow+numBlueInRow]
                            if checkLeft == ".":
                                setColumn = self.getColumnFromDictionary(firstBlueInRow,gameBoard,desiredKey,dictionary)
                            if checkRight == ".":
                                setColumn = self.getColumnFromDictionary(firstBlueInRow+numMaizeInRow+1,gameBoard,desiredKey,dictionary)
                        if "maize" in longest and "row" in key and len(longest)>=2:
                            checkBlue = -1
                            checkBlank = -1
                            firstMaizeInRow = dictionary[desiredKey].index("maize")
                            numMaizeInRow = len(longest)
                            if firstMaizeInRow-1>=0: # makes sure its still in range 
                                checkBlue = dictionary[desiredKey][firstMaizeInRow-1]
                            if firstMaizeInRow +numMaizeInRow <= 6: #makes sure its still in range
                                checkBlank = dictionary[desiredKey][firstMaizeInRow+numMaizeInRow]
                            if checkBlue == "blue":
                                setColumn = self.getColumnFromDictionary(firstMaizeInRow+numMaizeInRow+1,gameBoard,desiredKey,dictionary)
                if setColumn not in range(0,7):# this will allow strategy to play a random column
                    setColumn = random.randint(0,6)
        return setColumn 
        

    def getColumnFromDictionary(self, index, gameBoard, desiredKey, dictionary):
        
        setColumn = None
        if 'col' in desiredKey:#if it is a column
            setColumn = int(desiredKey[3])#third item in column key is the int of column
            return setColumn
        elif 'row' in desiredKey:#if it is a row
            rowNum = int(desiredKey[3])#third item in row key is the int of the row
            if rowNum<5:#if not the last row
                if index-1 in range (0,6):#if not the first column
                    rowDown = dictionary["row"+str(rowNum+1)][index-1]#go one row down and one column to the left
                    if rowDown == ".":#if that space is empty
                        setColumn = random.randint(0,6)#just play randomly, playing there doesn't advance the goal
                    else:
                        setColumn = index-1#the spaces are filled up to the place you want to play, advances goal
            elif index -1 >= 0: #if not the first column
                setColumn = index - 1   
            else:
                setColumn = index
            return setColumn
        
if __name__=="__main__":
    playGame()
                      