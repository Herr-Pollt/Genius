import pygame

class Screen():
    def __init__(self):
        pygame.init()
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
        button_color = (130, 136, 148)  # Adjusted shade of gray
        text_color = (255, 255, 255)  # White text color for better contrast
        button_rect = pygame.Rect(400, 300, 200, 60)
        font = pygame.font.SysFont('Arial', 30)
        
        # Draw a slightly rounded rectangle for a nicer look
        pygame.draw.rect(self.screen, button_color, button_rect, border_radius=8)
        
        # Render the text with anti-aliasing for smoother edges
        button_font = font.render('Press to Start!', True, text_color)
        button_font_rect = button_font.get_rect(center=button_rect.center)
        self.screen.blit(button_font, button_font_rect)
        
        pygame.display.update()

