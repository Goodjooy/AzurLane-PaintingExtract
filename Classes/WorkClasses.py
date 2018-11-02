import os

import wx

from Classes import Threads, noname
from Methub.Functions import girl_font_line_restore
from Methub.tools import all_file_path, find


class GirlsFrontLine(object):
    """a class only to the game girls front line"""

    def __init__(self, form: noname.MyFrame1, setting, default, start_path=os.getcwd()):
        self.form = form

        self.save_path = ''

        self.dialog = None
        self.start_path = start_path

        self.rgb_enter = {}
        self.alpha_enter = {}

        self.rgb_key = []
        self.alpha_key = []

        self.rgb_show = []
        self.alpha_show = []

        self.able_list = []

        self.unable_list = []
        self.unable_show = ['', "少女前线：", '']

        self.choice = None

        self.is_rgb_search = False
        self.rgb_search = []
        self.rgb_search_show = []
        self.rgb_search_result = []

        self.is_alpha_search = []
        self.alpha_search = []
        self.alpha_search_show = []
        self.alpha_search_result = []

        self.setting = setting["girl_line"]
        self.full = setting["full"]
        self.default = default['girl_line']
        self.lock = default['lock']
        self.export = default['export']

        self.work_thread = Threads.GirlSRestore(self.able_list, self.rgb_enter, self.alpha_enter, self.save_path, True,
                                                self.form, self.setting, self.full)

        self.temp = ''

    def update_setting(self, setting, default):
        self.setting = setting["girl_line"]

        self.full = setting["full"]

        self.default = default["girl_line"]

        self.lock = default['lock']

    def reset(self):
        self.work_thread = Threads.GirlSRestore(self.able_list, self.rgb_enter, self.alpha_enter, self.save_path, True,
                                                self.form, self.setting, self.full)

    def is_choice(self):
        return self.choice

    def is_able(self):
        return self.able_list != []

    def test_able(self):
        i = 0
        for val in self.alpha_enter.keys():
            if val in self.rgb_enter.keys():
                self.able_list.append(val)
                self.form.m_menuItem_all.Enable(True)
            else:
                self.unable_list.append(val)
                self.unable_show.append(f"{i}）\t {val}")
                i += 1
        self.form.m_listBox_unable.Set(self.unable_show)

    def load_rgb(self):
        if self.lock:
            address = self.default['default_rgb_dir']
        else:
            address = os.getcwd()

        self.dialog = wx.FileDialog(self.form, "打开RGB通道文件", address, 'QAQ.png', "*.png",
                                    style=wx.FD_OPEN | wx.FD_MULTIPLE)
        if self.dialog.ShowModal() == wx.ID_OK:
            self.form.m_gauge_RGB_load.SetValue(0)
            self.form.m_staticText_RGB_load.SetLabelText("开始")

            temp = self.dialog.GetFilenames()

            i = 0
            for val in temp:
                path = val
                val = val.split("\\")[-1]
                val = val.replace('.png', '')

                if val.split('_')[-1].lower() != 'alpha'.lower():
                    self.rgb_enter[val] = path
                    self.rgb_show.append("%d） %s" % (i, val))
                    self.rgb_key.append(val)
                    i += 1

                else:
                    pass

            self.form.m_gauge_RGB_load.SetValue(100)
            self.form.m_staticText_RGB_load.SetLabelText("完成")

            self.form.m_listBox_RGB.Set(self.rgb_show)

            self.test_able()

    def load_alpha(self):
        if self.lock:
            address = self.default['default_alpha_dir']
        else:
            address = os.getcwd()
        self.dialog = wx.FileDialog(self.form, "打开Alpha通道文件", address, 'QAQ.png', "*.png",
                                    style=wx.FD_OPEN | wx.FD_MULTIPLE)
        if self.dialog.ShowModal() == wx.ID_OK:
            self.form.m_gauge_alpha_load.SetValue(0)
            self.form.m_staticText_alpha_load.SetLabelText("开始")

            temp = self.dialog.GetFilenames()

            i = 0
            for val in temp:
                path = val
                val = val.split("\\")[-1]
                val = val.replace('.png', '')

                if val.split('_')[-1].lower() == 'alpha'.lower():
                    val = val.replace('_Alpha', "")
                    self.alpha_enter[val] = path
                    self.alpha_show.append("%d） %s" % (i, val))
                    self.alpha_key.append(val[:-6])
                    i += 1
                else:
                    pass

            self.form.m_gauge_alpha_load.SetValue(100)
            self.form.m_staticText_alpha_load.SetLabelText("完成")

            self.form.m_listBox_alpha.Set(self.alpha_show)

            self.test_able()

    def load_alpha_f(self):
        if self.lock:
            address = self.default['default_alpha_dir']
        else:
            address = os.getcwd()
        self.dialog = wx.DirDialog(self.form, "加载alpha通道文件夹", address,
                                   style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DIR_MUST_EXIST)

        if self.dialog.ShowModal() == wx.ID_OK:
            self.form.m_gauge_alpha_load.SetValue(0)
            self.form.m_staticText_alpha_load.SetLabelText("开始")
            temp = self.dialog.GetPath()

            files = all_file_path(temp)

            i = 0
            for file in files[1].keys():
                if file.lower()[-4:] == ".png":
                    val = file.replace(".png", '')
                    keen = val[-5:].lower()
                    if keen == "alpha".lower():
                        self.alpha_enter[val[:-6]] = files[1][file]

                        self.alpha_show.append("%d） %s" % (i, val))
                        self.alpha_key.append(val[:-6])
                        i += 1

            self.form.m_listBox_alpha.Set(self.alpha_show)
            self.test_able()
            self.form.m_gauge_alpha_load.SetValue(100)
            self.form.m_staticText_alpha_load.SetLabelText("完成")

    def load_rgb_f(self):
        if self.lock:
            address = self.default['default_rgb_dir']
        else:
            address = os.getcwd()
        self.dialog = wx.DirDialog(self.form, "加载RGB通道文件夹", address,
                                   style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DIR_MUST_EXIST)

        if self.dialog.ShowModal() == wx.ID_OK:
            self.form.m_gauge_RGB_load.SetValue(0)
            self.form.m_staticText_RGB_load.SetLabelText("开始")
            temp = self.dialog.GetPath()

            files = all_file_path(temp)

            for file in files[1].keys():
                if file.lower()[-4:] == ".png":
                    val = file.lower().replace(".png", '')
                    keen = val[-5:]
                    if keen != "alpha".lower():
                        self.rgb_enter[val] = files[1][file]
                        self.rgb_show.append(val)

            self.form.m_listBox_RGB.Set(self.rgb_show)

            self.test_able()
            self.form.m_gauge_RGB_load.SetValue(100)
            self.form.m_staticText_RGB_load.SetLabelText("完成")

    def load_rgb_alpha_f(self):
        self.dialog = wx.DirDialog(self.form, "加载RGB通道和alpha通道文件夹", os.getcwd(),
                                   style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DIR_MUST_EXIST)

        if self.dialog.ShowModal() == wx.ID_OK:
            self.form.m_gauge_alpha_load.SetValue(0)
            self.form.m_staticText_alpha_load.SetLabelText("开始")
            self.form.m_gauge_RGB_load.SetValue(0)
            self.form.m_staticText_RGB_load.SetLabelText("开始")
            temp = self.dialog.GetPath()

            files = all_file_path(temp)
            i = 0
            j = 0
            for file in files[1].keys():
                ie = file.split(' ')[-1]
                if ie[0] == "#":
                    pass
                if file.lower()[-4:] == ".png":
                    val = file.replace(".png", '')
                    keen = val[-5:].lower()
                    if keen != "alpha".lower():
                        self.rgb_enter[val] = files[1][file]
                        self.rgb_show.append("%d） %s" % (j, val))
                        self.rgb_key.append(val)
                        j += 1
                    else:
                        temp = val[:-6]
                        if temp == "2016xmas_02_again":
                            print(1)
                        self.alpha_enter[val[:-6]] = files[1][file]
                        self.alpha_show.append("%d） %s" % (i, val))
                        self.alpha_key.append(val[:-6])
                        i += 1

            self.form.m_listBox_RGB.Set(self.rgb_show)
            self.form.m_listBox_alpha.Set(self.alpha_show)

            self.test_able()
            self.form.m_gauge_RGB_load.SetValue(100)
            self.form.m_staticText_RGB_load.SetLabelText("完成")
            self.form.m_gauge_alpha_load.SetValue(100)
            self.form.m_staticText_alpha_load.SetLabelText("完成")

    def rgb_choice(self):

        if self.is_rgb_search:
            index = self.rgb_search_result[self.form.m_listBox_RGB.GetSelection()]
        else:
            index = self.form.m_listBox_RGB.GetSelection()

        self.choice = self.rgb_key[index]

        if self.choice in self.able_list:
            self.form.m_menuItem_choice.Enable(True)
        else:
            self.form.m_menuItem_choice.Enable(True)

    def alpha_choice(self):
        if self.is_alpha_search:
            index = self.alpha_search_result[self.form.m_listBox_alpha.GetSelection()]
        else:
            index = self.form.m_listBox_alpha.GetSelection()

        self.choice = self.alpha_key[index]

        if self.choice in self.able_list:
            self.form.m_menuItem_choice.Enable(True)
        else:
            self.form.m_menuItem_choice.Enable(True)

    def unable_choice(self):
        pass

    def skip_choice(self):
        pass

    def export_choice(self):

        self.dialog = wx.FileDialog(self.form, "保存（少女前线）", os.getcwd(), f"{self.choice}.png", '*.png',
                                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if self.dialog.ShowModal() == wx.ID_OK:
            temp = self.dialog.GetPath()
            try:
                girl_font_line_restore(self.rgb_enter[self.choice], self.alpha_enter[self.choice], temp, True)
            except KeyError:
                pass

    def export_all(self, path):

        self.reset()
        self.temp = path

        if self.setting["new_dir"]:
            self.temp += r"\少女前线-导出"

        os.makedirs(self.temp, exist_ok=True)

        self.test_able()

        self.work_thread.set_value(self.rgb_enter, self.alpha_enter, self.temp, self.able_list, self.setting, self.full)
        self.work_thread.set_work(True)
        self.work_thread.start()

    def search_rgb(self):
        key_word = self.form.m_searchCtrl_RGB.GetValue()
        if key_word != '':
            self.is_rgb_search = True

            self.rgb_search_result = find(key_word, self.rgb_search)

            self.rgb_search_show = [self.rgb_show[temp] for temp in self.rgb_search_result]

            self.form.m_listBox_RGB.Clear()
            self.form.m_listBox_RGB.Set(self.rgb_search_show)

        else:
            self.is_rgb_search = False

    def search_alpha(self):
        key_word = self.form.m_searchCtrl_alpha.GetValue()
        if key_word != '':
            self.is_alpha_search = True

            self.alpha_search_result = find(key_word, self.alpha_search, )

            self.alpha_search_show = [self.alpha_show[temp] for temp in self.alpha_search_result]

            self.form.m_listBox_alpha.Clear()
            self.form.m_listBox_alpha.Set(self.alpha_search_show)

        else:
            self.is_alpha_search = False
