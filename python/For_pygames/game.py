import pygame
import phy
import sys

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("drawing Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


font = pygame.font.SysFont("font_name", 30, False, False)
text = font.render("left time", True, white)

pos_x = SCREEN_WIDTH/2
pos_y = SCREEN_HEIGHT/2
speed = 1
clock = pygame.time.Clock()
i = 0
pen_size = 20

while True:
    clock.tick(60)
    block_map = phy.block_map(SCREEN_WIDTH, SCREEN_HEIGHT, pos_x, pos_y)
    if block_map == 0:
        print(f'블록 판정 : {block_map}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    key_event = pygame.key.get_pressed()
    print("x =", pos_x, "y =", pos_y)

    screen.blit(text, (800, 20))

    if key_event[pygame.K_LEFT]:
        if phy.block_map_event(block_map) == False:
            speed = 1
            pos_x = pos_x+speed
        else:
            pos_x = pos_x-speed

    if key_event[pygame.K_RIGHT]:
        if phy.block_map_event(block_map) == False:
            speed = 1
            pos_x = pos_x-speed
        else:
            pos_x = pos_x+speed

    if key_event[pygame.K_UP]:
        if phy.block_map_event(block_map) == False:
            speed = 1
            pos_y = pos_y+speed
        else:
            pos_y = pos_y-speed

    if key_event[pygame.K_DOWN]:
        if phy.block_map_event(block_map) == False:
            speed = 1
            pos_y = pos_y-speed
        else:
            pos_y = pos_y+speed

    if key_event[pygame.K_u]:
        pen_size = pen_size+0.1
    if key_event[pygame.K_d]:
        pen_size = pen_size-0.1

    if phy.block_map_event(block_map) == False:
        speed = 0
    else:
        speed = 1

    if key_event[pygame.K_SPACE]:
        if phy.block_map_event(block_map) == False:
            speed = 0
        else:
            speed = 5
    # if time
    for i in range(100):
        globals()[f'mob{i}'] = i
        print("자동변수 =", f'mob{i}')
    if phy.player_out_of_screen(SCREEN_WIDTH, SCREEN_HEIGHT, pos_x, pos_y) == True:
        pos_x = SCREEN_WIDTH/2
        pos_y = SCREEN_HEIGHT/2
      # 스피드 값이 0으로 되도 계속 1로 고정이 되어 블록 판정이 이뤄지지 않음.
        # 해결법 방향 인수 값을 알아내서 같이 넘긴 후 스피드를 이동 스피드의 부호 반대 값으로 전환 시키면 된다.

    # screen.fill(black)
    pygame.draw.circle(screen, white, (pos_x, pos_y), pen_size)
    pygame.display.update()
