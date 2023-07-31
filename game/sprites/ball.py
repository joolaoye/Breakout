import pygame as pg

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("ball.png")  # Loads in an image for my ball
        self.rect = self.image.get_rect(
            midbottom=(160, 442))  # Wraps a rect around the ball object and sets it's position
        self.x_vel = 2  # initializing the ball's x velocity
        self.y_vel = -2  # initializig the ball's y velocity

    def update(self):
        self.rect.x += self.x_vel  # Moves to the right by default
        self.rect.y += self.y_vel  # Moves up

        if self.rect.x <= 0 or self.rect.x >= 300:
            self.x_vel *= -1  # Changes direction when it hits an edge
        if self.rect.y <= 0:
            self.y_vel *= -1  # Changes direction when it hits the top

        if pg.sprite.spritecollide(ball, brick_group, dokill=True):
            self.x_vel *= 1
            self.y_vel *= -1  # Change the y position, move in the opposite direction

        if pg.sprite.collide_mask(ball, paddle):
            self.x_vel *= 1
            self.y_vel *= -1  # Move in opposite direction on collision with the paddle