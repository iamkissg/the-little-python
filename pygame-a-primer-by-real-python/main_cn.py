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

        # 创建 Surface 矩形, 白色填充
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))

        # 使用图片作为 Surface
        # image 也是 Surface 对象
        self.image = pygame.image.load("jet.bmp").convert()
        # 默认图片是透明的, 因此, 设置 colorkey 为白色, 模式为 RLEACCEL
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            # move_ip - move in place
            self.rect.move_ip(0, -1);
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1);
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0);
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0);

        # 保证 Player 在屏幕上
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
        # 随机初始化敌人的速度
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        # 当敌人离开屏幕区域, 用 kill 方法销毁, 释放内存
        if self.rect.right < 0:
            self.kill()

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


# 初始化所有导入的模块, 该函数必须在所有操作之前进行
pygame.init()

screen = pygame.display.set_mode((800, 600))

# 自定义事件, 唯一的, 且大于 USEREVENT
ADDENEMY = pygame.USEREVENT + 1
# 设置事件的计时器, 250 ms
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player()

# 设置背景为天蓝色
background = pygame.Surface(screen.get_size())
background.fill((135, 206, 250))

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

# 游戏主循环退出的标志
running = True

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

    # blit 用于绘制
    # 绘制背景, 需要在主循环内刷新绘制背景, 否则会很难看
    screen.blit(background, (0, 0))
    # 获取用户键入
    pressed_keys = pygame.key.get_pressed()
    # 根据用户键入, 更新 player
    player.update(pressed_keys)
    # 更新敌人与云
    enemies.update()
    clouds.update()

    # 绘制敌人
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # 冲突, 若敌人与 player 相撞, 消灭 player
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

    # flip 用于显示与上一次的差别
    pygame.display.flip()

