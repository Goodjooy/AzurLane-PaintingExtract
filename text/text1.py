import json
import os


def change_work():
    setting = {"azur_lane": {},
               "girl_line": {},
               "full": {}}
    setting["azur_lane"]["div_type"] = 0
    setting["azur_lane"]["export_type"] = 0
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


emm_work()
