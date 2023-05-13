from pygame import *
import pygame
from random import randint
font.init()
font = font.Font(None, 50)
win_ = font.render('YOU WIN!', True, (255,215,0))
lose_ = font.render('YOU LOSE!', True, (180,0,0))
window = display.set_mode((700, 500))
display.set_caption('window')
clock = time.Clock()
miss = 0
score = 0
sc = font.render('Счет:'+str(score), True, (255,255,255))
mi = font.render('Пропущено:'+str(miss), True, (255,255,255))
FPS = 60
game = True
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')
sprite1 = transform.scale(image.load('rocket.png'),(100, 100))
sprite2 = transform.scale(image.load('ufo.png'),(150, 100))
sprite3 = transform.scale(image.load('bullet.png'),(2, 10))
sprite4 = transform.scale(image.load('asteroid.png'),(100, 100))
background = transform.scale(image.load('galaxy.jpg'),(700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, imagep, x, y, sx, sy, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(imagep), (sx, sy))
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
    def reset(self):
        window.blit(self.image, (self.x,self.y))
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
class Player(GameSprite):
    def moved(self):
        self.x += 7
    def movea(self):
        self.x -= 7
    def fire(self):
        bullet_ = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet_)
class Enemy(GameSprite):
    def update(self):
        self.y += self.speed
        window.blit(self.image, (self.x,self.y))
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        global miss
        global score
        if self.y > 395:
            self.movea()
            miss += 1
        if None:
            self.movea()
            score += 1
    def movea(self):
        self.y = 5
        self.x = randint(5, 550)
class Bullet(GameSprite):
    def update(self):
        self.y -= self.speed
        window.blit(self.image, (self.x,self.y))
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
player_ = Player('rocket.png', 5,400,80,100,None)
enemys = sprite.Group()
for i in range(1,6):
    enemy_ = Enemy('ufo.png', randint(80, 620),-40,80,50,randint(1,4))
    enemys.add(enemy_)
bullets = sprite.Group()
while game:
    window.blit(background,(0,0))
    window.blit(sc, (5, 5))
    window.blit(mi, (5, 35))
    enemys.draw(window)
    bullets.draw(window)
    player_.reset()
    enemys.update()
    bullets.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_a] and player_.x > 5:
        player_.movea()
    if keys_pressed[K_d] and player_.x < 595:
        player_.moved()
    if keys_pressed[K_SPACE]:
        player_.fire()
        #fire_sound.play()
    sc = font.render('Счет:'+str(score), True, (255,255,255))
    mi = font.render('Пропущено:'+str(miss), True, (255,255,255))
    display.update()
    clock.tick(FPS)