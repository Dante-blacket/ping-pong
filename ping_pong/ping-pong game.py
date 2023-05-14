from pygame import *
import pygame
from random import randint
from time import sleep
font.init()
font = font.Font(None, 50)
win_ = font.render('PLAYER1 LOSE!', True, (255,215,0))
lose_ = font.render('PLAYER2 LOSE!', True, (180,0,0))
window = display.set_mode((700, 500))
display.set_caption('window')
clock = time.Clock()
miss = 0
score = 0
sc = font.render('Счет:'+str(score), True, (255,255,255))
mi = font.render('Пропущено:'+str(miss), True, (255,255,255))
FPS = 60
game = True
background = transform.scale(image.load('background.jpg'),(700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, imagep, x, y, sx, sy, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(imagep), (sx, sy))
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.speedy = speed
        self.speedx = speed
        self.rect = pygame.Rect(self.x, self.y, self.sx, self.sy)
    def reset(self):
        window.blit(self.image, (self.x,self.y))
        self.rect = pygame.Rect(self.x, self.y, self.sx, self.sy)
class Player(GameSprite):
    def moves(self):
        self.y += 4
    def movew(self):
        self.y -= 4
class Ball(GameSprite):
    def update(self):
        self.y += self.speedy
        self.x -= self.speedx
        window.blit(self.image, (self.x,self.y))
        self.rect = pygame.Rect(self.x, self.y, self.sx, self.sy)
    def collidel(self, player):
        if (player.y-self.y < 50 and player.y-self.y > -150) and (player.x-self.y < 1):
            pass
player_ = Player('racket.png', 30,200,50,150,None)
playerr = Player('racket.png', 620,200,50,150,None)
ball = Ball('tenis_ball.jpg', 200, 200, 50, 50, 3)
while game:
    window.blit(background,(0,0))
    player_.reset()
    playerr.reset()
    ball.update()
    if sprite.collide_rect(player_, ball) or sprite.collide_rect(playerr, ball):
        ball.speedx *= -1
    if ball.y > 450 or ball.y < 0:
        ball.speedy *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    if ball.x <= 0:
        window.blit(win_, (5, 5))
        game = False
    if ball.x >= 650:
        window.blit(lose_, (5, 5))
        game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_w] and player_.x > 5:
        player_.movew()
    if keys_pressed[K_s] and player_.x < 595:
        player_.moves()
    if keys_pressed[K_UP] and player_.x > 5:
        playerr.movew()
    if keys_pressed[K_DOWN] and player_.x < 595:
        playerr.moves()
    display.update()
    clock.tick(FPS)
sleep(1)