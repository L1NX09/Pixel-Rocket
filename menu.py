import pygame
import sys
from rocket import run_game
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

# Game Varibles
#diamond_count = 0

# Skärmkonfiguration
screen_width = 600
screen_height = 1000

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pixel Rocket #Main menu')

# Ladda bilder
start_button_image = pygame.image.load('Assets/start_button.png')
settings_button_image = pygame.image.load('Assets/setings_button.png')
skins_button_img = pygame.image.load('Assets/skins_button.png')
bg_img = pygame.image.load('Assets/space_bg.jpg')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
bg2_img = pygame.image.load('Assets/space_bg.jpg')
bg2_img = pygame.transform.scale(bg2_img, (screen_width, screen_height))
rocket_menu = pygame.image.load('Assets/rocket_player.png')
rocket_menu = pygame.transform.scale(rocket_menu, (100, 200))

# Ladda ljud
pygame.mixer.music.load('Music/menu_song.mp3')
pygame.mixer.music.set_volume(0.3)

play_fx = pygame.mixer.Sound('Music/fx_button.wav')
play_fx.set_volume(0.5)

# Skala knappbilder för hover-effekt
start_button_image_small = pygame.transform.scale(start_button_image, (130, 60))
start_button_image_large = pygame.transform.scale(start_button_image, (150, 80))
settings_button_image_small = pygame.transform.scale(settings_button_image, (150, 60))
settings_button_image_large = pygame.transform.scale(settings_button_image, (170, 80))
skins_button_image_small = pygame.transform.scale(skins_button_img, (150, 60))
skins_button_image_large = pygame.transform.scale(skins_button_img, (170, 80))

# Initial knappstorlek och position
start_button = start_button_image_small.get_rect(center=(screen_width // 2, screen_height // 2 +200))
settings_button = settings_button_image_small.get_rect(center=(screen_width // 2 -90, screen_height // 2 +280))
skins_button = settings_button_image_small.get_rect(center=(screen_width // 2 +90, screen_height // 2 +280))

# För scrolande backgrund
bg_y = 0
bg2_y = -1000
bg_speed = 0.3

# Ladda och förbereda titelfont
title_font = pygame.font.Font('Assets/stay-pixel-font/StayPixelRegular-EaOxl.ttf', 80)  # Ange storlek på din font här

def fade_in(win, speed=30):
    fade_surface = pygame.Surface((screen_width, screen_height))
    fade_surface.fill((0,0,0))
    for alpha in range(0, 255, speed):
        fade_surface.set_alpha(alpha)
        win.blit(fade_surface, (0,0))
        pygame.display.update()
        pygame.time.delay(50)

def draw_title():
    title_surface = title_font.render('Pixel Rocket', True, (255, 255, 255))  # Vit färg
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 7))
    win.blit(title_surface, title_rect)

def draw_buttons(mouse_pos):
    # Ritar Start-knappen och ändrar storlek vid hover
    if start_button.collidepoint(mouse_pos):
        win.blit(start_button_image_large, start_button_image_large.get_rect(center=start_button.center))
    else:
        win.blit(start_button_image_small, start_button)

    # Ritar Settings-knappen och ändrar storlek vid hover
    if settings_button.collidepoint(mouse_pos):
        win.blit(settings_button_image_large, settings_button_image_large.get_rect(center=settings_button.center))
    else:
        win.blit(settings_button_image_small, settings_button)

    if skins_button.collidepoint(mouse_pos):
        win.blit(skins_button_image_large, skins_button_image_large.get_rect(center=skins_button.center))
    else:
        win.blit(skins_button_image_small, skins_button)

def main_menu():
    global bg_y, bg2_y
    pygame.mixer.music.play()
    running = True
    while running:
        win.blit(bg_img, (0, bg_y))
        win.blit(bg2_img, (0, bg2_y))
        win.blit(rocket_menu, (screen_width // 2 - 50, screen_height // 2.5))
        mouse_pos = pygame.mouse.get_pos()
        draw_title()
        draw_buttons(mouse_pos)

        clock = pygame.time.Clock()

        bg_y += bg_speed
        bg2_y += bg_speed

        if bg_y > screen_height:
            bg_y = -1000
        
        if bg2_y > screen_height:
            bg2_y = -1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(mouse_pos):
                    play_fx.play()
                    fade_in(win, speed=30) 

                    pygame.mixer.music.fadeout(500)
                    run_game(win)

                elif settings_button.collidepoint(mouse_pos):
                    play_fx.play()
                    print("Open Settings")

                elif skins_button.collidepoint(mouse_pos):
                    play_fx.play()
                    print("Open Skins")

        pygame.display.flip()

        clock.tick(60)

main_menu()
