import pygame
import random


class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.alive = True
        self.speed = 5
        self.y_dir = 0
        self.x_dir = 0
        self.image, self.rect = load_image('images/spaceship.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10

    def update(self):
        self.x += self.x_dir
        self.y += self.y_dir

    def display(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))

    def off_screen(self):
        if self.y < 10:      #top
            self.y = 20

        if self.x > 420:    #right
            self.x = 420

        if self.y > 640:     #down
            self.y =  640

        if self.x < 10:       #left
            self.x =  10

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'aliens'
        self.x = x
        self.y = y
        self.x_dir = 0
        self.y_dir = 0
        self.image = pygame.image.load('images/alien.png').convert_alpha()
        self.alive = True
        self.alien = +1
        self.Sound = True



    def display(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))


    def update(self):
        self.x += self.x_dir
        self.y += self.y_dir

        rand_direction = random.randint(0,7)


        if rand_direction == 0:   # top or north
            self.x_dir = 0
            self.y_dir = -1

        elif rand_direction == 1:  #right or east
            self.x_dir = 1
            self.y_dir = 0

        elif rand_direction == 2:  #down or south
            self.x_dir =0
            self.y_dir = 1

        elif rand_direction == 3:  #left or west
            self.x_dir =-1
            self.y_dir = 0

        elif rand_direction == 4:   # Northeast - topright
            self.x_dir = 1
            self.y_dir = -1

        elif rand_direction == 5:  # Northwest - top left
            self.x_dir = -1
            self.y_dir = -1

        elif rand_direction == 6:  # Southwest - bottom left
            self.x_dir = -1
            self.y_dir = 1

        elif rand_direction == 7:  # South east - bottom right
            self.x_dir = 1
            self.y_dir = 1


    def off_screen(self):
        if self.y < 0:      #top
            self.y =  480
        else:
            self.y -= 5

        if self.x > 512:    #right
            self.x = 0
        else:
            self.x += 5

        if self.y > 480:     #down
            self.y =  0
        else:
            self.y += 5

        if self.x < 0:       #left
            self.x =  512
        else:
            self.x -= 5


class Wormhole(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'wormhole'
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/wormhole.png').convert_alpha()
        self.alive = True
        self.Sound = True


    def display(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))


class Wormhole2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'wormhole'
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/wormhole2.png').convert_alpha()
        self.alive = True
        self.Sound = True


    def display(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))


class spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'spaceship'
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/spaceship.png').convert_alpha()
        self.alive = True
        self.Sound = True


    def display(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))



class Background():
    def __init__(self):
        self.name = 'spaceship'
        self.width = 500
        self.height = 700
        self.background1 = pygame.image.load('images/scene1.png').convert_alpha()
        self.background2 = pygame.image.load('images/scene2.png').convert_alpha()
        self.background3 = pygame.image.load('images/scene3.png').convert_alpha()
        self.alive = 1
        self.Sound = True

    def display(self, screen):
        if self.alive == 1:
            screen.blit(self.image, (self.x,self.y))
        if self.alive == 2:
            screen.blit(self.image, (self.x,self.y))
        if self.alive == 3:
            screen.blit(self.image, (self.x,self.y))


game_loop = True

def main():

    width = 500
    height = 700

    white = (255, 250, 250)
    purple = (132, 112, 255)
    yellow = (255, 215, 0)

    pygame.init()

    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont('monospace', 30)      #sysfont creates font object
    surfacefont = font.render('Level 1', True, purple, white)
    surfacer = surfacefont.get_rect()

    surfacer.center = (250,650)

    wormhole_sound = pygame.mixer.Sound('sounds/music.wav')
    music = pygame.mixer.Sound('sounds/music.wav')
    lose_effect = pygame.mixer.Sound('sounds/lose.wav')
    win_effect = pygame.mixer.Sound('sounds/win.wav')

    start_ticks=pygame.time.get_ticks() #starter tick

    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()


    player1 = Player1(100,550)

    alien = Aliens(70, 70)
    alien2 = Aliens(400, 100)
    alien3 = Aliens(500,400)

    wormhole = Wormhole(30,40)
    wormhole2 = Wormhole2(90,500)
    spaceship = spaceship(300,40)

    music.play()


    wormholes = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    aliens.groups = allgroup


    scene1 = Background()
    scene2 = Background()
    scene3 = Background()



while True:
    if pygame.sprite.spritecollide(bird,pipes):
        print "Game Over"



    #assign default groups to each sprite class
    Bird.groups = birdgroup, allgroup
    BirdCatcher.groups = allgroup
    Bird()
    # display the BirdCatcher and name it "hunter"
    hunter = BirdCatcher()


    stop_game = False

    change_dir_counter = 0       # original change_dir_count


    while not stop_game:

        for event in pygame.event.get():


# this is for controlling the player1 with the keyboard, declared keys at
#the top of the page, and set controls in the pygame.event.get()

            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    player1.y += 30
                elif event.key == KEY_UP:
                    player1.y -= 30
                elif event.key == KEY_LEFT:
                    player1.x -= 30
                elif event.key == KEY_RIGHT:
                    player1.x += 30

            if event.type == pygame.QUIT:
                stop_game = True

        # for alien in alien_list:        #moves alien
        #     print alien.update()
        # for alien in alien_list:        #call aliens from list
        #     print alien.off_screen()


        # seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        # if seconds>25: # if more than 10 seconds close the game
        #     break
        # print (seconds)
        # # Game logic

        if pygame.sprite.spritecollide(bird,pipes):
            print "Game Over"

# this changes the direct by adding 1 to the original change_dir_count = 0
# every 120 seconds it changes direction
        change_dir_counter += 1

        if change_dir_counter == 120:
            alien.change_direction()   # changes alien direction
            alien2.change_direction()
            alien3.change_direction()
            change_dir_counter = 0
