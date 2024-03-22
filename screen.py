import pygame
import sys

class Screen():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 500))

    def MakeScreen(self):
        background_colour = (0, 105, 148)  # Adjusted shade of blue
        
        game_loop = True
        pygame.display.set_caption('Derek and Enzo Game') 
        self.screen.fill(background_colour) 
        
        while game_loop: 
            self.makeButton()
            pygame.display.flip() 

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    game_loop = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        return "next_screen"  # Return something to indicate button is clicked

    def makeButton(self):
        button_color = (130, 136, 148)  
        text_color = (255, 255, 255)  
        button_rect = pygame.Rect(400, 300, 200, 60)
        font = pygame.font.SysFont('Arial', 30)
        
        pygame.draw.rect(self.screen, button_color, button_rect, border_radius=8)
        
        button_font = font.render('Press to Start!', True, text_color)
        button_font_rect = button_font.get_rect(center=button_rect.center)
        self.screen.blit(button_font, button_font_rect)
        
        self.button_rect = button_rect  # Store button rectangle for collision detection

        pygame.display.update()



