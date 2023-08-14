import pygame
import phy
import sys

"""
펜 이동 방향키 키 

펜 부가 기능
펜 줄이기 j, 펜 키우기 k, 전체 지우개 p, 펜 비활성화 n, 펜 활성화 m

펜 속도
빠르게 z 느리게 x

rgb 값 변경
r 증가 q,  g 증가 w, b 증가 e
r 감소 a,  g 감소 e, b 감소 d
"""

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

r = 255
g = 255
b = 255

color = (r, g, b)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("drawing Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = SCREEN_WIDTH/2
pos_y = SCREEN_HEIGHT/2
speed = 1
clock = pygame.time.Clock()


pen_size = 20
last_pen_size = 20

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

# ================방향키 설정====================
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
# ===============================================
    if key_event[pygame.K_k]:  # 펜 사이즈 키우기
        pen_size = pen_size+0.1
        last_pen_size = pen_size

    if key_event[pygame.K_j]:  # 펜 사이즈 줄이기
        if pen_size < 1.5:
            pen_size = 1
            last_pen_size = pen_size
        else:
            pen_size = pen_size-0.1
            last_pen_size = pen_size

    if key_event[pygame.K_p]:  # 전체 지우개
        screen.fill(black)
    if key_event[pygame.K_n]:  # 펜 비활성화
        pen_size = 0
    if key_event[pygame.K_m]:  # 펜 활성화(마지막 펜 사이즈 기준)
        pen_size = last_pen_size

    if phy.block_map_event(block_map) == False:  # 펜 맵 이탈 방지
        speed = 0
    else:
        speed = 1

    if key_event[pygame.K_z]:  # 빠르게 그리기
        if phy.block_map_event(block_map) == False:
            speed = 0
        if pen_size <= 2.5:
            speed = 1
        else:
            speed = speed + 0.01
    if key_event[pygame.K_x]:  # 느리게 그리기
        if phy.block_map_event(block_map) == False:
            speed = 0
        if pen_size <= 2.5:
            speed = 1
        if speed < 0:
            speed = 0.02
        else:
            speed = speed - 0.01
# =============색 조절 영역==============================
    if key_event[pygame.K_q]:  # r값 증가
        if r >= 255:
            r = 255
        else:
            r = r+1

    if key_event[pygame.K_a]:  # r값 감소
        if r <= 0:
            r = 0
        else:
            r = r-1

    if key_event[pygame.K_w]:  # g값 증가
        if g >= 255:
            g = 255
        else:
            g = g+1

    if key_event[pygame.K_s]:  # g값 감소
        if g <= 0:
            g = 0
        else:
            g = g-1

    if key_event[pygame.K_e]:  # b값 증가
        if b >= 255:
            b = 255
        else:
            b = r+1

    if key_event[pygame.K_d]:  # r값 감소
        if b <= 0:
            b = 0
        else:
            b = b-1
    color = (r, g, b)
# ========================================================
    if phy.player_out_of_screen(SCREEN_WIDTH, SCREEN_HEIGHT, pos_x, pos_y) == True:  # 초기 펜 위치
        pos_x = SCREEN_WIDTH/2
        pos_y = SCREEN_HEIGHT/2
    # 색 다르게 만들어보기
    pygame.draw.circle(screen, color, (pos_x, pos_y), pen_size)
    pygame.display.update()
