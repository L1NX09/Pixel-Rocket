import pygame
import random
import time
from pygame import mixer

def end_menu(font, win, score_font, score, BLACK, screen_height, screen_width, home_button_img, retry_button_img, line_img, is_mouse_clicked, fade_counter):

    play_fx = pygame.mixer.Sound('Music/fx_button.wav')
    play_fx.set_volume(0.5)

    mouse_pos = pygame.mouse.get_pos()

    # Ladda och rendera "Leader Board" texten här istället
    title = font.render('Leader Board', True, (255, 255, 255))  # Vit text mot svart bakgrund

    output = score_font.render(f'score: {score}', True, (255, 255, 255))  # Vit text mot svart bakgrund
    
    pygame.mixer.music.fadeout(1000)
    
    game_active = False

    # Ritar en svart rektangel som glider in från toppen
    pygame.draw.rect(win, BLACK, (0, 0, screen_width, fade_counter))

    # Ritar en svart rektangel som glider in från botten
    pygame.draw.rect(win, BLACK, (0, screen_height - fade_counter, screen_width, fade_counter))

    # Skala knappbilder för hover-effekt
    home_button_image_small = pygame.transform.scale(home_button_img, (100, 100))
    home_button_image_large = pygame.transform.scale(home_button_img, (120, 120))
    retry_button_image_small = pygame.transform.scale(retry_button_img, (100, 100))
    retry_button_image_large = pygame.transform.scale(retry_button_img, (120, 120))

    # Initial knappstorlek och position
    home_button_small_rect = home_button_image_small.get_rect(center=(screen_width // 2, 800))
    retry_button_small_rect = retry_button_image_small.get_rect(center=(screen_width // 2 + 70, 800))

    # Beräkna den nya positionen för större knappar så att de är centrerade
    home_button_large_rect = home_button_image_large.get_rect(center=home_button_small_rect.center)
    retry_button_large_rect = retry_button_image_large.get_rect(center=retry_button_small_rect.center)

    if fade_counter >= screen_height // 2:
        win.blit(title, (125, 50))  # Visa "Leader Board" texten här
        win.blit(output, (120, 550))
        win.blit(line_img, (110, 500))

        if is_mouse_clicked:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

        def draw_buttons(mouse_pos):
            # Ritar Start-knappen och ändrar storlek vid hover
            if home_button_small_rect.collidepoint(mouse_pos):
                win.blit(home_button_image_large, home_button_large_rect)
            else:
                win.blit(home_button_image_small, home_button_small_rect)

            # Ritar Settings-knappen och ändrar storlek vid hover
           # if retry_button_small_rect.collidepoint(mouse_pos):
              #  win.blit(retry_button_image_large, retry_button_large_rect)
          #  else:
                #win.blit(retry_button_image_small, retry_button_small_rect)

        draw_buttons(mouse_pos)

        if is_mouse_clicked:
            if home_button_small_rect.collidepoint(mouse_pos):
                print("Home")
                play_fx.play()
                return 'home'

          #  elif retry_button_small_rect.collidepoint(mouse_pos):
              #  print("retry")
               # play_fx.play()
                #return 'retry'
        
    return None