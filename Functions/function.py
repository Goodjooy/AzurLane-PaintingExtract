import PIL.Image

import os


def get_longest(array_enter):
    return max([len(value) for value in array_enter])


def find(string, array_enter):
    # one->index two->value
    if not array_enter:
        return array_enter
    able_next = [[], []]
    indexes = range(get_longest(array_enter))
    text_val = string[0]
    able_index = []
    array_copy = [[index, array_enter[index]] for index in range(len(array_enter))]
    pass_list = []

    for index in indexes:
        for value in range(len(array_enter)):
            try:
                val1 = (array_copy[value][1][index]).lower()
            except IndexError:
                continue

            if val1 == text_val and value not in pass_list:
                able_next[0].append(value)
                able_index.append(value)
                pass_list.append(value)
                able_next[1].append(array_enter[value][index + 1:])

    string = string[1:]
    if len(able_next) >= 1 and len(string) > 0:
        value = find(string, able_next[1])
        able_index = []
        for index in value:
            able_index.append(able_next[0][index])
        return able_index
    else:
        return able_index


def all_file(dir_name):
    had = []
    list_keep = os.listdir(dir_name)
    out_list = []
    dir_list = []
    for file in list_keep:
        if not isfile(dir_name + "\\" + file) and not (file in had):
            dir_list.append(file)
        else:
            out_list.append(file)
    for file in dir_list:
        re_1 = all_file(dir_name + "\\" + file)
        had.extend(re_1)
        out_list.extend(re_1)

    return out_list


def all_file_path(dir_name):
    had = []
    list_keep = os.listdir(dir_name)
    diction = {}
    dir_list = []
    file_name_list = []
    file_list = []
    for file in list_keep:
        if not isfile(dir_name + "\\" + file) and not (file in had):
            dir_list.append(file)
        elif file.split(' ')[0] == "UISprite":
            pass
        elif file.split(' ')[-1][0] == "#":
            temp = file.split('\\')[-1].lower().replace('.png', '').split(" ")
            if temp[0].split("_")[-1].lower() == "alpha":
                temp = '_Alpha ' + temp[-1]
                file_list.append(file)
                file_name_list.append(file.replace(temp, "_again_Alpha"))
            else:
                temp = " " + temp[-1]
                file_list.append(file)
                file = file.replace(temp, "_again")
                file_name_list.append(file)

        else:
            file_list.append(file)
            file_name_list.append(file)
    for file in dir_list:
        re = all_file_path(dir_name + "\\" + file)
        had.extend(re[0])
        file_name_list.extend(re[0])
        for keys in re[1]:
            diction[keys] = re[1][keys]
    for index in range(len(file_name_list)):
        if not file_name_list[index] in had:
            diction[file_name_list[index]] = dir_name + "\\" + file_list[index]
            file_list[index] = dir_name + "\\" + file_list[index]

    return file_list, diction


def isfile(file):
    try:
        with open(file, 'r'):
            pass
    except FileNotFoundError:
        return False
    except PermissionError:
        return False
    else:
        return True


def re_int(num):
    """四舍五入"""
    return round(num)


def az_paint_restore(mesh_path: str, pic_path: str):
    """

    :param mesh_path:the path of mesh file
    :param pic_path: the path of tex file
    :return: PIL.Image->restored image
    """
    # 用于存储相应参数
    blit_place = [None]
    cut_place = [None]
    restore_way = []
    printer = []

    # 文件信息读取，分类
    with open(mesh_path, 'r', encoding="utf-8")as info:
        for msg in info.readlines():

            if msg[0] == "g":
                continue

            elif msg[0] == "v" and msg[1] != 't':
                msg = msg[:-3]
                msg = msg.split(" ")
                msg = msg[1:]
                msg = [int(msg[0]), int(msg[1])]
                blit_place.append(msg)

            elif msg[0] == "v" and msg[1] == "t":
                msg = msg[:-1]
                msg = msg.split(" ")
                msg = msg[1:]
                msg = [float(msg[0]), float(msg[1])]
                cut_place.append(msg)

            elif msg[0] == 'f':
                msg = msg[:-1]
                msg = msg.split(" ")
                msg = [int(msg[1].split('/')[0]),
                       int(msg[2].split('/')[0]),
                       int(msg[3].split('/')[0]),
                       ]
                restore_way.append(msg)

    # 拼图准备
    temp = ([], [])
    for num in blit_place[1:]:
        temp[0].append(num[0])
        temp[1].append(num[1])

    X = (max(temp[0]) - min(temp[0]))
    Y = (max(temp[1]) - min(temp[1]))

    del temp

    # 背景准备

    bg = PIL.Image.new('RGBA', (X, Y), (255, 255, 255, 0))

    # 图片加载
    img = PIL.Image.open(pic_path, 'r')

    width = img.width
    height = img.height

    # 坐标镜像处理

    for num in range(len(blit_place) - 1):
        blit_place[num + 1][0] = -blit_place[num + 1][0]
        blit_place[num + 1][1] = Y - blit_place[num + 1][1]
        cut_place[num + 1][0] = cut_place[num + 1][0]
        cut_place[num + 1][1] = 1 - cut_place[num + 1][1]
    pos = [[], []]
    for num in blit_place[1:]:
        pos[0].append(num[0])
        pos[1].append(num[1])

    move_x = min(pos[0])
    move_y = min(pos[1])

    # 切割模块
    for index in restore_way:
        # 索引，拆分
        print_p = [blit_place[index[0]], blit_place[index[1]], blit_place[index[2]]]
        cut_p = [cut_place[index[0]], cut_place[index[1]], cut_place[index[2]]]

        print_area = [min(print_p[0][0], print_p[1][0], print_p[2][0]) - move_x,
                      min(print_p[0][1], print_p[1][1], print_p[2][1]) - move_y]

        cut_x = re_int(min(cut_p[0][0], cut_p[1][0], cut_p[2][0]) * width)
        cut_y = re_int(min((cut_p[0][1], cut_p[1][1], cut_p[2][1])) * height)

        end_x = re_int(
            (max(cut_p[0][0], cut_p[1][0], cut_p[2][0])) * width)
        end_y = re_int(
            (max(cut_p[0][1], cut_p[1][1], cut_p[2][1])) * height)

        cut_size = (cut_x, cut_y, end_x, end_y)

        cut = img.crop(cut_size)

        printer.append([print_area, cut])

    # 开始拼图
    num = 0
    for index in printer:
        bg.paste(index[1], index[0])
        num += 1

    return bg


def restore_tool(ship_name, names, mesh_in_path, pic_in_path, save_area):
    """拼图用的函数
    """

    pic = az_paint_restore(mesh_in_path[ship_name], pic_in_path[ship_name])

    try:
        names[ship_name]
    except KeyError:
        name = ship_name
    else:
        name = names[ship_name]
    pic.save("%s\\%s.png" % (save_area, name))


def restore_tool_one(mesh_path, pic_path, save_as, ):
    """拼图用的函数"""

    pic = az_paint_restore(mesh_path=mesh_path, pic_path=pic_path)

    assert isinstance(save_as, str)
    pic.save(save_as)


def restore_tool_no_save(mesh_path, pic_path, size: tuple):
    """拼图用的函数"""
    pic = az_paint_restore(mesh_path, pic_path)
    bg = PIL.Image.new("RGBA", size, (255, 255, 255, 0))

    scale = min(bg.size[0] / pic.size[0], bg.size[1] / pic.size[1])
    size = (round(pic.size[0] * scale), round(pic.size[1] * scale))

    pic = pic.resize(size, PIL.Image.ANTIALIAS)
    x = round(bg.size[0] / 2 - pic.size[0] / 2)
    y = round(bg.size[1] / 2 - pic.size[1] / 2)
    bg.paste(pic, (x, y, x + pic.size[0], y + pic.size[1]))
    return bg


def pic_transform(path, size):
    pic = PIL.Image.open(path)
    bg = PIL.Image.new("RGBA", size, (255, 255, 255, 0))

    scale = min(bg.size[0] / pic.size[0], bg.size[1] / pic.size[1])
    size = (round(pic.size[0] * scale), round(pic.size[1] * scale))

    pic = pic.resize(size, PIL.Image.ANTIALIAS)
    x = round(bg.size[0] / 2 - pic.size[0] / 2)
    y = round(bg.size[1] / 2 - pic.size[1] / 2)
    bg.paste(pic, (x, y, x + pic.size[0], y + pic.size[1]))
    return bg


def body_enter(path: str):
    """

    :param path: address of pic
    :return: PIL.Image type
    """
    return PIL.Image.open(path, 'r')


def cuter(pic: PIL.Image, xy, size, rotate):

    pic = pic.crop((xy[0], xy[1], xy[0] + size[0], xy[1] + size[1]))

    if rotate:
        pic = pic.rotate(-90, PIL.Image.BICUBIC, 1)

    return pic
