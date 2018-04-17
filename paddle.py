import pygame
import numpy


class Paddle(pygame.sprite.Sprite):
    thickness = 10
    colour = [255, 0, 0]

    def __init__(self, position, size=150):
        pygame.sprite.Sprite.__init__(self)

        # Setup texture
        self.image = pygame.Surface((size, Paddle.thickness))
        self.image.fill(Paddle.colour)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect.topleft = position

    def update(self, breakout):
        # Set x position to same as the mouse's x position, as long as it is inside the window
        self.rect.x = numpy.clip(pygame.mouse.get_pos()[0] - self.rect.width / 2, 0, breakout.window_size[0] - self.rect.width)

        # def render(self, screen):
        #     pygame.draw.line(screen, Paddle.color, self.position, (self.position[0] + self.size, self.position[1]),
        #                      Paddle.thickness)
