import PIL.Image
import numpy
import os

info_item = []
scale = 0.5


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
        re = all_file(dir_name + "\\" + file)
        had.extend(re)
        out_list.extend(re)

    return out_list


def all_file_path(dir_name):
    had = []
    list_keep = os.listdir(dir_name)
    diction = {}
    dir_list = []
    file_list = []
    for file in list_keep:
        if not isfile(dir_name + "\\" + file) and not (file in had):
            dir_list.append(file)
        elif file.split(' ')[0] != "UISprite":
            file_list.append(file)
    for file in dir_list:
        re = all_file_path(dir_name + "\\" + file)
        had.extend(re[0])
        file_list.extend(re[0])
        for keys in re[1]:
            diction[keys] = re[1][keys]
    for index in range(len(file_list)):
        if not file_list[index] in had:
            diction[file_list[index]] = dir_name + "\\" + file_list[index]
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
    if scale >= 1:
        return num
    else:
        int_num = int(num)
        float_num = num - int_num

        if float_num >= scale:
            return int_num + 1
        if float_num < scale:
            return int_num


def restore_tool(ship_name, names, mesh_in_path, pic_in_path, save_area):
    """拼图用的函数"""

    # 用于存储相应参数
    blit_place = [None]
    cut_place = [None]
    restore_way = []
    printer = []

    # 文件信息读取，分类
    with open(mesh_in_path[ship_name], 'r')as info:
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
    img = PIL.Image.open(pic_in_path[ship_name], 'r')

    width = img.width
    height = img.height

    # 坐标镜像处理

    for num in range(len(blit_place) - 1):
        blit_place[num + 1][0] = -blit_place[num + 1][0]
        blit_place[num + 1][1] = Y - blit_place[num + 1][1]
        cut_place[num + 1][0] = cut_place[num + 1][0]
        cut_place[num + 1][1] = 1 - cut_place[num + 1][1]
    Pos = [[], []]
    for num in blit_place[1:]:
        Pos[0].append(num[0])
        Pos[1].append(num[1])

    move_x = min(Pos[0])
    move_y = min(Pos[1])
    info_item.append("\t完成坐标计算")
    # 切割模块
    for index in restore_way:
        # 索引，拆分
        blit_p = [blit_place[index[0]], blit_place[index[1]], blit_place[index[2]]]
        cut_p = [cut_place[index[0]], cut_place[index[1]], cut_place[index[2]]]

        blit_area = [min(blit_p[0][0], blit_p[1][0], blit_p[2][0]) - move_x,
                     min(blit_p[0][1], blit_p[1][1], blit_p[2][1]) - move_y]

        cut_x = re_int(min(cut_p[0][0], cut_p[1][0], cut_p[2][0]) * width)
        cut_y = re_int(min((cut_p[0][1], cut_p[1][1], cut_p[2][1])) * height)

        end_x = re_int(
            (max(cut_p[0][0], cut_p[1][0], cut_p[2][0])) * width)
        end_y = re_int(
            (max(cut_p[0][1], cut_p[1][1], cut_p[2][1])) * height)

        cut_size = (cut_x, cut_y, end_x, end_y)

        cut = img.crop(cut_size)

        printer.append([blit_area, cut])
    info_item.append("\t完成图片切割")

    # 开始拼图

    for index in printer:
        bg.paste(index[1], index[0])

    info_item.append("\t完成拼图")

    pic = bg

    try:
        names[ship_name]
    except KeyError:
        name = ship_name
    else:
        name = names[ship_name]
    pic.save("%s\\%s.png" % (save_area, name))


def restore_tool_one(mesh_path, pic_path, save_as, value, ):
    """拼图用的函数"""

    # 用于存储相应参数
    blit_place = [None]
    cut_place = [None]
    restore_way = []
    printer = []

    # 文件信息读取，分类
    with open(mesh_path, 'r')as info:
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
    info_item.append("完成坐标计算")
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
    info_item.append("完成图片切割")
    value.SetValue(25)
    # 开始拼图
    num = 0
    for index in printer:
        bg.paste(index[1], index[0])
        num += 1
        finished = re_int(75 * (num / len(printer)))
        value.SetValue(finished)
    info_item.append("完成拼图")
    pic = bg

    assert isinstance(save_as, str)
    pic.save(save_as)
    value.SetValue(100)


def restore_tool_no_save(mesh_path, pic_path):
    """拼图用的函数"""

    # 用于存储相应参数
    blit_place = [None]
    cut_place = [None]
    restore_way = []
    printer = []

    # 文件信息读取，分类
    with open(mesh_path, 'r')as info:
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
    info_item.append("完成坐标计算")
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

    pic = bg

    return pic


def girl_font_line_restore(pic_path, pic_alpha, save_path):
    pic = PIL.Image.open(pic_path, 'r')
    pic_a = PIL.Image.open(pic_alpha, 'r')

    out = PIL.Image.new("RGBA", pic.size, (255, 255, 255, 0))
    alpha = PIL.Image.new("RGBA", pic.size, 0)

    pic_a = pic_a.resize(pic.size, PIL.Image.ANTIALIAS)
    alpha.paste(pic_a, (0, 0, pic.size[0], pic.size[1]))

    out.paste(pic, (0, 0, pic.size[0], pic.size[1]))

    alpha_list = numpy.asarray(alpha)
    alpha_list = alpha_list[:, :, -1]
    temp = numpy.asarray(out)
    temp = temp.copy()
    temp[:, :, -1] = alpha_list

    out = temp.fromarray(numpy.uint8(temp))

    pic_path = pic_path.split("\\")[-1]
    pic_path = pic_path[4:]
    pic_path = pic_path.split('.')[0]

    out.save("%s\\%s.png" % (save_path, pic_path))
