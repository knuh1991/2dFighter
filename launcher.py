import sys
import pygame
from character import Character

class Launcher:
    """ The Launcher class that will be the first view when the game is initiated."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,400))
        pygame.display.set_caption("Best Adevnture Game Ever")
        self.bg_color = (50,50,225)



        #Character
        self.character = Character(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.bg_color)

        #Draws the characters basic stance animation on the screen
        self.character.basic_stance()
        # Updates the screen so that it redraws itself. If placed inbetween a sprite that is meant to be displayed, the sprite that is placed below this command will never be shown.
        pygame.display.flip()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keyup_events(self,event):
        if event.key == pygame.K_d:
            self.character.basic_stance()
    def _check_keydown_events(self,event):
        if event.key == pygame.K_q:
            sys.exit()




if __name__ == '__main__':
    launcher = Launcher()
    launcher.run_game()
