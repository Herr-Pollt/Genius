import pygame

class Screen():
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 500))
    
    def MakeScreen(self):
        background_colour = ('#006994') 
        #To Fullscreen - (0, 0), pygame.FULLSCREEN

        # Variable to keep our game loop running 
        game_loop = True

        # Set the caption of the screen 
        pygame.display.set_caption('Derek and Enzo Game') 
        
        # Fill the background colour to the screen 
        self.screen.fill(background_colour) 
        
        
        
        # game loop 
        while game_loop: 
            self.makeButton()
            # Update the display using flip 
            pygame.display.flip() 

            # for loop through the event queue   
            for event in pygame.event.get(): 
            
                # Check for QUIT event       
                if event.type == pygame.QUIT: 
                    game_loop = False
    
    def makeButton(self):
        color = ("#848884")
        pygame.draw.rect(self.screen, color, pygame.Rect(250, 250, 60, 60))
        pygame.display.flip()