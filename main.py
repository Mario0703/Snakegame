import pygame
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
pygame.display.init()
FPS = 60
Window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
Snake_x,Snake_y = 500,500
Food_x, Food_y = 100,100
food_width, food_height = 30,30
Snake_width,Snake_height = 25,25

snake_speed_x = 0
snake_speed_y = 0
snake_speed = 3

x1 = Snake_width/2
y1 = Snake_height/2

red = (255,255,0)
green = (0,128,0)
snake_x = 50
snake_y = 50
snake_List = []
snake_lenght = 1
food = pygame.Rect((Food_x,Food_y),(food_width,food_height))

def Draw_on_to_screen():
    Window.fill((0,0,0))

    for snake_coordinate in snake_List:
        pygame.draw.rect(Window, red, [snake_coordinate[0], snake_coordinate[1], 50, 50])
    pygame.draw.rect(Window,green,food)
    pygame.display.update()
def move_snake(keys):
    global snake_speed_x
    global snake_speed_y
    global Snake_body
    global snake_lenght
    if keys[pygame.K_g]:
        snake_lenght+=1
    if keys[pygame.K_a]:
        snake_speed_x = -snake_speed
        snake_speed_y = 0
    elif keys[pygame.K_d]:
        snake_speed_x = snake_speed
        snake_speed_y = 0
    elif keys[pygame.K_w]:
        snake_speed_x = 0
        snake_speed_y = -snake_speed
    elif keys[pygame.K_s]:
        snake_speed_x = 0
        snake_speed_y = snake_speed

def main():
    global x1
    global y1
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        x1 += snake_speed_x
        y1 += snake_speed_y

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_lenght:
            del snake_List[0]
            #print(snake_Head,snake_List)
        keys = pygame.key.get_pressed()
        move_snake(keys)
        Draw_on_to_screen()
if __name__ == '__main__':
    main()

