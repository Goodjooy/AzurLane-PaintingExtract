import json
import os
import numpy as np
import PIL.Image


def change_work():
    setting = {"azur_lane": {},
               "girl_line": {},
               "full": {}}
    setting["azur_lane"]["div_type"] = 0
    setting["azur_lane"]["export_type"] = 0
    setting["azur_lane"]["div_use"] = 0
    setting["azur_lane"]["tex_limit"] = r'^\S\.[pP][Nn][Gg]$'
    setting["azur_lane"]["mesh_limit"] = r'^\S-mesh\.[oO][Bb][jJ]$'
    setting["azur_lane"]["divide_list"] = [{'name': 'else', 'dir': '其他', 'pattern': r'^.+$'}]

    setting["azur_lane"]["export_with_cn"] = True
    setting["azur_lane"]["new_dir"] = True

    setting["girl_line"]["div_type"] = 0
    setting["girl_line"]["export_type"] = 0
    setting["girl_line"]["check_before_start"] = True
    setting["girl_line"]["new_dir"] = True

    setting["full"]["open_dir"] = True
    setting["full"]["skip_had"] = True
    setting["full"]["auto_open"] = True
    setting["full"]["finish_exit"] = False

    with open("..\\files\\setting.json", 'w')as i:
        json.dump(setting, i)


# change_work()


def emm_work():
    default = {"azur_lane": {},
               "girl_line": {},
               "lock": False}

    default["azur_lane"]['default_tex_dir'] = os.getcwd()
    default["azur_lane"]['default_mesh_dir'] = os.getcwd()

    default["girl_line"]['default_rgb_dir'] = os.getcwd()
    default["girl_line"]['default_alpha_dir'] = os.getcwd()

    default['export'] = os.getcwd()

    with open("..\\files\\default.json", 'w')as file:
        json.dump(default, file)


# emm_work()
def encrypt_easy(path: str):
    path = PIL.Image.open(path, 'r')
    array_img = np.array(path)

    array_r = array_img[:, :, 0]
    array_g = array_img[:, :, 1]
    array_b = array_img[:, :, 2]
    array_a = array_img[:, :, 3]

    array_img[:, :, 0] = 255 - array_r
    array_img[:, :, 1] = 255 - array_g
    array_img[:, :, 2] = 255 - array_b
    array_img[:, :, 3] = 255 - array_a

    r_pic = PIL.Image.fromarray(np.uint8(array_img))

    r_pic.show()
    r_pic.save('5.png')
    return r_pic


# encrypt_easy('4.png')
def crypt_easy(path: str):
    path = PIL.Image.open(path, 'r')
    path_pic = PIL.Image.new('RGBA', path.size, (255, 255, 255, 0))
    path_pic.paste(path, (0, 0, path_pic.size[0], path_pic.size[1]))
    array_img = np.array(path_pic)

    array_r = 255 - array_img[:, :, 0]
    array_g = 255 - array_img[:, :, 1]
    array_b = 255 - array_img[:, :, 2]
    array_a = array_img[:, :, 3]

    print(array_a[50])
    print()
    print(array_g[50])
    print()
    print(array_r[50])
    array_img[:, :, 1] = array_r
    array_img[:, :, 3] = array_g
    array_img[:, :, 0] = array_b
    array_img[:, :, 2] = array_a  # array_b

    r_pic = PIL.Image.fromarray(np.uint8(array_img))
    r_pic.show()
    r_pic.save('5.png')
    return r_pic


crypt_easy('22.png')
