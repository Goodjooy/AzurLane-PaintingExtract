import re
import PIL.Image
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

def ex_port(mesh_path: str, tex_path: str):
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

    x_poses, y_poses = zip(*draw_pic)
    print(list(x_poses))
    print(list(y_poses))
    print(len(list(x_poses)))
    print(len(list(y_poses)))

    x_pic = (max(x_poses))
    y_pic = (max(y_poses))
    print(x_pic)
    print(y_pic)

ex_port('1.obj','1.png')


