from typing import Any
import pygame
import time
from objects.conf import ENEMY_SPRITES
pygame.init()

class Witch(pygame.sprite.Sprite):
    def __init__(self ,x ,y ,who,gs):
        pygame.sprite.Sprite.__init__(self)
        self.who = who 
        self.size = gs.enemy_sizes[gs.current_window_size]
        self.enemy(x,y) 
        self.suund = 0
        self.move_timer = time.time()
        self.hit_timer = 0
        self.death_image = pygame.transform.scale(ENEMY_SPRITES["dead"],self.size)
        self.animation_counter = 0
        
        
    def __str__(self) -> str:
        return f"Who:{self.who},HP:{self.hp},(x,y):({self.rect.x},{self.rect.y})"
    
    def enemy(self,x,y):
        if self.who == "green":
            self.image = ENEMY_SPRITES["green"].convert_alpha()
            self.hit_image = ENEMY_SPRITES["bull_hit"].convert_alpha()
            self.image = pygame.transform.scale(self.image,self.size)
            self.hit_image = pygame.transform.scale(self.hit_image,self.size)
            self.rect = self.image.get_rect(topleft = (x,y))
            self.mask = pygame.mask.from_surface(self.image)
            self.hp = 2
            self.points = 30

        elif self.who == "red":
            self.image = ENEMY_SPRITES["red"].convert_alpha()
            self.hit_image = ENEMY_SPRITES["enemy_hit"].convert_alpha()
            self.image = pygame.transform.scale(self.image,self.size)
            self.hit_image = pygame.transform.scale(self.hit_image,self.size)
            self.rect = self.image.get_rect(topleft = (x,y))
            self.mask = pygame.mask.from_surface(self.image)
            self.hp = 2
            self.points = 20
           
        elif self.who == "blue":
            self.image = ENEMY_SPRITES["blue"].convert_alpha()
            self.hit_image = ENEMY_SPRITES["enemy_hit"].convert_alpha()
            self.image = pygame.transform.scale(self.image,self.size)
            self.hit_image = pygame.transform.scale(self.hit_image,self.size)
            self.rect = self.image.get_rect(topleft = (x,y))
            self.mask = pygame.mask.from_surface(self.image)
            self.hp = 4
            self.points = 40
           
        elif self.who == "teeth":
            self.image = ENEMY_SPRITES["teeth"].convert_alpha()
            self.hit_image = ENEMY_SPRITES["bull_hit"].convert_alpha()
            self.image = pygame.transform.scale(self.image,self.size)
            self.hit_hit_image = pygame.transform.scale(self.hit_image,self.size)
            self.rect = self.image.get_rect(topleft = (x,y))
            self.mask = pygame.mask.from_surface(self.image)
            self.hp = 1 
            self.points = 10
             
    def resize(self,scale_factor_x:float,scale_factor_y:float):
        self.hit_image = pygame.transform.scale(self.hit_image,(self.size[0]*scale_factor_x,self.size[1]*scale_factor_y))
        self.death_image = pygame.transform.scale(self.death_image,(self.size[0]*scale_factor_x,self.size[1]*scale_factor_y)) 
        self.image = pygame.transform.scale(self.image,(self.size[0]*scale_factor_x,self.size[1]*scale_factor_y))
        self.mask = pygame.mask.from_surface(self.image)
        self.size = (self.size[0]*scale_factor_x,self.size[1]*scale_factor_y)
        if self.rect != None:
            self.rect.x = self.rect.x * scale_factor_x
            self.rect.y = self.rect.y * scale_factor_y

    def xandy(self):
        return (self.rect.x,self.rect.y)
    
    def red_move(self,info_struct:object):  
        if time.time()-self.move_timer>=0.75 and self.suund<1:
            self.move_timer=time.time()
            if self.rect.x+(5/1540*info_struct.screen_width) < (1540-55)/1540 * info_struct.screen_width:    
                self.rect.move_ip(30/1540 * info_struct.screen_width,0)
            else:
                self.rect.move_ip(0,150/1540*info_struct.screen_height)
                self.suund = 2
            
        elif time.time()-self.move_timer>=0.75 and self.suund>1:
            self.move_timer=time.time()
            if self.rect.x-5/1540*info_struct.screen_width>0:    
                self.rect.move_ip(-30/1540*info_struct.screen_width,0)   
            else:
                self.rect.move_ip(0,150/1540*info_struct.screen_height)
                self.suund = 0 
            
    def blue_move(self,info_struct):
        if time.time()-self.move_timer>=0.75 and self.suund<1:
            self.move_timer=time.time()
            if self.rect.x+(5/1540*info_struct.screen_width) < (1540-55)/1540 * info_struct.screen_width:    
                self.rect.move_ip(30/1540 * info_struct.screen_width,0)
            else:
                self.rect.move_ip(0,150/1540*info_struct.screen_height)
                self.suund = 2
            
        elif time.time()-self.move_timer>=0.75 and self.suund>1:
            self.move_timer=time.time()
            if self.rect.x-5/1540*info_struct.screen_width>0:    
                self.rect.move_ip(-30/1540*info_struct.screen_width,0)   
            else:
                self.rect.move_ip(0,150/1540*info_struct.screen_height)
                self.suund = 0 

    def hambad_move(self,info_struct):
        if time.time()-self.move_timer>=0.1:
            if self.rect.y > info_struct.screen_height:
                self.rect.y = 0
                self.rect.x += 50/1540*info_struct.screen_width
            if self.rect.x > info_struct.screen_width:
                self.rect.x = 0
            self.move_timer=time.time()
            self.rect.move_ip(0,4/800*info_struct.screen_height)
               
    def green_move(self,info_struct):
        if time.time()-self.move_timer>=0.6 and self.suund<6:
            self.move_timer=time.time()
            self.rect.move_ip(0,100/1540*info_struct.screen_height)
            self.suund = self.suund+1
            
        elif time.time()-self.move_timer>=0.6 and 12>self.suund>=6:
            self.move_timer=time.time()
            if self.rect.x+50/1540*info_struct.screen_width<1490/1540*info_struct.screen_width:
                self.rect.move_ip(30/1540*info_struct.screen_width,0)
            self.suund+=1 
        elif time.time()-self.move_timer>=0.6 and 18>self.suund>=12:
            self.move_timer=time.time()
            self.rect.move_ip(0,-100/1540*info_struct.screen_height)    
            self.suund+=1 
        elif time.time()-self.move_timer>=0.6 and 24>self.suund>=18:
            self.move_timer=time.time()
            if self.rect.x-30>0:    
                self.rect.move_ip(-30/1540*info_struct.screen_width,0)    
            self.suund+=1 
        elif self.suund == 24:
            self.suund = 0
               
    def update(self,info_struct:object):
        if self.hp == -1 and time.time()-self.hit_timer<3:
            pass
        elif time.time()-self.hit_timer < 3:
            if self.animation_counter % 10 == 0:
                self.rect.move_ip(20/1540*info_struct.screen_width,0)
            elif self.animation_counter % 10 == 1:
                self.rect.move_ip(-20/1540*info_struct.screen_width,0)
        else:
            if self.who == "green":        
                self.green_move(info_struct)
            elif self.who == "red":
                self.red_move(info_struct)
            elif self.who == "blue":
                self.blue_move(info_struct)
            elif self.who == "teeth":
                self.hambad_move(info_struct)
        
    def draw(self,screen:object):
        if self.hp == -1 and time.time()-self.hit_timer<1:
            self.animation_counter+=1
            if self.animation_counter % 2 != 0:
                screen.blit(self.image,(self.rect.x,self.rect.y))
            else:
                screen.blit(self.hit_image,(self.rect.x,self.rect.y))
            screen.blit(self.death_image,(self.rect.x,self.rect.y))
        
        elif time.time()-self.hit_timer < 3 and self.hp != -1:
            self.animation_counter+=1
            if self.animation_counter % 3 == 0:
                screen.blit(self.image,(self.rect.x,self.rect.y))
            elif self.animation_counter % 3 > 0:
                screen.blit(self.hit_image,(self.rect.x,self.rect.y))
        else:   
            self.animation_counter = 0
            if self.hp != -1:
                screen.blit(self.image,(self.rect.x,self.rect.y))
            else:
                self.hp = -100
                         
    def hit(self,info_struct:object):
        if time.time()-self.hit_timer>0.5:
            if self.rect.y>self.size[0]/2:
                self.rect.move_ip(0,-10/800*info_struct.screen_height)
            else:
                self.rect.y = 0
        if self.hp == 0:
            self.hit_timer = time.time()
            self.hp = -1 
        elif self.hp != -1:
            self.hit_timer = time.time()
            self.hp -= 1
        return self.hp
              
