import pygame
from objects.witch import Witch
from objects.card import Card
from objects.conf import CHARGE_ATTACK_COORDINATES,MAGE_POSITION_EVEN,MAGE_POSITION_ODD
import time
pygame.init()

def spawn_enemies(round:int = 1 , env_object : object = None)->None:
    """Adds new rounds enemies to the enemy list inside env_object class based on the round uses scales instead of raw coordinates"""
    if round == 1:
        for i in  CHARGE_ATTACK_COORDINATES:
            bitch = Witch(i[0]*env_object.screen_width,i[1]*env_object.screen_height,"teeth",env_object)
            
            env_object.add_witch(bitch) 

    elif round == 2:
        for i in MAGE_POSITION_EVEN:
            bitch = Witch(i[0]*env_object.screen_width,i[1]*env_object.screen_height,"blue",env_object)
            
            env_object.add_witch(bitch) 
        for j in CHARGE_ATTACK_COORDINATES:
            bitch = Witch(j[0]*env_object.screen_width,j[1]*env_object.screen_height,"green",env_object)
            
            env_object.add_witch(bitch) 

    elif round == 3:
        [env_object.add_witch(Witch(i[0]*env_object.screen_width,i[1]*env_object.screen_height,"red",env_object)) for i in  MAGE_POSITION_EVEN]
        [env_object.add_witch(Witch(j[0]*env_object.screen_width, j[1]*env_object.screen_height ,"blue",env_object)) for j in  MAGE_POSITION_ODD]
        [env_object.add_witch(Witch(k[0]*env_object.screen_width,k[1]*env_object.screen_height,"green",env_object)) for k in  CHARGE_ATTACK_COORDINATES]
    
def move(player:object,env_object:object)->None:
    
        keys = pygame.key.get_pressed()  # Checking pressed 
        player.x_vel=0
        player.y_vel=0
        #movement check
        if keys[pygame.K_d]:
            player.move_right()
        if keys[pygame.K_a]: 
            player.move_left()    
        if keys[pygame.K_s]: 
            player.move_down()
        if keys[pygame.K_w]:
            player.move_up(env_object.screen_height)
        
        #shooting check
        if keys[pygame.K_UP] and time.time()-env_object.fire_rate>=0.5:
            env_object.fire_rate=time.time()
            env_object.add_card(Card(player.x()+ 3/4*player.size[0],player.y()))
