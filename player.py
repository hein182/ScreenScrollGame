import pygame
#create a square player class
class Player:
    def __init__(self, screen, x, y, width, height, color, speed):
        self.speed2 = 1
        self.screen = screen
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 1)
    
    def move(self, x, y):
        if x <= self.speed:
            self.x += x
            self.y += y
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        else:
            self.x += self.speed
            self.y += self.speed
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def keyPress(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            if self.speed2 <= self.speed:
                self.move(-self.speed2, -self.speed2)
                self.speed2 += 0.1
            else:
                self.move(-self.speed, -self.speed)
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            if self.speed2 <= self.speed:
                self.move(-self.speed2, self.speed2)
                self.speed2 += 0.1
            else:
                self.move(-self.speed, self.speed)
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            if self.speed2 <= self.speed:
                self.move(self.speed2, -self.speed2)
                self.speed2 += 0.1
            else:
                self.move(self.speed, -self.speed)
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            if self.speed2 <= self.speed:
                self.move(self.speed2, self.speed2)
                self.speed2 += 0.1
            else:
                self.move(self.speed, self.speed)
        elif keys[pygame.K_LEFT]:
            if self.speed2 <= self.speed:
                self.move(-self.speed2, 0)
                self.speed2 += 0.1
            else:
                self.move(-self.speed, 0)
        elif keys[pygame.K_RIGHT]:
            if self.speed2 <= self.speed:
                self.move(self.speed2, 0)
                self.speed2 += 0.1
            else:
                self.move(self.speed, 0)
        elif keys[pygame.K_UP]:
            if self.speed2 <= self.speed:
                self.move(0, -self.speed2)
                self.speed2 += 0.1
            else:
                self.move(0, -self.speed)
        elif keys[pygame.K_DOWN]:
            if self.speed2 <= self.speed:
                self.move(0, self.speed2)
                self.speed2 += 0.1
            else:
                self.move(0, self.speed)
        else:
            self.speed2 = 1

    def update(self):
        self.draw()