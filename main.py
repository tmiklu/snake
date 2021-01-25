import pygame

pygame.init()

bb = pygame.display.list_modes()

aa = map(lambda x: x, bb)
print(list(aa))

pygame.display.set_mode((600, 600))


running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit was pressed")
            running = False
  