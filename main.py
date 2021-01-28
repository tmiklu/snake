import pygame
import random

pygame.init()

bb = pygame.display.list_modes()

aa = map(lambda x: x, bb)
print(list(aa))

screen = pygame.display.set_mode((640, 640))

snake_img = pygame.image.load('snake/square.png')
snake_x = 0
snake_y = 0
snake_move_x = [0, 64, 128, 192, 256, 320, 384, 448, 512, 576]
snake_move_y = [0, 64, 128, 192, 256, 320, 384, 448, 512, 576]

tail_img = pygame.image.load('snake/tail.png')
tail_x = random.choice(snake_move_x)
tail_y = random.choice(snake_move_y)

def snake(x, y):
    screen.blit(snake_img, (x, y))

def tail(x, y):
    screen.blit(tail_img, (x, y))

# background color
GREEN = (0, 255, 0)


running = True
index_x = 0
index_y = 0

while running:

    screen.fill(GREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit was pressed")
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if snake_move_x[index_x] == 576:
                    snake_move_x[9]
                else:
                    snake_move_x[index_x]
                    print("RIGHT x:", snake_move_x[index_x])
                    index_x += 1
            if event.key == pygame.K_LEFT:
                if snake_move_x[index_x] == 0:
                    snake_move_x[0]
                else:
                    index_x += -1
                    snake_move_x[index_x]
                    print("LEFT x:", snake_move_x[index_x])

            if event.key == pygame.K_DOWN:
                if snake_move_y[index_y] == 576:
                    snake_move_y[9]
                else:
                    index_y += 1
                    snake_move_y[index_y]
                    print("DOWN y:", snake_move_y[index_y])

            if event.key == pygame.K_UP:
                if snake_move_y[index_y] == 0:
                    snake_move_y[0]
                else:
                    index_y += -1
                    snake_move_y[index_y]
                    print("UP y:", snake_move_y[index_y])
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #snake_move = 0
                pass

  
    snake_x = snake_move_x[index_x]
    snake_y = snake_move_y[index_y]

    snake(snake_x, snake_y)
    tail(tail_x, tail_y)
    pygame.display.update()
  