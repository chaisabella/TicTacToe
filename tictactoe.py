
from graphics import *

def createAndDrawBoard():
    """
    Creates a window and draws the board in it.

    returns: a GraphWin object
    """
    # Create the window
    win = GraphWin("Tic Tac Toe", 600, 600)
    win.setCoords(-0.25, -0.75, 3.25, 3.25)
    win.setBackground("white")

    # Draw the lines
    for i in range(1, 3):
        horizontalLine = Line(Point(0, i), Point(3, i))
        horizontalLine.draw(win)
        
        verticalLine = Line(Point(i, 0), Point(i, 3))
        verticalLine.draw(win)

    # Return the window
    return win

def setPlayerText(label, player):
    """
    Updates the player text label to indicate whose turn it is.

    label: a Text object
    player: 1 or 2
    """
    if player == 1:
        label.setText("Player 1, please place an X.")
    else:
        label.setText("Player 2, please place an O.")

def getGridLocation(point):
    """
    Returns the x,y grid coordinates of a point.

    point: a Point object
    returns: a pair of grid positions: x,y
    """
    gridX = int(point.getX())
    gridY = int(point.getY())
    return gridX, gridY

def isValidGridCell(boardState, gridX, gridY):
    """
    Returns a Boolean indicating whether the given grid position
    is a valid selection given the current board state.
    Also checks if the grid position is within the bounds of the board.

    boardState: a nested list containing the board state
    gridX: the grid x position
    gridY: the grid y position
    returns: True if a piece can be placed at (gridX, gridY),
             False otherwise
    """
    
    row = boardState[gridY]
    val = row[gridX]

    if val == 0 and (0 <= gridX < 3) and (0 <= gridY < 3):
        return True
    else:
        return False
        

def updateBoardState(boardState, gridX, gridY, player):
    """
    Updates the board state to indicate a player placed
    a marker at the specified grid position on the board.

    boardState: a nested list containing the board state
    gridX: the grid x position
    gridY: the grid y position
    player: 1 or 2
    """
    
    row = boardState[gridY]

    if player == 1:
        row[gridX] = 1

    else:
        row[gridX] = 2


def drawPlayerMarker(win, gridX, gridY, player):
    """
    Draws a player marker (X for player 1, O for player 2)
    at the specified grid position.

    win: the GraphWin for the board
    gridX: x-coordinate of grid cell
    gridY: y-coordinate of grid cell
    player: 1 or 2
    """
    if player == 1:
        line1 = Line(Point(gridX+0.15, gridY+0.15), Point(gridX+0.85, gridY+0.85)).draw(win)
        line2 = Line(Point(gridX+0.85, gridY+0.15), Point(gridX+0.15, gridY+0.85)).draw(win)
        line1.setWidth(7)
        line2.setWidth(7)
        
    else: 
        circ = Circle(Point(gridX+0.5, gridY+0.5), 0.4).draw(win)
        circ.setWidth(7)


def didPlayerWinWithRow(boardState, player, row):
    """
    Returns a Boolean indicating whether the player
    won the game due to the given row.

    boardState: a nested list containing the board state
    player: 1 or 2
    row: 0, 1, or 2
    returns: a Boolean (True if the player has an entire row,
             False otherwise)
    """
    r = boardState[row]
        
    for i in range(3):
        val = r[i]
            
        if val != player:
            return False

    return True


def didPlayerWinWithColumn(boardState, player, col):
    """
    Returns a Boolean indicating whether the player
    won the game due to the given column.

    boardState: a nested list containing the board state
    player: 1 or 2
    col: 0, 1, or 2
    returns: a Boolean (True if the player has an entire column,
             False otherwise)
    """
    
    for i in range(3):
        r = boardState[i]
        c = [r[col]]
        
        for val in c:
            if val != player:
                return False

    return True
    

def didPlayerWinWithDiagonal(boardState, player):
    """
    Returns a Boolean indicating whether the player
    won the game due to either diagonal.

    boardState: a nested list containing the board state
    player: 1 or 2
    returns: a Boolean (True if the player has an entire diagonal,
             False otherwise)
    """
    #Check for bottom diagonals (left and right)
    
    leftDiagonal = []
    rightDiagonal = []
    
    for i in range(3):
        d1 = boardState[i][i]
        leftDiagonal.append(d1)
        
        d2 = boardState[i][2-i]
        rightDiagonal.append(d2)

    if leftDiagonal.count(player) == 3:
        return True
    elif rightDiagonal.count(player) == 3:
        return True
    else:
        return False


def didPlayerWin(boardState, player):
    """
    Returns a Boolean indicating whether the player has
    won the game.
    
    boardState: a nested list containing the board state
    player: 1 or 2
    returns: a Boolean (True if the player won, False otherwise)
    """
    # First, check the rows
    for row in range(3):
        if didPlayerWinWithRow(boardState, player, row):
            return True

    # Second, check the columns
    for col in range(3):
        if didPlayerWinWithColumn(boardState, player, col):
            return True

    # Finally, check the diagonals
    if didPlayerWinWithDiagonal(boardState, player):
        return True

    # No win condition was met
    return False

def isDraw(boardState):
    """
    Returns a Boolean indicating whether the game has ended in a draw.
    Assumes neither player has won.
    
    boardState: a nested list containing the board state
    returns: a Boolean (True if the game is a draw, False otherwise)
    """

    for i in range(3):
        row = boardState[i]
        
        for j in range(3):
            val = row[j]

            if val == 0: 
                return False
                  
    return True

def getCellString(gridValue):
    """
    Returns a string corresponding to the provided value from the board state.

    gridValue: 0 (none) or 1 (player 1) or 2 (player 2)
    returns: " " (0) or "x" (player 1) or "o" (player 2)
    """
    if gridValue == 0:
        return " "
    elif gridValue == 1:
        return "x"
    else:
        return "o"

def printRow(boardState, row):
    """
    Prints out the current board state of the given row.

    boardState: a nested list containing the board state
    row: the row for which to print the board state
    """
    myRow = boardState[row]
    myList = []
    for i in range(len(myRow)):
        val = myRow[i]
        myList.append(getCellString(val))

    listToPrint = "|".join(myList)
    print(listToPrint)


def printBoardState(boardState):
    """
    Prints out the current board state for debugging.

    boardState: a nested list containing the board state
    """
    print()
    
    # Print top row
    printRow(boardState, 2)
    
    # Divider line
    print("-----")

    # Print middle row
    printRow(boardState, 1)
    
    # Divider line
    print("-----")

    # Print bottom row
    printRow(boardState, 0)

##############################################################
## Testing code                                             ##
##############################################################

def testDrawPlayerMarker():
    """
    Tests drawPlayerMarker by drawing five pieces based on where
    the user clicks.  *Does not* check for the location being valid,
    just tests the drawing code.
    """
    # Create and set up the board
    win = createAndDrawBoard()

    # Add a label to indicate to the players whose turn it is
    textLabel = Text(Point(1.5, -0.5),
                     "Place five markers.  Click anywhere to start.")
    textLabel.draw(win)
    win.getMouse() # wait until they click to start it all

    # Start with player 1
    player = 1

    # Draw five pieces
    for i in range(5):
        # Update the player text
        setPlayerText(textLabel, player)

        # Wait for the player to click a valid grid cell
        gridX, gridY = getGridLocation(win.getMouse())

        # Draw a marker for the current player
        drawPlayerMarker(win, gridX, gridY, player)

        # Switch players
        player = 3 - player # switches between 1 and 2

    # Update the text label -- we're done
    textLabel.setText("All done -- click again to quit.")
    win.getMouse()
    win.close()

def testPrintBoardState():
    """
    Tests drawPlayerMarker by drawing five pieces based on where
    the user clicks.  Does not check for the location being valid,
    just tests the drawing code.
    """
    # Set up the board state
    boardState = [[0,1,0], # bottom row
                  [1,2,0], # middle row
                  [2,0,0]] # top row

    # Print out the actual list
    print("The boardState list is:", boardState)

    # Print out the board state (useful for debugging)
    printBoardState(boardState)

def testPlacingValidMarkers():
    """
    Tests drawPlayerMarker by drawing five pieces based on where
    the user clicks.  *Does* check for the location being valid, and
    updates the board state as it goes.
    """
    # Create and set up the board
    win = createAndDrawBoard()

    # Add a label to indicate to the players whose turn it is
    textLabel = Text(Point(1.5, -0.5),
                     "Place five markers.  Click anywhere to start.")
    textLabel.draw(win)
    win.getMouse() # wait until they click to start it all

    # Start with player 1
    player = 1

    # Maintain the board state as a list of lists; each list
    # corresponds to a row on the game board
    boardState = [[0, 0, 0], # bottom row
                  [0, 0, 0], # middle row
                  [0, 0, 0]] # top row

    # Draw five pieces
    for i in range(5):
        # Update the player text
        setPlayerText(textLabel, player)

        # Wait for the player to click a valid grid cell
        isValidCell = False
        while not isValidCell:
            gridX, gridY = getGridLocation(win.getMouse())
            isValidCell = isValidGridCell(boardState, gridX, gridY)

        # Update the board state
        updateBoardState(boardState, gridX, gridY, player)

        # For debugging: print the board state
        printBoardState(boardState)

        # Draw a marker for the current player
        drawPlayerMarker(win, gridX, gridY, player)

        # Switch players
        player = 3 - player # switches between 1 and 2

    # Update the text label -- we're done
    textLabel.setText("All done -- click again to quit.")
    win.getMouse()
    win.close()

##############################################################
## The actual game                                          ##
##############################################################

def playGame():
    """
    Play a game of Tic Tac Toe.
    """
    # Create and set up the board
    win = createAndDrawBoard()

    # Add a label to indicate to the players whose turn it is
    textLabel = Text(Point(1.5, -0.5), "")
    textLabel.draw(win)

    # Start with player 1
    player = 1

    # Maintain the board state as a list of lists; each list
    # corresponds to a row on the game board
    boardState = [[0, 0, 0], # bottom row
                  [0, 0, 0], # middle row
                  [0, 0, 0]] # top row

    # Loop until the game is over
    isGameOver = False
    while not isGameOver:
        # Update the player text
        setPlayerText(textLabel, player)

        # Wait for the player to click a valid grid cell
        isValidCell = False
        while not isValidCell:
            gridX, gridY = getGridLocation(win.getMouse())
            isValidCell = isValidGridCell(boardState, gridX, gridY)

        # Update the board state
        updateBoardState(boardState, gridX, gridY, player)

        # For debugging: print the board state
        printBoardState(boardState)

        # Draw a marker for the current player
        drawPlayerMarker(win, gridX, gridY, player)

        # Check if the game is over; if not, switch players
        if didPlayerWin(boardState, player):
            textLabel.setText("Player {0} wins!".format(player))
            isGameOver = True
        elif isDraw(boardState):
            textLabel.setText("The game is a draw.")
            isGameOver = True
        else:
            player = 3 - player # switches between 1 and 2

if __name__ == "__main__":
    # Problem 1
##    testDrawPlayerMarker()

    # Problem 2
##    testPrintBoardState()

    # Problem 3
##    testPlacingValidMarkers()

    # Problem 4
    playGame()
