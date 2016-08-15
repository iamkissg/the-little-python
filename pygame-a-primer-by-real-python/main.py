import random
import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    """
    Sprites is the screen object's 2D expression
    Indeed, Sprite is a pic
    """
    def __init__(self):
        super(Player, self).__init__()

        # old way, ugly white rectangle
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))

        # use image as surface
        # image is also a Surface object
        # load a pic, and set color
        self.image = pygame.image.load("jet.bmp").convert()
        # by default, pic will be transparent
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            # move in place
            self.rect.move_ip(0, -1);
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1);
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0);
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0);

        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))

        self.image = pygame.image.load("missile.bmp").convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.speed = 1
        # self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()  # delete, release memory

class Cloud(pygame.sprite.Sprite):

    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load("cloud.bmp").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center = (random.randint(820, 900), random.randint(0, 600))
        )

    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()


# init all the imported model
# do this before any other operations
pygame.init()

# create a screen to display
screen = pygame.display.set_mode((800, 600))

# custom event need a unique value, and > USEREVENT
ADDENEMY = pygame.USEREVENT + 1
# 250 ms trigger event ADDENEMY
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player()

# set background
background = pygame.Surface(screen.get_size())
background.fill((135, 206, 250))

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

# running sign
running = True

# main loop
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif (event.type == ADDENEMY):
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif (event.type == ADDCLOUD):
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)


    # screen is also a Surface instance
    # then we create another Surface instance
    # surf = pygame.Surface((50, 50))
    # set color, and split surf from screen
    # surf.fill((255, 255, 255))
    # rect = surf.get_rect()

    # update displaying, must be in loop
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

    # blit(surface_instance, coordinate)

    # update the whole screen
    # will display the differences between the 2 flips
    pygame.display.flip()

