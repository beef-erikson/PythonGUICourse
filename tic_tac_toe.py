from guizero import App, PushButton, Text, Box
from random import randint

app = App(layout="grid", title="Tic-Tac-Toe")

# Fields
player = randint(1,2)
symbol = ""
if player == 1:
    symbol = "X"
else:
    symbol = "O"
 
# Button clicked, passes button to placePiece
def clickTopLeft():
    placePiece(topLeft)

def clickTopCenter():
    placePiece(topCenter)

def clickTopRight():
    placePiece(topRight)

def clickMiddleLeft():
    placePiece(middleLeft)

def clickMiddleCenter():
    placePiece(middleCenter)

def clickMiddleRight():
    placePiece(middleRight)

def clickBottomLeft():
    placePiece(bottomLeft)

def clickBottomCenter():
    placePiece(bottomCenter)

def clickBottomRight():
    placePiece(bottomRight)

# Changes player symbol
def changeSymbol():
    global player
    global symbol
    if player == 1:
        player = 2
        symbol = "O"
    else:
        player = 1
        symbol = "X"

# Check for win
def checkWin():
    # Checks first row and first column wins
    if not topLeft.text == "  ":
        if (topLeft.text == topCenter.text == topRight.text or 
        topLeft.text == middleLeft.text == bottomLeft.text):
            changeSymbol()
            app.info("Win!", "Player " + str(player) + " has won!")
            exit()
    # Checks second row, second column and both diagonal wins
    if not middleCenter.text == "  ":
        if (middleLeft.text == middleCenter.text == middleRight.text or
        topCenter.text == middleCenter.text == bottomCenter.text or
        topLeft.text == middleCenter.text == bottomRight.text or
        topRight.text == middleCenter.text == bottomLeft.text):
            changeSymbol()
            app.info("Win!", "Player " + str(player) + " has won!")
            exit()
    # Checks third row and third column wins
    if not bottomRight.text == "  ":
        if (topRight.text == middleRight.text == bottomRight.text or
        bottomLeft.text == bottomCenter.text == bottomRight.text):
            changeSymbol()
            app.info("Win!", "Player " + str(player) + " has won!")
            exit()

# Places X or O
def placePiece(button):
    global player
    if button == topLeft and topLeft.text == "  ":
        topLeft.text = symbol
        changeSymbol()
    if button == topCenter and topCenter.text == "  ":
        topCenter.text = symbol
        changeSymbol()
    if button == topRight and topRight.text == "  ":
        topRight.text = symbol
        changeSymbol()
    if button == middleLeft and middleLeft.text == "  ":
        middleLeft.text = symbol
        changeSymbol()
    if button == middleCenter and middleCenter.text == "  ":
        middleCenter.text = symbol
        changeSymbol()
    if button == middleRight and middleRight.text == "  ":
        middleRight.text = symbol
        changeSymbol()
    if button == bottomLeft and bottomLeft.text == "  ":
        bottomLeft.text = symbol
        changeSymbol()
    if button == bottomCenter and bottomCenter.text == "  ":
        bottomCenter.text = symbol
        changeSymbol()
    if button == bottomRight and bottomRight.text == "  ":
        bottomRight.text = symbol
        changeSymbol()           
    checkWin()

# Defines grid
topLeft = PushButton(app, text="  ", command=clickTopLeft, grid=[0,0])
topCenter = PushButton(app, text="  ", command=clickTopCenter, grid=[1,0])
topRight = PushButton(app, text="  ", command=clickTopRight, grid=[2,0])
middleLeft = PushButton(app, text="  ", command=clickMiddleLeft, grid=[0,1])
middleCenter = PushButton(app, text="  ", command=clickMiddleCenter, grid=[1,1])
middleRight = PushButton(app, text="  ", command=clickMiddleRight, grid=[2,1])
bottomLeft = PushButton(app, text="  ", command=clickBottomLeft, grid=[0,2])
bottomCenter = PushButton(app, text="  ", command=clickBottomCenter, grid=[1,2])
bottomRight = PushButton(app, text="  ", command=clickBottomRight, grid=[2,2])

app.info("Player turn", "Player " + str(player) + " goes first.")
app.display()
