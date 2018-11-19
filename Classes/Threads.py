import os
import re
import shutil
import threading
import time

import wx

from Classes import noname
from Functions import function


class RestoreThread(threading.Thread):

    def __init__(self, id_thread, name, list_pic, form, name_dic, mesh_list_path_dir,
                 tex_list_path_dir, save_path,
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
                    text = name
                else:
                    text = self.names[name]
                self.format.m_staticText_now.SetLabel("当前：%s" % text)
                choice = self.format.m_listBox_log.Append("开始第%d个！为%s 类型-直接还原" % (self.index, text))
                self.format.m_listBox_log.SetSelection(choice)
                if self.setting["export_with_cn"]:
                    names = self.names
                else:
                    names = {}
                if self.setting['div_use'] == 0:
                    if self.setting["div_type"] == 1:
                        key_use = name.split("_")[0]
                        dir_name = self.names[key_use]
                        save_path = f"{self.save_path}\\{dir_name}"
                        os.makedirs(save_path, exist_ok=True)

                    elif self.setting["div_type"] == 2:
                        pattern_skin = re.compile(r'^[a-zA-Z0-9_]+_\d$')
                        pattern_power = re.compile(r'^[a-zA-Z0-9_]+_[gG]$')
                        pattern_marry = re.compile(r'^[a-zA-Z0-9_]+_[hH]$')
                        pattern_self = re.compile(r'^[a-zA-Z0-9_]+$')
                        if pattern_skin.match(name) is not None:

                            save_path = f"{self.save_path}\\皮肤"

                        elif pattern_marry.match(name) is not None:
                            save_path = f"{self.save_path}\\婚纱"

                        elif pattern_power.match(name) is not None:
                            save_path = f"{self.save_path}\\改造"

                        elif pattern_self.match(name) is not None:
                            save_path = f"{self.save_path}\\原皮"
                        else:
                            save_path = f"{self.save_path}\\其他"

                    else:
                        save_path = self.save_path

                elif self.setting['div_use'] == 1:
                    list_work = self.setting['divide_list']
                    paths = filter(lambda x: re.match(x['pattern'], name), list_work[1:])
                    paths = list(map(lambda x: f"{self.save_path}\\{x['dir']}", paths))

                    if not paths:
                        save_path = f"{self.save_path}\\其他"
                    else:
                        save_path = paths[0]

                else:
                    save_path = self.save_path

                os.makedirs(save_path, exist_ok=True)

                time_1 = time.time()
                function.restore_tool(name, names, self.mesh_list_path_dir, self.tex_list_path_dir, save_path)
                time_1 = time.time() - time_1
                self.format.m_listBox_log.Append("      tex文件：%s" % self.tex_list_path_dir[name])
                self.format.m_listBox_log.Append("      mesh文件：%s" % self.mesh_list_path_dir[name])
                self.format.m_listBox_log.Append("      保存位置：%s" % save_path + "\\" + text + '.png')

                self.format.m_listBox_log.Append("完成%s！用时：%.2fs" % (text, time_1))
                choice = self.format.m_listBox_log.Append("")
                self.format.m_listBox_log.SetSelection(choice)

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

        self.format.m_gauge_all.SetValue(100)

        if self.full["open_dir"]:
            os.system(r"start %s" % self.save_path)

        if self.full['finish_exit']:
            self.format.exit(True)

    def stop_(self, stop: bool):
        self.stop = stop

    def add_save_path(self, save_path: str):
        self.save_path = save_path

    def update_list(self, restore_list, unable_restore_list):
        self.list = restore_list
        self.unable_restore_list = unable_restore_list


class QuickRestore(threading.Thread):

    def __init__(self, index, list_tex, list_mesh=None, father: noname.MyFrame1 = None, work_path='', full=None,
                 back=2):
        threading.Thread.__init__(self)

        self.tex = list_tex[index]
        if list_mesh is None:
            self.no_restore = True
        else:
            self.no_restore = False
            self.mesh = list_mesh[index]
        self.father = father

        self.path = work_path
        self.full = full

        self.back = back

    def run(self):
        size = tuple(self.father.m_bitmap_show.GetSize())
        if not self.no_restore:
            pic = function.restore_tool_no_save(self.mesh, self.tex, size)

        else:
            pic = function.pic_transform(self.tex, size)

        pic.save("%s\\temp.png" % self.path)
        temp = wx.Image('%s\\temp.png' % self.path, wx.BITMAP_TYPE_PNG)

        temp = temp.ConvertToBitmap()
        self.father.m_bitmap_show.ClearBackground()
        self.father.m_bitmap_show.SetBitmap(temp)

        self.father.m_notebook_info.SetSelection(2)

        # time.sleep(3)
        # if
        # self.father.m_notebook_info.SetSelection(self.back)
        if self.full["auto_open"] and False:
            os.system(r'start ' + "%s\\temp.png" % self.path)


class BackInfo(threading.Thread):
    def __init__(self, az, ):
        super(BackInfo, self).__init__()
        self.father = az

    def run(self):
        self.father.update_names()


class CompareThread(threading.Thread):
    def __init__(self, father):
        super().__init__()
        self.father = father

    def compare(self):
        num = 0
        for name in self.father.old_fold_list[0]:
            name_old = name
            name = name[len(self.father.old_fold) + 1:]
            name = "%s\\%s" % (self.father.new_fold, name)

            if name not in self.father.new_fold_list[0]:
                num += 1
                if name not in self.father._new_add:
                    self.father._new_add.append(name_old)
                    self.father._new_add_show.append("%d） %s" % (num, name_old))
        self.father.frame.m_listBox_deffer.Clear()
        self.father.frame.m_listBox_deffer.Set(self.father._new_add_show)

    def run(self):
        self.compare()


class EncryptTread(threading.Thread):
    def __init__(self, list_pic, type_use, dic_pic, save_path, frame: noname.MyDialog_Setting):
        super(EncryptTread, self).__init__()

        self.list_pic = list_pic
        self.type = type_use

        self.dic_list = dic_pic
        self.save = save_path
        self.frame = frame

    def run(self):
        num = 1
        self.frame.m_gauge_works.SetValue(0)
        for val in self.list_pic:
            if self.type == 0:
                function.encrypt_basic(self.dic_list[val]).save(os.path.join(self.save, val + ".png"))
            if self.type == 1:
                function.encrypt_easy(self.dic_list[val]).save(os.path.join(self.save, val + ".png"))
            if self.type == 2:
                function.encrypt_differ(self.dic_list[val]).save(os.path.join(self.save, val + ".png"))

            num += 1

            self.frame.m_gauge_works.SetValue(round(100 * (num / len(self.list_pic))))

        self.frame.m_button_star.Enable(True)
        self.frame.m_gauge_works.SetValue(100)


class CryptTread(EncryptTread):
    def __init__(self, list_pic, type_use, dic_pic, save_path, frame: noname.MyDialog_Setting):
        super(CryptTread, self).__init__(list_pic, type_use, dic_pic, save_path, frame)

    def run(self):
        num = 1
        self.frame.m_gauge_work_in.SetValue(0)
        for val in self.list_pic:
            if self.type == 0:
                function.crypt_basic(self.dic_list[val]).save(os.path.join(self.save, val + ".png"))
            if self.type == 1:
                function.crypt_easy(self.dic_list[val]).save(os.path.join(self.save, val + ".png"))
            if self.type == 2:
                function.crypt_differ(self.dic_list[val]).save(os.path.join(self.save, val + ".png"))

            num += 1

            self.frame.m_gauge_work_in.SetValue(round(100 * (num / len(self.list_pic))))

        self.frame.m_button_star_in.Enable(True)
        self.frame.m_gauge_work_in.SetValue(100)
