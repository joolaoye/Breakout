import pygame as pg   # import the pygame package


pg.init()  # Initializes all pygame modules


# Creating a main window for the game
width = 320
height = 480
screen = pg.display.set_mode((width, height))  # This creates the main window
screen.fill("#ADD8E6")  # Filled the main window with the colour
pg.display.set_caption("Brick Breaker")  # Overwrite the default name 
icon = pg.image.load("assets/game_icon.png")  # Loads in an image from your working directory
pg.display.set_icon(icon)   # Overwrite the default icon


clock = pg.time.Clock()  # Creates a clock object that controls the frame rate of the game



surface = pg.image.load("assets/background.jpg")  # Loads in my game screen



# Creating a ball object
class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/ball.png")  # Loads in an image for my ball
        self.rect = self.image.get_rect(midbottom=(160, 442))  # Wraps a rect around the ball object and sets it's position
        self.x_vel = 2  # initializing the ball's x velocity
        self.y_vel = -2  # initializig the ball's y velocity
        

    def update(self):
        self.rect.x += self.x_vel   # Moves to the right by default
        self.rect.y += self.y_vel  # Moves up

        if self.rect.x <= 0 or self.rect.x >= 300:  
            self.x_vel *= -1  # Changes direction when it hits an edge
        if self.rect.y <= 0:  
            self.y_vel *= -1   # Changes driection when it hits the top

        if pg.sprite.spritecollide(ball, brick_group, dokill=True):
            self.x_vel *= 1 
            self.y_vel *= -1  # Change the y postion, move in the opposite direction

        if pg.sprite.collide_mask(ball,paddle):
            self.x_vel *= 1
            self.y_vel *= -1 # Move in opposite direction on collision with the paddle

# Creating a paddle object 
class Paddle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/paddle3.png")
        self.rect = self.image.get_rect(midbottom=(160, 466))
        

    def movement(self):
        if pressed_left:  # If left Navigation key is pressed
            if self.rect.x > -12: # Checks if it is not at the left edge of the screen
                self.rect.x -= 2  # Moves the paddle to the left

        if pressed_right:  # If right Navigation key is pressed
            if self.rect.x < 233: # Checks if it is not at the right edge of the screen
                self.rect.x += 2  # Moves the paddle to the left

# Create a brick object
class Brick(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((50, 20))
        self.image.fill("#ae4308")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

# Keyboard variables
pressed_left = False
pressed_right = False

# The game loop variables
active = False 
ball_active = False 
paddle_active = False
running = False

# Lives counter
lives = 3  

# Main loop variable
flag = True

brick_group = pg.sprite.Group()  # Synonymous to creating a list that stores the brick object

gap = 4  # The space between bricks
for x in range(2):  # Create 2 horizontal bricks left alligned
    for y in range(6):  # Create 6 vertical bricks
        brick = Brick((50 * x) + (gap * x), (20 * y) + (gap * y))
        brick_group.add(brick)

for x in range(4, 6): # Create 2 horizontal bricks right alligned
    for y in range(6):
        brick = Brick((50 * x) + (gap * x), (20 * y) + (gap * y))
        brick_group.add(brick)

# My Main loop
while flag:
    for event in pg.event.get():  # Checks for the events
        if event.type == pg.KEYDOWN:  # If keyboard is pressed down
            if event.key == pg.K_LEFT:  # Check if left navigation key is pressed
                pressed_left = True  # Move the paddle left
            elif event.key == pg.K_RIGHT:  # Check if right navigation key is pressed
                pressed_right = True  # Move the paddle right
                
            elif event.key == pg.K_SPACE:  # Check if space key is pressed
                if not active:
                    active = True  # Start main game loop
                    running = True
                    ball = Ball()  # initialize the ball object
                    ball_group = pg.sprite.GroupSingle()  # Makes a single grouped sprite (independent)
                    ball_group.add(ball)
                    paddle = Paddle()  # initialize paddle object

            elif event.key == pg.K_RETURN:  # If Enter key pressed
                ball_active = True  # Set ball moveming
                paddle_active = True  # Set paddle movement active

        elif event.type == pg.KEYUP:  # If user releases key
            if event.key == pg.K_LEFT:  # If user releases left key
                pressed_left = False  # Stop moving paddle left
            elif event.key == pg.K_RIGHT: # If user releases right key
                pressed_right = False # Stop moving paddle right

        if event.type == pg.QUIT:  # If user clicks quit button on the window
            flag = False  # End the program

    # My game loop
    if active:
        if ball_active:  # If ball moving
            ball.update()  # Move the ball and detect collisions
        if paddle_active:   # If paddle movement active
            paddle.movement()  # Allow for paddle movement

    
        if len(brick_group) == 0:  # If there is no brick left on the screen
            flag = False  # End Program

        screen.blit(surface,(0,0))  # Place the background on the screen

        screen.blit(paddle.image, paddle.rect)  # Display the paddle on the screen

        ball_group.draw(screen)  # Display the ball on the screen

        brick_group.draw(screen)  # Display the bricks on the screen

        if not ball_active:  # If ball is not moving
            # Display this message
            font = pg.font.SysFont("Verdana", 30)
            text = font.render("Hit Enter to Start", True, "red")
            text_rect = text.get_rect(center=(160, 240))
            screen.blit(text, text_rect)

        live = pg.image.load("assets/heart.png") # Load heart image
        for i in range(lives):  # Display an heart for each life user has
                x = (i * 21)
                live_rect = live.get_rect(bottomleft=(x, 480))
                screen.blit(live, live_rect)

        if ball.rect.y >= 427:  # If the ball hits the bottom of my game screen
            lives -= 1  # Reduce the number of lives the user has
            active = False   # Stop game loop


    else:  # If not in game loop
        ball_active = False  # Stop the ball from moving
        paddle_active = False  # Stop the paddle from moving

        font = pg.font.SysFont("Helvetica", 25)
        text1 = font.render("Hit Space to Retry", True, "red")
        text1_rect = text1.get_rect(center=(150, 240))

        text2 = font.render("Hit Space to Start Game", True, "red")
        text2_rect = text2.get_rect(center=(150, 240))
        
        # if game loop ends but game active, that is the ball hits the bottom of the game screen
        screen.fill("#ADD8E6")
        screen.blit(text1, text1_rect)  # Display hit space to retry

        if not running:  # If game has not been started
            # Display Hit Space to Start Game
            screen.fill("#ADD8E6")
            screen.blit(text2, text2_rect)

        if lives < 0:  # If there are no more lives
            flag = False

    pg.display.update()  # Updates what's displayed on the window
    clock.tick(60)  #  Controls the number of frames displayed per second
