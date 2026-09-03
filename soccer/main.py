import pygame
from classGame import GameObject, Player, Ball,ImageFade
import resources

pygame.init()
display = pygame.display.set_mode(resources.RESOLUTION_GAME)

pygame.font.init()
font = pygame.font.Font(None, 50)

menu = GameObject(resources.IMG_MENU)
campo = GameObject(resources.IMG_BG)
gameOver = GameObject(resources.IMG_GAMEOVER)

player1 = Player(resources.IMG_PLAYER1)
player2 = Player(resources.IMG_PLAYER2, right=1280)

placar_player1 = font.render(str(player1.score), True, "white")
placar_player2 = font.render(str(player2.score), True, "white")

ball = Ball(resources.IMG_BALL,center=(1280/2, 720/2) )

fade = ImageFade(resources.RESOLUTION_GAME)

objects_draws = [campo, ball, player1, player2, fade]

resources.GAME_SOUND.play(-1)
cena = 1
loop = True
while loop:

    match cena:
        case 1:

            fade.fadeAlpha()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            loop = False  
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                 cena = 2
                                 resources.START_SOUND.play()
                                 fade.reset() 
                            if event.key == pygame.K_q:
                                 loop = False

            display.fill((0,0,0))
            menu.draw(display)
            fade.draw(display)
         
        case 2:

            fade.fadeAlpha()
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
                resources.HIT_SOUND.play()

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
                fade.reset()

            display.fill((0,0,0))
        
            for obj in objects_draws: 
                 obj.draw(display)

            display.blit(placar_player1, (500,50))
            display.blit(placar_player2, (780,50))

        case 3:

            fade.fadeAlpha()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                            player1.reset()
                            placar_player1 = font.render(str(player1.score), True, "white")
                            player2.reset()
                            placar_player2 = font.render(str(player2.score), True, "white") 
                            ball.reset()
                            fade.reset()
                            cena = 1
                            
            display.fill((0,0,0))
            gameOver.draw(display)
            fade.draw(display)

    resources.FPS.tick(60)
    pygame.display.flip()

