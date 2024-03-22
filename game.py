import pygame
from screen import Screen

class Game():
    def __init__(self) -> None:
        self.screen = Screen().screen
        self.background_color = (0, 0, 0)
    def start(self):
        self.screen.fill(self.background_color)
        print("hello")
        pygame.display.flip()