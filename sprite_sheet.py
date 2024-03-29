
import pygame
class Sprite_Sheet():
    """ The Sprite Sheet class will deal with all the sprite related functions."""
    def __init__(self,image):
        self.sprite_sheet = pygame.image.load(image).convert()


    def image_at(self,rectangle, colorkey = None):
        """Loads image from x,y,x+offset, y+offset"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sprite_sheet, (0,0),rect)

        if colorkey is not None:
            if colorkey is -1:
                color = image.get_at((0,0))
            image.set_colorkey(colorkey,pygame.RLEACCEL)


        return image


    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)]
        return self.images_at(tups,colorkey)
