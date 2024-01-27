'''
This is the main file for the pong game. It uses the Pygame library to create a graphical user interface.
The game includes two paddles and a ball. Each paddle can move up and down, and the ball moves in a random direction.
If the ball hits a paddle, it bounces back. If the ball hits the left or right edge of the screen, it means that the player on the opposite side scores a point, and the ball should be reset to the center.
'''
import pygame
import sys
import random
# Define some constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
BALL_SIZE = 15
PADDLE_SPEED = 2
BALL_SPEED = 1
class Paddle:
    '''
    This class represents a paddle. It has methods to draw the paddle and move it up and down.
    '''
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
    def move(self, speed, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key]:
            self.rect.move_ip(0, -speed)
        elif keys[down_key]:
            self.rect.move_ip(0, speed)
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
class Ball:
    '''
    This class represents the ball. It has methods to draw the ball and move it.
    '''
    def __init__(self, x, y, dx, dy):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.dx = dx
        self.dy = dy
    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
    def move(self):
        self.rect.move_ip(self.dx, self.dy)
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dy *= -1
    def reset(self):
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.dx = BALL_SPEED if random.randint(0, 1) == 0 else -BALL_SPEED
        self.dy = BALL_SPEED if random.randint(0, 1) == 0 else -BALL_SPEED
def main():
    '''
    This function controls the game loop. It handles events, updates the game state, and redraws the screen.
    '''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    paddle1 = Paddle(WIDTH // 4, HEIGHT // 2)
    paddle2 = Paddle(WIDTH * 3 // 4, HEIGHT // 2)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_SPEED, BALL_SPEED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        paddle1.move(PADDLE_SPEED, pygame.K_w, pygame.K_s)
        paddle2.move(PADDLE_SPEED, pygame.K_UP, pygame.K_DOWN)
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.move()
        ball.draw(screen)
        if paddle1.rect.colliderect(ball.rect) or paddle2.rect.colliderect(ball.rect):
            ball.dx *= -1
        if ball.rect.left < 0 or ball.rect.right > WIDTH:
            ball.reset()
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()