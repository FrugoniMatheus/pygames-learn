import pygame

pygame.init()

hit = pygame.mixer.Sound("assets/pong.wav")

start = pygame.mixer.Sound("assets/start.wav")

music_game = pygame.mixer.Sound("assets/music.ogg")

pygame.font.init()

font = pygame.font.Font(None, 50)

display = pygame.display.set_mode((1280, 720))

menu_img = pygame.image.load("assets/menu.png").convert_alpha()
menu = menu_img.get_rect()


gameOver_img = pygame.image.load("assets/go.png").convert_alpha()
gameOver = gameOver_img.get_rect()

fade_img = pygame.Surface((1280,720)).convert_alpha() 
#Imagem transparente
fade = fade_img.get_rect()
fade_img.fill("black")
fade_alpha = 255


player1_img = pygame.image.load("assets/player1.png").convert_alpha()
# player1 = pygame.Rect(0,0,30,150)
player1 = player1_img.get_rect()
player1_score = 0
player1_speed = 6

player2_img = pygame.image.load("assets/player2.png").convert_alpha()
# player2 = pygame.Rect(1250,0,30,150)
player2 = player2_img.get_rect(right=1280)
player2_score = 0

ball_img = pygame.image.load("assets/ball.png").convert_alpha()
ball = ball_img.get_rect(center=(1280/2, 720/2))
# ball = pygame.Rect(600,350,15,15)
ball_dir_x = 6
ball_dir_y = 6


campo_img = pygame.image.load("assets/bg.png")
campo = campo_img.get_rect()

placar_player1 = font.render(str(player1_score), True, "white")

placar_player2 = font.render(str(player2_score), True, "white")

fps = pygame.time.Clock()

music_game.play(-1)
cena = 1
loop = True
while loop:

    match cena:
        case 1:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            loop = False  
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                 cena = 2
                                 start.play()
                                 fade_alpha = 255 
                            if event.key == pygame.K_q:
                                 loop = False

            if fade_alpha >= 0:
                fade_alpha -= 8
                fade_img.set_alpha(fade_alpha)

            display.fill((0,0,0))
            display.blit(menu_img, menu)
            display.blit(fade_img, fade)
            # title = font.render("My game", True, "white")
            # text_win = font.render("Press start to play", True, "white")
            # display.blit(title, (440, 160)) 
            # display.blit(text_win, (440, 460)) 
         
        case 2:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            loop = False
            
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            player1_speed = -6
                        elif event.key == pygame.K_s:
                            player1_speed = 6
                        elif event.key == pygame.K_a:
                            ball_speed = -6
                        elif event.key == pygame.K_d:
                            ball_speed = 6

            if player2_score >= 3:
                cena = 3
                fade_alpha = 255

            if ball.colliderect(player1) or ball.colliderect(player2): 
                ball_dir_x *= -1
                hit.play()
        
            if player1.y <= 0:        
                player1.y = 0
            elif player1.y >= 720 - 150:
                player1.y = 720 - 150
        
            player1.y += player1_speed
        
        
            if ball.x <= 0:
                player2_score += 1
                placar_player2 = font.render(str(player2_score), True, "white") 
                ball.x = 600
                ball_dir_x *= -1
            elif ball.x >= 1280:
                player1_score += 1
                placar_player1 = font.render(str(player1_score), True, "white")
                ball.x = 600
                ball_dir_x *= -1
        
            if ball.y <= 0:        
                ball_dir_y *= -1
            elif ball.y >= 720 - 15:
                ball_dir_y *= -1
        
        
        
            ball.x += ball_dir_x
            ball.y += ball_dir_y
        
            player2.y = ball.y
        
            if player2.y <= 0:        
                player2.y = 0
            elif player2.y >= 720 - 150:
                player2.y = 720 - 150
        
        
        
            display.fill((0,0,0))
        
            # pygame.draw.rect(display, "white", player1)
        
            # pygame.draw.rect(display, "white", player2)
        
            # pygame.draw.circle(display, "red", ball.center, 8)

            display.blit(campo_img, campo)
            display.blit(ball_img, ball)

            display.blit(placar_player1, (500,50))
            display.blit(player1_img, player1)
        
            display.blit(placar_player2, (780,50))
            display.blit(player2_img, player2)

        case 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                            player1_score = 0
                            placar_player1 = font.render(str(player1_score), True, "white")
                            player2_score = 0
                            placar_player2 = font.render(str(player2_score), True, "white") 
                            player1.y = 0
                            player2.y = 0
                            ball.x = 640
                            ball.y = 320
                            cena = 1
                            fade_alpha = 255

            if fade_alpha >= 0:     
                fade_alpha -= 8   
                fade_img.set_alpha(fade_alpha)
            
            display.fill((0,0,0))
            display.blit(gameOver_img, gameOver)
            display.blit(fade_img, fade)

    fps.tick(60)
    pygame.display.flip()

