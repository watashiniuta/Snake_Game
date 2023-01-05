import pygame
import random

pygame.init()#Initialize the game

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0, 0, 0)
size = [400, 400]
screen = pygame.display.set_mode(size)
clock= pygame.time.Clock()

def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 20, position[0] * 20),
                        (20, 20))
    pygame.draw.rect(screen, color, block)

class Snake:
    def __init__(self):
        self.position = [(0, 2), (0, 1), (0, 0)]
        self.direction = ''
        self.len = 3

    def move(self):
        self.head_position = self.position[0]
        y, x = self.head_position

        if self.direction == 'L':
            self.position = [(y, x - 1)] + self.position[:-1]
        elif self.direction == 'R':
            self.position = [(y, x + 1)] + self.position[:-1]
        elif self.direction == 'U':
            self.position = [(y - 1, x)] + self.position[:-1]
        elif self.direction == 'D':
            self.position = [(y + 1, x)] + self.position[:-1]

    def grow(self):
        self.tail_position = self.position[-1]
        y, x = self.tail_position
        self.len += 1

        if self.direction == 'L':
            self.position = self.position[:] + [(y, x - 1)] # this line of code same as this self.position.append((y, x - 1))
        elif self.direction == 'R':
            self.position = self.position[:] + [(y, x + 1)]
        elif self.direction == 'U':
            self.position = self.position[:] + [{y - 1, x}]
        elif self.direction == 'D':
            self.position = self.position[:] + [(y + 1, x)]

    def draw(self):
        for position in self.position:         
            draw_block(screen, GREEN, list(position))

"""
    it can use this code

    def __init__(self):
        ~
        self.len = 3
        ~

    def grow(self):
        ~
        self.len += 1
        ~

    def draw(self):
        for index in range(0, self.len):
            draw_block(screen, GREEN, self.position[index])
"""

class Apple:
    def __init__(self, position = (5, 5)):
        self.position = position

    def position_change(self):
        self.position = (random.randint(0, 19), random.randint(0, 19))

    def draw(self):
        draw_block(screen, RED, self.position)

def main():    
    snake = Snake()
    apple = Apple()

    #infinite loop
    running = True
    while running:
        screen.fill(BLACK)
        clock.tick(15)
        print('1')
        for event in pygame.event.get():#check the event
            print("event worked!")
            if event.type == pygame.QUIT:#check the program quit
                running = False

            if event.type == pygame.KEYDOWN:#check the key down
                if event.key == pygame.K_LEFT:
                    snake.direction = 'L'
                elif event.key == pygame.K_RIGHT:
                    snake.direction = 'R'            
                elif event.key == pygame.K_UP:
                    snake.direction = 'U'
                elif event.key == pygame.K_DOWN:
                    snake.direction = 'D'
                        
        #뱀 이동
        snake.move()
        print(snake.position)

        #collide with apple of condition and then result
        if snake.head_position == apple.position:
            apple.position_change()
            snake.grow()

        #collide himself of condition and then result
        if snake.position[0] in snake.position[1:]:
            running = False
            print('!!Game over!!')

        snake.draw()
        apple.draw()

        pygame.display.update()#reset game background         

if __name__ == '__main__':
    main()

#게임종료
pygame.quit()