import pygame
import random
import time
from pygame import mixer


pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

def run_game(win):
    screen_width = 600
    screen_height = 1000

    win = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Pixel Rocket')

    space_bg = pygame.image.load('Assets/space_bg.jpg')
    space_bg = pygame.transform.scale(space_bg, (screen_width, screen_height))

    space2_bg = pygame.image.load('Assets/space_bg.jpg')
    space2_bg = pygame.transform.scale(space_bg, (screen_width, screen_height))

    rocket_img = pygame.image.load('Assets/rocket_player.png')
    rocket_img = pygame.transform.scale(rocket_img, (45, 75))

    astroid_img = pygame.image.load('Assets/astroid.png')
    astroid_img = pygame.transform.scale(astroid_img, (60, 60))

    astroid2_img = pygame.image.load('Assets/astroid.png')
    astroid2_img = pygame.transform.scale(astroid2_img, (60, 60))

    astroid3_img = pygame.image.load('Assets/astroid.png')
    astroid3_img = pygame.transform.scale(astroid3_img, (60, 60))

    astroid4_img = pygame.image.load('Assets/astroid.png')
    astroid4_img = pygame.transform.scale(astroid4_img, (60, 60))

    astroid5_img = pygame.image.load('Assets/astroid.png')
    astroid5_img = pygame.transform.scale(astroid5_img, (60, 60))

    alien_img = pygame.image.load('Assets/ufo.png')
    alien_img = pygame.transform.scale(alien_img, (80, 80))

    lazer_img = pygame.image.load('Assets/lazer.png')
    lazer_img = pygame.transform.scale(lazer_img, (10, 20))

    shield_img = pygame.image.load('Assets/shield.png')
    shield_img = pygame.transform.scale(shield_img, (30, 30))

    diamond_img = pygame.image.load('Assets/diamond.png')
    diamond_img = pygame.transform.scale(diamond_img, (30, 30))

    home_button_img = pygame.image.load('Assets/home_button.png')
    home_button_img = pygame.transform.scale(home_button_img, (100, 100))

    retry_button_img = pygame.image.load('Assets/retry_button.png')
    retry_button_img = pygame.transform.scale(retry_button_img, (100, 100))

    line_img = pygame.image.load('Assets/white_line.png')
    line_img = pygame.transform.scale(line_img, (400, 10))


    # Load Sound
    songs = ['Music/game_lost_in_space.mp3',
             'Music/game_floating.mp3']

    pygame.mixer.music.load(random.choice(songs))
    pygame.mixer.music.set_volume(0.2)  # Justera volymen här
    pygame.mixer.music.play()

    collect_fx = pygame.mixer.Sound('Music/coin_sound.mp3')
    collect_fx.set_volume(0.5)

    button_sound = pygame.mixer.Sound('Music/fx_button.wav')
    button_sound.set_volume(0.5)

    # Initialize fade_counter for the sliding out effect
    fade_counter = screen_height  # Start with a full screen black overlay

    # Flag to keep track if the initial fade-out effect is done
    initial_fade_out_done = False

    # Game varibles
    diamond_count = 0
    is_dead = False
    score = 0
    BLACK = (0, 0, 0)
    WHITE = (0, 0, 0)
    start_ticks = 0  # Tiden då spelet startades
    
    # Spelar Variabler
    player_x = screen_width // 2 - 30
    player_y = screen_height // 2
    player_speed = 5
    is_jumping = False
    player_vel = 0
    gravity = 0.25 

    # Diamond Variables
    diamond_x = random.randint(0, screen_width)
    diamond_y = -40

    # Astroid Variabler
    max_speed = 8
    slowest_speed = 3
    astroid_spawn = -40

    diamond_speed = random.randint(slowest_speed, max_speed)

    astroid_x = random.randint(0, screen_width)
    astroid_y = -100
    astroid_speed = random.randint(slowest_speed, max_speed)
    astroid2_x = random.randint(0, screen_width)
    astroid2_y = -100
    astroid2_speed = random.randint(slowest_speed, max_speed)
    astroid3_x = random.randint(0, screen_width)
    astroid3_y = -100
    astroid3_speed = random.randint(slowest_speed, max_speed)
    astroid4_x = random.randint(0, screen_width)
    astroid4_y = -100
    astroid4_speed = random.randint(slowest_speed, max_speed)
    astroid5_x = random.randint(0, screen_width)
    astroid5_y = -100
    astroid5_speed = random.randint(slowest_speed, max_speed)


    # Alien Variabler
    alien_x = screen_width // 2 +10
    alien_state = 'follow'
    lazer_x = alien_x

    # background variabler
    background_y = 0
    background2_y = -999
    background_speed = 0.3

    # Så spelet körs FPS gånger i sekunden
    clock = pygame.time.Clock()
    FPS = 60

    font_path = 'Assets/unlearned/unlearne.ttf' # crackdown/crkdwno1.ttf
    font2_path = 'Assets/crackdown/crkdwno1.ttf'
    
    score_font_size = 43
    score_font = pygame.font.Font(None, score_font_size)

    title_size = 80
    font2 = pygame.font.Font(font_path, title_size)

    font_size = 60
    font = pygame.font.Font(font_path, font_size)
    start_ticks = pygame.time.get_ticks()  # Tidräknare för att uppdatera poängen

    game_active = False
    asteroids_active = False
    asteroid_delay = 2000

    is_mouse_clicked = False

    while True:
        is_mouse_clicked = False
        current_time = pygame.time.get_ticks() # få nuvarande tid
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                is_mouse_clicked = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not game_active:
                    start_ticks = current_time  # Återställer tidräknaren när spelet börjar

        # Initial black screen sliding out effect
        if not initial_fade_out_done:
            fade_speed = 15  # Justera detta för snabbare eller långsammare slide-out
            fade_counter -= fade_speed  # Minska räknaren för att slidea ut

            # Ritar ut de glidande svarta rektanglarna
            pygame.draw.rect(win, BLACK, (0, 0, screen_width, fade_counter // 2))
            pygame.draw.rect(win, BLACK, (0, screen_height - (fade_counter // 2), screen_width, fade_counter // 2))

            if fade_counter <= 0:
                initial_fade_out_done = True
                game_active = True  # Se till att detta endast händer en gång fade-out är komplett
                start_ticks = pygame.time.get_ticks()  # Återställ starttid för fördröjningsberäkningar

        if is_dead == False:
            # Koden för backgrunds scroll
            background_y += background_speed
            background2_y += background_speed
            if background_y > 1000:
                background_y = -1000
            if background2_y > 1000:
                background2_y = -1000

            win.blit(space_bg, (0, background_y))
            win.blit(space2_bg, (0, background2_y))

            win.blit(rocket_img, (player_x, player_y))
            score_text = font.render(str(score), True, (255, 255, 255))
            text_rect = score_text.get_rect(center=(screen_width / 2, 50))
            win.blit(score_text, text_rect)



        if game_active and not is_dead:

            seconds = (pygame.time.get_ticks() - start_ticks) // 500  # Konverterar millisekunder till sekunder
            score = seconds

            # spelar rörelsen aktiveras endast när spelet är aktivt
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                player_y -= player_speed
                is_jumping = True

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player_x -= player_speed

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player_x += player_speed


            if is_jumping:
                player_vel = -5  # Ge spelaren en uppåtrörelse
                is_jumping = False

            player_vel += gravity
            player_y += player_vel  

            # Kontroll av spelarens position för att inte gå utanför skärmen
            if player_x <= -50:
                player_x = screen_width
            elif player_x >= screen_width: 
                player_x = -50

            # Koden för att röra asteroiderna och alien visas bara när spelet är aktivt
            if not asteroids_active and (current_time - start_ticks) > asteroid_delay:
                asteroids_active = True  # Aktivera asteroiderna

            if asteroids_active:
                diamond_y += diamond_speed
                astroid_y += astroid_speed

                if diamond_y > screen_height:
                    diamond_x = random.randint(0, screen_width)
                    diamond_y = astroid_spawn

                if astroid_y > screen_height:
                    astroid_x = random.randint(0, screen_width)
                    astroid_y = astroid_spawn
                    astroid_speed = random.randint(slowest_speed, max_speed)

                astroid2_y += astroid2_speed
                if astroid2_y > screen_height:
                    astroid2_x = random.randint(0, screen_width)
                    astroid2_y = astroid_spawn
                    astroid2_speed = random.randint(slowest_speed, max_speed)

                astroid3_y += astroid3_speed
                if astroid3_y > screen_height:
                    astroid3_x = random.randint(0, screen_width)
                    astroid3_y = astroid_spawn
                    astroid3_speed = random.randint(slowest_speed, max_speed)

                astroid4_y += astroid4_speed
                if astroid4_y > screen_height:
                    astroid4_x = random.randint(0, screen_width)
                    astroid4_y = astroid_spawn
                    astroid4_speed = random.randint(slowest_speed, max_speed)

                astroid5_y += astroid5_speed
                if astroid5_y > screen_height:
                    astroid5_x = random.randint(0, screen_width)
                    astroid5_y = astroid_spawn
                    astroid5_speed = random.randint(slowest_speed, max_speed)

                if alien_state == 'follow':
                    alien_x = player_x - 60

                # Uppdatera spelarens Rect för kollision
                player_rect = rocket_img.get_rect(center=(player_x, player_y)).inflate(-20, -20)

                # Diamanternas hitbox
                diamond_rect = diamond_img.get_rect(center=(diamond_x, diamond_y)).inflate(-5, -5)

                # Uppdatera Rects för asteroiderna
                astroid_rect = astroid_img.get_rect(center=(astroid_x, astroid_y)).inflate(-20, -20)
                astroid2_rect = astroid2_img.get_rect(center=(astroid2_x, astroid2_y)).inflate(-20, -20)
                astroid3_rect = astroid3_img.get_rect(center=(astroid3_x, astroid3_y)).inflate(-20, -20)
                astroid4_rect = astroid4_img.get_rect(center=(astroid4_x, astroid4_y)).inflate(-20, -20)
                astroid5_rect = astroid5_img.get_rect(center=(astroid5_x, astroid5_y)).inflate(-20, -20)

                # Kolla kollisioner
                if (player_rect.colliderect(astroid_rect) or player_rect.colliderect(astroid2_rect) or 
                    player_rect.colliderect(astroid3_rect) or player_rect.colliderect(astroid4_rect) or 
                    player_rect.colliderect(astroid5_rect)):
                    is_dead = True

                if (player_rect.colliderect(diamond_rect)):
                    diamond_count += 1  # Anta att du håller reda på antalet samlade diamanter
                    print(f"Diamonds collected: {diamond_count}")
                    collect_fx.play()
                    diamond_x = random.randint(0, screen_width - diamond_img.get_width())
                    diamond_y = random.randint(-100, -50)  # Starta diamanten lite utanför skärmen

                if player_y > 960 or player_y < 150:
                    is_dead = True
                    

            if player_y > 960:
                is_dead = True

            if player_y < 150:
                is_dead = True
                  
            # Gör så spelet går snabare och snabare
            if score == 100:
                max_speed = 12
                slowest_speed = 7
            if score == 200:
                max_speed = 15
                slowest_speed = 10
            if score == 300:
                max_speed = 17
                slowest_speed = 12
            if score == 400:
                max_speed = 24
                slowest_speed = 17
            if score == 500:
                max_speed = 28
                slowest_speed = 24
            if score == 700:
                max_speed = 50
                slowest_speed = 40 

            win.blit(diamond_img, (diamond_x, diamond_y))
            win.blit(astroid_img, (astroid_x, astroid_y))
            win.blit(astroid2_img, (astroid2_x, astroid2_y))
            win.blit(astroid3_img, (astroid3_x, astroid3_y))
            win.blit(astroid4_img, (astroid4_x, astroid4_y))
            win.blit(astroid5_img, (astroid5_x, astroid5_y))
            win.blit(alien_img, (alien_x, -200))
            win.blit(lazer_img, (lazer_x, -100))

        else:
            if is_dead:
                # Ladda och rendera "Leader Board" texten här istället
                title = font.render('Leader Board', True, (255, 255, 255))  # Vit text mot svart bakgrund

                output = score_font.render(f'score: {score}', True, (255, 255, 255))  # Vit text mot svart bakgrund
                
                pygame.mixer.music.fadeout(1000)
                fade_speed = 10
                fade_counter += fade_speed

                # Ritar en svart rektangel som glider in från toppen
                pygame.draw.rect(win, BLACK, (0, 0, screen_width, fade_counter))

                # Ritar en svart rektangel som glider in från botten
                pygame.draw.rect(win, BLACK, (0, screen_height - fade_counter, screen_width, fade_counter))
                

                if fade_counter >= screen_height // 2:
                    game_active = False

                if game_active == False:
                    win.blit(home_button_img, (180, 800))
                    win.blit(retry_button_img, (320, 800))
                    win.blit(title, (125, 50))  # Visa "Leader Board" texten här
                    win.blit(output, (120, 550))
                    win.blit(line_img, (110, 500))

                if is_mouse_clicked:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                     
                 
        pygame.display.flip()  # Uppdaterar hela skärmen

        clock.tick(FPS)

if __name__ == "__main__":
    screen_width = 600
    screen_height = 1000
    win = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Pixel Rocket #Game')
    run_game(win)
