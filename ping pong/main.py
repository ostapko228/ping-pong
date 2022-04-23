from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.self.rect.y < 5:
            self.rect.y -= self.speed
        if keys[K_s]and self.self.rect.y < win_height - 120:
            self.rect.y +- self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.self.rect.y < 5:
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.self.rect.y < win_height - 120:
            self.rect.y +- self.speed

back = (200, 255, 255)
win_wight = 600
win_height = 500
window = display.set_mode((win_wight, win_height))
window.fill(back)
display.set_caption('Ping pong')

game = True
clock = time.Clock()
FPS = 120
finich = False

racket1 = Player('racket1.png', 30, 200, 4, 12, 120)
racket2 = Player('racket2.png', 550, 200, 4, 12, 120)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finich:
        window.fill(back)
        racket1.update_1()
        racket2.update_r()

        racket1.reset()
        racket2.reset()

    display.update()
    clock.tick(FPS)
    
