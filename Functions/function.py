import re

import PIL.Image
import numpy as np
import os
import functools

from Classes import InfoClasses
from Functions import tools

functools.partial(os.makedirs, exist_ok=True)


def find(s, l):
    return tools.find(s, l)


def all_file(dir_name):
    return tools.all_file(dir_name)


def all_file_path(dir_name):
    return tools.all_file_path(dir_name)


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


def cut_pic_builder(size):
    """

    :param size: the input img size(wide,high)
    :return: a callable func
    """

    def cut_pic(info):
        a = [round(float(info[1]) * size[0]), round((1 - float(info[2])) * size[1])]

        return a

    return cut_pic


def draw(pic, pos):
    pic.paste(pos[0], pos[1])
    return pic


def division_builder(val1, val2, pic):
    def division(val):
        print_p = [val1[val[0] - 1], val1[val[1] - 1], val1[val[2] - 1]]
        cut_p = [val2[val[0] - 1], val2[val[1] - 1], val2[val[2] - 1]]

        print_area = [min(print_p[0][0], print_p[1][0], print_p[2][0]),
                      min(print_p[0][1], print_p[1][1], print_p[2][1])]

        cut_x = round(min(cut_p[0][0], cut_p[1][0], cut_p[2][0]))
        cut_y = round(min((cut_p[0][1], cut_p[1][1], cut_p[2][1])))

        end_x = round(
            (max(cut_p[0][0], cut_p[1][0], cut_p[2][0])))
        end_y = round(
            (max(cut_p[0][1], cut_p[1][1], cut_p[2][1])))

        cut_size = (cut_x, cut_y, end_x, end_y)

        cut = pic.crop(cut_size)
        return cut, print_area

    return division


def az_paint_restore(mesh_path: str, tex_path: str):
    """
    a higher func version for extract AzurLane painting
    :param mesh_path: mesh_file address,str
    :param tex_path: texture file address
    :return: PIL.Image -> the final pic
    """
    img = PIL.Image.open(tex_path)

    size = img.size

    tex_cuter = cut_pic_builder(size)

    with open(mesh_path, 'r', encoding='utf-8')as file:
        files_line = file.readlines()

    draw_pic = filter(lambda x: re.match(r'^v\s-*\d+\s-*\d+\s-*\d+\n$', x), files_line)
    tex_pos = filter(lambda x: re.match(r'^vt\s0\.\d+\s0\.\d+\n$', x), files_line)
    print_pos = filter(lambda x: re.match(r'^f\s\d+/\d+/\d+\s\d+/\d+/\d+\s\d+/\d+/\d+\n$', x), files_line)

    draw_pic = map(lambda x: re.split(r'\D+', x), draw_pic)
    tex_pos = map(lambda x: re.split(r'[^0-9.]+', x), tex_pos)
    print_pos = map(lambda x: re.split(r'\D+', x), print_pos)

    draw_pic = (map(lambda x: [int(x[1]), int(x[2])], draw_pic))
    tex_pos = (map(tex_cuter, tex_pos))
    print_pos = (map(lambda x: [int(x[1]), int(x[4]), int(x[7])], print_pos))
    draw_pic = list(draw_pic)
    pos = draw_pic.copy()
    x_poses, y_poses = zip(*pos)

    x_pic = (max(x_poses))
    y_pic = (max(y_poses))

    pic = PIL.Image.new("RGBA", (x_pic, y_pic), (255, 255, 255, 0))

    draw_pic = (map(lambda x: [(x[0]), (y_pic - x[1])], draw_pic))

    division = division_builder(list(draw_pic), list(tex_pos), img)

    restore = (map(division, print_pos))

    pic_out = functools.reduce(draw, restore, pic)

    return pic_out


def restore_tool(now_info: InfoClasses.PerInfo):
    """拼图用的函数
    """
    try:
        pic = az_paint_restore(now_info.mesh_path, now_info.tex_path)

        pic.save(now_info.save_path)
    except RuntimeError as info:
        return False, info

    else:
        return True, "成功还原：%s" % now_info.name_cn


def restore_tool_one(mesh_path, pic_path, save_as, ):
    """拼图用的函数"""

    pic = az_paint_restore(mesh_path=mesh_path, tex_path=pic_path)

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
    if rotate:

        pic = pic.crop((xy[0], xy[1], xy[0] + size[1], xy[1] + size[0]))
        pic = pic.rotate(-90, expand=True)
    else:
        pic = pic.crop((xy[0], xy[1], xy[0] + size[0], xy[1] + size[1]))

    return pic


def encrypt_easy(path: str):
    path = PIL.Image.open(path, 'r')
    path_pic = PIL.Image.new('RGBA', path.size, (255, 255, 255, 0))
    path_pic.paste(path, (0, 0, path_pic.size[0], path_pic.size[1]))
    array_img = np.array(path_pic)

    array_r = array_img[:, :, 3]
    array_g = array_img[:, :, 2]
    array_b = array_img[:, :, 1]
    array_a = array_img[:, :, 0]

    array_img[:, :, 0] = 255 - array_r
    array_img[:, :, 1] = 255 - array_g
    array_img[:, :, 2] = 255 - array_b
    array_img[:, :, 3] = 255 - array_a

    r_pic = PIL.Image.fromarray(np.uint8(array_img))

    return r_pic


def encrypt_differ(path: str):
    path = PIL.Image.open(path, 'r')
    path_pic = PIL.Image.new('RGBA', path.size, (255, 255, 255, 0))
    path_pic.paste(path, (0, 0, path_pic.size[0], path_pic.size[1]))
    array_img = np.array(path_pic)

    array_r = array_img[:, :, 0]
    array_g = array_img[:, :, 1]
    array_b = array_img[:, :, 2]
    array_a = array_img[:, :, 3]

    r_pic = PIL.Image.fromarray(np.uint8(array_r))
    g_pic = PIL.Image.fromarray(np.uint8(array_g))
    b_pic = PIL.Image.fromarray(np.uint8(array_b))
    a_pic = PIL.Image.fromarray(np.uint8(array_a))

    r_pic = r_pic.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    g_pic = g_pic.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    b_pic = b_pic.rotate(180)
    a_pic = a_pic.rotate(180).transpose(PIL.Image.FLIP_TOP_BOTTOM)

    array_r = np.array(r_pic)
    array_g = np.array(g_pic)
    array_b = np.array(b_pic)
    array_a = np.array(a_pic)

    array_img[:, :, 0] = 255 - array_b
    array_img[:, :, 1] = 255 - array_r
    array_img[:, :, 2] = 255 - array_a
    array_img[:, :, 3] = array_g

    r_pic = PIL.Image.fromarray(np.uint8(array_img))
    return r_pic


def encrypt_basic(path: str):
    path = PIL.Image.open(path, 'r')
    path_pic = PIL.Image.new('RGBA', path.size, (255, 255, 255, 0))
    path_pic.paste(path, (0, 0, path.size[0], path.size[1]))
    array_img = np.array(path_pic)

    array_r = array_img[:, :, 0]
    array_g = array_img[:, :, 1]
    array_b = array_img[:, :, 2]
    array_a = array_img[:, :, 3]

    array_img[:, :, 0] = 255 - array_r
    array_img[:, :, 1] = 255 - array_g
    array_img[:, :, 2] = 255 - array_b
    array_img[:, :, 3] = 255 - array_a

    r_pic = PIL.Image.fromarray(np.uint8(array_img))

    return r_pic


def crypt_basic(path: str):
    return encrypt_basic(path)


def crypt_easy(path: str):
    path = PIL.Image.open(path, 'r')
    path_pic = PIL.Image.new('RGBA', path.size, (255, 255, 255, 0))
    path_pic.paste(path, (0, 0, path_pic.size[0], path_pic.size[1]))
    array_img = np.array(path_pic)

    array_r = 255 - array_img[:, :, 0]
    array_g = 255 - array_img[:, :, 1]
    array_b = 255 - array_img[:, :, 2]
    array_a = 255 - array_img[:, :, 3]

    array_img[:, :, 0] = array_r
    array_img[:, :, 1] = array_g
    array_img[:, :, 2] = array_b
    array_img[:, :, 3] = array_a

    r_pic = PIL.Image.fromarray(np.uint8(array_img))

    return r_pic


def crypt_differ(path: str):
    path = PIL.Image.open(path, 'r')
    path_pic = PIL.Image.new('RGBA', path.size, (255, 255, 255, 0))
    path_pic.paste(path, (0, 0, path_pic.size[0], path_pic.size[1]))
    array_img = np.array(path_pic)

    array_r = array_img[:, :, 0]
    array_g = array_img[:, :, 1]
    array_b = array_img[:, :, 2]
    array_a = array_img[:, :, 3]

    g_pic = PIL.Image.fromarray(np.uint8(array_r))
    a_pic = PIL.Image.fromarray(np.uint8(array_g))
    r_pic = PIL.Image.fromarray(np.uint8(array_b))
    b_pic = PIL.Image.fromarray(np.uint8(array_a))

    g_pic = g_pic.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    a_pic = a_pic.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    r_pic = r_pic.rotate(-180)
    b_pic = b_pic.rotate(-180).transpose(PIL.Image.FLIP_TOP_BOTTOM)

    array_r = np.array(r_pic)
    array_g = np.array(g_pic)
    array_b = np.array(b_pic)
    array_a = np.array(a_pic)

    array_img[:, :, 0] = 255 - array_r
    array_img[:, :, 1] = 255 - array_g
    array_img[:, :, 2] = 255 - array_b
    array_img[:, :, 3] = array_a

    r_pic = PIL.Image.fromarray(np.uint8(array_img))
    return r_pic
