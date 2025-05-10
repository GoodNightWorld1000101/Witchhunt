import pygame
from objects.witch import Witch
from objects.card import Card


pygame.init()

def hitboks(env_object:object):
    """function to check players hits from enemy protejctiles/attack and enemy hits from player protejctiles"""
    if pygame.sprite.spritecollide(env_object.player,env_object.spells,False):
        if pygame.sprite.spritecollide(env_object.player, env_object.spells, True, pygame.sprite.collide_mask):
            env_object.player.hit(0.5)
    if pygame.sprite.spritecollide(env_object.player,env_object.witches,False):
            env_object.player.hit(1)

    for i in env_object.witches:

        if pygame.sprite.spritecollide(i, env_object.cards, False):
            if pygame.sprite.spritecollide(i, env_object.cards, True, pygame.sprite.collide_mask):
                i.hit(env_object)
                    
                
                