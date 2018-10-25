import os
import shutil
import threading

from Functions import function, tools


class RestoreThread(threading.Thread):

    def __init__(self, id_thread, name, list_pic, form, name_dic, mesh_list_path_dir, tex_list_path_dir, save_path,
                 setting, unable_restore_list, full):
        threading.Thread.__init__(self)
        self.threadID = id_thread

        self.name = name

        self.index = 0

        self.list = list_pic

        self.format = form
        self.names = name_dic

        self.mesh_list_path_dir = mesh_list_path_dir
        self.tex_list_path_dir = tex_list_path_dir
        self.save_path = save_path

        self.stop = False

        self.setting = setting

        self.unable_restore_list = unable_restore_list
        self.full = full

    def run(self):
        for self.index in range(len(self.list)):
            if self.index < len(self.list) and not self.stop:
                name = self.list[self.index]
                if name not in self.names.keys():
                    text=name
                else:
                    text=self.names[name]
                self.format.m_staticText_now.SetLabel("当前：%s" % text)
                if self.setting["export_with_cn"]:
                    names = self.names
                else:
                    names = {}

                if self.setting["div_type"] == 1:
                    dir_name = self.names[name.split("_")[0]]
                    save_path = f"{self.save_path}\\{dir_name}"
                    os.makedirs(save_path, exist_ok=True)

                elif self.setting["div_type"] == 2:
                    dir_name = name.split("_")[-1]
                    try:
                        if dir_name == "22" or dir_name == "33":
                            raise ValueError
                        dir_name = int(dir_name)
                        save_path = f"{self.save_path}\\皮肤"
                        os.makedirs(save_path, exist_ok=True)
                    except ValueError:
                        if dir_name.lower() == "h":
                            save_path = f"{self.save_path}\\婚纱"
                            os.makedirs(save_path, exist_ok=True)

                        elif dir_name.lower() == "g":
                            save_path = f"{self.save_path}\\改造"
                            os.makedirs(save_path, exist_ok=True)
                        elif len(dir_name) <= 2:
                            save_path = f"{self.save_path}\\{dir_name}"
                            os.makedirs(save_path, exist_ok=True)

                        else:
                            save_path = f"{self.save_path}\\原皮"
                            os.makedirs(save_path, exist_ok=True)

                else:
                    save_path = self.save_path

                function.restore_tool(name, names, self.mesh_list_path_dir, self.tex_list_path_dir, save_path)

                val_percent = str(round(100 * (self.index / len(self.list)), 2))
                val = function.re_int(100 * (self.index / len(self.list)))
                self.format.m_staticText_all.SetLabel("总进度：%s %%" % val_percent)
                self.format.m_gauge_all.SetValue(val)
                self.index += 1

        if self.setting["export_type"] == 1:
            num = 0
            os.makedirs(f'{self.save_path}\\拷贝', exist_ok=True)

            for name in self.unable_restore_list:
                num += 1

                try:
                    shutil.copyfile(self.tex_list_path_dir[name], f'{self.save_path}\\拷贝\\{self.names[name]}.png')
                except KeyError:
                    shutil.copyfile(self.tex_list_path_dir[name], f'{self.save_path}\\拷贝\\{name}.png')

                self.format.m_gauge_all.SetValue(function.re_int(100 * (num / len(self.unable_restore_list))))

        else:
            pass

        self.format.m_staticText_all.SetLabel("总进度：%s %%" % '100')
        self.format.start = False

        if self.full["open_dir"]:
            os.system(r"start %s" % self.save_path)

        if self.full['finish_exit']:
            self.format.exit()

    def stop_(self, stop: bool):
        self.stop = stop

    def add_save_path(self, save_path: str):
        self.save_path = save_path

    def update_list(self, restore_list, unable_restore_list):
        self.list = restore_list
        self.unable_restore_list = unable_restore_list


class QuickRestore(threading.Thread):

    def __init__(self, index, list_tex, list_mesh, father, work_path, full):
        threading.Thread.__init__(self)

        self.tex = list_tex[index]
        self.mesh = list_mesh[index]
        self.father = father

        self.path = work_path
        self.full = full

    def run(self):
        pic = function.restore_tool_no_save(self.mesh, self.tex)

        pic.save("%s\\temp.png" % self.path)

        if self.full["auto_open"]:
            os.system(r'start ' + "%s\\temp.png" % self.path)


class GirlSRestore(threading.Thread):

    def __init__(self, able_list: list, rgb_list: dict, alpha_list: dict, save_path: str, is_work: bool, form,
                 setting: dict, full: dict):
        super(GirlSRestore, self).__init__()

        self.able_list = able_list
        self.rgb_list = rgb_list
        self.alpha_list = alpha_list
        self.save_path = save_path
        self.is_work = is_work

        self.form = form

        self.setting = setting
        self.full = full

    def run(self):
        length = len(self.rgb_list)
        if not self.is_work:
            pass
        else:
            i = 0
            if self.setting["check_before_start"]:
                for val in self.able_list:
                    tools.search(self.rgb_list, self.alpha_list, list(self.alpha_list.keys()), val)
                    i += 1
                    val_percent = str(round(100 * (i / len(self.able_list)), 2))
                    val = function.re_int(100 * (i / len(self.rgb_list)))
                    self.form.m_staticText_all.SetLabel("扫描进度：%s %%" % val_percent)
                    self.form.m_gauge_all.SetValue(val)
                i = 0

            for val in self.able_list:
                if self.setting["export_type"] == 1:
                    if val.split("_")[0].lower() != "pic":
                        length -= 1
                        continue
                if self.setting["div_type"] == 1:
                    if val.split("_")[0].lower() == "pic":
                        name = val.split("_")[1]
                        save_path = f"{self.save_path}\\人形\\{name}"
                        os.makedirs(save_path, exist_ok=True)

                    else:
                        save_path = f"{self.save_path}\\其他"
                        os.makedirs(save_path, exist_ok=True)

                elif self.setting["div_type"] == 1:
                    if val.split("_")[0].lower() == "pic":
                        if val.split("_")[-1].lower() == "d":
                            save_path = f"{self.save_path}\\人形\\大破"
                            os.makedirs(save_path, exist_ok=True)
                        else:
                            save_path = f"{self.save_path}\\人形\\普通"
                            os.makedirs(save_path, exist_ok=True)
                    else:
                        save_path = f"{self.save_path}\\其他"
                        os.makedirs(save_path, exist_ok=True)

                else:
                    save_path = self.save_path

                function.girl_font_line_restore(self.rgb_list[val], self.alpha_list[val], save_path)
                i += 1

                val_percent = str(round(100 * (i / length), 2))
                self.form.m_staticText_now.SetLabel("当前：%s" % val)
                val = function.re_int(100 * (i / length))
                self.form.m_staticText_all.SetLabel("总进度：%s %%" % val_percent)
                self.form.m_gauge_all.SetValue(val)

            self.form.m_staticText_all.SetLabel("总进度：%s %%" % '100')
            self.form.start = False

            if self.full["open_dir"]:
                os.system(r"start %s" % self.save_path)

    def set_value(self, rgb_list, alpha_list, save_path, able_list, setting, full):
        self.rgb_list = rgb_list
        self.alpha_list = alpha_list
        self.save_path = save_path
        self.able_list = able_list

        self.setting = setting
        self.full = full

    def set_work(self, is_work: bool):
        self.is_work = is_work
