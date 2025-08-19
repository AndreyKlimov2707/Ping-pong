from pygame import *
from random import randint
from time import time as timer

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
score1 = 0
score2 = 0
score_label = font1.render(str(score1) + ':' + str(score2), None, (250, 250, 250))
goal_label = font1.render('Гол!', None, (250, 250, 250))


last_goal_time = 0
game = True
end = False
new_goal = True
clock = time.Clock()
while game:
    if not end:
        window.blit(background, (0, 0))
        rakcet1.reset()
        rakcet1.update(K_w, K_s)
        racket2.reset()
        racket2.update(K_UP, K_DOWN)
        ball.reset()
        window.blit(score_label, (300, 0))
        if sprite.collide_rect(rakcet1, ball):
            ball_direction1 = 'right'
        if sprite.collide_rect(ball, racket2):
            ball_direction1 = 'left'


        if score1 > 2:
            end_label = font1.render('Игрок 1 победил!', None, (250, 0, 0))
            end = True
            last_goal_time = 0
        if score2 > 2:
            end_label = font1.render('Игрок 2 победил!', None, (0, 0, 250))
            end = True
            last_goal_time = 0

        if timer() - last_goal_time > 3:
            if new_goal:
                new_goal = False
                if randint(0, 1) == 0:
                    ball_direction1 = 'left'
                else:
                    ball_direction1 = 'right'
                if randint(0, 1) == 0:
                    ball_direction2 = 'up'
                else:
                    ball_direction2 = 'down'
                ball.speed = 5
            move_ball()
        else:
            window.blit(goal_label, (300, 225))

        if ball.rect.x <= -41:
            score2 += 1
            ball.speed = 0
            new_goal = True
            last_goal_time = timer()
            ball.rect.x = 425
            ball.rect.y = 325
            score_label = font1.render(str(score1) + ':' + str(score2), None, (250, 250, 250))
            
        if ball.rect.x >= 700:
            score1 += 1
            ball.speed = 0
            new_goal = True
            last_goal_time = timer()
            ball.rect.x = 425
            ball.rect.y = 325
            score_label = font1.render(str(score1) + ':' + str(score2), None, (250, 250, 250))

    if end:
        window.blit(end_label, (150, 225))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
