import pygame
import random
import matplotlib.pyplot as plt

run = True 
x = []
y = [] 
count1 = 1
count2 = 0
while run:
    pygame.init()#Initialize the game
    RED = (255,0,0)
    BLUE = (0, 0, 255)
    GREEN = (0,255,0)
    BLACK = (0, 0, 0)
    size = [600, 600]
    number = size[0] / 20
    screen = pygame.display.set_mode(size)
    clock= pygame.time.Clock()
    font = pygame.font.SysFont("arial", 20, True, True)
    text_color = (255, 255, 255)
    pygame.display.set_caption('Snake Game')

    def graph(count1, count2):
        x.append(count1)
        y.append(count2)
        plt.plot(x, y, 'ro')
        plt.axis([0, 20, 0, 30])
        plt.title("Users score")
        plt.xlabel("Game number")
        plt.ylabel("Score")
        plt.show(block = False)
        plt.pause(5)
        plt.close()

    def draw_block(screen, color, position):
        block = pygame.Rect((position[1] * 20, position[0] * 20),
                            (20, 20))
        pygame.draw.rect(screen, color, block)

    class Snake:
        def __init__(self):
            self.position = [(0, 2), (0, 1), (0, 0)]
            self.direction = ''
            self.before_direction = ''
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
                self.position = self.position[:] + [(y, x - 1)] # this line of code same as "self.position.append((y, x - 1))"
            elif self.direction == 'R':
                self.position = self.position[:] + [(y, x + 1)]
            elif self.direction == 'U':
                self.position = self.position[:] + [{y - 1, x}]
            elif self.direction == 'D':
                self.position = self.position[:] + [(y + 1, x)]

        def draw(self):
            for position in self.position:
                if position == self.position[0]:
                    draw_block(screen, BLUE, list(position))
                else:
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
        def __init__(self, position = (random.randint(0, number - 1), random.randint(0, number - 1))):
            self.position = position

        def position_change(self):
            self.position = (random.randint(0, number - 1), random.randint(0, number - 1))

        def draw(self):
            draw_block(screen, RED, self.position)

    def main():  
        global run, count2  
        tick = 15
        snake = Snake()
        apple = Apple()
        text = font.render("length : %d" % snake.len, True, text_color)

        #infinite loop
        running = True
        while running:
            screen.fill(BLACK)
            clock.tick(tick)
            print('1')
            for event in pygame.event.get():#check the event
                print("event worked!")
                if event.type == pygame.QUIT:#check the program quit
                    running = False
                    run = False
                if event.type == pygame.KEYDOWN:#check the key down
                    if event.key == pygame.K_LEFT:
                        snake.direction = 'L'
                    elif event.key == pygame.K_RIGHT:
                        snake.direction = 'R'            
                    elif event.key == pygame.K_UP:
                        snake.direction = 'U'
                    elif event.key == pygame.K_DOWN:
                        snake.direction = 'D'
                    
                    #check the original direction and opposite direction
                    if snake.direction == 'L' and snake.before_direction == 'R':
                        snake.direction = 'R'
                    elif snake.direction == 'R' and snake.before_direction == 'L':
                        snake.direction = 'L'    
                    elif snake.direction == 'U' and snake.before_direction == 'D':
                        snake.direction = 'D'
                    elif snake.direction == 'D' and snake.before_direction == 'U':
                        snake.direction = 'U'

            #move model
            snake.move()
            snake.before_direction = snake.direction #input data of before direction after move
            print(snake.position)

            #collide with apple of condition and then result
            if snake.head_position == apple.position:
                apple.position_change()
                snake.grow()
                tick += 1
                count2 += 1
                text = font.render("length : %d" % snake.len, True, text_color)

            #collide himself of condition and then result
            if snake.position[0] in snake.position[1:]:
                running = False
                print('!!Game over!!')

            #collide on wall of condition and the result
            if (snake.position[0][0] == -1 or snake.position[0][0] == number) or (snake.position[0][1] == -1 or snake.position[0][1] == number):
                running = False
                print('!!Game over!!')

            snake.draw()
            apple.draw()
            screen.blit(text, (0, 0))
            
            pygame.display.update()#reset game background         

    if __name__ == '__main__':
        main()

    #quit the game
    pygame.quit() 

    #drawing graph
    if run == False:
        pass
    else:
        graph(count1, count2)
        count1 += 1
        count2 = 0
