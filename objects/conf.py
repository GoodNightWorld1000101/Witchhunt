import pyautogui
import pygame
from objects.button import BUTTON
pygame.init()

#Screen resolutsions
#start resolution
SCREEN_WIDTH, SCREEN_HEIGHT = 1540, 800

#numbers
NUMBERS = {0:pygame.image.load("objects/Pixel_art/numbers/zero.png"),1:pygame.image.load("objects/Pixel_art/numbers/one.png"),2:pygame.image.load("objects/Pixel_art/numbers/two.png"),3:pygame.image.load("objects/Pixel_art/numbers/three.png"),4:pygame.image.load("objects/Pixel_art/numbers/four.png"),5:pygame.image.load("objects/Pixel_art/numbers/five.png"),6:pygame.image.load("objects/Pixel_art/numbers/six.png"),7:pygame.image.load("objects/Pixel_art/numbers/seven.png"),8:pygame.image.load("objects/Pixel_art/numbers/eight.png"),9:pygame.image.load("objects/Pixel_art/numbers/nine.png")}
#buttons
pic_start_basic = pygame.image.load("objects/Pixel_art/buttons/start.png")
pic_settings_basic = pygame.image.load("objects/Pixel_art/buttons/settings.png")
pic_main_menu_basic = pygame.image.load("objects/Pixel_art/buttons/main_menu.png")
pic_quit_basic = pygame.image.load("objects/Pixel_art/buttons/quit.png")

pic_1920x1080_basic = pygame.image.load("objects/Pixel_art/buttons/1920x1080.png")
pic_1600x900_basic = pygame.image.load("objects/Pixel_art/buttons/1600x900.png")
pic_1366x768_basic = pygame.image.load("objects/Pixel_art/buttons/1366x768.png")

pic_start_hit = pygame.image.load("objects/Pixel_art/buttons/hover_start.png")
pic_settings_hit = pygame.image.load("objects/Pixel_art/buttons/hover_settings.png")
pic_main_menu_hit = pygame.image.load("objects/Pixel_art/buttons/hover_main_menu.png")
pic_quit_hit = pygame.image.load("objects/Pixel_art/buttons/hover_quit.png")

pic_1920x1080_hit = pygame.image.load("objects/Pixel_art/buttons/1920x1080_hit.png")
pic_1600x900_hit = pygame.image.load("objects/Pixel_art/buttons/1600x900_hit.png")
pic_1366x768_hit = pygame.image.load("objects/Pixel_art/buttons/1366x768_hit.png")

BUTTONS = {"start":BUTTON(pic_start_basic,pic_start_hit,0.3),
           "settings":BUTTON(pic_settings_basic,pic_settings_hit,0.5),
           "quit":BUTTON(pic_quit_basic,pic_quit_hit,0.7),
           "main menu":BUTTON(pic_main_menu_basic,pic_main_menu_hit,0.7),
           "1920x1080":BUTTON(pic_1920x1080_basic,pic_1920x1080_hit,0.3),
           "1600x900":BUTTON(pic_1600x900_basic,pic_1600x900_hit,0.5),
           "1366x768":BUTTON(pic_1366x768_basic,pic_1366x768_hit,0.7)}

#player
PLAYER_VEL = int(5)
pic_1 = pygame.image.load("objects/Pixel_art/Player_sprites/card_master_pink.png")
pic_2 = pygame.image.load("objects/Pixel_art/Player_sprites/card_player_hit.png")
pic_3 = pygame.image.load("objects/Pixel_art/Player_sprites/card_master.png")
PLAYER_SPRITES = {"normal":pic_1,"hit":pic_2,"hit_blue":pic_3}

#player attack
GOLD_CARD = pygame.image.load("objects/Pixel_art/Prayer_cards/card_yellow.png")
CARD = pygame.image.load("objects/Pixel_art/Prayer_cards/card.png")

#health
FULL_HEART = pygame.image.load("objects/Pixel_art/Heart_art/full_heart.png")
HALF_HEART = pygame.image.load("objects/Pixel_art/Heart_art/half_heart_left.png")
EMPTY_HEART = pygame.image.load("objects/Pixel_art/Heart_art/empty_heart.png")

#possible death animations
BANISHMENT_RITUAL_CIRCLE = pygame.image.load("objects/Pixel_art/Witch_sprites/orange_penta.png")
BANISHMENT = pygame.image.load("objects/Pixel_art/Player_sprites/card_master_dark.png")

BACKGROUND = pygame.image.load("objects/Pixel_art/Background/Devil_eyes.png")

#enemy
prayer_pic = pygame.image.load("objects/Pixel_art/Witch_sprites/cross.png")
ENEMY_SPRITES = {"green":pygame.image.load("objects/Pixel_art/Witch_sprites/Bull_mage.png"),
               "red":pygame.image.load("objects/Pixel_art/Witch_sprites/mage.png"),
               "blue":pygame.image.load("objects/Pixel_art/Witch_sprites/High_mage.png"),
               "teeth":pygame.image.load("objects/Pixel_art/Witch_sprites/teeth.png"),
               "enemy_hit":pygame.image.load("objects/Pixel_art/Witch_sprites/enemy_hit.png"),
               "bull_hit":pygame.image.load("objects/Pixel_art/Witch_sprites/bull_hit.png"),"dead":pygame.image.load("objects/Pixel_art/Witch_sprites/red_x.png")}

#SPAWN POINTS
#Teeth and Bull monster attack spawn coordinates
CHARGE_ATTACK_COORDINATES = [(0.1299, 0.25), (0.1299, 0.375), (0.2597, 0.25), (0.2597, 0.375), 
                             (0.3896, 0.25), (0.3896, 0.375), (0.5195, 0.25), (0.5195, 0.375), 
                             (0.6494, 0.25), (0.6494, 0.375), (0.7792, 0.25), (0.7792, 0.375)]

#Mage and High mage spawn coordinates
MAGE_POSITION_EVEN = [(0.0, 0.0125), (0.0649, 0.0125), (0.1299, 0.0125), (0.1948, 0.0125),
                    (0.2597, 0.0125), (0.3247, 0.0125), (0.3896, 0.0125), (0.4545, 0.0125),
                    (0.5195, 0.0125), (0.5844, 0.0125), (0.6494, 0.0125), (0.7143, 0.0125),
                    (0.7792, 0.0125), (0.8442, 0.0125), (0.9091, 0.0125)] 

MAGE_POSITION_ODD = [(0.0325, 0.125), (0.0974, 0.125), (0.1623, 0.125), (0.2273, 0.125),
                    (0.2922, 0.125), (0.3571, 0.125), (0.4221, 0.125), (0.487, 0.125),
                    (0.5519, 0.125), (0.6169, 0.125), (0.6818, 0.125), (0.7468, 0.125), 
                    (0.8117, 0.125), (0.8766, 0.125)]
