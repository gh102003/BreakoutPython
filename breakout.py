import pygame
import paddle
import bullet
import brick
import numpy
import random

class Breakout:
    window_size = (1280, 720)

    # Create font
    pygame.font.init()
    overlay_font = pygame.font.SysFont("consolas", 20)

    score = 0

    # Create sprites
    # Create group for bricks
    bricks = pygame.sprite.Group()

    # Create bricks
    for i in range(20):
        # Calculate colour
        colour = (i * 10 + 55, 200 - i * 10, random.randrange(0, stop=150) + i * 3, 0)

        brickRef = brick.Brick(colour, (i * brick.Brick.dimensions[0], 0))
        bricks.add(brickRef)

    # Add bullet and paddle and create group for all sprites
    sprites = pygame.sprite.Group(bricks)
    paddleRef = paddle.Paddle([window_size[0] / 2, window_size[1] - 80])
    bulletRef = bullet.Bullet(numpy.divide(window_size, 2), [1, 1])
    sprites.add(paddleRef)
    sprites.add(bulletRef)

    def __init__(self):

        # initialize the pygame module
        pygame.init()
        # load and set the logo
        # logo = pygame.image.load(os.path.join("img", "brick.png"))
        # pygame.display.set_icon(logo)
        pygame.display.set_caption("Breakout")

        # create a surface on screen that has the size of 1280x720
        screen = pygame.display.set_mode(Breakout.window_size)

        # define a variable to control the main loop
        running = True

        # a clock for controlling the fps later
        clock = pygame.time.Clock()

        # main loop
        while running:

            # event handling, gets all event from the eventqueue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

            self.update()

            # Format text overlay
            text_overlay = ["Score:{:>10}".format(Breakout.score),
                            "Bullet Speed:{:>6.2f}".format(numpy.round(bullet.Bullet.speed, decimals=2)),
                            "Paddle size:{:>4}".format(Breakout.paddleRef.rect.width),
                            "FPS:{:>15.2f}".format(numpy.round(clock.get_fps(), decimals=2))]

            self.render(screen, text_overlay)

            # FPS control
            clock.tick(60)

    def update(self):
        Breakout.sprites.update(self)

        # # Detect collisions with bullet and blocks
        # for brick in pygame.sprite.spritecollide(bulletRef, bricks, False):
        #     global score
        #     score += 100
        #     brick.kill()
        #
        # # Detect collisions with bullet and paddle
        # if pygame.sprite.collide_rect(bulletRef, paddleRef):
        #     bulletRef.movement[1] *= -1

    def render(self, screen, overlay_text):
        # bullet1.render(screen)
        # paddle1.render(screen)

        # Fill background
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, Breakout.window_size[0], Breakout.window_size[1]))

        Breakout.sprites.draw(screen)

        for i in range(len(overlay_text)):
            text_overlay = Breakout.overlay_font.render(overlay_text[i], 2, (255, 255, 255))
            screen.blit(text_overlay, (Breakout.window_size[0] - 240, i * 25 + 10))

        pygame.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    Breakout()
