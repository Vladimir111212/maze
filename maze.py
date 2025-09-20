from pygame import *
init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height, weight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (height, weight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x       
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if keys_press[K_a] and self.rect.x > -5:
            self.rect.x -= self.speed
        if keys_press[K_d] and self.rect.x < 600:
            self.rect.x += self.speed
        if keys_press[K_w] and self.rect.y > -2:
            self.rect.y -= self.speed
        if keys_press[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height, weight):
        super().__init__(player_image, player_x, player_y, player_speed, height, weight)
        self.direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= 480:
            self.direction = 'right'
        elif self.rect.x >= 660:
            self.direction = 'left'
        
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_height, wall_weight):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.height = wall_height
        self.weight = wall_weight
        self.image = Surface((self.height, self.weight))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        win.blit(self.image, (self.rect.x, self.rect.y))




finish = False
win = display.set_mode((700, 500))
font1 = font.SysFont('Arial', 80)
window1 = font1.render('YOU WIN!', True, (255, 220, 6))
font2 = font.SysFont('Arial', 80)
window2 = font2.render('YOU LOSE!', True, (0, 0, 255))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))
music = mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
sprite1 = Player('hero.png', 0, 420, 4, 45, 50)
sprite2 = Enemy('cyborg.png', 620, 290, 5, 60, 60)
sprite3 = GameSprite('treasure.png', 560, 400, 0, 80, 80)
wall1 = Wall(20, 225, 0, 80, 390, 80, 10)
wall2 = Wall(20, 225, 0, 80, 480, 180, 10)
wall3 = Wall(20, 225, 0, 160, 100, 10, 300)
wall4 = Wall(20, 225, 0, 250, 220, 10, 265)
wall5 = Wall(20, 225, 0, 100, 90, 70, 10)
wall6 = Wall(20, 225, 0, 100, 10, 10, 85)
wall7 = Wall(20, 225, 0, 100, 10, 490, 10)
wall8 = Wall(20, 225, 0, 250, 80, 10, 140)
wall9 = Wall(20, 225, 0, 250, 80, 200, 10)
wall10 = Wall(20, 225, 0, 580, 10, 10, 80)
wall11 = Wall(20, 225, 0, 530, 80, 50, 10)
wall12 = Wall(20, 225, 0, 450, 80, 10, 450)
wall13 = Wall(20, 225, 0, 530, 80, 10, 70)
wall14 = Wall(20, 225, 0, 530, 150, 140, 10)
wall15 = Wall(20, 225, 0, 660, 150, 10, 40)



clock = time.Clock()
FPS = 60


game = True
while game:
    keys_press = key.get_pressed()
    if finish != True:
        win.blit(background, (0, 0))
        sprite1.reset()
        sprite2.reset()
        sprite3.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()
        wall11.draw_wall()
        wall12.draw_wall()
        wall13.draw_wall()
        wall14.draw_wall()
        wall15.draw_wall()

        sprite1.update()
        sprite2.update()
        if sprite.collide_rect(sprite1, sprite3):
            win.blit(window1, (200, 200))
            finish = True
            money.play()
        
        if sprite.collide_rect(sprite1, sprite2):
            win.blit(window2, (200, 200))
            finish = True
            kick.play()
        
        if sprite.collide_rect(sprite1, wall1) or sprite.collide_rect(sprite1, wall2) or sprite.collide_rect(sprite1, wall3) or sprite.collide_rect(sprite1, wall4) or sprite.collide_rect(sprite1, wall5) or sprite.collide_rect(sprite1, wall6) or sprite.collide_rect(sprite1, wall7) or sprite.collide_rect(sprite1, wall8) or sprite.collide_rect(sprite1, wall9) or sprite.collide_rect(sprite1, wall10) or sprite.collide_rect(sprite1, wall11) or sprite.collide_rect(sprite1, wall12) or sprite.collide_rect(sprite1, wall13) or sprite.collide_rect(sprite1, wall14) or sprite.collide_rect(sprite1, wall15):
            sprite1.rect.x = 0
            sprite1.rect.y = 420
            kick.play()

    if finish == True:
        if keys_press[K_r]:
            finish = False
            sprite1.rect.x = 0
            sprite1.rect.y = 420


    for i in event.get():
            if i.type == QUIT:
                game = False
    clock.tick(FPS)
    display.update()








