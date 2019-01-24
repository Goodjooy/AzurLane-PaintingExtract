import os
import re
import shutil
import threading
import time

import wx

from Classes import noname, InfoClasses
from Functions import function


class RestoreThread(threading.Thread):

    def __init__(self, id_thread, name, able: InfoClasses.PerWorkList, unable: InfoClasses.PerWorkList, parent, setting,
                 full, names, save_path):
        threading.Thread.__init__(self)
        self.full = full
        self.names = names
        self.setting = setting
        self.format = parent

        self.able = able
        self.unable = unable

        self.threadID = id_thread

        self.name = name

        self.index = 0

        self.stop = False

        self.save_path = save_path

    def run(self):

        for self.index in range(len(self.able)):

            if self.stop:
                break
            if self.index < len(self.able) and not self.stop:
                now_info: InfoClasses.PerWork = self.able[self.index]
                self.format.m_staticText_now.SetLabel("当前：%s" % now_info.name_cn)
                choice = self.format.m_listBox_log.Append(
                    "开始第%d个！为：%s 类型-直接还原" % (self.index + 1, now_info.name_cn))
                self.format.m_listBox_log.SetSelection(choice)

                now_info.set_ex_as_cn = self.setting["export_with_cn"]

                if self.setting['div_use'] == 0:
                    if self.setting["div_type"] == 1:

                        save_path = f"{self.save_path}\\{now_info.name_cn}"
                        os.makedirs(save_path, exist_ok=True)

                    elif self.setting["div_type"] == 2:
                        pattern_skin = re.compile(r'^[a-zA-Z0-9_]+_\d$')
                        pattern_power = re.compile(r'^[a-zA-Z0-9_]+_[gG]$')
                        pattern_marry = re.compile(r'^[a-zA-Z0-9_]+_[hH]$')
                        pattern_self = re.compile(r'^[a-zA-Z0-9_]+$')
                        if pattern_skin.match(now_info.name) is not None:

                            save_path = f"{self.save_path}\\皮肤"

                        elif pattern_marry.match(now_info.name) is not None:
                            save_path = f"{self.save_path}\\婚纱"

                        elif pattern_power.match(now_info.name) is not None:
                            save_path = f"{self.save_path}\\改造"

                        elif pattern_self.match(now_info.name) is not None:
                            save_path = f"{self.save_path}\\原皮"
                        else:
                            save_path = f"{self.save_path}\\其他"

                    else:
                        save_path = self.save_path

                elif self.setting['div_use'] == 1:
                    list_work = self.setting['divide_list']
                    paths = filter(lambda x: re.match(x['pattern'], now_info.name), list_work[1:])
                    paths = list(map(lambda x: f"{self.save_path}\\{x['dir']}", paths))

                    if not paths:
                        save_path = f"{self.save_path}\\其他"
                    else:
                        save_path = paths[0]

                else:
                    save_path = self.save_path

                os.makedirs(save_path, exist_ok=True)

                now_info.add_save(save_path)

                time_1 = time.time()
                is_good, info = function.restore_tool(now_info)
                time_1 = time.time() - time_1
                self.format.m_listBox_log.Append("      tex文件：%s" % now_info.tex_path)
                self.format.m_listBox_log.Append("      mesh文件：%s" % now_info.mesh_path)
                self.format.m_listBox_log.Append("      保存位置：%s" % now_info.save_path)
                if not is_good:
                    self.format.append_error(info)

                self.format.m_listBox_log.Append("%s，用时：%.2fs" % (info, time_1))

                choice = self.format.m_listBox_log.Append("")
                self.format.m_listBox_log.SetSelection(choice)

                val_percent = str(round(100 * (self.index / len(self.able)), 2))
                val = function.re_int(100 * (self.index / len(self.able)))
                self.format.m_staticText_all.SetLabel("总进度：%s %%" % val_percent)
                self.format.m_gauge_all.SetValue(val)
                self.index += 1

        self.format.m_listBox_log.Append("直接还原部分完成")
        choice = self.format.m_listBox_log.Append("")

        self.format.m_listBox_log.SetSelection(choice)

        if self.setting["export_type"] == 1:

            self.format.m_listBox_log.Append("仅拷贝开始")
            choice = self.format.m_listBox_log.Append("")

            self.format.m_listBox_log.SetSelection(choice)
            num = 0
            os.makedirs(f'{self.save_path}\\拷贝', exist_ok=True)

            for name in self.unable:
                name: InfoClasses.PerWork = name
                name.add_save(f'{self.save_path}\\拷贝')
                num += 1
                shutil.copyfile(name.tex_path, name.save_path)

                self.format.m_gauge_all.SetValue(function.re_int(100 * (num / len(self.unable))))

        self.format.m_staticText_all.SetLabel("总进度：%s %%" % '100')
        self.format.start = False

        self.format.m_gauge_all.SetValue(100)

        if self.full["open_dir"]:
            os.system(r'start "%s"' % self.save_path)

        if self.full['finish_exit']:
            self.format.exit(True)

        if self.format.any_error():
            self.format.m_notebook_info.SetSelection(2)






    def stop_(self, stop: bool):
        self.stop = stop

    def add_save_path(self, save_path: str):
        self.save_path = save_path

    def update_value(self, able, unable):
        self.able = able
        self.unable = unable


class QuickRestore(threading.Thread):

    def __init__(self, info: InfoClasses.PerWork, father: noname.MyFrame1 = None, work_path='', full=None,
                 back=2):
        threading.Thread.__init__(self)

        self.info = info
        self.father = father

        self.path = work_path
        self.full = full

        self.back = back

    def run(self):
        try:
            size = tuple(self.father.m_bitmap_show.GetSize())
            if self.info.is_able_work:
                pic = function.restore_tool_no_save(self.info.mesh_path, self.info.tex_path, size)
            elif self.info.lay_in != '':
                pic = function.pic_transform(self.info.lay_in, size)
            else:
                pic = function.pic_transform(self.info.tex_path, size)

            pic.save("%s\\temp.png" % self.path)
            temp = wx.Image('%s\\temp.png' % self.path, wx.BITMAP_TYPE_PNG)

            temp = temp.ConvertToBitmap()
            self.father.m_bitmap_show.ClearBackground()
            self.father.m_bitmap_show.SetBitmap(temp)

            self.father.m_notebook_info.SetSelection(1)

            # time.sleep(3)
            # if
            # self.father.m_notebook_info.SetSelection(self.back)
            if self.full["auto_open"] and False:
                os.system(r'start ' + "\"%s\\temp.png\"" % self.path)

        except RuntimeError as info:
            self.father.append_error(info)

        if self.father.any_error():
            self.father.m_notebook_info.SetSelection(2)


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
