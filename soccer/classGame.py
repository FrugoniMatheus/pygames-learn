import pygame
pygame.font.init()

class GameObject:
    def __init__(self, url_img,**args):
        self.img = pygame.image.load(url_img).convert_alpha()
        self.rect = self.img.get_rect(**args)

    def draw(self, display):
        display.blit(self.img, self.rect)
        

class Player(GameObject):
    font = pygame.font.Font(None, 50)
    def __init__(self, url_img, **args):
        super().__init__(url_img, **args)
        self.score = 0
        self.speed = 6
        self.placar = self.font.render(str(self.score), True, "white")

    def move(self):
        self.rect.y += self.speed
        if self.rect.y <= 0:        
            self.rect.y = 0
        elif self.rect.y >= 720 - self.rect.height:
            self.rect.y = 720 - self.rect.height

    def placarDraw(self, display, argsViewPlacar):
        display.blit(self.placar, argsViewPlacar)
        
    def addPoint(self):
        self.score += 1


class Ball(GameObject):
    def __init__(self, url_img, **args):
        super().__init__(url_img, **args)
        self.dir_x = 6
        self.dir_y = 6
        self.start_pos = self.rect.center 

    def move(self):
        self.rect.x += self.dir_x
        self.rect.y += self.dir_y

        if self.rect.y <= 0 or self.rect.y >= 720 - self.rect.height:
            self.dir_y *= -1

    def bounce_x(self):
        self.dir_x *= -1

    def reset(self):
        self.rect.center = self.start_pos
        self.dir_x *= -1