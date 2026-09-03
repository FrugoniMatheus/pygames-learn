import pygame

pygame.init()

# Sounds
HIT_SOUND = pygame.mixer.Sound("assets/sounds/pong.wav")
START_SOUND = pygame.mixer.Sound("assets/sounds/start.wav")
GAME_SOUND = pygame.mixer.Sound("assets/sounds/music.ogg")

# Images
IMG_MENU = "assets/imgs/menu.png"
IMG_BG = "assets/imgs/bg.png"
IMG_GAMEOVER = "assets/imgs/go.png"
IMG_PLAYER1 = "assets/imgs/player1.png"
IMG_PLAYER2 = "assets/imgs/player2.png"
IMG_BALL = "assets/imgs/ball.png"

# Resolution
RESOLUTION_GAME = (1280,720)

# FPS
FPS = pygame.time.Clock()
