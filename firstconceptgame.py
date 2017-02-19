import pygame
import random
import time


KEY_UP = 273
KEY_DOWN = 274
KEY_RIGHT = 275
KEY_LEFT = 276

class allScenes(object):
    def __init__(self):
        self.height = 700
        self.width = 500



class Scene_1(allScenes):
    def __init__(self):
        self.height = 700
        self.width = 500
        self.background = pygame.image.load('images/scene1.png').convert_alpha()


    def displayScene(self, screen):
        screen.blit(self.background, (0,0))



class Scene_2(allScenes):
    def __init__(self):
        self.height = 500
        self.width = 700
        self.background = pygame.image.load('images/scene2.png').convert_alpha()

    def displayScene(self,screen):
        screen.blit(self.background, (0,0))

    def multiply(self):
        pygame.draw.alien()



class Scene_3(allScenes):
    def __init__(self):
        self.height = 700
        self.width = 500
        self.background = pygame.image.load('images/scene3.png').convert_alpha()

    def displayScene(self, screen):
        screen.blit(self.background, (0,0))



class Character(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.x_dir = 0
        self.y_dir = 0
        self.image = image
        self.alive = True
        self.Sound = True
        self.health = 3


    def displayCharacter(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))

    def move_character(self):
        self.x += self.x_dir
        self.y += self.y_dir

class Player1(Character):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/spaceship.png').convert_alpha()
        self.name = 'Player 1'
        self.x = x
        self.y = y
        self.x_dir = 0
        self.y_dir = 0
        self.alive = True
        self.health = 10
        self.power = 5


    def displayCharacter(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))

    def off_screen(self):
        if self.y < 31:      #top
            self.y = 31

        if self.x > 450:    #right
            self.x = 450

        if self.y > 680:     #down
            self.y =  680

        if self.x < 31:       #left
            self.x =  31



class Aliens(Character):
    def __init__(self, x, y):
        self.name = 'aliens'
        self.x = x
        self.y = y
        self.x_dir = 0
        self.y_dir = 0
        self.image = pygame.image.load('images/alien.png').convert_alpha()
        self.alive = True
        self.Sound = True

    def displayCharacter(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))


    def change_direction(self):

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


class Wormhole(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_dir = 1
        self.y_dir = 1
        self.alive = True
        self.image = pygame.image.load('images/wormhole.png').convert_alpha()

    def displayCharacter(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))

    def restart(self, screen):
        if self.alive == False:
            self.alive == True


# class Map(object):
#     def __init__(self):
#         pass
#
#     def scene_1(self, start_name):
#         pass
#
#     def scene_2(self, start_name):
#         pass
#
#     def scene_3(self, start_name):
#         pass



def main():
    width = 500
    height = 700
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/scene1.png').convert_alpha()
    music = pygame.mixer.Sound('sounds/music.wav')
    lose_effect = pygame.mixer.Sound('sounds/lose.wav')
    win_effect = pygame.mixer.Sound('sounds/win.wav')

    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()


    # Game initialization

    player1 = Player1(250,550)
    alien_list = [
        Aliens(30,90),
        Aliens(90,50),
        Aliens(400,60)
    ]

    alien = Aliens(30,90)

    # alien = Aliens(30,90)

    wormhole = Wormhole(30,50)

    scene1 = Scene_1()
    scene2 = Scene_2()
    scene3 = Scene_3()





    music.play()


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


        # Game logic



        alien.move_character()    #moves alien around

# this changes the direct by adding 1 to the original change_dir_count = 0
# every 120 seconds it changes direction
        change_dir_counter += 1
        if change_dir_counter == 120:
            alien.change_direction()   # changes alien direction
            change_dir_counter = 0

        alien.off_screen()             #keeps alien on screen
        player1.off_screen()                #keeps player1 inside screen


        #Colission Detection
        if player1.x + 40 < alien.x:
            pass
            # print "No Collision"
        elif alien.x + 40 < player1.x:
            pass
            # print "No Collision"
        elif player1.y + 40 < alien.y:
            pass
            # print "No Collision"
        elif alien.y + 40 < player1.y:
            pass
            # print "No Collision"
        else:
            player1.alive = False
            lose_effect.play()
            stop_game = True


        if wormhole.x + 32 < player1.x:
            pass
            # print "No Collision"
        elif wormhole.x + 32 < player1.x:
            pass
            # print "No Collision"
        elif wormhole.y + 32 < player1.y:
            pass
            # print "No Collision"
        elif wormhole.y + 32 < player1.y:
            pass
            # print "No Collision"
        else:
            wormhole.alive = False
            win_effect.play()




        #
        # screen.blit(background_image, (0,0))

        # scene1.displayScene(screen)
        scenes = [scene1, scene2, scene3]

        scene1.displayScene(screen)


        alien.displayCharacter(screen)

        wormhole.displayCharacter(screen)
        player1.displayCharacter(screen)




        # for scene in scenes:
        #     scenes = scene + 1
        #     print "the scene is changing i hope" % scene
        #
        #     #  # print "what scene is playing %s" % scenes
            #     m = scenes[i].displayScene(screen)







        pygame.display.update()

main()
