from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self, image_1, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image_1),(70,70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 600:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x > win.height:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win.height:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direct = 'Right'
    def update(self):
        if self.rect.x > 600:
            direct = "left"
        if self.rect.x < 5:
            direct = 'right'
        if self.direct == 'left':
            self.rect.x -= self.speed
        if self.direct == 'right':
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1    
        self.color2 = color2   
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


w1 = Wall(0,250,0,120,0,5,410)
w2 = Wall(0,250,0,210,85,5,430)
w3 = Wall(0,250,0,210,85,200,5)
w4 = Wall(0,250,0,410,85,5,100)
w5 = Wall(0,250,0,410,185,150,5)
window = display.set_mode((700,500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.jpg'),(700,500))
window.blit(background,(0, 0))

hero = Hero('hero.png',7,30,20)
cyborg = Enemy('cyborg.png',5,630,300)

final = GameSprite('treasure.png',0,600,400)


clock = time.Clock()
fps = 60
game = True
mixer.music.play()
while game:

    window.blit(background,(0, 0))
    hero.reset()
    cyborg.reset()
    cyborg.update()
    final.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    key_pressed = key.get_pressed()

    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    
    clock.tick(fps)
    display.update()
