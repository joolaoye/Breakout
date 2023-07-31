import pygame as pg

class Brick(pg.sprite.Sprite):
    def __init__(self, x : int, y : int, image : str):
        super().__init__()
        image = pg.image.load(image)
        self.image = pg.transform.scale(image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, screen : 'pg.surface.Surface'):
        screen.blit(self.image, (self.rect.x,self.rect.y))
class L1_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y,"C:/Users/olaoy/Brick_Breaker/assets/block (1).png")
        self._hit = 1


class L2_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y, "C:/Users/olaoy/Brick_Breaker/assets/brick-wall.png")
        self._hit = 2

class L3_brick(Brick):
    def __init__(self, x, y):
        super().__init__(x,y,"C:/Users/olaoy/Brick_Breaker/assets/floor.png")
        self._hit = float('inf')


class wall(Brick):
    def __init__(self, x, y):
        super().__init__(x, y,"C:/Users/olaoy/Brick_Breaker/assets/edge.png")
        self._hit = float('inf')