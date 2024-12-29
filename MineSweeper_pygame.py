import random 
import sys
import pygame
import os
import json

# Loads .txt file
try:
    with open('settings.txt') as settings_file:
        settings = json.load(settings_file)
#

# If there is no txt file the program will make one
except:
    settings = {
        'rows': 16,
        'columns': 30,
        'block_length': 40,
        'mines': 99,
        'dark_mode': False
    }
    with open('settings.txt','w') as settings_file:
        json.dump(settings, settings_file)
#

# Constants
fps = 30
row = settings["rows"]
col = settings["columns"]
block_length = settings["block_length"]
num_mines = settings["mines"]

# Sets up window
window = pygame.display.set_mode((block_length*col, block_length*row))

class mine_sweeper_field:
    def __init__(self, row_input, col_input, num_mines_input):
        self.row = row_input
        self.col = col_input
        self.num_mines = num_mines_input
        self.visable_setup()
        self.hidden_setup()
    #

    def init(self):
        self.visable_setup()
        self.hidden_setup()
    #

    # Sets up visable field
    def visable_setup(self):
        self.visable = self.__create_field('#')
    #

    # Sets up hidden field
    def hidden_setup(self):
        # First build and empty array with borders
        self.hidden = self.__create_field(' ')

        # Then add the mines to the field 
        mine_count = 0
        while (mine_count < self.num_mines):
            i = random.randint(1, self.row)
            j = random.randint(1, self.col)
            if (self.hidden[i][j] == '*'):
                continue
            self.hidden[i][j] = '*'
            mine_count += 1
        #

        # Then places numbers next to the mines
        for i in range(1, self.row + 1):
            for j in range (1, self.col + 1):
                if (self.hidden[i][j] != '*'):
                    self.hidden[i][j] = self.__count_mines(i, j)
            #
        #
    #

    def __create_field(self, fill: str):
        field = [[fill for i in range(self.col + 2)] for j in range(self.row + 2)]
        return field
    #

    # Count how many mines are next to the square
    def __count_mines(self, i, j): 
        num_mines = 0

        if (self.hidden[i - 1][j - 1] == '*'): # Check top left
            num_mines += 1
        if (self.hidden[i - 1][j] == '*'): # Check top
            num_mines += 1
        if (self.hidden[i - 1][j + 1] == '*'): # Check Top right
            num_mines += 1
        if (self.hidden[i][j - 1] == '*'): # Check left
            num_mines += 1
        if (self.hidden[i][j + 1] == '*'): # Check right
            num_mines += 1
        if (self.hidden[i + 1][j - 1] == '*'): # Check bottom left
            num_mines += 1
        if (self.hidden[i + 1][j] == '*'): # Check bottom
            num_mines += 1
        if (self.hidden[i + 1][j + 1] == '*'): # Check bottom right
            num_mines += 1

        return num_mines
    #
#

def import_images(dark_mode):
    global covered_block
    global empty_block
    global flag_block
    global mine_block
    global wrong_mine_block
    global one_block
    global two_block
    global three_block
    global four_block
    global five_block
    global six_block
    global seven_block
    global eight_block

    image_folder = "Dark" if dark_mode else "Light"

    covered_block = pygame.image.load(os.path.join(f'Images/{image_folder}','block.png')).convert()
    covered_block = pygame.transform.scale(covered_block, (block_length, block_length))

    empty_block = pygame.image.load(os.path.join(f'Images/{image_folder}','EmptyBlock.png')).convert()
    empty_block = pygame.transform.scale(empty_block, (block_length, block_length))

    flag_block = pygame.image.load(os.path.join(f'Images/{image_folder}','Flag.png')).convert()
    flag_block = pygame.transform.scale(flag_block, (block_length, block_length))

    mine_block = pygame.image.load(os.path.join(f'Images/{image_folder}','mine.png')).convert()
    mine_block = pygame.transform.scale(mine_block, (block_length, block_length))

    wrong_mine_block = pygame.image.load(os.path.join(f'Images/{image_folder}','wrongMine.png')).convert()
    wrong_mine_block = pygame.transform.scale(wrong_mine_block, (block_length, block_length))

    one_block = pygame.image.load(os.path.join(f'Images/{image_folder}','1.png')).convert()
    one_block = pygame.transform.scale(one_block, (block_length, block_length))

    two_block = pygame.image.load(os.path.join(f'Images/{image_folder}','2.png')).convert()
    two_block = pygame.transform.scale(two_block, (block_length, block_length))

    three_block = pygame.image.load(os.path.join(f'Images/{image_folder}','3.png')).convert()
    three_block = pygame.transform.scale(three_block, (block_length, block_length))

    four_block = pygame.image.load(os.path.join(f'Images/{image_folder}','4.png')).convert()
    four_block = pygame.transform.scale(four_block, (block_length, block_length))

    five_block = pygame.image.load(os.path.join(f'Images/{image_folder}','5.png')).convert()
    five_block = pygame.transform.scale(five_block, (block_length, block_length))

    six_block = pygame.image.load(os.path.join(f'Images/{image_folder}','6.png')).convert()
    six_block = pygame.transform.scale(six_block, (block_length, block_length))

    seven_block = pygame.image.load(os.path.join(f'Images/{image_folder}','7.png')).convert()
    seven_block = pygame.transform.scale(seven_block, (block_length, block_length))

    eight_block = pygame.image.load(os.path.join(f'Images/{image_folder}','8.png')).convert()
    eight_block = pygame.transform.scale(eight_block, (block_length, block_length))
#

# This function expands the field when a the user uncovers an empty square
def check_empty(visable, hidden, rowInput, colInput):
    hidden[rowInput][colInput] = '!'
    check = True
    
    # This block of code uncovers the marked square with '!'. It then checks adjacenct squares with '0'. then marks them with '!'. This goes on until there are no more '!'
    while (check):
        check = False
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if (hidden[i][j] == '!'):
                    visable[i][j] = ' '
                    hidden[i][j] = ' '
                    check = True
                    if (hidden[i-1][j-1] != 0): # Check top left
                        visable[i-1][j-1] = hidden[i-1][j-1]
                    else:
                        hidden[i-1][j-1] = '!'
                    if (hidden[i-1][j] != 0): # Check top
                        visable[i-1][j] = hidden[i-1][j]
                    else:
                        hidden[i-1][j] = '!'                         
                    if (hidden[i-1][j+1] != 0): # Check Top right
                        visable[i-1][j+1] = hidden[i-1][j+1]
                    else:
                        hidden[i-1][j+1] = '!'
                    if (hidden[i][j-1] != 0): # Check left
                        visable[i][j-1] = hidden[i][j-1]
                    else:
                        hidden[i][j-1] = '!'
                    if (hidden[i][j+1] != 0): # Check right
                        visable[i][j+1] = hidden[i][j+1]
                    else:
                        hidden[i][j+1] = '!'                       
                    if (hidden[i+1][j-1] != 0): # Check bottom left
                        visable[i+1][j-1] = hidden[i+1][j-1]
                    else:
                        hidden[i+1][j-1] = '!'                     
                    if (hidden[i+1][j] != 0): # Check bottom
                        visable[i+1][j] = hidden[i+1][j]
                    else:
                        hidden[i+1][j] = '!'                     
                    if (hidden[i+1][j+1] != 0): # Check bottom right
                        visable[i+1][j+1] = hidden[i+1][j+1]
                    else:
                        hidden[i+1][j+1] = '!'
#

# Converts the posion of the mouse input to the array index
def pos_to_index():
    x_pos, y_pos = pygame.mouse.get_pos()
    j = (x_pos//block_length) + 1
    i = (y_pos//block_length) + 1
    return i, j
#

# Tell the player where all the misplaced flags where on the field
def check_wrong_flag(visable, hidden):
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if (visable[i][j] == 'f' and hidden[i][j] != '*'):
                hidden[i][j] = 'x'
    pygame.display.set_caption("\
                                \
                                \
                                \
                                \
                                \
            Game Over")   
    return hidden
#

def check_win_condition(visable, hidden): # Checks if the player won the game
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if (visable[i][j] == '#' and hidden[i][j] != '*'):
                return True
            
    # If the player won, the blocks without flags get flags on them
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if (visable[i][j] == '#'):
                visable[i][j] = 'f'
    pygame.display.set_caption("\
                                \
                                \
                                \
                                \
                                            You Win!")   
    return False
#

def place_flag(visable_field, num_flags, i, j): # Places or removes a flag i fth player right clicks a block
    if (visable_field[i][j] == '#'):
        visable_field[i][j] = 'f'
        num_flags += 1
    elif (visable_field[i][j] == 'f'):
        visable_field[i][j] = '#'
        num_flags -= 1
    pygame.display.set_caption("Number of Mines: " + str(num_mines - num_flags) + "\
                                                                           \
                                                            Minesweeper")
    return num_flags
#
   
def draw_screen(visable_field):  # Draws the field 
    window.fill("black")
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if (visable_field[i][j] == '#'):
                window.blit(covered_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == ' '):
                window.blit(empty_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == '*'):
                window.blit(mine_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 'f'):
                window.blit(flag_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 'x'):
                window.blit(wrong_mine_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 0):
                window.blit(empty_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 1):
                window.blit(one_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 2):
                window.blit(two_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 3):
                window.blit(three_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 4):
                window.blit(four_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 5):
                window.blit(five_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 6):
                window.blit(six_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 7):
                window.blit(seven_block, (block_length*(j - 1), block_length*(i - 1)))
            elif (visable_field[i][j] == 8):
                window.blit(eight_block, (block_length*(j - 1), block_length*(i - 1)))
        #
    #
    pygame.display.update()
#

def main(): 
    field.init()
    num_flags = 0
    pygame.display.set_caption("Number of Mines: "+str(num_mines-num_flags)+"\
                                                                           \
                                                            Minesweeper")
    clock = pygame.time.Clock()
    run = True
    first_block = True

    while (run):
        clock.tick(fps)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                with open('settings.txt', 'w') as settings_file:
                    json.dump(settings, settings_file)
                pygame.quit()
                sys.exit()
            #

            mouse_press = pygame.mouse.get_pressed()
            keyboard_press = pygame.key.get_pressed()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                i, j = pos_to_index()

                if (mouse_press[0]):
                    if (first_block):
                        while(field.hidden[i][j] != 0):
                            field.hidden_setup()
                        first_block = False

                    if (field.hidden[i][j] == '*' and field.visable[i][j] != 'f'):
                        field.visable = check_wrong_flag(field.visable, field.hidden)
                        run = False

                    elif (field.hidden[i][j] == 0 and field.visable[i][j] != 'f'):
                        check_empty(field.visable, field.hidden, i, j) 
                        run = check_win_condition(field.visable, field.hidden)

                    elif (field.visable[i][j] != 'f'):
                        field.visable[i][j] = field.hidden[i][j]
                        run = check_win_condition(field.visable, field.hidden)
                #

                # if (mouse_press[1]):
                #     # TODO: Add the middle click function
                # #

                if (mouse_press[2]):
                    num_flags = place_flag(field.visable, num_flags, i, j)
                #
            #

            if (event.type == pygame.KEYDOWN):
                if (keyboard_press[pygame.K_SPACE]):
                    settings["dark_mode"] = not settings["dark_mode"]
                    import_images(settings["dark_mode"])
                #
            #
        #

        draw_screen(field.visable)
    #
    
    while (not run):
        clock.tick(fps)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                with open('settings.txt', 'w') as settings_file:
                    json.dump(settings, settings_file)
                pygame.quit()
                sys.exit()
            #

            if (event.type == pygame.MOUSEBUTTONDOWN):
                run = True
    #
#

if (__name__ == "__main__"):
    import_images(settings["dark_mode"])
    field = mine_sweeper_field(row, col, num_mines)

    while(True):
        main()
#