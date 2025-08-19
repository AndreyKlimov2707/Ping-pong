from pygame import *
from random import randint

class Game_sprite(sprite.Sprite):
    def __init__(self, sprite_image, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game_sprite):
    def update(self, key_up, key_down):
        keys = key.get_pressed()
        if keys[key_up] and self.rect.y >= -25:
            self.rect.y -= self.speed
        if keys[key_down] and self.rect.y <= 300:
            self.rect.y += self.speed

class Ball(Game_sprite):
    def reset(self):
        window.blit(self.image, (self.rect.x - 41, self.rect.y - 41))

def move_ball():
    global ball_direction1
    global  ball_direction2
    if ball_direction1 == 'right':
        ball.rect.x += ball.speed
    if ball_direction1 == 'left':
        ball.rect.x -= ball.speed
    if ball_direction2 == 'up':
        ball.rect.y -= ball.speed
    if ball_direction2 == 'down':
        ball.rect.y += ball.speed
    if ball.rect.y <= 0:
        ball_direction2 = 'down'
    if ball.rect.y >= 459:
        ball_direction2 = 'up'


window = display.set_mode((700, 500))
background = surface.Surface((700, 500))
background.fill((66, 135, 245))
rakcet1 = Player('Sus.png', 25, 0, 62, 250, 5)
racket2 = Player('Sus.png', 613, 0, 62, 250, 5)
ball = Ball('Zoz.png', 425, 325, 125, 125, 5)
ball.rect = rect.Rect(ball.rect.x, ball.rect.y, 41, 41)
if randint(0, 1) == 0:
    ball_direction1 = 'left'
else:
    ball_direction1 = 'right'
if randint(0, 1) == 0:
    ball_direction2 = 'up'
else:
    ball_direction2 = 'down'

font.init()
font1 = font.Font(None, 70)


game = True
end = False
clock = time.Clock()
while game:
    if not end:
        window.blit(background, (0, 0))
        rakcet1.reset()
        rakcet1.update(K_w, K_s)
        racket2.reset()
        racket2.update(K_UP, K_DOWN)
        ball.reset()
        move_ball()
        if sprite.collide_rect(rakcet1, ball):
            ball_direction1 = 'right'
        if sprite.collide_rect(ball, racket2):
            ball_direction1 = 'left'

        if ball.rect.x <= 0:
            end = True
            end_label = font1.render('Игрок 2 победил!', None, (0, 250, 0))
        if ball.rect.x >= 700:
            end = True
            end_label = font1.render('Игрок 1 победил!', None, (0, 250, 0))

    if end:
        window.blit(end_label, (250, 250))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)