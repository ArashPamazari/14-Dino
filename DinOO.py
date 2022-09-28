import random
import time
import arcade


from dino_playground import Dino, Ground, Ptera , Cactus


class Game(arcade.Window):
    def __init__(self):
        self.w = 1300
        self.h = 600
        self.gravity = 0.2
        super().__init__(self.w , self.h , 'Dino')
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image_night = arcade.load_texture(":resources:images/cybercity_background/far-buildings.png")
        self.background_image_day = arcade.load_texture(':resources:images/backgrounds/abstract_2.jpg')
        self.time_backgroundChange = time.time()
#ground
        self.ground_list =arcade.SpriteList()
        for i in range(0,1400,120):
            ground = Ground(i,40)
            self.ground_list.append(ground)
#dino
        self.dino = Dino()
        self.die_sound = arcade.load_sound(':resources:sounds/gameover3.wav')
        self.jumping_sound = arcade.load_sound(':resources:sounds/jump2.wav')
        self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.dino , self.ground_list , gravity_constant=self.gravity)
#ptera
        self.ptera_list = arcade.SpriteList()
        self.ptera_time1 = time.time()
#cactus
        self.cactus_list = arcade.SpriteList()
        self.cactus_time1 = time.time()
#score
        self.score = 0
        self.high_score = self.score
        self.time = time.time()
        self.score_speed = 0
#flag
        self.flagDay = 0
        self.flagNight = 0
        self.game_over = False
        self.night = True
    #-------------------------------------------------------------------------------------------------------------------------------------#
    def on_draw(self):
        arcade.start_render()
        self.time_now = time.time()
        if self.game_over:
            if self.night:
                arcade.draw_text('YOU Lose', self.w//2-200, self.h//2, arcade.color.BLACK, 36 , width=400, font_name='Kenney Mini Square', align='center')
            else:
                arcade.draw_text('YOU Lose', self.w//2-200, self.h//2, arcade.color.BLACK, 36 , width=400, font_name='Kenney Mini Square', align='center')
        else:
            arcade.start_render()
            if self.time_now - self.time_backgroundChange > 15:
                self.time_backgroundChange = time.time()
                if self.night:
                    self.night = False
                else:
                    self.night = True
            if self.night:
                arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image_night)
            else:
                arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image_day)

            if self.night:
                arcade.draw_text('High_Score  %s  %s' %(str(self.high_score).zfill(5), str(self.score).zfill(5)), self.w-220, self.h-30, arcade.color.WHITE, 10 , width=400, font_name='Kenney Mini Square', align='left')
            else:
                arcade.draw_text('High_Score  %s  %s' %(str(self.high_score).zfill(5), str(self.score).zfill(5)), self.w-220, self.h-30, arcade.color.BLACK, 10 , width=400, font_name='Kenney Mini Square', align='left')
        
#ground  
        for ground in self.ground_list:
            ground.draw()
#dino
        self.dino.draw()
#ptera
        for ptera in self.ptera_list :
            ptera.draw()
#cactus
        for cactus in self.cactus_list :
            cactus.draw()

    #-------------------------------------------------------------------------------------------------------------------------------------#
    def on_update(self, delta_time: float):
        
#dino
        self.dino.update_animation()
        self.my_physics_engine.update()

        self.time_score = time.time()
        if not self.game_over:
            self.score = int((self.time -self.time_score)*3)

#ptera        
        if self.score > 100:        
                self.ptera_time2 = time.time()
                if self.ptera_time2 - self.ptera_time1 > 10 :
                        new_ptera = Ptera(1300 , 1300)
                        self.ptera_list.append(new_ptera)
                        self.ptera_time1 = time.time()

                
                for ptera in self.ptera_list :
                        ptera.move()

        for ptera in self.ptera_list:
                if  arcade.check_for_collision(self.dino ,ptera) :
                        arcade.play_sound(self.die_sound)
                        self.game_over = True
                        self.ptera_time1 = time.time()
                        self.new_score = self.score
                        if self.new_score >= self.high_score :
                                self.high_score = self.score
                                arcade.set_background_color(arcade.color.WHITE)
                                #dino
                                self.dino = Dino()
                                self.die_sound = arcade.load_sound(':resources:sounds/gameover3.wav')
                                self.jumping_sound = arcade.load_sound(':resources:sounds/jump2.wav')
                                self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.dino , self.ground_list , gravity_constant=self.gravity)
                        #ptera
                                self.ptera_list = arcade.SpriteList()
                                self.ptera_time1 = time.time()
                        #cactus
                                self.cactus_list = arcade.SpriteList()
                                self.cactus_time1 = time.time()
                        #score
                                self.score = 0
                                self.high_score = self.score

                        #flag
                                self.flagDay = 0
                                self.flagNight = 0
                        

#cactus
        
        self.cactus_time2 = time.time()
        if self.cactus_time2 - self.cactus_time1 > 3 :
            new_cactus = Cactus(1300 , 1300)
            self.cactus_list.append(new_cactus)
            self.cactus_time1 = time.time()

        for cactus in self.cactus_list :
            cactus.move()
        for cactus in self.cactus_list:
                if  arcade.check_for_collision(self.dino ,cactus) :
                        arcade.play_sound(self.die_sound)
                        self.game_over = True
                        self.cactus_time1 = time.time()
                        self.new_score = self.score
                        if self.new_score >= self.high_score :
                                self.high_score = self.score
                                arcade.set_background_color(arcade.color.WHITE)
                                #dino
                                self.dino = Dino()
                                self.die_sound = arcade.load_sound(':resources:sounds/gameover3.wav')
                                self.jumping_sound = arcade.load_sound(':resources:sounds/jump2.wav')
                                self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.dino , self.ground_list , gravity_constant=self.gravity)
                        #ptera
                                self.ptera_list = arcade.SpriteList()
                                self.ptera_time1 = time.time()
                        #cactus
                                self.cactus_list = arcade.SpriteList()
                                self.cactus_time1 = time.time()
                        #score
                                self.score = 0
                                self.high_score = self.score

                        #flag
                                self.flagDay = 0
                                self.flagNight = 0
        
    #-------------------------------------------------------------------------------------------------------------------------------------#
    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            if self.my_physics_engine.can_jump():
                self.dino.change_y = 8
                arcade.play_sound(self.jumping_sound)
                
        if key == arcade.key.DOWN:
            self.dino.texture = arcade.load_texture('dinoimage/17.png')
            self.dino.change_x = 0.00001
        
        if key == arcade.key.SPACE:
            self.game_over = False
            if self.score > self.high_score:
                self.high_score = self.score
            self.dino.write_highscore()
            self.score = 0
            self.time = time.time() 

    #-------------------------------------------------------------------------------------------------------------------------------------#
    def on_key_release(self, key , modifiers):
        self.dino.change_x = 0 


#-------------------------------------------------------------------------------------------------------------------------------------#
game = Game()
arcade.run()
