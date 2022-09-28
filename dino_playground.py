import arcade
import random

class Ground(arcade.Sprite):
    def __init__(self, x , y):
        super().__init__()

        self.texture = arcade.load_texture(":resources:images/tiles/grassRight.png")

        self.center_x = x
        self.center_y = y

        self.width = 120
        self.height = 120
        

class Dino(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()

        self.name = 'Dino'

        self.stand_right_textures = [arcade.load_texture('dinoimage/Dino.png'),arcade.load_texture('dinoimage/Dino2.png')]

        self.walk_right_textures = [arcade.load_texture('dinoimage/Dino.png'),
                                    arcade.load_texture('dinoimage/Dino2.png')]

        self.center_x = 100
        self.center_y = 130
        try:
            myFile = open('lastscore.txt', 'r')
            self.highscore = int(myFile.read())
            myFile.close()
        except:
            self.highscore = 0

    def write_highscore(self):
        myFile = open('highscore.txt', 'w')
        myFile.write('%s' %self.score)
        myFile.close()


class Ptera(arcade.Sprite):
    def __init__(self, w , h):
        super().__init__(':resources:images/space_shooter/playerShip2_orange.png')
        self.speed = 4
        self.center_x = w
        self.center_y = random.randint(200,350)
        self.angle = 90
        self.width = 60
        self.height = 60
    def move(self):
        self.center_x -= self.speed

class Cactus(arcade.Sprite):
    def __init__(self, w , h):
        super().__init__(':resources:images/tiles/cactus.png')
        self.speed = 4
        self.center_x = w
        self.center_y = 160
        self.angle = 0
        self.width = 130
        self.height = 130
    def move(self):
        self.center_x -= self.speed




