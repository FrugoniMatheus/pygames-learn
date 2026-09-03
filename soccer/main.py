import pygame
from classGame import GameObject, Player, Ball

pygame.init()
pygame.font.init()

fps = pygame.time.Clock()
hit = pygame.mixer.Sound("assets/pong.wav")
start = pygame.mixer.Sound("assets/start.wav")
music_game = pygame.mixer.Sound("assets/music.ogg")
font = pygame.font.Font(None, 50)

display = pygame.display.set_mode((1280, 720))

fade_img = pygame.Surface((1280,720)).convert_alpha() 
#Imagem transparente
fade = fade_img.get_rect()
fade_img.fill("black")
fade_alpha = 255


menu = GameObject("assets/menu.png")
campo = GameObject("assets/bg.png")
gameOver = GameObject("assets/go.png")

player1 = Player("assets/player1.png")
player2 = Player("assets/player2.png", right=1280)

placar_player1 = font.render(str(player1.score), True, "white")
placar_player2 = font.render(str(player2.score), True, "white")

ball = Ball("assets/ball.png",center=(1280/2, 720/2) )

music_game.play(-1)
cena = 1
loop = True
while loop:

    match cena:
        case 1:

            if fade_alpha >= 0:
                fade_alpha -= 8
                fade_img.set_alpha(fade_alpha)

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

            display.fill((0,0,0))
            menu.draw(display)
            display.blit(fade_img, fade)
         
        case 2:
    
            player1.move()
            player2.move()
            ball.move()

            player2.rect.y = ball.rect.y

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            loop = False
            
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            player1.speed = -6
                        elif event.key == pygame.K_s:
                            player1.speed = 6
                        elif event.key == pygame.K_a:
                            ball_speed = -6
                        elif event.key == pygame.K_d:
                            ball_speed = 6

            if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect): 
                ball.bounce_x()
                hit.play()

            if ball.rect.x <= 0:
                player2.addPoint()
                placar_player2 = font.render(str(player2.score), True, "white") 
                ball.reset()
            elif ball.rect.x >= 1280:
                player1.addPoint()
                placar_player1 = font.render(str(player1.score), True, "white")
                ball.reset()

            if player2.score >= 3:
                cena = 3
                fade_alpha = 255

            display.fill((0,0,0))
        
            campo.draw(display)
            ball.draw(display)

            display.blit(placar_player1, (500,50))
            player1.draw(display)
        
            display.blit(placar_player2, (780,50))
            player2.draw(display)
                    
        case 3:

            if fade_alpha >= 0:     
                fade_alpha -= 8   
                fade_img.set_alpha(fade_alpha)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                            player1.score = 0
                            placar_player1 = font.render(str(player1.score), True, "white")
                            player2.score = 0
                            placar_player2 = font.render(str(player2.score), True, "white") 
                            player1.y = 0
                            player2.y = 0
                            ball.x = 640
                            ball.y = 320
                            cena = 1
                            fade_alpha = 255

            display.fill((0,0,0))
            gameOver.draw(display)
            display.blit(fade_img, fade)

    fps.tick(60)
    pygame.display.flip()

