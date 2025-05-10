from typing import Any
import pygame
import time
from objects.conf import PLAYER_SPRITES


pygame.init()
class Cardmaster(pygame.sprite.Sprite):
    def __init__(self ,x ,y ):
        pygame.sprite.Sprite.__init__(self)
        """Sprite related stuff"""
        self.size = (75,75)
        self.pictures = PLAYER_SPRITES
        self.image = self.pictures["normal"].convert_alpha()
        self.image = pygame.transform.scale(self.image,self.size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x ,y )
        
        """Movement related stuff"""
        self.x_vel = 0
        self.y_vel = 0
        self.jump = 0
        self.velocity = 5
        
        """Damage taken related stuff"""
        self.hp = 3
        self.hit_timer = 0
        self.hit_frame = 0

    def __str__(self) -> str:
        return f"Player(x,y):{self.rect.x} , {self.rect.y} vel_X: {self.x_vel} vel_Y:{self.y_vel}"
    
    def x(self):
        return self.rect.x
    
    def y(self):
        return self.rect.y
    
    def resize(self,scale_factor_x:float,scale_factor_y:float):
        """resize player.size,player.image,player.mask,player.velocity"""
        self.rect.x = self.rect.x * scale_factor_x
        self.rect.y = self.rect.y * scale_factor_y
        self.size = (self.size[0]*scale_factor_x,self.size[1]*scale_factor_y)
        self.image = pygame.transform.scale(self.image,self.size)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity *= (scale_factor_x + scale_factor_y)/2
        
    
    def movement_calculation_based_on_previous_speed(self,dx:float,dy:float,screen_width:int,screen_height:int):
        if self.rect.x+dx > screen_width*0.9875:
            self.rect.x = screen_width*0.9875
            
        elif self.rect.x+dx < screen_width*0.0125:
            self.rect.x = screen_width*0.0125 
        else:
            self.rect.x += dx
        if self.rect.y+dy > screen_height-self.rect.height/2:
           self.rect.y = screen_height-self.rect.height/2
        elif self.rect.y+dy < screen_height/2:
            self.rect.y = screen_height/2
        else:
            self.rect.y+=dy
    
        
    def Move(self,screen_width,screen_height):    
        self.velocity = screen_width*0.00325
        #Gravity
        if screen_height/2<self.rect.y+self.y_vel<screen_height-self.size[1]*2:
            self.y_vel+=0.00125*screen_height/2

        if -5 < self.rect.x + self.x_vel and self.rect.x + self.x_vel < screen_width-self.size[0]/2 and screen_height/2 < self.rect.y + self.y_vel and self.rect.y + self.y_vel < screen_height*(14/16):
            self.movement_calculation_based_on_previous_speed(self.x_vel,self.y_vel,screen_width,screen_height)
        
    
    def move_left(self):
        self.x_vel = -self.velocity
        
    def move_right(self):
        self.x_vel = self.velocity
        
    def move_up(self,screen_height):
        if self.jump==0 and self.rect.y<screen_height*15/16:
            self.y_vel= -2*self.velocity
        elif self.rect.y >= 7/8*screen_height:
            self.jump = 0
    
    def move_down(self):
        self.y_vel = self.velocity
    def movement_control(self,x,y):
        if y == 0:
            self.y_vel = 0
        if x == 0:
            self.x_vel = 0
    def HP(self):
        print(self.size)
        if time.time() - self.hit_timer <= 3:
            if self.hit_frame < 10:
                self.hit_frame+=1
                #vaja panna confi ja koik tuleb ara resizeida
                self.image =self.pictures["hit"].convert_alpha()
                self.image = pygame.transform.scale(self.image,self.size)
            else:
                self.hit_frame+=1
                self.image = self.pictures["hit_blue"].convert_alpha()
                self.image = pygame.transform.scale(self.image,self.size)
                if self.hit_frame==20:
                    self.hit_frame=0
        else:
            self.hit_frame=0
            self.image = self.pictures["normal"].convert_alpha()
            self.image = pygame.transform.scale(self.image,self.size)
        return self.hp
    
    def hit(self,damage)->None:
        """Starts hit timer that last for 3 seconds and reduces hp equal to damage"""
        if time.time()-self.hit_timer>=3:
            self.hit_timer = time.time()
            self.hp-=damage
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
          