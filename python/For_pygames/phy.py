def block_map(SCREEN_WIDTH, SCREEN_HEIGHT, pos_x, pos_y):
    p1_area_x = SCREEN_WIDTH
    p1_area_y = SCREEN_HEIGHT

    if p1_area_x-20 < pos_x or p1_area_y-20 < pos_y:
        return 0
    if 20 > pos_x or 20 > pos_y:
        return 0
    else:
        return 1
# x = 800.0 y = 450.0


def block_map_event(block_map):
    if block_map == False:
        A = 0
        return A
    else:
        A = 1
        return A


def player_out_of_screen(SCREEN_WIDTH, SCREEN_HEIGHT, pos_x, pos_y):
    if pos_x > SCREEN_WIDTH or pos_y > SCREEN_HEIGHT:
        return 1
    if pos_x < 0 or pos_y < 0:
        return 1
    else:
        return 0
