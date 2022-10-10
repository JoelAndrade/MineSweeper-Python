import random
from array import *

def rowConversion(letter): # Lowercases the user input and converst the letter the corresponding array
    letter = letter.lower()
    letter = ord(letter) - 96
    return letter

def countMines(mines,rowInput,colInput): # Count how many mines are next to the square
    numMines = 0
    if (mines[rowInput-1][colInput-1] == '*'): # Check top left
        numMines = numMines + 1
    if (mines[rowInput-1][colInput] == '*'): # Check top
        numMines = numMines + 1
    if (mines[rowInput-1][colInput+1] == '*'): # Check Top right
        numMines = numMines + 1
    if (mines[rowInput][colInput-1] == '*'): # Check left
        numMines = numMines + 1
    if (mines[rowInput][colInput+1] == '*'): # Check right
        numMines = numMines + 1
    if (mines[rowInput+1][colInput-1] == '*'): # Check bottom left
        numMines = numMines + 1
    if (mines[rowInput+1][colInput] == '*'): # Check bottom
        numMines = numMines + 1
    if (mines[rowInput+1][colInput+1] == '*'): # Check bottom right
        numMines = numMines + 1
    return numMines 

def checkEmpty(field,mines,rowInput,colInput,row,col): # This function expands the field when a the user uncovers an empty square
    field[rowInput][colInput] = ' ' # This fisrt block checks to see if the there are any empty blocks adjacent to the square. I then marks the adjacent square with an '!'
    check = False
    if (mines[rowInput-1][colInput-1] != 0): # Check top left
        field[rowInput-1][colInput-1] = mines[rowInput-1][colInput-1]
    else:
        mines[rowInput-1][colInput-1] = '!'
        check = True
    if (mines[rowInput-1][colInput] != 0): # Check top
        field[rowInput-1][colInput] = mines[rowInput-1][colInput]
    else:
        mines[rowInput-1][colInput] = '!' 
        check = True
    if (mines[rowInput-1][colInput+1] != 0): # Check Top right
        field[rowInput-1][colInput+1] = mines[rowInput-1][colInput+1]
    else:
        mines[rowInput-1][colInput+1] = '!'
        check = True
    if (mines[rowInput][colInput-1] != 0): # Check left
        field[rowInput][colInput-1] = mines[rowInput][colInput-1]
    else:
        mines[rowInput][colInput-1] = '!'
        check = True
    if (mines[rowInput][colInput+1] != 0): # Check right
        field[rowInput][colInput+1] = mines[rowInput][colInput+1] 
    else:
        mines[rowInput][colInput+1] = '!'
        check = True
    if (mines[rowInput+1][colInput-1] != 0): # Check bottom left
        field[rowInput+1][colInput-1] = mines[rowInput+1][colInput-1]
    else:
        mines[rowInput+1][colInput-1] = '!'
        check = True
    if (mines[rowInput+1][colInput] != 0): # Check bottom
        field[rowInput+1][colInput] = mines[rowInput+1][colInput]
    else:
        mines[rowInput+1][colInput] = '!'
        check = True
    if (mines[rowInput+1][colInput+1] != 0): # Check bottom right
        field[rowInput+1][colInput+1] = mines[rowInput+1][colInput+1]
    else:
        mines[rowInput+1][colInput+1] = '!'
        check = True # This block of code uncovers the marked squres with '!'. It then checks adjacenct squares with '!'. This process repeates itself until all '!' are uncovered. 
        
    while (check == True):
        check = False
        for i in range(1,row,1):
            for j in range(1,col,1):
                if (mines[i][j] == '!'):
                    field[i][j] = ' '
                    mines[i][j] = ' '
                    check = True
                    if (mines[i-1][j-1] != 0): # Check top left
                        field[i-1][j-1] = mines[i-1][j-1]
                    else:
                        mines[i-1][j-1] = '!'
                        check = True
                    if (mines[i-1][j] != 0): # Check top
                        field[i-1][j] = mines[i-1][j]
                    else:
                        mines[i-1][j] = '!' 
                        check = True
                    if (mines[i-1][j+1] != 0): # Check Top right
                        field[i-1][j+1] = mines[i-1][j+1]
                    else:
                        mines[i-1][j+1] = '!'
                        check = True
                    if (mines[i][j-1] != 0): # Check left
                        field[i][j-1] = mines[i][j-1]
                    else:
                        mines[i][j-1] = '!'
                        check = True
                    if (mines[i][j+1] != 0): # Check right
                        field[i][j+1] = mines[i][j+1] 
                    else:
                        mines[i][j+1] = '!'
                        check = True
                    if (mines[i+1][j-1] != 0): # Check bottom left
                        field[i+1][j-1] = mines[i+1][j-1]
                    else:
                        mines[i+1][j-1] = '!'
                        check = True
                    if (mines[i+1][j] != 0): # Check bottom
                        field[i+1][j] = mines[i+1][j]
                    else:
                        mines[i+1][j] = '!'
                        check = True
                    if (mines[i+1][j+1] != 0): # Check bottom right
                        field[i+1][j+1] = mines[i+1][j+1]
                    else:
                        mines[i+1][j+1] = '!'
                        check = True
    return field
            
def printField(numMines): # Prints the field
    print('                                      Mines:',numMines)
    for i in range(0,row+2,1):
        for j in range(0,col+2,1):
            if ((j >= 10 and i == 0) or (j >= 10 and i == row + 1)):
                print(field[i][j], end = " ") # By default python’s print() function ends with a newline. Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’. You can end a print statement with any character/string using this parameter.
            else:
                print(field[i][j], end = "  ")
        print()

row = 16 # Sets up the field
col = 30
field = [['#' for i in range(col+2)] for j in range(row)]
x = ord('a')
for i in range(0,row):
    field[i][0] = chr(x+i)
    field[i][col + 1] = chr(x+i)
xlabel = []
for i in range(0,col+2):
    x = str(i)
    xlabel.append(x)
field.insert(0,xlabel)
field.insert(17,xlabel)
field[0][0] = ' '
field[0][col+1] = ' '

numMines = 99 # Sets up the mines 
mines = [[' ' for i in range(col+2)] for j in range(row)]
x = ord('a')
for i in range(0,row):
    mines[i][0] = chr(x+i)
    mines[i][col + 1] = chr(x+i)
xlabel = []
for i in range(0,col + 2):
    x = str(i)
    xlabel.append(x)
mines.insert(0,xlabel)
mines.insert(17,xlabel)
mines[0][0] = ' '
mines[0][col + 1] = ' '
z = 0
while(z < numMines):
    x = random.randint(1,row)
    y = random.randint(1,col)
    if (mines[x][y] == '*'):
        z = z - 1
    mines[x][y] = '*'
    z = z + 1
x = 0
for i in range(1,row+1,1):
    for j in range (1,col+1,1):
        if (mines[i][j] != '*'):
            numSquare = countMines(mines,i,j)
            mines[i][j] = numSquare

printField(numMines)

# for i in range(0,row+2,1):
#     for j in range(0,col+2,1):
#         if ((j >= 10 and i == 0) or (j >= 10 and i == row + 1)):
#             print(mines[i][j], end = " ") # By default python’s print() function ends with a newline. Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’. You can end a print statement with any character/string using this parameter.
#         else:
#             print(mines[i][j], end = "  ")
#     print()

# This is where the game starts 
square = True
while (square == True): # This loops until the user hits a mine or the user wins 
    rowInput = input('Please enter the row: ') # Asks the user for which square they want to interact with
    rowInput = rowConversion(rowInput)
    colInput = int(input('Please enter the column: '))

    print('Press u to uncover a square:') # Asks the user if the want to uncover or flag a square
    flag = input('Press f for to use a flag: ')
    flag = flag.lower()

    if (flag == 'u'): # Case where the user wants to uncover a square
        if (mines[rowInput][colInput] == '*'): # Case where the user hits mine and the game ends
            field[rowInput][colInput] = mines[rowInput][colInput]
            printField(numMines)
            print("YOU SUCK ASS AT MINECRAFT KLAJSDFLKJHGALISDBNFLASDIFG")
            square = False
        elif (mines[rowInput][colInput] == 0): # Case where the user uncovers a zero block
            field = checkEmpty(field,mines,rowInput,colInput,row,col)
            printField(numMines)
        else: # Case where the user hits a number 
            field[rowInput][colInput] = mines[rowInput][colInput]
            printField(numMines)

        x = 0 # This block of code checks the win condition
        for i in range(1,row,1):
            for j in range(1,col,1):
                if (field[i][j] == '#' and mines[i][j] != '*'):
                    x = x + 1
        if (x == 0):
            print('Your win. What a cool guy')
            square = False

    if (flag == 'f'): # Case where the user wants to flag or unflag a block
        if (field[rowInput][colInput] == '#'):
            field[rowInput][colInput] = 'f'
            numMines = numMines - 1
        elif (field[rowInput][colInput] == 'f'):
            field[rowInput][colInput] = '#'
            numMines = numMines + 1
        printField(numMines)




# This block of code is for the pygame debuger
# for i in range(0,row+2,1):
#     for j in range(0,col+2,1):
#         print(field.hidden[i][j], end = "  ")
#     print()
