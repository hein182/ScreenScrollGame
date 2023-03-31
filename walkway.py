#create a walkway for player to go through

import pygame
import sys
import random
import math
import time

class Walkway:
    def __init__(self, screen, x, y, width, height, color):
        self.screen = screen
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
        self.x += x
        self.y += y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.draw()