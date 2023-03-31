import sys
import pygame
from walkway import Walkway
from player import Player

#constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

tryCounter = 0
walkWayCount = 0
playerHitEnd = False

pathWidth = 40

if __name__ == '__main__':    
    
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Pygame Window')
    clock = pygame.time.Clock()

    # create a player on start position
    player = Player(screen, SCREEN_WIDTH/2 - 10, -40+280, 20, 20, (100,255,200), 5)

    arr = []

    #create a walkway
    start = Walkway(screen, SCREEN_WIDTH/2 - 20, -40, pathWidth, 40, BLUE)
    w1 = Walkway(screen, SCREEN_WIDTH/2 - 20, 0, pathWidth, 270, BLACK)
    w2 = Walkway(screen, SCREEN_WIDTH/2 + 20, 270 - pathWidth, 269, pathWidth, BLACK)
    w3 = Walkway(screen, SCREEN_WIDTH/2 + 270 - 21, 269, pathWidth, 270, BLACK)
    w4 = Walkway(screen, SCREEN_WIDTH/2 + 19, 270 - 41 + 270, 270, pathWidth, BLACK)
    w5 = Walkway(screen, SCREEN_WIDTH/2 - 20, 270 - 41 + 270, pathWidth, 270, BLACK)
    end = Walkway(screen, SCREEN_WIDTH/2 - 20, 270 - 41 + 270+270, pathWidth, 40, GREEN)

    arr = [start, w1, w2, w3, w4, w5, end]


    for walkway in arr:
        walkway.move(0,270)

    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)



        #increase position of y in all objects
        if playerHitEnd == False:
            for walkway in arr:
                walkway.move(0, -0.7)

        #player logic
        #keyPress()
        if playerHitEnd == False:
            player.keyPress()
        #make sure player cant leave the screen
        if player.x < 0:
            player.x = 0
        if player.x > SCREEN_WIDTH - player.width:
            player.x = SCREEN_WIDTH - player.width
        if player.y < 0:
            player.y = 0

        if player.y > SCREEN_HEIGHT - player.height:
            player.y = SCREEN_HEIGHT - player.height

        #if player is on top of walkway
        for walkway in arr:
            if player.x+10 >= walkway.x and player.x+10 <= walkway.x + walkway.width and player.y+10 >= walkway.y and player.y+10 <= walkway.y + walkway.height:
                walkWayCount += 1
            else:
                walkWayCount -= 1

            #check if player collides with end
            if player.x+10 >= end.x and player.x+10 <= end.x + end.width and player.y+10 >= end.y and player.y+10 <= end.y + end.height:
                playerHitEnd = True
                

        if walkWayCount >= 1-len(arr):
            print("player is in walkway")
        else:
            tryCounter += 1
            #reset game
                # create a player on start position
            player = Player(screen, SCREEN_WIDTH/2 - 10, -40+280, 20, 20, (100,255,200), 5)

            arr = []

            #create a walkway
            start = Walkway(screen, SCREEN_WIDTH/2 - 20, -40, pathWidth, 40, BLUE)
            w1 = Walkway(screen, SCREEN_WIDTH/2 - 20, 0, pathWidth, 270, BLACK)
            w2 = Walkway(screen, SCREEN_WIDTH/2 + 20, 270 - pathWidth, 269, pathWidth, BLACK)
            w3 = Walkway(screen, SCREEN_WIDTH/2 + 270 - 21, 269, pathWidth, 270, BLACK)
            w4 = Walkway(screen, SCREEN_WIDTH/2 + 19, 270 - 41 + 270, 270, pathWidth, BLACK)
            w5 = Walkway(screen, SCREEN_WIDTH/2 - 20, 270 - 41 + 270, pathWidth, 270, BLACK)
            end = Walkway(screen, SCREEN_WIDTH/2 - 20, 270 - 41 + 270+270, pathWidth, 40, GREEN)

            arr = [start, w1, w2, w3, w4, w5, end]


            for walkway in arr:
                walkway.move(0,270)

        def draw():
            screen.fill(WHITE)

            #draw the walkway
            for walkway in arr:
                walkway.update()

            #draw the player
            player.update()
            #draw try counter
            font = pygame.font.SysFont('Arial', 30)
            text = font.render('Tries: ' + str(tryCounter), True, (0, 0, 0))
            screen.blit(text, (10, 10))
            if playerHitEnd == True:
                font = pygame.font.SysFont('Arial', 30)
                text = font.render('You Win!', True, (0, 243, 0))
                screen.blit(text, (SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2 - 50))

        draw()
        
        walkWayCount = 0
        pygame.display.update()