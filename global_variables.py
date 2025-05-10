import pygame
import time
from objects.conf import SCREEN_HEIGHT,SCREEN_WIDTH
from objects.Player import Cardmaster

class Global:
    def __init__(self,screen_width = SCREEN_WIDTH ,screen_height = SCREEN_HEIGHT) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.witches = pygame.sprite.Group()
        self.dead_witches = pygame.sprite.Group()
        self.cards = pygame.sprite.Group()
        self.spells = pygame.sprite.Group()
        self.enemy_sizes = {"1920x1080":(96.42857142857143, 101.25),"1600x900":(75,75),"1366x768":(64.03125, 64.0)}
        self.current_window_size = "1366x768"
        self.player = None
        self.scale_x = 1
        self.scale_y = 1
        self.fire_rate = 0
    
    def reset(self):
        self.witches = pygame.sprite.Group()
        self.dead_witches = pygame.sprite.Group()
        self.cards = pygame.sprite.Group()
        self.spells = pygame.sprite.Group()
        self.add_player()
        self.scale_x = 1
        self.scale_y = 1
        self.fire_rate = 0
        
    
    def screen_width(self):
        return self.screen_width
    
    def screen_height(self):
        return self.screen_height
    
    def set_screen_dimensions(self,scale_x:float,scale_y:float) -> None: 
        """function to set new screen dimensions"""
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.screen_width = self.scale_x * SCREEN_WIDTH
        self.screen_height = self.scale_y * SCREEN_HEIGHT

    def add_witch(self,witch:object)->None:
        """function to add witches to the class group witches"""
        self.witches.add(witch)
    
    def add_dead_witch(self,dead_witch:object)->None:
        """function to add dead witch to the dead witch class group"""
        self.dead_witches.add(dead_witch)
    
    def add_card(self,card:object)->None:
        """function to add player protjectiles to the protjectile class group"""
        self.cards.add(card)

    def add_spell(self,spell:object)->None:
        """function to add enemy protjectiles to the enemy protjectile class group"""
        self.spells.add(spell)
    
    def add_player(self)->None:
        """function to initisilize player object"""
        self.player = Cardmaster(self.screen_width/2,self.screen_height/2)
    
    def set_fire_rate(self,new_fire_rate:int)->None:
        """function to record last time player fired a protjectile"""
        self.fire_rate = new_fire_rate