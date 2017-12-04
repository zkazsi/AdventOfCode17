import math

def advcode3(ertek):
    coordCol = 0
    coordRow = 0
    squareroot = math.sqrt(ertek)
    if int(squareroot) % 2 == 0:
        squaresize = int(squareroot) + 1
    else:
        squaresize = int(squareroot) + 2

    coord1Row = int(squaresize / 2) + 1
    coord1Col = coord1Row
    valueRowXColX = math.pow(squaresize, 2)
    valueRow1Col1 =  math.pow(squaresize-1, 2) + 1
    valueRow1Colx = valueRow1Col1 - (squaresize - 1)
    valueRowXCol1 = valueRowXColX - (squaresize - 1)
    # smallest: valueRow1Colx; largest: valueRowXColX
    # valueRow1Colx < valueRow1Col1 < valueRowXCol1 < valueRowXColX

    # Define coordinates of ertek: 
    if ertek > valueRowXCol1:
        coordRow = squaresize
        coordCol = valueRowXColX - ertek
    elif ertek > valueRow1Col1:
        coordRow = valueRowXCol1 - ertek
        coordCol = 1
    elif ertek > valueRow1Colx:
        coordRow = 1
        coordCol = valueRow1Col1 - ertek
    else:
        coordRow = valueRow1Colx - ertek
        coordCol = squaresize
    
    # Calculate length of path: 'rows to 1' + 'columns to 1'
    # Correction: for some reason, answer is 1 less: added '-1'
    lengthPath = abs(coord1Col - coordCol) + abs(coord1Row - coordRow) - 1
      
    print("The length of the path to the center portal, no 1 is ", lengthPath)
