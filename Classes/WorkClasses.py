import PIL.Image
import json
import os
import shutil
import time
import re
import win32clipboard

import win32con
import wx

from Classes import Threads, FrameClasses, noname
from Functions import function, tools


class BaseWorkClass:
    def __init__(self, frame):
        self.frame = frame


class PaintingWork(BaseWorkClass):
    """a class only to deal with the tex for azur lane"""

    def __init__(self, form: noname.MyFrame1, setting, default, start_path=os.getcwd()):

        super(PaintingWork, self).__init__(form)

        self.start_path = start_path
        self.form = self.frame

        self.__dialog = None

        # Azur lane values
        self.tex_name = []
        self.mesh_name = []
        self.tex_name_china = []
        self.mesh_name_china = []

        self.tex_list_path_dir = {}
        self.mesh_list_path_dir = {}

        self.choice = None
        try:
            with open('%s\\files\\names.json' % self.start_path, 'r')as file:
                self.names = json.load(file)
        except FileNotFoundError:
            self.names = {}

        self.pass_finish = True

        self.able_restore = 0

        self.able_restore_list = []

        self.unable_restore_list_showed = []
        self.unable_restore_list = []

        self.passed_show = []
        self.passed_list = []

        self.save_path = ''
        self.save_path_list = []

        self._searched_tex = []
        self._searched_mesh = []
        self._search_skip = []
        self._search_unable = []

        self.form.m_choice_pass.Enable(False)
        self.form.m_choice_unable.Enable(False)

        self.tex_search = False
        self.mesh_search = False
        self.skip_search = False
        self.unable_search = False

        self.search_mesh_show = []
        self.search_tex_show = []
        self.search_skip_show = []
        self.search_unable_show = []

        self.search_mesh_index = []
        self.search_tex_index = []
        self.search_pass_index = []
        self.search_unable_index = []

        self.restore_list = []

        self.setting = setting["azur_lane"]

        self.full = setting["full"]

        self.default = default["azur_lane"]

        self.lock = default['lock']

        self.pattern_tex = re.compile(self.setting['tex_limit'])
        self.pattern_mesh = re.compile(self.setting['mesh_limit'])

        self.restore = Threads.RestoreThread(1, 'restore', self.restore_list, self.form, self.names,
                                             self.mesh_list_path_dir, self.tex_list_path_dir, self.save_path,
                                             self.setting, full=self.full, unable_restore_list=self.unable_restore_list)

        self.able_add = False
        # file load method

    def is_able_add(self):
        return self.able_add

    def is_choice(self):
        return self.choice

    def is_able(self):
        return self.able_restore_list != []

    def load_tex(self):
        self.form.m_gauge_tex_load.SetValue(0)
        if self.lock:
            address = self.default['default_tex_dir']
        else:
            address = os.getcwd()
        self.__dialog = wx.FileDialog(self.form, "打开", address, "AzurLane.png",
                                      "*.PNG", style=wx.FD_MULTIPLE | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST)

        if self.__dialog.ShowModal() == wx.ID_OK:

            self.form.m_staticText_load_tex.SetLabel("开始")
            self.form.m_gauge_tex_load.SetValue(0)
            paths = self.__dialog.GetPaths()
            returned = tools.file_deal(paths, self.tex_name, self._searched_tex, self.tex_name_china,
                                       self.tex_list_path_dir, self.full['clear_list'], self.pattern_tex, True, '',
                                       self.names)
            if returned[0]:
                self.form.m_gauge_tex_load.SetValue(100)

                self.form.m_listBox_tex.Set(self.tex_name_china)
            self.form.m_staticText_load_tex.SetLabel(returned[1])
            address = paths
        else:
            address = ''
        self.info_check()

        return address

    def load_mesh(self):
        self.form.m_gauge_tex_load.SetValue(0)
        if self.lock:
            address = self.default['default_mesh_dir']
        else:
            address = os.getcwd()
        self.__dialog = wx.FileDialog(self.form, "打开", address,
                                      wildcard="*.OBJ", style=wx.FD_MULTIPLE | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST)

        if self.__dialog.ShowModal() == wx.ID_OK:
            self.form.m_staticText_mesh_load.SetLabel("开始")
            self.form.m_gauge_mesh_load.SetValue(0)
            paths = self.__dialog.GetPaths()
            returned = tools.file_deal(paths, self.mesh_name, self._searched_mesh, self.mesh_name_china,
                                       self.mesh_list_path_dir, self.full['clear_list'],
                                       self.pattern_mesh, True, "-mesh", self.names)

            if returned[0]:
                self.form.m_gauge_mesh_load.SetValue(function.re_int(100))

                self.form.m_listBox_mesh.Set(self.mesh_name_china)
            self.form.m_staticText_mesh_load.SetLabel(returned[1])

            address = paths
        else:
            address = ''

        self.info_check()

        return address

    def load_mesh_fold(self):
        self.form.m_gauge_tex_load.SetValue(0)
        if self.lock:
            address = self.default['default_mesh_dir']
        else:
            address = os.getcwd()

        self.__dialog = wx.DirDialog(self.form, "打开", address,
                                     style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE |
                                           wx.DD_DIR_MUST_EXIST)

        if self.__dialog.ShowModal() == wx.ID_OK:
            paths = self.__dialog.GetPath()
            self.form.m_staticText_mesh_load.SetLabel("开始")
            self.form.m_gauge_mesh_load.SetValue(0)

            paths = function.all_file_path(paths)[1]
            returned, info = tools.file_deal(paths, self.mesh_name, self._searched_mesh, self.mesh_name_china,
                                             self.mesh_list_path_dir, self.full['clear_list'],
                                             self.pattern_mesh, False, "-mesh", self.names)
            if returned:
                self.form.m_gauge_mesh_load.SetValue(100)
                self.form.m_staticText_mesh_load.SetLabel(info)
                self.form.m_listBox_mesh.Set(self.mesh_name_china)
            self.form.m_staticText_mesh_load.SetLabel(info)
            address = self.__dialog.GetPath()
        else:
            address = 'None'

        self.info_check()

        return address

    def load_tex_fold(self):
        self.form.m_gauge_tex_load.SetValue(0)
        if self.lock:
            address = self.default['default_tex_dir']
        else:
            address = os.getcwd()

        self.__dialog = wx.DirDialog(self.form, "打开", address,
                                     style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE
                                           | wx.DD_DIR_MUST_EXIST)
        info = self.__dialog.ShowModal()
        if info == wx.ID_OK:
            self.form.m_staticText_load_tex.SetLabel("开始")
            paths = self.__dialog.GetPath()

            paths = function.all_file_path(paths)[1]
            returned, info = tools.file_deal(paths, self.tex_name, self._searched_tex, self.tex_name_china,
                                             self.tex_list_path_dir, self.full['clear_list'], self.pattern_tex, False,
                                             '',
                                             self.names)
            if returned:
                self.form.m_gauge_tex_load.SetValue(100)

                self.form.m_listBox_tex.Set(self.tex_name_china)
            self.form.m_staticText_load_tex.SetLabel(info)

            address = self.__dialog.GetPath()
        else:
            address = 'None'

        self.info_check()

        return address

    def load_tex_and_mesh(self):
        self.form.m_gauge_tex_load.SetValue(0)
        self.__dialog = wx.DirDialog(self.form, "打开", os.getcwd(),
                                     style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE |
                                           wx.DD_DIR_MUST_EXIST)

        if self.__dialog.ShowModal() == wx.ID_OK:
            paths = self.__dialog.GetPath()
            self.form.m_staticText_load_tex.SetLabel('开始')
            self.form.m_staticText_mesh_load.SetLabel('开始')

            paths = function.all_file_path(paths)[1]

            returned_tex, tex_info = tools.file_deal(paths, self.tex_name, self._searched_tex, self.tex_name_china,
                                                     self.tex_list_path_dir, self.full['clear_list'], self.pattern_tex,
                                                     False, '',
                                                     self.names)

            returned_mesh, mesh_info = tools.file_deal(paths, self.mesh_name, self._searched_mesh, self.mesh_name_china,
                                                       self.mesh_list_path_dir, self.full['clear_list'],
                                                       self.pattern_mesh, False, "-mesh", self.names)
            if returned_tex:
                self.form.m_gauge_tex_load.SetValue(100)

                self.form.m_listBox_tex.Set(self.tex_name_china)
            self.form.m_staticText_load_tex.SetLabel(tex_info)
            if returned_mesh:
                self.form.m_gauge_mesh_load.SetValue(100)

                self.form.m_listBox_mesh.Set(self.mesh_name_china)
            self.form.m_staticText_mesh_load.SetLabel(mesh_info)

            address = self.__dialog.GetPath()
        else:
            address = 'None'

        self.info_check()

        return address

    # choice
    def mesh_choice(self):

        if self.mesh_search:
            self.choice = self.mesh_name[self.search_mesh_index[self.form.m_listBox_mesh.GetSelection()]]
        else:
            self.choice = self.mesh_name[self.form.m_listBox_mesh.GetSelection()]
        if self.choice in self.tex_name:
            self.form.m_menuItem_choice.Enable(True)
            show = Threads.QuickRestore(self.choice, self.tex_list_path_dir, self.mesh_list_path_dir, self.form,
                                        self.start_path, full=self.full)
            show.start()

    def tex_choice(self):
        if self.tex_search:
            self.choice = self.tex_name[self.search_tex_index[self.form.m_listBox_tex.GetSelection()]]
        else:
            self.choice = self.tex_name[self.form.m_listBox_tex.GetSelection()]
        if self.choice in self.mesh_name:
            self.form.m_menuItem_choice.Enable(True)
            show = Threads.QuickRestore(self.choice, self.tex_list_path_dir, self.mesh_list_path_dir, self.form,
                                        self.start_path, self.full)
            show.start()

    def open_file(self):
        if self.unable_search:
            index = self.search_unable_index[self.form.m_listBox_unable.GetSelection()]
        else:
            index = self.form.m_listBox_unable.GetSelection()
        name = self.unable_restore_list[index]
        show = Threads.QuickRestore(name, self.tex_list_path_dir, None, self.form,
                                    self.start_path, full=self.full, back=1)
        show.start()
        # os.system("start %s" % path)

    def open_pass(self):
        name = ''
        if self.skip_search:
            index = self.search_pass_index[self.form.m_listBox_info.GetSelection()]
        else:
            index = self.form.m_listBox_info.GetSelection()
        for guide in self.names.keys():
            if guide == self.passed_list[index]:
                name = f"{self.names[guide]}.png"
        try:
            path = self.save_path_list[1][name]
        except KeyError:
            name = name[:-4] + ".PNG"
            path = self.save_path_list[1][name]

        path = path.split("\\")[-1]

        show = Threads.QuickRestore(path, self.save_path_list[1], None, self.form,
                                    self.start_path, full=self.full, back=0)
        show.start()

        # export

    # export
    def export_choice(self):
        self.__dialog = wx.FileDialog(self.form, "保存", os.getcwd(), self.names[self.choice], "*.png", style=wx.FD_SAVE)

        if self.__dialog.ShowModal() == wx.ID_OK:
            self.form.m_gauge_all.SetValue(0)
            self.save_path = self.__dialog.GetPath()

            shutil.copy(f"{self.start_path}\\temp.png", self.save_path)

        self.form.m_gauge_all.SetValue(100)
        if self.full['auto_open']:
            os.system("start %s" % self.save_path)

    def export_all(self, path):
        if self.setting["new_dir"]:
            path += r"\碧蓝航线-导出"

        os.makedirs(path, exist_ok=True)

        self.restart()
        self.save_path = path
        self.form.m_gauge_all.SetValue(0)

        self.able_restore_list = list(set(self.able_restore_list))

        if self.full["skip_had"]:
            self.save_path_list = function.all_file_path(self.save_path)

            num = 1
            able_restore = self.able_restore_list
            for able in self.able_restore_list:
                try:
                    text = f"{self.names[able]}.png"
                    text2 = f"{self.names[able]}.PNG"
                except KeyError:
                    text = f"{able}.png"
                    text2 = "{able}.PNG"
                if text in self.save_path_list[1].keys() or \
                        text2 in self.save_path_list[1].keys():
                    self.passed_show.append('%s——%s,第%d个' % (self.names[able], able, num))
                    self.passed_list.append(able)
                    self._search_skip.append(f"{able}{self.names[able]}")
                    num += 1
                    able_restore.remove(able)
            self.able_restore_list = able_restore
            self.form.m_notebook_info.SetSelection(0)

        self.form.m_listBox_skip.Clear()
        self.form.m_listBox_skip.Set(self.passed_show)

        self.restore.update_list(self.able_restore_list, self.unable_restore_list)
        self.restore.add_save_path(self.save_path)
        if self.restore.is_alive():
            self.restore.stop_(True)
            while self.restore.is_alive():
                time.sleep(1)
            self.restore.start()
        else:
            self.restore.start()

    def copy_file(self):
        self.__dialog = wx.DirDialog(self.form, "保存", os.getcwd(),
                                     style=wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON
                                           | wx.DD_DEFAULT_STYLE)
        if self.__dialog.ShowModal() == wx.ID_OK:
            path = self.__dialog.GetPath()
            num = 0
            self.form.m_gauge_all.SetValue(0)
            for name in self.unable_restore_list:
                num += 1

                shutil.copyfile(self.tex_list_path_dir[name], f'{path}\\{self.names[name]}.png')

                self.form.m_gauge_all.SetValue(function.re_int(100 * (num / len(self.unable_restore_list))))

            if self.full['auto_open']:
                os.system(self.save_path)

        # search

    # search
    def search_mesh(self):
        value = self.form.m_searchCtrl_mesh.GetValue()
        if value != '':
            indexes = function.find(value, self._searched_mesh)

            self.mesh_search = True

            self.search_mesh_show.clear()
            self.search_mesh_index.clear()

            for index in indexes:
                self.search_mesh_show.append(self.mesh_name_china[index])
                self.search_mesh_index.append(index)

            self.form.m_listBox_mesh.Clear()
            self.form.m_listBox_mesh.Set(self.search_mesh_show)
        else:
            self.mesh_search = False
            self.form.m_listBox_mesh.Clear()
            self.form.m_listBox_mesh.Set(self.mesh_name_china)

    def search_tex(self):
        value = self.form.m_searchCtrl_tex.GetValue()
        if value != '':
            indexes = function.find(value, self._searched_tex)
            self.tex_search = True

            self.search_tex_show.clear()
            self.search_tex_index.clear()

            for index in indexes:
                self.search_tex_show.append(self.tex_name_china[index])
                self.search_tex_index.append(index)

            self.form.m_listBox_tex.Clear()
            self.form.m_listBox_tex.Set(self.search_tex_show)
        else:
            self.tex_search = False
            self.form.m_listBox_tex.Clear()
            self.form.m_listBox_tex.Set(self.tex_name_china)

    def search_pass(self):
        value = self.form.m_searchCtrl_pass.GetValue()
        if value != '':
            indexes = function.find(value, self._search_skip)

            self.skip_search = True

            self.search_pass_index.clear()
            self.search_skip_show.clear()

            for index in indexes:
                self.search_skip_show.append(self.passed_show[index])
                self.search_pass_index.append(index)

            self.form.m_listBox_skip.Clear()
            self.form.m_listBox_skip.Set(self.search_skip_show)
        else:
            self.skip_search = False
            self.form.m_listBox_skip.Clear()
            self.form.m_listBox_skip.Set(self.passed_show)

    def search_unable(self):
        value = self.form.m_searchCtrl_unable.GetValue()
        if value != "":
            indexes = function.find(value, self._search_unable)

            self.unable_search = True

            self.search_unable_index.clear()
            self.search_unable_show.clear()

            for index in indexes:
                self.search_unable_show.append(self.unable_restore_list_showed[index])
                self.search_unable_index.append(index)

            self.form.m_listBox_unable.Clear()
            self.form.m_listBox_unable.Set(self.search_unable_show)
        else:
            self.unable_search = False
            self.form.m_listBox_unable.Clear()
            self.form.m_listBox_unable.Set(self.unable_restore_list_showed)

        # else

    # else
    def able_export(self):
        for name in self.mesh_name:
            if name in self.tex_name:
                self.able_restore += 1
                self.able_restore_list.append(name)
        if self.able_restore >= 1:
            num = 0
            self.unable_restore_list = []
            self.unable_restore_list_showed.clear()
            for name in self.tex_name:
                if name not in self.mesh_name and name.split(' ')[0] != "UISprite":
                    num += 1
                    try:
                        self.unable_restore_list_showed.append("%d） %s" % (num, self.names[name]))
                    except KeyError:
                        self.unable_restore_list_showed.append("%d） %s" % (num, name))
                    self.unable_restore_list.append(name)
                    try:
                        self._search_unable.append(f"{name}{self.names[name]}")
                    except KeyError:
                        self._search_unable.append(f"{name}{name}")

            self.form.m_listBox_unable.Clear()
            self.form.m_listBox_unable.Set(self.unable_restore_list_showed)

        if len(self.tex_name) >= 1:
            self.able_add = True
        else:
            self.able_add = False

        return self.able_restore >= 1

    def restart(self):

        self.passed_show = []
        self.passed_list = []
        self._search_skip.clear()

        for name in self.mesh_name:
            if name in self.tex_name:
                self.able_restore += 1
                self.able_restore_list.append(name)

        self.restore = Threads.RestoreThread(1, 'restore', self.restore_list, self.form, self.names,
                                             self.mesh_list_path_dir, self.tex_list_path_dir, self.save_path,
                                             self.setting, full=self.full, unable_restore_list=self.unable_restore_list)

        self.form.m_staticText_all.SetLabel("总进度：%s %%" % '0')
        self.form.m_gauge_all.SetValue(0)

    def update_setting(self, setting, default):
        self.setting = setting["azur_lane"]

        self.full = setting["full"]

        self.default = default["azur_lane"]

        self.lock = default['lock']

        self.pattern_tex = re.compile(self.setting['tex_limit'])
        self.pattern_mesh = re.compile(self.setting['mesh_limit'])

    def update_names(self):
        self.mesh_name_china.clear()
        self._searched_mesh.clear()

        self.tex_name_china.clear()
        self._searched_tex.clear()

        self.unable_restore_list_showed.clear()
        self._search_unable.clear()

        self.passed_show.clear()
        self._search_skip.clear()

        num = 1
        with open("%s\\files\\names.json" % self.start_path, 'r')as file:
            names = json.load(file)
        self.names = names
        for name in self.mesh_name:

            try:
                self.mesh_name_china.append(f"{num}）{self.names[name]}——{name}")
                self._searched_mesh.append(f"{self.names[name]}{name}")
            except KeyError:
                self.mesh_name_china.append(f"{num}）{name}——{name}")
                self._searched_mesh.append(f"{name}")
            num += 1
        num = 1

        for path in self.tex_name:

            try:
                self.tex_name_china.append(f"{num}）{self.names[path]}——{path}")
                self._searched_tex.append(f"{self.names[path]}{path}")
            except KeyError:
                self.tex_name_china.append(f"{num}）{path}——{path}")
                self._searched_tex.append(f"{path}")
            num += 1

        num = 1
        for able in self.passed_list:

            try:
                self.passed_show.append('%s——%s,第%d个' % (self.names[able], able, num))
            except KeyError:
                self.passed_show.append('%s——%s,第%d个' % (able, able, num))
            try:
                self._search_skip.append(f"{able}{self.names[able]}")
            except KeyError:
                self._search_skip.append(f"{able}{able}")
            num += 1
        num = 1
        for name in self.unable_restore_list:

            try:
                self.unable_restore_list_showed.append("%d） %s" % (num, self.names[name]))
            except KeyError:
                self.unable_restore_list_showed.append("%d） %s" % (num, name))
            try:
                self._search_unable.append(f"{name}{self.names[name]}")
            except KeyError:
                self._search_unable.append(f"{name}{name}")

        self.form.m_listBox_mesh.Set(self.mesh_name_china)
        self.form.m_listBox_tex.Set(self.tex_name_china)
        self.form.m_listBox_skip.Set(self.passed_show)
        self.form.m_listBox_unable.Set(self.unable_restore_list_showed)

    def info_check(self):
        if self.able_export():
            self.form.m_menuItem_all.Enable(True)
        else:
            self.form.m_menuItem_all.Enable(False)

        if len(self.unable_restore_list) >= 1:
            self.form.m_menuItem_copy_only.Enable(True)
        else:
            self.form.m_menuItem_copy_only.Enable(False)


class SpineDivideWork(BaseWorkClass):
    def __init__(self, frame: noname.MyFrame1, start_path=os.getcwd()):
        super(SpineDivideWork, self).__init__(frame)

        self.path = start_path

        self.dialog = wx.Dialog

        self.cuter = ''

        self.body: PIL.Image = None

        self.bodies = []

        self.name = ''

        self.root = self.frame.m_treeCtrl_boys.AddRoot("娃娃")

        self.frame.m_bpButton_ex_spine.Enable(False)

    def need_work(self):

        if self.body is not None and len(self.cuter) >= 1:
            self.work()

    def load_body(self):
        self.dialog = wx.FileDialog(self.frame, 'body', os.getcwd(), '', "*.png",
                                    wx.FD_FILE_MUST_EXIST | wx.FD_OPEN | wx.FD_CHANGE_DIR)

        if self.dialog.ShowModal() == wx.ID_OK:
            self.body = None
            self.body = function.body_enter(self.dialog.GetFilename())

            self.need_work()

    def load_cuter(self):
        self.dialog = wx.FileDialog(self.frame, 'divide', os.getcwd(), '', "*.atlas.txt",
                                    wx.FD_FILE_MUST_EXIST | wx.FD_OPEN | wx.FD_CHANGE_DIR)
        if self.dialog.ShowModal() == wx.ID_OK:
            with open(self.dialog.GetFilename(), 'r')as file:
                self.cuter = file.read()

            self.need_work()

    def work(self):
        self.bodies.clear()

        pattern = re.compile(r'.+?\.png\nsize: \d+,\d+\nformat: \w+\nfilter: Linear,Linear\nrepeat: none')
        cuter = pattern.findall(self.cuter)

        cuter = cuter[0].replace('\\n', '\n')

        name = re.findall(r'.+\.png', cuter)[0]
        self.name = os.path.splitext(name)[0]
        name = self.name

        self.cuter = self.cuter.replace(cuter, '')

        pattern = re.compile(r'\w+\n\s\s[ \S,]+\n\s\s[ \S,]+\n\s\s[ \S,]+\n\s\s[ \S,]+\n\s\s[ \S,]+\n\s\s[ \S,]+')
        bodies = pattern.findall(self.cuter)
        root = self.frame.m_treeCtrl_boys.AppendItem(self.root, name)
        self.frame.m_treeCtrl_boys.Expand(self.root)
        for body in bodies:
            body = body.split("\n  ")

            pattern = re.compile(r'[0-9]+')
            xy = [int(info) for info in pattern.findall(body[2])]
            size = [int(info) for info in pattern.findall(body[3])]
            rotate = json.loads(body[1].split(' ')[-1])
            cuter = function.cuter(self.body, xy, size, rotate)
            self.bodies.append({'name': body[0],
                                'xy': xy,
                                'size': size,
                                'rotate': rotate,
                                'pic': cuter})
            body = self.frame.m_treeCtrl_boys.AppendItem(root, 'name: ' + body[0])
            xy_item = self.frame.m_treeCtrl_boys.AppendItem(body, "[X，Y]: " + json.dumps(xy))
            self.frame.m_treeCtrl_boys.AppendItem(xy_item, "X：%d" % (xy[0]))
            self.frame.m_treeCtrl_boys.AppendItem(xy_item, "Y：%d" % (xy[1]))
            size_item = self.frame.m_treeCtrl_boys.AppendItem(body, 'size: ' + json.dumps(size))
            self.frame.m_treeCtrl_boys.AppendItem(size_item, "wide：%d" % (size[0]))
            self.frame.m_treeCtrl_boys.AppendItem(size_item, "high：%d" % (size[1]))

            self.frame.m_treeCtrl_boys.AppendItem(body, 'rotate: ' + json.dumps(rotate))

            self.frame.m_bpButton_ex_spine.Enable(True)
            self.frame.m_bpButton_cut_way.Enable(False)
            self.frame.m_bpButton_body.Enable(False)

            self.frame.m_staticText_now.SetLabel("OK")

    def pic_open(self):
        print(self.frame.m_treeCtrl_boys.GetSelection())

    def export_pic(self):
        self.dialog = wx.DirDialog(self.frame, 'divide', os.getcwd(),
                                   wx.DD_DIR_MUST_EXIST | wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR)

        if self.dialog.ShowModal() == wx.ID_OK:
            path = os.path.join(self.dialog.GetPath(), self.name)
            os.makedirs(path, exist_ok=True)
            for val in self.bodies:
                path_save = os.path.join(path, f"{val['name']}.png")
                val['pic'].save(path_save)

            self.frame.m_gauge_ex_spine.SetValue(100)
            self.frame.m_bpButton_ex_spine.Enable(False)

    def reset(self):

        self.cuter = ''

        self.body: PIL.Image = None

        self.bodies = []

        self.name = ''

        self.frame.m_bpButton_ex_spine.Enable(False)
        self.frame.m_bpButton_cut_way.Enable(True)
        self.frame.m_bpButton_body.Enable(True)


class EncryptImage(BaseWorkClass):
    def __init__(self, frame: noname.MyDialog_Setting):
        super(EncryptImage, self).__init__(frame)
        self.dialog = None
        self.in_show = []
        self.path = {}

    def in_file(self):
        self.frame.m_gauge_file.SetValue(0)
        self.dialog = wx.FileDialog(self.frame, "打开", wildcard="*.png",
                                    style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_MULTIPLE | wx.FD_FILE_MUST_EXIST)

        if self.dialog.ShowModal() == wx.ID_OK:
            returned = tools.file_deal(self.dialog.GetPaths(), self.in_show, [], [], self.path,
                                       pattern=r'^.+\.[Pp][Nn][Gg]$')

            if returned:
                self.frame.m_gauge_file.SetValue(100)
                self.frame.m_listBox_pics.Clear()
                self.frame.m_listBox_pics.Set(self.in_show)

    def in_folder(self):
        self.frame.m_gauge_dir.SetValue(0)
        self.dialog = wx.DirDialog(self.frame, "打开",
                                   style=wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON | wx.DD_DIR_MUST_EXIST)

        if self.dialog.ShowModal() == wx.ID_OK:
            path = function.all_file_path(self.dialog.GetPath())[1]

            returned = tools.file_deal(path, self.in_show, [], [], self.path,
                                       pattern=r'^.+\.[Pp][Nn][Gg]$', is_file=False)

            if returned:
                self.frame.m_gauge_dir.SetValue(100)
                self.frame.m_listBox_pics.Clear()
                self.frame.m_listBox_pics.Set(self.in_show)

    def start(self):
        self.dialog = wx.DirDialog(self.frame, "保存",
                                   style=wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON | wx.DD_DIR_MUST_EXIST)
        if self.dialog.ShowModal() == wx.ID_OK:
            thread = Threads.EncryptTread(self.in_show, self.frame.m_choice_type.GetSelection(), self.path,
                                          self.dialog.GetPath(), self.frame)
            thread.start()
            self.frame.m_button_star.Enable(False)


class CryptImage(EncryptImage):
    def __init__(self, frame: noname.MyDialog_Setting):
        super(CryptImage, self).__init__(frame)

    def in_file(self):
        self.frame.m_gauge_file_in.SetValue(0)
        self.dialog = wx.FileDialog(self.frame, "打开", wildcard="*.png",
                                    style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_MULTIPLE | wx.FD_FILE_MUST_EXIST)

        if self.dialog.ShowModal() == wx.ID_OK:
            returned = tools.file_deal(self.dialog.GetPaths(), self.in_show, [], [], self.path,
                                       pattern=r'^.+\.[Pp][Nn][Gg]$')

            if returned:
                self.frame.m_gauge_file_in.SetValue(100)
                self.frame.m_listBox_pic_in.Clear()
                self.frame.m_listBox_pic_in.Set(self.in_show)

    def in_folder(self):
        self.frame.m_gauge_fold_in.SetValue(0)
        self.dialog = wx.DirDialog(self.frame, "打开",
                                   style=wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON | wx.DD_DIR_MUST_EXIST)

        if self.dialog.ShowModal() == wx.ID_OK:
            path = function.all_file_path(self.dialog.GetPath())[1]

            returned = tools.file_deal(path, self.in_show, [], [], self.path,
                                       pattern=r'^.+\.[Pp][Nn][Gg]$', is_file=False)

            if returned:
                self.frame.m_gauge_fold_in.SetValue(100)
                self.frame.m_listBox_pic_in.Clear()
                self.frame.m_listBox_pic_in.Set(self.in_show)

    def start(self):
        self.dialog = wx.DirDialog(self.frame, "保存",
                                   style=wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON | wx.DD_DIR_MUST_EXIST)
        if self.dialog.ShowModal() == wx.ID_OK:
            thread = Threads.CryptTread(self.in_show, self.frame.m_choice_type_in.GetSelection(), self.path,
                                        self.dialog.GetPath(), self.frame)
            thread.start()
            self.frame.m_button_star_in.Enable(False)


class Add(object):
    def __init__(self, parent: noname.MyDialog_Setting, name_list, names, start_path):

        self.parent = parent
        self.name_list = name_list
        self.need_add = []
        self.need_add_show = []
        self.finish_num = 0

        self.start_path = start_path

        self.names = names

    def get_new_dic(self):
        return self.names

    def show_info(self):
        for name in self.name_list:
            if name not in self.names.keys():
                self.need_add.append(name)
                self.need_add_show.append("%s: " % name)

        self.parent.m_listBox_new.Set(self.need_add_show)

    def open_add_name(self):
        index = self.parent.m_listBox_new.GetSelection()
        value = self.need_add[index]
        if value in self.names.keys():
            value_cn = self.names[value]
        else:
            value_cn = ''

        writer = FrameClasses.Writer(self.parent, value, value_cn)
        writer.ShowModal()
        if writer.is_able():
            name = writer.GetValue()
            if name != '':
                self.finish_num += 1
            elif value in self.names.keys() and name == '':
                self.finish_num -= 1
            self.names[value] = name
            self.need_add_show[index] = "%s：%s" % (self.need_add[index], name)

            self.parent.m_listBox_new.SetString(index, self.need_add_show[index])
        scale = function.re_int(100 * (self.finish_num / len(self.need_add)))
        self.parent.m_gauge5.SetValue(scale)


class Compare:
    def __init__(self, parent: noname.MyDialog_Setting):
        self.frame = parent
        self.thread = Threads.CompareThread(self)

        self.old_fold = ''
        self.new_fold = ''

        self.old_fold_list = []
        self.new_fold_list = []

        self._new_add = []
        self._new_add_show = []

    def writer_into(self):
        index = self.frame.m_listBox_deffer.GetSelection()

        info = self._new_add[index]

        win32clipboard.OpenClipboard()

        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, info)
        win32clipboard.CloseClipboard()

    def test(self):
        if self.frame.m_dirPicker6.GetPath() != '':
            self.new_fold = self.frame.m_dirPicker6.Path
            self.new_fold_list = function.all_file_path(self.new_fold)
        if self.frame.m_dirPicker_old.GetPath() != '':
            self.old_fold = self.frame.m_dirPicker_old.GetPath()
            self.old_fold_list = function.all_file_path(self.old_fold)

        if self.new_fold != '' and self.old_fold != '':
            self.start()

    def start(self):
        self.thread.start()


class ChangeName:
    def __init__(self, parent: noname.MyDialog_Setting, start_path):
        self.frame = parent

        self.start_path = start_path

        with open("%s\\files\\names.json" % self.start_path, 'r')as file:
            self.names = json.load(file)

        self.show_list = []
        self.key_list = []
        self.searched_list = []

        self.searched_show = []
        self.search_list = []

        self.searched = False

    def show_all(self):
        num = 0
        for index in self.names.keys():
            num += 1
            self.show_list.append("%d）\t%s：%s" % (num, index, self.names[index]))
            self.key_list.append(index)
            self.searched_list.append("%s%s" % (index, self.names[index]))
        self.frame.m_listBox_change.Clear()
        self.frame.m_listBox_change.Set(self.show_list)

    def change_name(self):
        index = self.frame.m_listBox_change.GetSelection()
        if not self.searched:
            name = self.key_list[index]
        else:
            name = self.search_list[index]
        name_cn = self.names[name]

        writer = FrameClasses.Writer(self.frame, name, name_cn)
        writer.ShowModal()
        if writer.is_able():
            name_cn = writer.GetValue()

            self.names[name] = name_cn

            self.show_list[index] = "%d）\t%s：%s" % (index + 1, self.key_list[index], self.names[self.key_list[index]])
            self.key_list[index] = name

            self.frame.m_listBox_change.SetString(index, self.show_list[index])

    def searching(self):
        value = self.frame.m_searchCtrl2.GetValue()
        if value != '':
            self.searched = True
            indexes = function.find(value, self.searched_list)

            self.searched_show.clear()

            self.search_list.clear()

            for index in indexes:
                self.searched_show.append(self.show_list[index])
                self.search_list.append(self.key_list[index])

        else:
            self.searched_show = self.show_list.copy()
            self.search_list = self.key_list.copy()
            self.searched = False
        self.frame.m_listBox_change.Clear()
        self.frame.m_listBox_change.Set(self.searched_show)

    def get_change(self):
        return self.names
