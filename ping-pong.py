from pygame import *
from random import randint
from time import time as timer

lost = 0
score = 0
num_fire = 0 
rel_time = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,speed_y,speed_x, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < 328:
            self.rect.y += self.speed_y
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < 328:
            self.rect.y += self.speed_y
class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y   
        if self.rect.y >=465 or self.rect.y <= 5:
            self.speed_y = self.speed_y * -1
        if self.rect.x >= 665 or self.rect.x <=5:
            self.speed_x = self.speed_x * -1
            
window = display.set_mode((700,500))

clock = time.Clock()
FPS = 60

background = transform.scale(image.load("background.jpg"), (700,500))
player = Player('player.png', 645, 222,5,0, 50, 170)
player2 = Player('player.png', 6, 222,5, 0,50, 170)
ball = Ball('ball.png',350,250,8,8,50,50)

finish = False
game = True
while game:
    if not finish:
        window.blit(background,(0,0))
        player.reset()
        player.update()
        player2.reset()
        player2.update2()
        ball.reset()
        ball.update()
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)