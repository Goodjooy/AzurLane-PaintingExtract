import functools
import json
import os
import re
import shutil
import threading
import time
import win32clipboard

import PIL.Image
import win32con
import wx

from Classes import Threads, FrameClasses, noname, InfoClasses
from Functions import function, tools


class BaseWorkClass:
    def __init__(self, frame):
        self.frame = frame


class PaintingWork(BaseWorkClass):
    """a class only to deal with the tex for azur lane"""

    def __init__(self,
                 form: noname.MyFrame1 = ...,
                 setting: dict = ...,
                 default: dict = ...,
                 start_path: str = os.getcwd()):

        super(PaintingWork, self).__init__(form)

        self.tex_type = 1
        self.mesh_type = 2

        self.start_path = start_path
        self.form = self.frame

        self.__dialog = None
        # infomation
        self.info: InfoClasses.PerWorkList = InfoClasses.PerWorkList()

        self.unable: InfoClasses.PerWorkList = InfoClasses.PerWorkList()

        self.skip: InfoClasses.PerWorkList = InfoClasses.PerWorkList()

        self.able: InfoClasses.PerWorkList = InfoClasses.PerWorkList()

        # search

        self.search_mesh_val: InfoClasses.PerWorkList = InfoClasses.PerWorkList()
        self.search_tex_val: InfoClasses.PerWorkList = InfoClasses.PerWorkList()
        self.search_skip_val: InfoClasses.PerWorkList = InfoClasses.PerWorkList()
        self.search_unable_val: InfoClasses.PerWorkList = InfoClasses.PerWorkList()
        # choice
        self.choice: InfoClasses.PerWorkList = InfoClasses.PerWorkList()

        try:
            with open('%s\\files\\names.json' % self.start_path, 'r')as file:
                self.names = json.load(file)
        except FileNotFoundError:
            self.names = {}

        self.save_path = ''
        self.save_path_list = []

        self.form.m_choice_pass.Enable(False)
        self.form.m_choice_unable.Enable(False)

        self.tex_search = False
        self.mesh_search = False
        self.skip_search = False
        self.unable_search = False

        self.error_list = []

        self.setting = setting["azur_lane"]

        self.full = setting["full"]

        self.default = default["azur_lane"]

        self.lock = default['lock']

        self.pattern_tex = re.compile(self.setting['tex_limit'])
        self.pattern_mesh = re.compile(self.setting['mesh_limit'])

        self.restore: Threads.RestoreThread = threading.Thread()

        self.able_add = False

        # file load method

    def any_error(self):
        return self.error_list != []

    def is_able_add(self):
        return self.able_add

    def is_choice(self):
        return self.choice

    def is_able(self):
        return bool(self.able)

    # load
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

            if self.full['clear_list']:
                self.info.clear()

            returned = tools.file_deal2(paths, self.info, self.full['clear_list'], self.pattern_tex, True, '',
                                        self.names, self.tex_type)
            if returned[0]:
                self.form.m_gauge_tex_load.SetValue(100)

                self.form.m_listBox_tex.Set(
                    self.info.for_show)
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

            if self.full['clear_list']:
                self.info.clear()

            returned = tools.file_deal2(paths, self.info, self.full['clear_list'], self.pattern_mesh, True, "-mesh",
                                        self.names, self.mesh_type)

            if returned[0]:
                self.form.m_gauge_mesh_load.SetValue(function.re_int(100))

                self.form.m_listBox_mesh.Set(
                    self.info.for_show)
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

            if self.full['clear_list']:
                self.info.clear()

            returned, info = tools.file_deal2(paths, self.info, self.full['clear_list'],
                                              self.pattern_mesh, False, "-mesh", self.names, self.mesh_type)
            if returned:
                self.form.m_gauge_mesh_load.SetValue(100)
                self.form.m_staticText_mesh_load.SetLabel(info)
                self.form.m_listBox_mesh.Set(
                    self.info.for_show)
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

            if self.full['clear_list']:
                self.info.clear()

            returned, info = tools.file_deal2(paths, self.info, self.full['clear_list'], self.pattern_tex, False, '',
                                              self.names, self.tex_type)
            if returned:
                self.form.m_gauge_tex_load.SetValue(100)

                self.form.m_listBox_tex.Set(
                    self.info.for_show)
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

            if self.full['clear_list']:
                self.info.clear()

            returned_tex, tex_info = tools.file_deal2(paths, self.info, self.full['clear_list'], self.pattern_tex,
                                                      False, '',
                                                      self.names, self.tex_type)

            returned_mesh, mesh_info = tools.file_deal2(paths, self.info, self.full['clear_list'],
                                                        self.pattern_mesh, False, "-mesh", self.names, self.mesh_type)
            if returned_tex:
                self.form.m_gauge_tex_load.SetValue(100)

                self.form.m_listBox_tex.Set(
                    self.info.for_show)
            self.form.m_staticText_load_tex.SetLabel(tex_info)
            if returned_mesh:
                self.form.m_gauge_mesh_load.SetValue(100)

                self.form.m_listBox_mesh.Set(
                    self.info.for_show)
            self.form.m_staticText_mesh_load.SetLabel(mesh_info)

            address = self.__dialog.GetPath()
        else:
            address = 'None'

        self.info_check()

        return address

    def drop_work(self, file_names, ):
        try:
            file_names = list(file_names)
            self.form.m_staticText_load_tex.SetLabel('开始')
            self.form.m_staticText_mesh_load.SetLabel('开始')

            dir_name = (filter(lambda x: not os.path.isfile(x), file_names))
            dir_name = map(lambda x: function.all_file_path(x)[1].values(), dir_name)
            list(map(lambda x: file_names.extend(x), dir_name))

            file_names = (filter(lambda x: os.path.isfile(x), file_names))

            if self.full['clear_list']:
                self.info.clear()

            paths = list(filter(lambda x: re.match(r'^UISprite\s#\d+\.png$', os.path.basename(x)) is None, file_names))

            returned_tex, tex_info = tools.file_deal2(paths, self.info, self.full['clear_list'], self.pattern_tex,
                                                      True, '', self.names, self.tex_type)

            returned_mesh, mesh_info = tools.file_deal2(paths, self.info, self.full['clear_list'],
                                                        self.pattern_mesh, True, "-mesh", self.names, self.mesh_type)
            if returned_tex:
                self.form.m_gauge_tex_load.SetValue(100)

                self.form.m_listBox_tex.Set(
                    self.info.for_show)
            self.form.m_staticText_load_tex.SetLabel(tex_info)
            if returned_mesh:
                self.form.m_gauge_mesh_load.SetValue(100)

                self.form.m_listBox_mesh.Set(self.info.for_show)
            self.form.m_staticText_mesh_load.SetLabel(mesh_info)

            self.info_check()

        except RuntimeError as info:
            return False, info

        else:
            return True, ''

    def open_give(self, dir_address):

        files = function.all_file_path(dir_address)[1].values()
        # print(files)
        self.drop_work(files)

    # choice
    def mesh_choice(self):

        indexes = self.frame.m_listBox_mesh.GetSelections()

        last = self.choice
        if self.mesh_search:
            self.choice = self.search_mesh_val.build_search(indexes)
        else:
            self.choice = self.info.build_search(indexes)

        last = last.get_new(self.choice)

        if len(last) > 0:
            if last.is_all_able():
                self.form.m_menuItem_choice.Enable(True)
            show = Threads.QuickRestore(last[-1], self.form, self.start_path, self.full)
            show.start()

    def tex_choice(self):
        indexes = self.frame.m_listBox_tex.GetSelections()

        last = self.choice
        if self.tex_search:
            self.choice = self.search_tex_val.build_search(indexes)
        else:
            self.choice = self.info.build_search(indexes)

        last = last.get_new(self.choice)

        if len(last) > 0:
            if last.is_all_able():
                self.form.m_menuItem_choice.Enable(True)
            show = Threads.QuickRestore(last[-1], self.form, self.start_path, self.full)
            show.start()

    def open_file(self):
        indexes = self.frame.m_listBox_unable.GetSelections()

        last = self.choice
        if self.unable_search:
            self.choice = self.search_unable_val.build_search(indexes)
        else:
            self.choice = self.unable.build_search(indexes)

        last = last.get_new(self.choice)

        if len(last) > 0:
            show = Threads.QuickRestore(last[-1], self.form, self.start_path, self.full)
            show.start()
        # os.system("start %s" % path)

    def open_pass(self):
        indexes = self.frame.m_listBox_skip.GetSelections()

        last = self.choice
        if self.skip_search:
            self.choice = self.search_skip_val.build_search(indexes)
        else:
            self.choice = self.skip.build_search(indexes)

        last = last.get_new(self.choice)

        if len(last) > 0:
            show = Threads.QuickRestore(last[-1], self.form, self.start_path, self.full)
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
            os.system(r'"start %s"' % self.save_path)

    def export_all(self, path, for_work: InfoClasses.PerWorkList = None, for_unable: InfoClasses.PerWorkList = None):
        if self.setting["new_dir"]:
            path += r"\碧蓝航线-导出"

        os.makedirs(path, exist_ok=True)

        self.restart()
        self.save_path = path
        self.form.m_gauge_all.SetValue(0)

        if isinstance(for_work, InfoClasses.PerWorkList):
            for_work = for_work
            for_work = for_work.build_able()
        else:
            for_work = self.able
        if isinstance(for_work, InfoClasses.PerWorkList):
            for_work = for_work
            for_work = for_work.build_able()
        else:
            for_work = self.able
            for_unable = self.able

        if self.full["skip_had"]:
            self.save_path_list = function.all_file_path(self.save_path)

            self.skip = for_work.build_skip(self.save_path_list[1])
            able = for_work.remove(self.skip)

        else:
            able = for_work

        self.form.m_listBox_skip.Clear()
        self.form.m_listBox_skip.Set(self.skip.for_show)

        self.restore.add_save_path(self.save_path)
        self.restore.update_value(able, self.unable)
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
            for name in self.unable:
                num += 1
                name.add_save(path)
                shutil.copyfile(name.tex_path, name.save_path)

                self.form.m_gauge_all.SetValue(function.re_int(100 * (num / len(self.unable))))

            if self.full['auto_open']:
                os.system(r'"%s"' % self.save_path)

        # search

    # search
    def search_mesh(self):
        value = self.form.m_searchCtrl_mesh.GetValue()
        self.search_mesh_val.clear()
        if value != '':
            indexes = function.find(value, self.info.for_search)

            self.mesh_search = True

            self.search_mesh_val.extend(self.info.build_search(indexes))

            self.frame.m_menuItem_mesh_search.Enable(True)

            self.form.m_listBox_mesh.Clear()
            self.form.m_listBox_mesh.Set(self.search_mesh_val.for_show)
        else:
            self.mesh_search = False
            self.frame.m_menuItem_tex_search.Enable(False)
            self.form.m_listBox_mesh.Clear()
            self.form.m_listBox_mesh.Set(self.info.for_show)

    def search_tex(self):
        value = self.form.m_searchCtrl_tex.GetValue()
        self.search_tex_val.clear()
        if value != '':
            indexes = function.find(value, self.info.for_search)
            self.tex_search = True

            self.search_tex_val.extend(self.info.build_search(indexes))

            self.frame.m_menuItem_tex_search.Enable(True)

            self.form.m_listBox_tex.Clear()
            self.form.m_listBox_tex.Set(self.search_tex_val.for_show)
        else:
            self.tex_search = False
            self.frame.m_menuItem_tex_search.Enable(False)
            self.form.m_listBox_tex.Clear()
            self.form.m_listBox_tex.Set(self.info.for_show)

    def search_pass(self):
        value = self.form.m_searchCtrl_pass.GetValue()
        self.search_skip_val.clear()
        if value != '':
            indexes = function.find(value, self.skip.for_search)

            self.skip_search = True

            self.search_skip_val.extend(self.skip.build_search(indexes))

            self.form.m_listBox_skip.Clear()
            self.form.m_listBox_skip.Set(self.search_skip_val.for_show)
        else:
            self.skip_search = False
            self.form.m_listBox_skip.Clear()
            self.form.m_listBox_skip.Set(self.skip.for_show)

    def search_unable(self):
        value = self.form.m_searchCtrl_unable.GetValue()
        self.search_unable_val.clear()
        if value != "":
            indexes = function.find(value, self.unable.for_search)

            self.unable_search = True

            self.search_unable_val.extend(self.info.build_search(indexes))

            self.form.m_listBox_unable.Clear()
            self.form.m_listBox_unable.Set(self.search_unable_val.for_show)
        else:
            self.unable_search = False
            self.form.m_listBox_unable.Clear()
            self.form.m_listBox_unable.Set(self.unable.for_show)

        # else

    # else
    def able_export(self):
        self.able.extend(self.info.build_able())

        self.unable.extend(self.info.build_unable())

        self.form.m_listBox_unable.Clear()
        self.form.m_listBox_unable.Set(self.unable.for_show)

        if len(self.info) >= 1:
            self.able_add = True
        else:
            self.able_add = False

        return bool(self.able)

    def restart(self):

        self.skip.clear()

        self.restore = Threads.RestoreThread(1, 'restore', self.able, self.unable, self.frame, self.setting, self.full,
                                             self.names, self.save_path)
        self.form.m_staticText_all.SetLabel("总进度：%s %%" % '0')
        self.form.m_gauge_all.SetValue(0)

    def update_setting(self, setting, default):
        self.setting = setting.azur_lane_setting.to_dict()

        self.full = setting.full_setting.to_dict()

        self.default = default["azur_lane"]

        self.lock = default['lock']

        print(self.setting)

        self.pattern_tex = re.compile(self.setting['tex_limit'])

        self.pattern_mesh = re.compile(self.setting['mesh_limit'])

    def update_names(self):
        with open("%s\\files\\names.json" % self.start_path, 'r')as file:
            names = json.load(file)
        self.names = names

        self.info.up_date_name_cn(self.names)
        self.unable.up_date_name_cn(self.names)
        self.able.up_date_name_cn(self.names)
        self.skip.up_date_name_cn(self.names)

        self.form.m_listBox_mesh.Set(self.info.for_show)
        self.form.m_listBox_tex.Set(self.info.for_show)
        self.form.m_listBox_skip.Set(self.skip.for_show)
        self.form.m_listBox_unable.Set(self.unable.for_show)

    def info_check(self):
        if self.able_export():
            self.form.m_menuItem_all.Enable(True)
        else:
            self.form.m_menuItem_all.Enable(False)

        if len(self.unable) >= 1:
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


class Setting(BaseWorkClass):

    def __init__(self, parent,
                 setting_dic,
                 default,
                 def_path,
                 able_add,
                 ):
        super().__init__(frame=parent)

        self.path = def_path

        self.default_tex_pattern = "^.+\\.[pP][Nn][Gg]$"
        self.default_mesh_pattern = "^.+-mesh\\.[oO][Bb][jJ]$"
        self.azur_lane_setting = InfoClasses.SettingHolder(setting_dic["azur_lane"])
        self.full_setting = InfoClasses.SettingHolder(setting_dic["full"])

        az_dict = {
            'div_type': [self.frame.m_radioBox_az_div.SetSelection, self.frame.m_radioBox_az_div.GetSelection],
            'export_type': [self.frame.m_radioBox_ex_type.SetSelection, self.frame.m_radioBox_ex_type.GetSelection],
            'div_use': [self.frame.m_radioBox_type_use.SetSelection, self.frame.m_radioBox_type_use.GetSelection],

            'new_dir': [self.frame.m_checkBox_add_dir.SetValue, self.frame.m_checkBox_add_dir.GetValue],
            'export_with_cn': [self.frame.m_checkBox_in_cn.SetValue, self.frame.m_checkBox_in_cn.GetValue],

            'tex_limit': [self.frame.m_textCtrl_tex_limit.SetLabel, self.frame.m_textCtrl_tex_limit.GetLabel],
            'mesh_limit': [self.frame.m_textCtrl_mesh_limit.SetLabel, self.frame.m_textCtrl_mesh_limit.GetLabel],
            'divide_list': [self.frame.m_checkList_az_limits.Set, None],

            'input_use': [self.frame.m_radioBox_im.SetSelection, self.frame.m_radioBox_im.GetSelection]
        }

        full_dict = {
            'open_dir': [self.frame.m_checkBox_autoopen.SetValue,
                         self.frame.m_checkBox_autoopen.GetValue],
            'skip_had': [self.frame.m_checkBox_pass_finished.SetValue,
                         self.frame.m_checkBox_pass_finished.GetValue],
            'auto_open': [self.frame.m_checkBox_open_temp.SetValue,
                          self.frame.m_checkBox_open_temp.GetValue],
            'finish_exit': [self.frame.m_checkBox4_finish_exit.SetValue,
                            self.frame.m_checkBox4_finish_exit.GetValue],
            'clear_list': [self.frame.m_checkBox_clear.SetValue,
                           self.frame.m_checkBox_clear.GetValue],
            'save_all': [self.frame.m_checkBox_save_all.SetValue,
                         self.frame.m_checkBox_save_all.GetValue],
        }

        self.azur_lane_setting.link_dict(az_dict)
        self.full_setting.link_dict(full_dict)

        io_group_1 = [
            self.frame.m_bpButton_del,
            self.frame.m_bpButton_add,

            self.frame.m_bpButton_up,
            self.frame.m_bpButton_down,

            self.frame.m_bpButton6_default_mesh,
            self.frame.m_bpButton_defualt_tex,

            self.frame.m_checkList_az_limits,
            self.frame.m_staticText15,
            self.frame.m_staticText161,
            self.frame.m_staticText171,

            self.frame.m_textCtrl_mesh_limit,
            self.frame.m_textCtrl_tex_limit,
        ]
        io_group_2 = [
            self.frame.m_radioBox_im,
            self.frame.m_radioBox_az_div,
        ]

        self.work_io_1 = InfoClasses.TeamWork(io_group_1,
                                              [functools.partial(self.frame.m_textCtrl_mesh_limit.SetLabel,
                                                                 label=self.default_mesh_pattern),
                                               functools.partial(self.frame.m_textCtrl_mesh_limit.SetLabel,
                                                                 label=self.azur_lane_setting.mesh_limit.value)],
                                              [functools.partial(self.frame.m_textCtrl_tex_limit.SetLabel,
                                                                 self.default_tex_pattern),
                                               functools.partial(self.frame.m_textCtrl_tex_limit.SetLabel,
                                                                 self.azur_lane_setting.tex_limit.value)],
                                              )
        self.work_io_2 = InfoClasses.TeamWork(io_group_2, )

        self.divide_list: InfoClasses.PattenEdit = self.azur_lane_setting.divide_list

        self.change_input()
        self.change_div()

        self.default = default

        self.IsChange = False
        self.lock = self.default["lock"]
        self.export = self.default["export"]

        self.az_div_list = []

        self.index = len(self.az_div_list) + 1

        self.__choice = -1
        self.frame.m_bpButton_del.Enable(False)
        self.frame.m_bpButton_up.Enable(False)
        self.frame.m_bpButton_down.Enable(False)

        self.frame.m_bpButton6_default_mesh.Enable(False)
        # self.frame.m_bpButton_default_tex.Enable(False)

        self.tex_work = False
        self.mesh_work = False

        self.able_add = able_add

        self.frame.m_radioBox_im.Enable(False)

        self.frame.m_choice_type_in.Enable(False)
        self.frame.m_choice_type.Enable(False)

        self.names = {}

        # print(self.azur_lane_setting)

    def io_type_change(self, selection):
        if selection == 0:
            self.work_io_1(False)
            self.work_io_2(True)
        if selection == 1:
            self.work_io_1(True)
            self.work_io_2(False)
        else:
            pass

    def initial(self):
        self.azur_lane_setting.initial_val()
        self.full_setting.initial_val()
        self.io_type_change(self.azur_lane_setting.div_use.value)

    def change_work(self):
        self.azur_lane_setting.get_value()
        self.full_setting.get_value()

        # print(self.azur_lane_setting)
        # print(self.full_setting)
        self.lock = self.default['lock'] = self.frame.m_toggleBtn_lock.GetValue()

        if self.lock:
            self.default["azur_lane"]['default_tex_dir'] = self.frame.m_dirPicker_az_tex_dir.GetPath()
            self.default["azur_lane"]['default_mesh_dir'] = self.frame.m_dirPicker_az_mesh_dir.GetPath()

            self.default['export'] = self.frame.m_dirPicker_export.GetPath()

        with open(self.path + "\\files\\names.json", 'w')as file:
            json.dump(self.names, file)

    def lock_address(self):

        self.lock = self.default['lock'] = self.frame.m_toggleBtn_lock.GetValue()

        self.frame.m_dirPicker_export.Enable(not self.lock)

        self.frame.m_dirPicker_az_mesh_dir.Enable(not self.lock)
        self.frame.m_dirPicker_az_tex_dir.Enable(not self.lock)

    def choice(self, ):
        self.__choice = self.frame.m_checkList_az_limits.GetSelection()

        if self.__choice != 0:
            self.frame.m_bpButton_del.Enable(True)
        if self.__choice <= 1:
            self.frame.m_bpButton_up.Enable(False)
        else:
            self.frame.m_bpButton_up.Enable(True)
        if self.__choice == len(self.azur_lane_setting.divide_list) - 1 or self.__choice == 0:
            self.frame.m_bpButton_down.Enable(False)
        else:
            self.frame.m_bpButton_down.Enable(True)

    def change_div(self, ):

        if self.frame.m_radioBox_type_use.GetSelection() == 0:
            if self.frame.m_radioBox_az_div.GetSelection() == 2:

                self.frame.m_checkList_az_limits.Clear()
                self.frame.m_checkList_az_limits.Set([
                    r'1）其他：^.+$',
                    r'2）皮肤：^[a-zA-Z0-9_]+_\d$',
                    r'3）改造：^[a-zA-Z0-9_]+_[gG]$',
                    r'4）婚纱：^[a-zA-Z0-9_]+_[hH]$',
                    r'5）原皮：^[a-zA-Z0-9_]+$',
                ])
            else:
                self.frame.m_checkList_az_limits.Clear()

    def change_input(self, ):

        if self.frame.m_radioBox_type_use.GetSelection() == 0:
            choice = self.frame.m_radioBox_im.GetSelection()
            tex = [
                r'^.+\.[Pp][Nn][Gg]$',
                r'^[^_\s]+_\d\.[Pp][Nn][Gg]$',
                r'^[^_\s]+_[Hh]\.[Pp][Nn][Gg]$',
                r'^[^_\s]+_[Gg]\.[Pp][Nn][Gg]$',
                r'^[^_\s]+(_younv){0,1}\.[Pp][Nn][Gg]$',
            ]
            mesh = [
                r'^.+-mesh\.[oO][Bb][Jj]$',
                r'^[^_\s]+_\d-mesh\.[oO][Bb][Jj]$',
                r'^[^_\s]+_[Hh]-mesh\.[oO][Bb][Jj]$',
                r'^[^_\s]+_[Gg]-mesh\.[oO][Bb][Jj]$',
                r'^[^_\s]+(_younv){0,1}-mesh\.[oO][Bb][Jj]$',
            ]
            if choice == 0:
                self.frame.m_textCtrl_tex_limit.SetLabel(tex[0])
                self.frame.m_textCtrl_mesh_limit.SetLabel(mesh[0])
            elif choice == 1:
                self.frame.m_textCtrl_tex_limit.SetLabel(tex[1])
                self.frame.m_textCtrl_mesh_limit.SetLabel(mesh[1])
            elif choice == 2:
                self.frame.m_textCtrl_tex_limit.SetLabel(tex[2])
                self.frame.m_textCtrl_mesh_limit.SetLabel(mesh[2])
            elif choice == 3:
                self.frame.m_textCtrl_tex_limit.SetLabel(tex[3])
                self.frame.m_textCtrl_mesh_limit.SetLabel(mesh[3])
            elif choice == 4:
                self.frame.m_textCtrl_tex_limit.SetLabel(tex[4])
                self.frame.m_textCtrl_mesh_limit.SetLabel(mesh[4])
            else:
                pass
        self.frame.m_bpButton_defualt_tex.Enable(False)
        self.frame.m_bpButton6_default_mesh.Enable(False)

    def exit(self):
        var = {"azur_lane": self.azur_lane_setting.to_dict(), "full": self.full_setting.to_dict()}

        return var, self.default


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


class EditName(BaseWorkClass):
    def __init__(self,
                 parent: noname.MyDialog_Setting = ...,
                 info: InfoClasses.PerWorkList = ...,
                 start_path: str = ...
                 ):
        super().__init__(parent)

        self.start_path = start_path

        with open("%s\\files\\names.json" % self.start_path, 'r')as file:
            self.name_edit = InfoClasses.NamesEdit.form_dict(json.load(file))

        self.add_new_name = InfoClasses.NamesEdit.form_dict({})

        self.search = InfoClasses.NamesEdit()

        self.need_add = InfoClasses.NamesEdit(info.build_no_cn())

        self.finish_num = 0
        print(self.name_edit)

    def initial(self):
        self.change_name_init()
        self.add_init()

    def change_name_init(self):
        self.frame.m_listBox_change.Clear()
        self.frame.m_listBox_change.Set(self.name_edit.for_show)

    def change_name(self):

        index = self.frame.m_listBox_change.GetSelection()
        if not self.search:
            name = self.name_edit[index]
        else:
            name = self.search[index]

        writer = FrameClasses.Writer(self.frame, name)
        writer.ShowModal()
        if writer.is_able():
            value = writer.GetValue()

            self.name_edit.edit(value.name, value.val)
            if not self.search:
                index = self.name_edit.get_index(value)
            else:
                self.search.edit(value.name, value)
                index = self.search.get_index(value)

            self.frame.m_listBox_change.SetString(index, value.get_show(index))

    def searching(self):
        value = self.frame.m_searchCtrl2.GetValue()
        if value != '':

            indexes = function.find(value, self.name_edit.for_search)

            self.search = self.name_edit.build_search(indexes)
            self.frame.m_listBox_change.Clear()
            self.frame.m_listBox_change.Set(self.search.for_show)
        else:
            self.search.clear()
            self.frame.m_listBox_change.Clear()
            self.frame.m_listBox_change.Set(self.name_edit.for_show)

    def add_init(self):

        self.frame.m_listBox_new.Set(self.need_add.for_show)

    def open_add_name(self):
        index = self.frame.m_listBox_new.GetSelection()
        value = self.need_add[index]

        writer = FrameClasses.Writer(self.frame, value)
        writer.ShowModal()
        if writer.is_able():
            value = writer.GetValue()
            self.finish_num += 1
            self.need_add.set_self(value.name, value)
            index = self.need_add.get_index(value)

            self.frame.m_listBox_new.SetString(index, self.need_add[index].get_show(index + 1))
        else:
            self.finish_num -= 1

        scale = function.re_int(100 * (self.finish_num / len(self.need_add)))
        self.frame.m_gauge5.SetValue(scale)

    def add_new(self):
        dialog = FrameClasses.AddNewName(self.frame)
        dialog.ShowModal()
        if dialog.work:
            key, value = dialog.get_value()
            bo = self.add_new_name.append(key, value)

            if not bo:
                self.frame.m_listBox_new1.Append(self.add_new_name.for_show[-1])
            else:
                index = self.add_new_name.get_index(key)
                self.frame.m_listBox_new1.SetString(index, self.add_new_name.for_show[index])

    def del_name(self, index):
        dialog = wx.MessageBox(f'你确实要删除\n{self.name_edit[index]}吗？', '提示', wx.YES_NO)
        if dialog == wx.YES:

            self.add_new_name.del_name(index)

            self.frame.m_listBox_new1.Clear()
            self.frame.m_listBox_new1.Set(self.add_new_name.for_show)
        else:
            pass

    def edit_name(self, index):

        dialog = FrameClasses.AddNewName(self.frame, self.name_edit[index].name, self.name_edit[index])
        dialog.ShowModal()
        if dialog.work:
            key, value = dialog.get_value()
            self.add_new_name.edit(key, value)
            self.frame.m_listBox_new1.SetString(index, self.add_new_name.for_show[index])

    def get_change(self):
        return self.name_edit

    def exit(self):
        var = self.name_edit.form_dict()
        with open("%s\\files\\names.json" % self.start_path, 'w')as file:
            json.dump(var, file)

        return var


class FileDropLoad(wx.FileDropTarget):
    def __init__(self, work, parent):
        super(FileDropLoad, self).__init__()
        self.work = work
        self.parent = parent

    def OnDropFiles(self, x, y, filenames):
        try:
            func = functools.partial(self.work.drop_work, filenames)
            thread = threading.Thread(target=func)

            thread.start()
        except:
            return False
        else:
            return True
