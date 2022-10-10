import random 
import sys
import pygame
import os # Let me import images
import json

# Constants
fps = 30
row = 16
col = 30
blockLength = 40
numMines = 99

try: # Loads .txt file
    with open('settings.txt') as txtFile:
        settings = json.load(txtFile)
    row = settings['rows']
    col = settings['columns']
    blockLength = settings['blockLength']
    numMines = settings['Mines']
except: # If there is no txt file the program will make one
    settings = {
        'rows': row,
        'columns': col,
        'blockLength': blockLength,
        'Mines': numMines
    }
    with open('settings.txt','w') as txtFile:
        json.dump(settings, txtFile)

# Sets up window
window = pygame.display.set_mode((blockLength*col, blockLength*row))

# Imports Images
coveredBlock = pygame.image.load(os.path.join('Images','block.png')).convert()
coveredBlock = pygame.transform.scale(coveredBlock, (blockLength, blockLength))

emptyBlock = pygame.image.load(os.path.join('Images','EmptyBlock.png')).convert()
emptyBlock = pygame.transform.scale(emptyBlock, (blockLength, blockLength))

flagBlock = pygame.image.load(os.path.join('Images','Flag.png')).convert()
flagBlock = pygame.transform.scale(flagBlock, (blockLength, blockLength))

mineBlock = pygame.image.load(os.path.join('Images','mine.png')).convert()
mineBlock = pygame.transform.scale(mineBlock, (blockLength, blockLength))

wrongMineBlock = pygame.image.load(os.path.join('Images','wrongMine.png')).convert()
wrongMineBlock = pygame.transform.scale(wrongMineBlock, (blockLength, blockLength))

oneBlock = pygame.image.load(os.path.join('Images','1.png')).convert()
oneBlock = pygame.transform.scale(oneBlock, (blockLength, blockLength))

twoBlock = pygame.image.load(os.path.join('Images','2.png')).convert()
twoBlock = pygame.transform.scale(twoBlock, (blockLength, blockLength))

threeBlock = pygame.image.load(os.path.join('Images','3.png')).convert()
threeBlock = pygame.transform.scale(threeBlock, (blockLength, blockLength))

fourBlock = pygame.image.load(os.path.join('Images','4.png')).convert()
fourBlock = pygame.transform.scale(fourBlock, (blockLength, blockLength))

fiveBlock = pygame.image.load(os.path.join('Images','5.png')).convert()
fiveBlock = pygame.transform.scale(fiveBlock, (blockLength, blockLength))

sixBlock = pygame.image.load(os.path.join('Images','6.png')).convert()
sixBlock = pygame.transform.scale(sixBlock, (blockLength, blockLength))

sevenBlock = pygame.image.load(os.path.join('Images','7.png')).convert()
sevenBlock = pygame.transform.scale(sevenBlock, (blockLength, blockLength))

eightBlock = pygame.image.load(os.path.join('Images','8.png')).convert()
eightBlock = pygame.transform.scale(eightBlock, (blockLength, blockLength))

class field:
    def __init__(self):
        self.openSetup() # this is to make sure self.open and self.hidden
        self.hiddenSetup() # are set up even if the methods are not called 

    def openSetup(self): # Sets up visable field
        open = [['#' for i in range(col+2)] for j in range(row)]
        for i in range(0,row):
            open[i][0] = '|'
            open[i][col + 1] = '|'
        xlabel = []
        x = '|'
        for i in range(0,col+2):
            xlabel.append(x)
        open.insert(0,xlabel)
        open.insert(row + 1, xlabel)

        self.open = open

    def hiddenSetup(self): # Sets up hidden field
        # First build and empty array with borders
        hidden = [[' ' for i in range(col+2)] for j in range(row)]
        for i in range(0, row):
            hidden[i][0] = '|'
            hidden[i][col + 1] = '|'
        xlabel = []
        x = '|'
        for i in range(0, col + 2):
            xlabel.append(x)
        hidden.insert(0,xlabel)
        hidden.insert(row + 1,xlabel)

        # Then add the mines to the field 
        z = 0
        while(z < numMines):
            x = random.randint(1,row)
            y = random.randint(1,col)
            if (hidden[x][y] == '*'):
                z = z - 1
            hidden[x][y] = '*'
            z = z + 1

        # Then places numbers next to the mines
        for i in range(1,row+1):
            for j in range (1, col+1):
                if (hidden[i][j] != '*'):
                    numSquare = countMines(hidden, i, j)
                    hidden[i][j] = numSquare

        self.hidden = hidden   

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

def checkEmpty(open,hidden,rowInput,colInput): # This function expands the field when a the user uncovers an empty square
    hidden[rowInput][colInput] = '!'
    check = True
    
    # This block of code uncovers the marked squre with '!'. It then checks adjacenct squares with '0'. then marks them with '!'. This goes on until there are no more '!'
    while (check):
        check = False
        for i in range(1,row + 1):
            for j in range(1,col + 1):
                if (hidden[i][j] == '!'):
                    open[i][j] = ' '
                    hidden[i][j] = ' '
                    check = True
                    if (hidden[i-1][j-1] != 0): # Check top left
                        open[i-1][j-1] = hidden[i-1][j-1]
                    else:
                        hidden[i-1][j-1] = '!'   
                    if (hidden[i-1][j] != 0): # Check top
                        open[i-1][j] = hidden[i-1][j]
                    else:
                        hidden[i-1][j] = '!'                         
                    if (hidden[i-1][j+1] != 0): # Check Top right
                        open[i-1][j+1] = hidden[i-1][j+1]
                    else:
                        hidden[i-1][j+1] = '!'                       
                    if (hidden[i][j-1] != 0): # Check left
                        open[i][j-1] = hidden[i][j-1]
                    else:
                        hidden[i][j-1] = '!'                        
                    if (hidden[i][j+1] != 0): # Check right
                        open[i][j+1] = hidden[i][j+1] 
                    else:
                        hidden[i][j+1] = '!'                       
                    if (hidden[i+1][j-1] != 0): # Check bottom left
                        open[i+1][j-1] = hidden[i+1][j-1]
                    else:
                        hidden[i+1][j-1] = '!'                     
                    if (hidden[i+1][j] != 0): # Check bottom
                        open[i+1][j] = hidden[i+1][j]
                    else:
                        hidden[i+1][j] = '!'                     
                    if (hidden[i+1][j+1] != 0): # Check bottom right
                        open[i+1][j+1] = hidden[i+1][j+1]
                    else:
                        hidden[i+1][j+1] = '!'
    return open

def pos2Index(): # Converts the posion of the mouse input to the array index
    xPos, yPos = pygame.mouse.get_pos()
    j = (xPos//blockLength) + 1
    i = (yPos//blockLength) + 1
    return i, j

def checkWrongFlag(open, hidden): # Tell the player where all the misplaced flags where on the field
    for i in range(1,row + 1):
        for j in range(1,col + 1):
            if (open[i][j] == 'f' and hidden[i][j] != '*'):
                hidden[i][j] = 'x'
    pygame.display.set_caption("\
                                \
                                \
                                \
                                \
                                \
            Game Over")   
    return hidden

def checkWinCondition(open, hidden): # Checks if the player won the game
    x = 0
    run = True
    for i in range(1,row + 1):
        for j in range(1,col + 1):
            if (open[i][j] == '#' and hidden[i][j] != '*'):
                x = x + 1
    if (x == 0): # If the player won, the blocks without flags get flags on them
        for i in range(1,row + 1):
            for j in range(1,col + 1):
                if (open[i][j] == '#'):
                    open[i][j] = 'f'
        pygame.display.set_caption("\
                                    \
                                    \
                                    \
                                    \
                            You Win!")   
        run = False
    return run

def placeFlag(open, numFlags, i, j): # Places or removes a flag i fth player right clicks a block
    if (open[i][j] == '#'):
        open[i][j] = 'f'
        numFlags = numFlags + 1
    elif (open[i][j] == 'f'):
        open[i][j] = '#'
        numFlags = numFlags - 1
    pygame.display.set_caption("Number of Mines: "+str(numMines-numFlags)+"\
                                                                           \
                                                            Minesweeper")
    return numFlags, open
   
def drawScreen(open):  # Draws the field 
    window.fill("black")
    for i in range(1,row + 1):
        for j in range(1, col + 1):
            if (open[i][j] == '#'):
                window.blit(coveredBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == ' '):
                window.blit(emptyBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == '*'):
                window.blit(mineBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 'f'):
                window.blit(flagBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 'x'):
                window.blit(wrongMineBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 0):
                window.blit(emptyBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 1):
                window.blit(oneBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 2):
                window.blit(twoBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 3):
                window.blit(threeBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 4):
                window.blit(fourBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 5):
                window.blit(fiveBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 6):
                window.blit(sixBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 7):
                window.blit(sevenBlock,(blockLength*(j - 1), blockLength*(i - 1)))
            elif (open[i][j] == 8):
                window.blit(eightBlock,(blockLength*(j - 1), blockLength*(i - 1)))
    pygame.display.update()

def main(): 
    field.openSetup()
    field.hiddenSetup()
    numFlags = 0
    pygame.display.set_caption("Number of Mines: "+str(numMines-numFlags)+"\
                                                                           \
                                                            Minesweeper")
    clock = pygame.time.Clock()
    run = True
    firstBlock = True

    while (run):
        clock.tick(fps)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            mousePress = pygame.mouse.get_pressed()
            if (event.type == pygame.MOUSEBUTTONDOWN and mousePress[0]):
                i, j = pos2Index()
                if (firstBlock):
                    while(field.hidden[i][j] != 0):
                        field.hiddenSetup()
                    firstBlock = False
                if (field.hidden[i][j] == '*' and field.open[i][j] != 'f'):
                    field.open = checkWrongFlag(field.open, field.hidden)
                    run = False
                elif (field.hidden[i][j] == 0 and field.open[i][j] != 'f'):
                    field.open = checkEmpty(field.open, field.hidden,i,j) 
                    run = checkWinCondition(field.open, field.hidden)
                elif (field.open[i][j] != 'f'):
                    field.open[i][j] = field.hidden[i][j]
                    run = checkWinCondition(field.open, field.hidden)
            if (event.type == pygame.MOUSEBUTTONDOWN and mousePress[2]):
                i, j = pos2Index()
                numFlags, field.open = placeFlag(field.open, numFlags, i, j)

        drawScreen(field.open)
    
    while(run != True):
        clock.tick(fps)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                run = True

    main()            

if (__name__ == "__main__"): 
    field = field()
    main()