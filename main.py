# Import and initialize the pygame library
import pygame
import time
from paddle import Paddle 
from ball import Ball

# Initialize game (configures hardware)
pygame.init()

# Define the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GOLD = (204,204,0)

# Define window size and create new window
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")


# Create paddle objects for two players
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# Create ball object
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# List to store sprites
all_sprites_list = pygame.sprite.Group()

# Add paddles and ball to sprite list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The clock will be used to control how fast the screen udpates
clock = pygame.time.Clock()

# Function to pause game
def pause():

    # Variables
    paused = True

    # Paused Loop
    while paused:
        # Get users events/actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quite()
                quit()
            if event.type == pygame.KEYDOWN:
                # Unpause game
                if event.key == pygame.K_SPACE:
                    paused = False
                # Quite game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quite()
                    quite()
        # Display "Paused" when game is paused
        font = pygame.font.Font(None, 74)
        text = font.render("PAUSED", 1, GOLD)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
        pygame.display.update()

# Initialize players scores and winner
scoreA = 0
scoreB = 0
winner = 3


# Loop will continue unless user exits
running = True

# Main Loop
while running:

    
    # grab user inputs/events
    for event in pygame.event.get():
        # If user exits game stop running
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_x:
        	running = False
        # If user presses key
        elif event.type == pygame.KEYDOWN:
            # If user pauses game
            if event.key == pygame.K_SPACE:
                pause()


    # Move paddles when the user uses arrow keys (player A) or (W/S for B)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
    	paddleA.moveUp(5)
    if keys[pygame.K_s]:
    	paddleA.moveDown(5)
    if keys[pygame.K_UP]:
    	paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
    	paddleB.moveDown(5)

    # AI paddle
    if paddleB.rect.y < ball.rect.y:
        paddleB.moveDown(5)

    elif paddleB.rect.y > ball.rect.y:
        paddleB.moveUp(5)
    

    # GAME LOGIC SHOULD GO HERE
    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls:
    # if ball touches right side of screen
    if ball.rect.x>=690:
    	ball.velocity[0] = -ball.velocity[0]
    	scoreA+=1 # Player A scores
    if scoreA == winner:
        running = False
    # if ball touches left side of screen
    if ball.rect.x<=0:
    	ball.velocity[0] = -ball.velocity[0]
    	scoreB+=1 # Player B scores
    if scoreB == winner:
        running = False
    # if ball touches bottom of screen
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    # if ball touches top of screen
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]
    # Collide mask tests for collision between 2 sprites
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
    	ball.bounce()



    # DRAWING CODE SHOULD GO HERE

    # Make screen black
    screen.fill(BLACK)

    # Draw the net line(surface, startP, endP, SCREEN_WIDTH)
    pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)

    # Draw all the sprites
    all_sprites_list.draw(screen)

    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    # Display winner
    p1Text = font.render("Player 1 Wins!", 1, GOLD)
    p2Text = font.render("Player 2 Wins!", 1, GOLD)
    if scoreA == winner:
        screen.blit(p1Text, p1Text.get_rect(center=screen.get_rect().center))
        pygame.display.update()
        pygame.time.wait(3000)
    if scoreB == winner:
        screen.blit(p2Text, p2Text.get_rect(center=screen.get_rect().center))
        pygame.display.update()
        pygame.time.wait(3000)


    # Update screen
    pygame.display.flip()

    # Limit to 60 frames per sec
    clock.tick(60)

# Once we exit main loop we can stop game engine
pygame.quit()