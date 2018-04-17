import pygame
import os

brick_texture = pygame.image.load(os.path.join("img", "brick.png"))


class Brick(pygame.sprite.Sprite):
    dimensions = (40, 40)

    def __init__(self, colour, position):
        pygame.sprite.Sprite.__init__(self)

        # Setup texture
        self.image = pygame.Surface(Brick.dimensions)
        self.image.fill(colour)
        scaled_brick_texture = pygame.transform.scale(brick_texture, Brick.dimensions)
        self.image.blit(scaled_brick_texture, (0, 0))

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect.topleft = position
