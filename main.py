import pgzrun
import random


WIDTH = 900
HEIGHT = 500

centerX = WIDTH / 2
centerY = HEIGHT / 2

center = (centerX, centerY)

fontColour = (0,0,0)

itemsTemplate = ["bag","bottle","battery","box"]

finalLevel = 4
startingSpeed = 7

gameOver = False
gameComplete = False

currentLevel = 1

currentItems = []
currentItemsAnimations = []

def getOptionsToCreate(howMany):
    listOfItems = ["box"]
    for i in range(howMany):
        chosen = random.choice(itemsTemplate)
        if not chosen == "box":
            listOfItems.append(chosen)
    return listOfItems

def createItems(chosenItems):
    fish = []
    for item in chosenItems:
        newItem = Actor(item)
        fish.append(newItem)
    return fish #Baked

def layoutItems(items):
    gaps = len(items) + 1
    gapSize = WIDTH / gaps
    for index,item in enumerate(items):
        x = (index + 1) * gapSize
        item.x = x

def animateItems(items):
    global currentItemsAnimations
    for i in items:
        duration = startingSpeed - currentLevel
        i.anchor = ("center", "bottom")
        animation = animate(i, duration=duration, on_finished=handleGameOver,y=HEIGHT)
        currentItemsAnimations.append(animation)
            

def makeItems(howMany):
    toCreate = getOptionsToCreate(howMany)
    newItems = createItems(toCreate)
    layoutItems(newItems)
    animateItems(newItems)
    return newItems

def handleGameOver():
    global gameOver
    gameOver = True

def stopAnims(toStop):
    for anim in toStop:
        if anim.running:
            anim.stop()

def handleGameComplete():
    global gameComplete
    global currentItems
    global currentItemsAnimations
    global currentLevel
    global finalLevel
    stopAnims(currentItemsAnimations)
    if currentLevel == finalLevel:
         gameComplete = True
    else:
        currentLevel += 1
        currentItems = []
        currentItemsAnimations = []
       

def on_mouse_down(pos):
    global currentLevel
    global currentItems
    for item in currentItems:
        if item.collidepoint(pos):
            if item.image == "box":
                handleGameComplete()
            else:
                handleGameOver()

def update():
    global currentItems,currentLevel
    
    if len(currentItems) == 0:
        
        currentItems = makeItems(currentLevel)
       
def draw():
    global currentItems,currentLevel,currentItemsAnimations

    screen.clear()
    screen.blit("stockphoto", (0,0))
    if gameOver:
        screen.draw.text("Try again!", fontsize=40, center=center, color=fontColour)
        screen.draw.text("You did not make it.", fontsize=20, center=(centerX, centerY + 25), color=fontColour)
    elif gameComplete:
        screen.draw.text("Well done!", fontsize=40, center=center, color=fontColour)
        screen.draw.text("You won the game.", fontsize=20, center=(centerX, centerY + 25), color=fontColour)
    else:
        
        for item in currentItems:
            item.draw()
 
pgzrun.go()