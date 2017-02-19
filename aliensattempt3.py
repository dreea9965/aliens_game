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


    def display(self, screen):
        screen.blit(self.background, (0,0))



class Scene_2(allScenes):
    def __init__(self):
        self.height = 500
        self.width = 700
        self.background = pygame.image.load('images/scene2.png').convert_alpha()

    def display(self,screen):
        screen.blit(self.background, (0,0))

    def multiply(self):
        pygame.draw.alien()



class Scene_3(allScenes):
    def __init__(self):
        self.height = 700
        self.width = 500
        self.background = pygame.image.load('images/scene3.png').convert_alpha()

    def display(self, screen):
        screen.blit(self.background, (0,0))



class Character(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.x_dir = 0
        self.y_dir = 0
        self.image = image
        self.Sound = True



    def display(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))

    def update(self):
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


    def display(self,screen):
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
        self.alive = True
        self.image = pygame.image.load('images/wormhole.png').convert_alpha()
        self.background2 = pygame.image.load('images/wormhole2.png').convert_alpha()
        self.spaceship = pygame.image.load('images/spaceship.png').convert_alpha()

    def display(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))





class Wormhole_2(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.image = pygame.image.load('images/wormhole2.png').convert_alpha()

    def display(self,screen):
        if self.alive == True and wormhole.alive == False:
            screen.blit(self.image, (self.x,self.y))


class Home(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.image = pygame.image.load('images/homebase.png').convert_alpha()


    def display(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))



def main():
    width = 500
    height = 700

    white = (255, 250, 250)
    purple = (132, 112, 255)
    yellow = (255, 215, 0)



    pygame.init()
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont('monospace', 30)      #sysfont creates font object
    surfacefont = font.render('Do you want to play again?', True, purple, white)
    surfacer = surfacefont.get_rect()
    surfacer.center = (250,680)

    wormhole_sound = pygame.mixer.Sound('sounds/music.wav')
    music = pygame.mixer.Sound('sounds/music.wav')
    lose_effect = pygame.mixer.Sound('sounds/lose.wav')
    win_effect = pygame.mixer.Sound('sounds/win.wav')

    start_ticks=pygame.time.get_ticks() #starter tick

    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()


    # Game initialization

    player1 = Player1(100,550)

    alien = Aliens(70, 70)
    alien2 = Aliens(400, 100)
    alien3 = Aliens(500,400)

    wormhole = Wormhole(30,40)
    wormhole2 = Wormhole_2(30,490)
    spaceship = Home(300,40)

    music.play()



    scene1 = Scene_1()
    scene2 = Scene_2()
    scene3 = Scene_3()



    stop_game = False

    change_dir_counter = 0       # original change_dir_count


    while not stop_game:
        screen.blit(surfacefont, surfacer)

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




# this changes the direct by adding 1 to the original change_dir_count = 0
# every 120 seconds it changes direction
        change_dir_counter += 1

        if change_dir_counter == 120:
            alien.change_direction()   # changes alien direction
            alien2.change_direction()
            alien3.change_direction()
            change_dir_counter = 0






        alien.update()                  #moves alien around
        alien2.update()
        alien3.update()



        alien.off_screen()             #keeps alien on screen
        alien2.off_screen()
        alien3.off_screen()

        player1.off_screen()

                                    #keeps player1 inside screen

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


        if player1.x + 40 < alien2.x:
            pass
            # print "No Collision"
        elif alien2.x + 40 < player1.x:
            pass
            # print "No Collision"
        elif player1.y + 40 < alien2.y:
            pass
            # print "No Collision"
        elif alien2.y + 40 < player1.y:
            pass
            # print "No Collision"
        else:
            player1.alive = False
            lose_effect.play()
            stop_game = True


        if player1.x + 40 < alien3.x:
            pass
            # print "No Collision"
        elif alien3.x + 40 < player1.x:
            pass
            # print "No Collision"
        elif player1.y + 40 < alien3.y:
            pass
            # print "No Collision"
        elif alien3.y + 40 < player1.y:
            pass
            # print "No Collision"
        else:
            player1.alive = False
            lose_effect.play()
            stop_game = True


        if wormhole.x + 32 < player1.x:
            pass
            # print "No Collision"
        elif wormhole.x + 32 > player1.x:
            pass
            # print "No Collision"
        elif wormhole.y + 32 < player1.y:
            pass
            # print "No Collision"
        elif wormhole.y + 32 > player1.y:
            pass
            # print "No Collision"
        else:
            wormhole.alive = False
            win_effect.play()


        if wormhole.alive == False:
            wormhole2.display(screen)


        if wormhole2.x + 32 < player1.x:
            pass
            # print "No Collision"
        elif wormhole2.x + 32 > player1.x:
            pass
            # print "No Collision"
        elif wormhole2.y + 32 < player1.y:
            pass
            # print "No Collision"
        elif wormhole2.y + 32 > player1.y:
            pass
            # print "No Collision"
        else:
            wormhole2.alive = False
            win_effect.play()



        if wormhole.alive == False and wormhole2.alive == False:
            if spaceship.x + 32 < player1.x:
                pass
                # print "No Collision"
            elif spaceship.x + 32 > player1.x:
                pass
                # print "No Collision"
            elif spaceship.y + 32 < player1.y:
                pass
                # print "No Collision"
            elif spaceship.y + 32 > player1.y:
                pass
                # print "No Collision"
            else:
                spaceship.alive = False
        #

        if wormhole.alive == True:
            scene1.display(screen)

        elif wormhole.alive == False:
            scene2.display(screen)
            alien2.display(screen)
            wormhole2.display(screen)
            alien2.off_screen()

        # elif wormhole2.alive == False:
        #     scene3.display(screen)
        #     alien3.display(screen)
        #
        # elif spaceship.alive == False:
        #     break
        #
        # text you found the mothership, you win!




        # scenes = [scene1, scene2, scene3]

        # for scene in range(len(scenes)):
        #     background = scenes[scene].display(screen)
        #     background += 1
        #     if wormhole.alive == False:
        #         background
        #         print background
        #         break
        #
        # for scene in range(len(scenes)):
        #     new_scene = scenes[scene]
        #     if wormhole.alive == False:
        #         new_scene.displayScene(screen)
        #         print new_scene
        # #

        # scene1.display(screen)

        # for alien in alien_list:        #call aliens from list




        #
        alien.display(screen)

        wormhole.display(screen)
        wormhole2.display(screen)

        player1.display(screen)

        # scene1.displayScene(screen)



            #  # print "what scene is playing %s" % scenes
                # m = scenes[i].displayScene(screen)



        pygame.display.update()


main()
