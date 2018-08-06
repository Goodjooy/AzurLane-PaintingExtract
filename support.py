import pygame
import pygame.locals
import json
import sys
import restore_hand


def prepare():
    pygame.init()

    with open('index.json', 'r') as file:
        pic_files, rect_file, bg = json.load(file)

        for key_pic in pic_files.keys():
            restore_hand.pic_club[key_pic] = [pygame.image.load(pic_files[key_pic]), rect_file[key_pic][0]]

            restore_hand.rect_club[key_pic] = pygame.Rect(rect_file[key_pic])

            restore_hand.change_club[key_pic] = [0, 0]

        restore_hand.bg = pygame.image.load(bg)

    restore_hand.bg_wide, restore_hand.bg_high = restore_hand.bg.get_size()

    restore_hand.scale = min(100 / restore_hand.bg_high, 200 / restore_hand.bg_wide)

    restore_hand.work_space = pygame.Rect(0, 0, 500, 500)
    restore_hand.bar = pygame.Rect(501, 0, 200, 500)
    restore_hand.show = pygame.Rect(702, 0, 600, 500)
    restore_hand.guide = pygame.Rect(501, 0, 200, 100)
    restore_hand.guide_rect = pygame.Rect(501, 0, restore_hand.bg_wide * restore_hand.scale,
                                          restore_hand.bg_high * restore_hand.scale)
    restore_hand.guide_rect.center = restore_hand.guide.center

    pygame.font.init()

    restore_hand.font = pygame.font.Font('char.ttf', 20)

    restore_hand.save = restore_hand.font.render("保存", True, (200, 200, 200), (255, 0, 0))
    restore_hand.back = restore_hand.font.render("撤销", True, (200, 200, 200), (255, 0, 0))
    restore_hand.all_back = restore_hand.font.render("全部撤销", True, (200, 200, 200), (255, 0, 0))
    if not restore_hand.show_map_bool:
        restore_hand.show_map = restore_hand.font.render("显示辅助框", True, (200, 200, 200), (255, 0, 0))
    if restore_hand.show_map_bool:
        restore_hand.show_map = restore_hand.font.render("关闭辅助框", True, (200, 200, 200), (255, 0, 0))

    restore_hand.save_rect = restore_hand.save.get_rect().move(restore_hand.bar.x + 5, 300)
    restore_hand.back_rect = restore_hand.back.get_rect().move(restore_hand.bar.x + 5,
                                                               305 + restore_hand.save_rect.height)
    restore_hand.all_back_rect = restore_hand.all_back.get_rect().move(restore_hand.bar.x + 105, 300)
    restore_hand.show_map_rect = restore_hand.show_map.get_rect().move(restore_hand.bar.x + 105,
                                                                       305 + restore_hand.save_rect.height)


def load_sub_pic():
    pass


def load_bg():
    restore_hand.child_surface = pygame.Surface(restore_hand.bg.get_size(), flags=pygame.SRCALPHA, depth=32)


# noinspection PyGlobalUndefined
def catch_rect(mouse_left_press_area):
    global key
    for key in restore_hand.rect_club.keys():
        if restore_hand.rect_club[key].collidepoint(mouse_left_press_area):
            key = key
            break
        else:
            key = -1
    return key


def event_catch():
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        sys.exit()

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if restore_hand.work_space.collidepoint(event.pos):
            if event.button == 1:
                restore_hand.choice_rect = catch_rect(
                    [event.pos[0] - restore_hand.rel[0], event.pos[1] - restore_hand.rel[1]])
        elif restore_hand.save_rect.collidepoint(event.pos):
            if event.button == 1:
                pygame.image.save(restore_hand.child_surface, "out.png")
        elif restore_hand.back_rect.collidepoint(event.pos):
            if event.button == 1:
                go_back(restore_hand.choice_rect)
        elif restore_hand.all_back_rect.collidepoint(event.pos):
            if event.button == 1:
                all_go_back()

        elif restore_hand.show_map_rect.collidepoint(event.pos):
            if event.button == 1:
                press_show_map()

        else:
            pass
    elif event.type == pygame.MOUSEMOTION:
        if restore_hand.work_space.collidepoint(event.pos):
            if event.buttons[2] == 1:
                pic_move(event.rel)

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            restore_hand.pos_change = True
            move_sub_pic(restore_hand.choice_rect, restore_hand.left)
        if event.key == pygame.K_RIGHT:
            restore_hand.pos_change = True
            move_sub_pic(restore_hand.choice_rect, restore_hand.right)
        if event.key == pygame.K_UP:
            restore_hand.pos_change = True
            move_sub_pic(restore_hand.choice_rect, restore_hand.up)
        if event.key == pygame.K_DOWN:
            restore_hand.pos_change = True
            move_sub_pic(restore_hand.choice_rect, restore_hand.down)

        if event.key == pygame.K_a:
            restore_hand.pos_change = True
            move_sub_pic(restore_hand.choice_rect, restore_hand.a)
        if event.key == pygame.K_d:
            restore_hand.pos_change = True
            move_sub_pic(restore_hand.choice_rect, restore_hand.d)
        if event.key == pygame.K_w:
            restore_hand.pos_change = True
            move_sub_pic(restore_hand.choice_rect, restore_hand.w)
        if event.key == pygame.K_s:
            restore_hand.pos_change = True
            move_sub_pic(restore_hand.choice_rect, restore_hand.s)


def press_show_map():
    restore_hand.show_map_bool = not restore_hand.show_map_bool

    if not restore_hand.show_map_bool:
        restore_hand.show_map = restore_hand.font.render("显示辅助框", True, (200, 200, 200), (255, 0, 0))
    if restore_hand.show_map_bool:
        restore_hand.show_map = restore_hand.font.render("关闭辅助框", True, (200, 200, 200), (255, 0, 0))

def mouse_deal():
    pass


def pic_move(rel):
    restore_hand.rel[0] += rel[0]
    restore_hand.rel[1] += rel[1]
    if restore_hand.rel[0] + restore_hand.bg_wide - 500 < 0:
        restore_hand.rel[0] = -restore_hand.bg_wide + 500
    if restore_hand.rel[1] + restore_hand.bg_high - 500 < 0:
        restore_hand.rel[1] = -restore_hand.bg_high + 500
    if restore_hand.rel[0] > 0:
        restore_hand.rel[0] = 0
    if restore_hand.rel[1] > 0:
        restore_hand.rel[1] = 0


def move_sub_pic(key_pic, type_key):
    if key_pic == -1:
        pass
    else:

        if type_key == restore_hand.up:
            restore_hand.change_club[key_pic][1] -= 1
        if type_key == restore_hand.down:
            restore_hand.change_club[key_pic][1] += 1
        if type_key == restore_hand.left:
            restore_hand.change_club[key_pic][0] -= 1
        if type_key == restore_hand.right:
            restore_hand.change_club[key_pic][0] += 1

        if type_key == restore_hand.w:
            restore_hand.change_club[key_pic][1] -= 4
        if type_key == restore_hand.s:
            restore_hand.change_club[key_pic][1] += 4
        if type_key == restore_hand.a:
            restore_hand.change_club[key_pic][0] -= 4
        if type_key == restore_hand.d:
            restore_hand.change_club[key_pic][0] += 4


def go_back(key_pic):
    restore_hand.change_club[key_pic] = [0, 0]

    restore_hand.pos_change = True


def all_go_back():
    for key_pic in restore_hand.change_club.keys():
        restore_hand.change_club[key_pic] = [0, 0]

    restore_hand.pos_change = True


def print_pic():
    for key_pic in restore_hand.pic_club.keys():
        restore_hand.child_surface.blit(restore_hand.pic_club[key_pic][0],
                                        [restore_hand.pic_club[key_pic][1][0] + restore_hand.change_club[key_pic][0],
                                         restore_hand.pic_club[key_pic][1][1] + restore_hand.change_club[key_pic][1]])


def print_bg(scr):
    if restore_hand.show_map_bool:
        scr.screen.blit(restore_hand.bg, (0 + restore_hand.rel[0], 0 + restore_hand.rel[1]))
    scr.screen.blit(restore_hand.child_surface, (0 + restore_hand.rel[0], 0 + restore_hand.rel[1]))


def change_print():
    if restore_hand.pos_change:
        restore_hand.child_surface = pygame.Surface(restore_hand.bg.get_size(), flags=pygame.SRCALPHA, depth=32)

        for key_pic in restore_hand.pic_club.keys():
            restore_hand.child_surface.blit(restore_hand.pic_club[key_pic][0],
                                            [restore_hand.pic_club[key_pic][1][0]
                                             + restore_hand.change_club[key_pic][0],
                                             restore_hand.pic_club[key_pic][1][1] +
                                             restore_hand.change_club[key_pic][1]])
    restore_hand.pos_change = False


def right_up():
    restore_hand.rel = [0, 0]


def show_prepare():
    if restore_hand.choice_rect != -1:
        restore_hand.show_pic = restore_hand.pic_club[restore_hand.choice_rect][0]
        restore_hand.show_rect = restore_hand.show_pic.get_rect()
        restore_hand.show_rect.center = restore_hand.show.center

        restore_hand.font1 = restore_hand.font.render(
            "长：%d；宽：%d" % (restore_hand.show_rect.width, restore_hand.show_rect.height)
            , True, (255, 255, 255))
        restore_hand.font2 = restore_hand.font.render(
            "坐标：（%d，%d）" % (restore_hand.show_rect.x, restore_hand.show_rect.y)
            , True, (255, 255, 255))
    else:
        restore_hand.show_pic = None


def show(scr):
    if restore_hand.show_pic is not None:
        scr.screen.blit(restore_hand.show_pic, (restore_hand.show_rect.x, restore_hand.show_rect.y))
        scr.screen.blit(restore_hand.font1, (500, 120))
        scr.screen.blit(restore_hand.font2, (500, 122 + restore_hand.font1.get_height()))


def press(scr):
    scr.screen.blit(restore_hand.save, (restore_hand.save_rect.x, restore_hand.save_rect.y))
    scr.screen.blit(restore_hand.back, (restore_hand.back_rect.x, restore_hand.back_rect.y))
    scr.screen.blit(restore_hand.all_back, (restore_hand.all_back_rect.x, restore_hand.all_back_rect.y))
    scr.screen.blit(restore_hand.show_map, (restore_hand.show_map_rect.x, restore_hand.show_map_rect.y))
