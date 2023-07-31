import pygame as pg
class Paddle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("paddle3.png")
        self.rect = self.image.get_rect(midbottom=(160, 466))


    def movement(self):
        if pressed_left:  # If left Navigation key is pressed
            if self.rect.x > -12: # Checks if it is not at the left edge of the screen
                self.rect.x -= 2  # Moves the paddle to the left

        if pressed_right:  # If right Navigation key is pressed
            if self.rect.x < 233: # Checks if it is not at the right edge of the screen
                self.rect.x += 2  # Moves the paddle to the left
