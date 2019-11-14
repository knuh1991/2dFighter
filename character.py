import pygame
from pygame.sprite import Sprite

from sprite_sheet import Sprite_Sheet


class Character(Sprite):
    """ A class to represent the general character."""

    def __init__(self,game):
        """Initialize the starting position of the character to be at either
           the bottom left or bottom right corner of the screen."""
        super().__init__()

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Loading the sprite sheet and the get the rect of the basic character stances.
        self.sprite_sheet = Sprite_Sheet('images/drabbit_sheet.png')
        self.sprite_sheet_norm = pygame.image.load('images/drabbit_sheet.png')
        self.sprite_sheet_rect  = self.sprite_sheet_norm.get_rect()
        self.image = self.sprite_sheet.image_at((10,0,60,100))
        self.rect = self.image.get_rect()
        # Start the players character at the bottom left side corner of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Assigns animations
        self.assign_animations()



    def assign_animations(self):
        """Initialize all the animations"""

        #This method initializes all the animations from the spritesheet
        self.stance_animation_strip = self.sprite_sheet.load_strip((10,10,200,328),4)
        self.running_animation_strip = self.sprite_sheet.load_strip(())
        self.basic_punch_animation_strip = self.sprite_sheet.load_strip(())
        self.basic_kick_animation_strip = self.sprite_sheet.load_strip(())
        self.victory_animation_strip = self.sprite_sheet.load_strip(())
        self.damage_animation_strip = self.sprite_sheet.load_strip(())
        self.defeat_animation_strip = self.sprite_sheet.load_strip(())
        

        """
        Use the images_at function and then load the images using the coordinates of the first
        image of the sequence and the number of images that are part of the sequence.

        Example:
            Number of images that are part of the sequence = 4
            Position 1: x,y,w,h
            Position 2: x=x+w,y,w,h
            Position 3: x=x+w,y,w,h
            Position 4: x=x+w,y,w,h

            (The above only manages selecting the character animation from the spritesheet strip.
            The Movement that is related will be explained later.)

            Drawing each of the sprites:
            # Initiated when the user presses the right arrow key
            self.anim_pos = 0
            // This animation is preset to 0 in the constructor.
            def draw_running_animation(self):
                animation_sequence = 4 # The number of images that are part of the animation sequence
                pos_x, pos_y = 10,10
                width,height = 46,85
                if self.anim_pos < len(animation_sequence):
                    image = self.image_at((pos_x,pos_y,width,height))
                    self.rect = self.image
                    pos_x += width

                    #Display the selected sprite on the screen
                    self.blit(image,rect)





        """


        #basic punch

        #basic kick


    def blitme(self):
        """Draw the character at its current location."""
        pass

        #self.basic_stance()

    def running(self,isRunning = True):
        self.run_seq = self.sprite_sheet.load_strip((75,0,57,75),4)

        while isRunning:
            for run_img in self.run_seq:
                self.rect = run_img.get_rect()
                self.screen.blit(run_img, self.rect)

    def basic_stance(self):
        width = 46
        height = 82
        pos_x = 5
        pos_y = 5


    #The image with the punch or kick will have a larger width than the width of the other animations.
    def basic_punch(self):

        pass

    def basic_kick(self):
        pass

    def hurt_anim(self):
        pass

    def victory_stance(self):
        pass
