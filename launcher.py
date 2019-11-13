import sys
import pygame

class Launcher:
    """ The Launcher class that will be the first view when the game is initiated."""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Best Adevnture Game Ever")
        self.bg_color =(100,130,130)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.bg_color)
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
        pass
    def _check_keydown_events(self,event):
        pass



if __name__ == '__main__':
    launcher = Launcher()
    launcher.run_game()
