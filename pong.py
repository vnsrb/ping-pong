import sys
from pygame import *
from pygame.locals import QUIT

init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
pelota = 'pelota-de-tenis.png'
plataforma = 'plataforma.png'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACK_COLOR = (173, 216, 230)
FPS = 120

# Main screen
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Pong!')


# MainSprite class
class MainSprite(sprite.Sprite):

    def __init__(self, sprite_img, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Paddle class
class Paddle(MainSprite):

    def __init__(self, sprite_img, x, y, width, height, speed):
        super().__init__(sprite_img, x, y, width, height, speed)

    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

class Pelota(MainSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = randint(0, SCREEN_WIDTH - 50)
            


pelota = Pelota(pelota, 320, 240, 50, 50, 5)
speed_x, speed_y = 3, 3

#plataforma = Paddle(plataforma, 400, 560, 100, 30)

finish = False
run = True
clock = time.Clock()

while run:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()

    if not finish:
        screen.fill(BACK_COLOR)
        pelota.reset()
        pelota.rect.x += speed_x
        pelota.rect.y += speed_y

    if pelota.rect.y > SCREEN_HEIGHT - 50 or pelota.rect.y < 0:
        speed_y *= -1

    display.update()
    clock.tick(FPS)

quit()
