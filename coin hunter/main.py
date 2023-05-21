from pygame import *
import pygame
from random import randint
from time import sleep
font.init()
font = font.SysFont('FIXEDSYS', 70)
window = display.set_mode((700, 500))
display.set_caption('coin hunter')
clock = time.Clock()
scoreb = 0
scorer = 0
winb = font.render('PLAYER2 WIN!', True, (0,0,180))
winr = font.render('PLAYER1 WIN!', True, (180,0,0))
scr = font.render(str(scorer), True, (200,10,10))
scb = font.render(str(scoreb), True, (10,10,200))
FPS = 60
game = True
background = transform.scale(image.load('background.jpg'),(700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, imagep, x, y, sx, sy, speed=5):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(imagep), (sx, sy))
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.sx, self.sy)
    def reset(self):
        window.blit(self.image, (self.x,self.y))
        self.rect = pygame.Rect(self.x, self.y, self.sx, self.sy)
class Player(GameSprite):
    def moves(self):
        self.y += self.speed
    def movew(self):
        self.y -= self.speed
    def moved(self):
        self.x += self.speed
    def movea(self):
        self.x -= self.speed
player_ = Player('red.png', 30,200,50,50,5)
playerr = Player('blu.png', 620,200,50,50,5)
coin = GameSprite('aim.png', randint(0,130)*5, randint(0,90)*5, 50 ,50, 0)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    scr = font.render(str(scorer), True, (200,10,10))
    scb = font.render(str(scoreb), True, (10,10,200))
    window.blit(scr, (10, 10))
    window.blit(scb, (660, 10))
    player_.reset()
    playerr.reset()
    coin.reset()
    keys_pressed = key.get_pressed()
    if keys_pressed[K_w] and player_.y >= 0:
        player_.movew()
    if keys_pressed[K_s] and player_.y <= 450:
        player_.moves()
    if keys_pressed[K_d] and playerr.x >= 0:
        player_.moved()
    if keys_pressed[K_a] and player_.x <= 650:
        player_.movea()
    if keys_pressed[K_UP] and playerr.y >= 0:
        playerr.movew()
    if keys_pressed[K_DOWN] and playerr.y <= 450:
        playerr.moves()
    if keys_pressed[K_LEFT] and playerr.x >= 0:
        playerr.movea()
    if keys_pressed[K_RIGHT] and playerr.x <= 650:
        playerr.moved()
    if sprite.collide_rect(player_, coin):
        scorer += 1
        player_ = Player('red.png', 30,200,50,50,5)
        playerr = Player('blu.png', 620,200,50,50,5)
        coin = GameSprite('aim.png', randint(0,130)*5, randint(0,90)*5, 50 ,50, 0)
        if scorer >= 10:
            game = False
            window.blit(winr, (180, 220))
    if sprite.collide_rect(playerr, coin):
        scoreb += 1
        player_ = Player('red.png', 30,200,50,50,5)
        playerr = Player('blu.png', 620,200,50,50,5)
        coin = GameSprite('aim.png', randint(0,130)*5, randint(0,90)*5, 50 ,50, 0)
        if scorer >= 10:
            game = False
            window.blit(winb, (180, 220))
    display.update()
    clock.tick(FPS)
sleep(1)