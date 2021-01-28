import pygame

pygame.init()

bb = pygame.display.list_modes()

aa = map(lambda x: x, bb)
print(list(aa))

screen = pygame.display.set_mode((640, 640))

snake_img = pygame.image.load('snake/square.png')
snake_x = 0
snake_y = 0
snake_move = 0

def snake(x, y):
    screen.blit(snake_img, (x, y))

# background color
GREEN = (0, 255, 0)


running = True

while running:

    screen.fill(GREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit was pressed")
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_move += 1
            if event.key == pygame.K_LEFT:
                snake_move += -1
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                snake_move = 0
    
    snake_x += snake_move

    snake(snake_x, snake_y)
    pygame.display.update()
  