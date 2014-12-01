import pygame
import random
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
score    = 0
colorran1 = random.randrange(0,255)
colorran2 = random.randrange(0,255)
colorran3 = random.randrange(0,255)
colorran = (colorran1, colorran2, colorran3)
ranrow   = random.randrange(0,10)
rancol   = random.randrange(0,10)
 
# This sets the width and height of each grid location
width  = 50
height = 50
 
# This sets the margin between each cell
margin = 5
 

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0) # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
##grid[1][5] = 1
 
# Initialize pygame
pygame.init()
 
# Set the height and width of the screen
##size = [255, 255]
size = [640, 640]
screen = pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)
start_time = 60
frame_count = 0
frame_rate = 60
 
# -------- Main Program Loop -----------
while done == False:
    
    for event in pygame.event.get(): # User did something
        ##colorran   = (   random.randrange(0,255),   random.randrange(0,255),   random.randrange(0,255))
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:     
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # Set that location to zero
            ##grid[row][column] = 1
            grid[ranrow][rancol] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
        
            if((row==ranrow)&(column==rancol)) :
                score = score + 1
                print("Score : ", score)
                grid[ranrow][rancol] = 0
                colorran1 = random.randrange(0,255)
                colorran2 = random.randrange(0,255)
                colorran3 = random.randrange(0,255)
                colorran = (colorran1, colorran2, colorran3)
                ranrow   = random.randrange(0,10)
                rancol   = random.randrange(0,10) 
                grid[ranrow][rancol] = 1       
        
 
    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        color   = colorran
        for column in range(10):
            color = colorran
            ##colorran   = (   random.randrange(0,255),   random.randrange(0,255),   random.randrange(0,255))
            if grid[row][column] == 1 :
            #if grid[ranrow][rancol] == 0 :
                if (colorran3 > 205):
                    color = (colorran1, colorran2, colorran3-50+score)
                else :
                    color = (colorran1, colorran2, colorran3+50-score)

            pygame.draw.rect(screen,
                             color,
                             [(margin+width)*column+margin,
                              (margin+height)*row+margin,
                              width,
                              height])


    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        done = True;
        total_seconds = 0
     
    # Divide by 60 to get total minutes
    #minutes = total_seconds // 60
     
    # Use modulus (remainder) to get seconds
    seconds = total_seconds 
     
    # Use python string formatting to format in leading zeros
    #output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    output_string = "Time left: {0}       Score :  {1}".format(seconds, score)
     
    # Blit to the screen
    text = font.render(output_string, True, WHITE)
     
    screen.blit(text, [0, 600])
     
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1

    # Limit to 60 frames per second
    clock.tick(60)

 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
