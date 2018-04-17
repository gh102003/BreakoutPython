import numpy
import pygame
from pygame import gfxdraw


def normalise_vector(vector):
    magnitude = numpy.hypot(vector[0], vector[1])
    return numpy.divide(vector, magnitude)


class Bullet(pygame.sprite.Sprite):
    radius = 8
    speed = 8
    acceleration = 0.002

    def __init__(self, position, movement):
        pygame.sprite.Sprite.__init__(self)

        # Setup texture
        self.image = pygame.Surface((Bullet.radius * 2 + 1, Bullet.radius * 2 + 1))
        gfxdraw.aacircle(self.image, Bullet.radius, Bullet.radius, Bullet.radius, (255, 255, 255))
        gfxdraw.filled_circle(self.image, Bullet.radius, Bullet.radius, Bullet.radius, (255, 255, 255))

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect.topleft = position

        self.movement = movement

    def update(self, breakout):
        self.rect.center = numpy.add(self.rect.center, numpy.multiply(normalise_vector(self.movement), Bullet.speed))

        # Bounce if not on screen
        if self.rect.centerx <= 0 or self.rect.centerx >= breakout.window_size[0]:
            self.movement[0] *= -1

        if self.rect.centery <= 0 or self.rect.centery >= breakout.window_size[1]:
            self.movement[1] *= -1

        # Increase speed by acceleration
        Bullet.speed += Bullet.acceleration

        self.detect_collisions(breakout)

    def detect_collisions(self, breakout):
        # Detect collisions with bullet and bricks
        bricks_collided = pygame.sprite.spritecollide(self, breakout.bricks, False)
        for brick in bricks_collided:
            # Increment score
            breakout.score = 100

            # Detect point of brick that was hit in order to determine bounce direction
            collision_point = pygame.sprite.collide_mask(self, brick)
            print(pygame.sprite.collide_mask(self, brick))

            brick.kill()
        # Detect collisions with bullet and paddle
        if pygame.sprite.collide_rect(self, breakout.paddleRef):
            self.movement[1] *= -1
            # print(pygame.sprite.collide_rect(self, breakout.paddleRef))
            # print(self.mask.get_size())

            xoffset = breakout.paddleRef.rect[0] - self.rect[0]
            yoffset = breakout.paddleRef.rect[1] - self.rect[1]
            # print(yoffset, xoffset)
            # print(self.mask.overlap(pygame.mask.from_surface(breakout.paddleRef.image), (xoffset, yoffset)))
