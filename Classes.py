import os
import json
import noname
import function
import wx
import shutil
import win32clipboard
import win32con


class CaleFrame(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)

        self.file_dialog = None
        self.dir_dialog = None
        self.file_save = None
        self.dir_choice = None
        self.tex_name = []
        self.mesh_name = []
        self.tex_name_cn = []
        self.mesh_name_cn = []

        self.tex_list_path_dir = {}
        self.mesh_list_path_dir = {}

        self.choice = None

        with open('files\\names.json', 'r')as file:
            self.names = json.load(file)

        self.info_item = []

        self.pass_finish = True

        self.able_restore = 0
        self.able_restore_list = []
        self.disable_restore_list_show = []
        self.disable_restore_list = []

        self.index = 0

        self.passed = []
        self.passed_list = []

        self.save_path = ''
        self.save_path_list = []

        self.start = False
        self.info_item_update = False

        self.finished = False

        self.start_path = os.getcwd()

        self._searched_tex = []
        self._searched_mesh = []
        self._search_pass = []
        self._search_unable = []

        self.m_choice_pass.Enable(False)
        self.m_choice_unable.Enable(False)

        self.tex_search = False
        self.mesh_search = False
        self.pass_search = False
        self.unable_search = False

        self.search_mesh_show = []
        self.search_tex_show = []
        self.search_pass_show = []
        self.search_unable_show = []

        self.search_mesh_index = []
        self.search_tex_index = []
        self.search_pass_index = []
        self.search_unable_index = []

    # file load method
    def load_tex(self, event):
        self.file_dialog = wx.FileDialog(self, "打开", os.getcwd(), "AzurLane.png",
                                         "*.PNG", style=wx.FD_MULTIPLE)

        if self.file_dialog.ShowModal() == wx.ID_OK:

            self.m_staticText_load_tex.SetLabel("开始")
            self.m_gauge_tex_load.SetValue(0)
            paths = self.file_dialog.GetPaths()
            if not len(paths) == 0:
                num = 0
                for path in paths:
                    num += 1
                    name = path.split('\\')[-1].split('.')[0]

                    if name not in self.tex_name:
                        self.tex_name.append(name)
                        self.tex_list_path_dir[name] = path
                        try:
                            self.tex_name_cn.append(f"{num}）{self.names[name]}——{name}")
                            self._searched_tex.append(f"{self.names[name]}{name}")
                        except KeyError:
                            self.tex_name_cn.append(f"{num}）{name}——{name}")
                            self._searched_tex.append(f"{name}")

                    self.m_gauge_tex_load.SetValue(function.re_int(100 * (num / len(paths))))
                self.m_staticText_load_tex.SetLabel("完成")
            self.m_listBox_tex.Set(self.tex_name_cn)

        if self.able_export():
            self.m_menuItem_all.Enable(True)
        else:
            self.m_menuItem_all.Enable(False)
        if len(self.disable_restore_list) >= 1:
            self.m_menuItem_copy_only.Enable(True)
        else:
            self.m_menuItem_copy_only.Enable(False)

    def load_Mesh(self, event):
        self.file_dialog = wx.FileDialog(self, "打开", os.getcwd(),
                                         wildcard="*.OBJ", style=wx.FD_MULTIPLE)

        if self.file_dialog.ShowModal() == wx.ID_OK:
            self.m_staticText_mesh_load.SetLabel("开始")
            self.m_gauge_mesh_load.SetValue(0)
            paths = self.file_dialog.GetPaths()
            if not len(paths) == 0:
                num = 0
                for path in paths:

                    num += 1
                    name = path.split('\\')[-1].split('.')[0].split('-')
                    if name[-2] == 'ui':
                        name = name[0] + "-" + name[1]
                    else:
                        name = name[0]
                    if name not in self.mesh_name:
                        self.mesh_list_path_dir[name] = path
                        self.mesh_name.append(name)
                        try:
                            self.mesh_name_cn.append(f"{num}）{self.names[name]}——{name}")
                            self._searched_mesh.append(f"{self.names[name]}{name}")
                        except KeyError:
                            self.mesh_name_cn.append(f"{num}）{name}——{name}")
                            self._searched_mesh.append(f"{name}")

                    self.m_gauge_tex_load.SetValue(function.re_int(100 * (num / len(paths))))
                self.m_staticText_mesh_load.SetLabel("完成")

        self.m_listBox_mesh.Set(self.mesh_name_cn)
        if self.able_export():
            self.m_menuItem_all.Enable(True)
        else:
            self.m_menuItem_all.Enable(False)
        if len(self.disable_restore_list) >= 1:
            self.m_menuItem_copy_only.Enable(True)
        else:
            self.m_menuItem_copy_only.Enable(False)

    def load_mesh_fold(self, event):

        self.dir_dialog = wx.DirDialog(self, "打开", os.getcwd(),
                                       style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE |
                                             wx.DD_DIR_MUST_EXIST)

        if self.dir_dialog.ShowModal() == wx.ID_OK:
            paths = self.dir_dialog.GetPath()
            self.m_staticText_mesh_load.SetLabel("开始")
            self.m_gauge_mesh_load.SetValue(0)

            paths = function.all_file_path(paths)[1]
            self.m_gauge_mesh_load.SetValue(25)
            num = 0
            for path in paths.keys():
                if paths[path].split('.')[-1] == 'obj' or paths[path].split('.')[-1] == "OBJ":
                    path_old = path
                    path = path.split('.')[0].split('-')
                    if path[-2] == 'ui':
                        path = path[0] + "-" + path[1]
                    else:
                        path = path[0]

                    if path not in self.mesh_name:
                        self.mesh_list_path_dir[path] = paths[path_old]
                        self.mesh_name.append(path)
                        try:
                            self.mesh_name_cn.append(f"{num}）{self.names[path]}——{path}")
                            self._searched_mesh.append(f"{self.names[path]}{path}")
                        except KeyError:
                            self.mesh_name_cn.append(f"{num}）{path}——{path}")
                            self._searched_mesh.append(f"{path}")

                num += 1
                self.m_gauge_mesh_load.SetValue(25 + function.re_int(75 * (num / len(paths.keys()))))
            self.m_staticText_mesh_load.SetLabel("完成")
            self.m_listBox_mesh.Set(self.mesh_name_cn)
        if self.able_export():
            self.m_menuItem_all.Enable(True)
        else:
            self.m_menuItem_all.Enable(False)
        if len(self.disable_restore_list) >= 1:
            self.m_menuItem_copy_only.Enable(True)
        else:
            self.m_menuItem_copy_only.Enable(False)

    def load_tex_fold(self, event):
        self.dir_dialog = wx.DirDialog(self, "打开", os.getcwd(),
                                       style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE |
                                             wx.DD_DIR_MUST_EXIST)
        info = self.dir_dialog.ShowModal()
        if info == wx.ID_OK:
            self.m_staticText_load_tex.SetLabel("开始")
            paths = self.dir_dialog.GetPath()

            paths = function.all_file_path(paths)[1]
            self.m_gauge_tex_load.SetValue(25)
            num = 0
            for path in paths.keys():
                if paths[path].split('.')[-1] == 'png' or paths[path].split('.')[-1] == "PNG":
                    path_old = path
                    path = path.split('.')[0]
                    if path not in self.tex_name:
                        self.tex_list_path_dir[path] = paths[path_old]
                        self.tex_name.append(path)
                        try:
                            self.tex_name_cn.append(f"{num}）{self.names[path]}——{path}")
                            self._searched_tex.append(f"{self.names[path]}{path}")
                        except KeyError:
                            self.tex_name_cn.append(f"{num}）{path}——{path}")
                            self._searched_tex.append(f"{path}")
                num += 1
                self.m_gauge_tex_load.SetValue(25 + function.re_int(75 * (num / len(paths.keys()))))
        self.m_staticText_load_tex.SetLabel("完成")

        self.m_listBox_tex.Set(self.tex_name_cn)
        if self.able_export():
            self.m_menuItem_all.Enable(True)
        else:
            self.m_menuItem_all.Enable(False)
        if len(self.disable_restore_list) >= 1:
            self.m_menuItem_copy_only.Enable(True)
        else:
            self.m_menuItem_copy_only.Enable(False)

    def load_tex_and_mesh(self, event):
        self.dir_dialog = wx.DirDialog(self, "打开", os.getcwd(),
                                       style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE |
                                             wx.DD_DIR_MUST_EXIST)

        if self.dir_dialog.ShowModal() == wx.ID_OK:
            paths = self.dir_dialog.GetPath()
            self.m_staticText_load_tex.SetLabel('开始')
            self.m_staticText_mesh_load.SetLabel('开始')

            paths = function.all_file_path(paths)[1]

            self.m_gauge_tex_load.SetValue(25)
            self.m_gauge_mesh_load.SetValue(25)
            tex_num = mesh_num = 0
            for path in paths.keys():
                # Mesh
                if paths[path].split('.')[-1] == 'obj' or paths[path].split('.')[-1] == "OBJ":
                    path_old = path
                    path = path.split('.')[0].split('-')
                    if path[-2] == 'ui':
                        path = path[0] + "-" + path[1]
                    else:
                        path = path[0]

                    if path not in self.mesh_name:
                        self.mesh_list_path_dir[path] = paths[path_old]
                        self.mesh_name.append(path)
                        try:
                            self.mesh_name_cn.append(f"{mesh_num}）{self.names[path]}——{path}")
                            self._searched_mesh.append(f"{self.names[path]}{path}")
                        except KeyError:
                            self.mesh_name_cn.append(f"{mesh_num}）{path}——{path}")
                            self._searched_mesh.append(f"{path}")

                    mesh_num += 1
                    self.m_gauge_mesh_load.SetValue(25 + function.re_int(75 * (mesh_num / len(paths.keys()))))
                    break
                # texture2D
                if paths[path].split('.')[-1] == 'png' or paths[path].split('.')[-1] == "PNG":
                    path_old = path
                    path = path.split('.')[0]
                    if path not in self.tex_name:
                        self.mesh_list_path_dir[path] = paths[path_old]
                        self.mesh_name.append(path)
                        try:
                            self.tex_name_cn.append(f"{tex_num}）{self.names[path]}——{path}")
                            self._searched_tex.append(f"{self.names[path]}{path}")
                        except KeyError:
                            self.tex_name_cn.append(f"{tex_num}）{path}——{path}")
                            self._searched_tex.append(f"{path}")

                    tex_num += 1
                    self.m_gauge_tex_load.SetValue(25 + function.re_int(75 * (tex_num / len(paths.keys()))))
                    break
            self.m_gauge_tex_load.SetValue(100)
            self.m_gauge_mesh_load.SetValue(100)

            self.m_listBox_tex.Set(self.tex_name_cn)
            self.m_listBox_mesh.Set(self.mesh_name_cn)
        if self.able_export():
            self.m_menuItem_all.Enable(True)
        else:
            self.m_menuItem_all.Enable(False)

        if len(self.disable_restore_list) >= 1:
            self.m_menuItem_copy_only.Enable(True)
        else:
            self.m_menuItem_copy_only.Enable(False)

    # choice
    def mesh_choice(self, event):
        if self.mesh_search:
            self.choice = self.mesh_name[self.search_mesh_index[self.m_listBox_mesh.GetSelection()]]
        else:
            self.choice = self.mesh_name[self.m_listBox_mesh.GetSelection()]
        if self.choice in self.tex_name:
            self.m_menuItem_choice.Enable(True)

    def tex_choice(self, event):
        if self.tex_search:
            self.choice = self.tex_name[self.search_tex_index[self.m_listBox_tex.GetSelection()]]
        else:
            self.choice = self.tex_name[self.m_listBox_tex.GetSelection()]
        if self.choice in self.mesh_name:
            self.m_menuItem_choice.Enable(True)

    def open_file(self, event):
        if self.unable_search:
            index = self.search_unable_index[self.m_listBox_unable.GetSelection()]
        else:
            index = self.m_listBox_unable.GetSelection()
        path = self.tex_list_path_dir[self.disable_restore_list[index]]
        os.system("start %s" % path)

    def open_pass(self, event):
        name = ''
        if self.pass_search:
            index = self.search_pass_index[self.m_listBox_info.GetSelection()]
        else:
            index = self.m_listBox_info.GetSelection()
        for guide in self.names.keys():
            if guide == self.passed_list[index]:
                name = f"{self.names[guide]}.png"
        try:
            path = self.save_path_list[1][name]
        except KeyError:
            name = name[:-4] + ".PNG"
            path = self.save_path_list[1][name]
        os.system(u"start " + path)

    # export
    def export_choice(self, event):
        self.file_save = wx.FileDialog(self, "保存", os.getcwd(), self.names[self.choice], "*.png", style=wx.FD_SAVE)

        if self.file_save.ShowModal() == wx.ID_OK:
            self.m_gauge_now.SetValue(0)
            self.m_gauge_all.SetValue(0)
            self.save_path = self.file_save.GetPath()

            function.restore_tool_one(self.mesh_list_path_dir[self.choice], self.tex_list_path_dir[self.choice],
                                      self.save_path,
                                      self.m_gauge_now)

        self.m_gauge_all.SetValue(100)
        if self.m_checkBox_autoopen.GetValue():
            os.system("start %s" % self.save_path)

    def export_all(self, event):
        self.dir_choice = wx.DirDialog(self,
                                       "选择文件夹",
                                       os.getcwd(),
                                       style=wx.DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE
                                             | wx.DD_DIR_MUST_EXIST)

        if self.dir_choice.ShowModal() == wx.ID_OK:
            self.restart()
            self.save_path = self.dir_choice.GetPath()
            self.m_gauge_all.SetValue(0)

            self.able_restore_list = list(set(self.able_restore_list))

            if self.m_checkBox_pass_finished.GetValue():
                self.save_path_list = function.all_file_path(self.save_path)

                num = 1
                able_restore = self.able_restore_list.copy()
                for able in self.able_restore_list:
                    if f"{self.names[able]}.png" in self.save_path_list[1].keys() or \
                            f"{self.names[able]}.PNG" in self.save_path_list[1].keys():
                        self.passed.append('%s——%s,第%d个' % (self.names[able], able, num))
                        self.passed_list.append(able)
                        self._search_pass.append(f"{able}{self.names[able]}")
                        num += 1
                        able_restore.remove(able)
                self.able_restore_list = able_restore
            self.m_listBox_info.Clear()
            self.m_listBox_info.Set(self.passed)

            self.start = True
            self.m_timer_restore.Start(250)

    def copy_file(self, event):
        self.file_save = wx.DirDialog(self, "保存", os.getcwd(),
                                      style=wx.DD_DIR_MUST_EXIST |
                                            wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON | wx.DD_DEFAULT_STYLE)
        if self.file_save.ShowModal() == wx.ID_OK:
            path = self.file_save.GetPath()
            num = 0
            self.m_gauge_all.SetValue(0)
            for name in self.disable_restore_list:
                num += 1
                self.m_gauge_now.SetValue(0)
                shutil.copyfile(self.tex_list_path_dir[name], f'{path}\\{self.names[name]}.png')
                self.m_gauge_now.SetValue(100)
                self.m_gauge_all.SetValue(function.re_int(100 * (num / len(self.disable_restore_list))))

            if self.m_checkBox_autoopen.GetValue():
                os.system(self.save_path)

    # restore
    def restore_way(self, event):

        if self.start and self.index < len(self.able_restore_list):
            self.m_timer_restore.Stop()
            name = self.able_restore_list[self.index]
            self.m_staticText_now.SetLabel("当前：%s" % self.names[name])
            self.m_gauge_now.SetValue(0)

            function.restore_tool(name, self.names, self.mesh_list_path_dir, self.tex_list_path_dir, self.save_path)
            self.m_gauge_now.SetValue(100)
            val_percent = str(round(100 * (self.index / len(self.able_restore_list)), 2))
            val = function.re_int(100 * (self.index / len(self.able_restore_list)))
            self.m_staticText_all.SetLabel("总进度：%s %%" % val_percent)
            self.m_gauge_all.SetValue(val)
            self.index += 1
            self.m_timer_restore.Start(250)
        elif self.start and self.index >= len(self.able_restore_list):
            self.m_gauge_all.SetValue(100)

            self.m_staticText_all.SetLabel("总进度：%s %%" % '100')
            self.start = False
            self.m_timer_restore.Stop()

            if self.m_checkBox_autoopen.GetValue():
                os.system(u"start %s" % self.save_path)

    # tool

    def add_new(self, event):
        dialog = AddDialog(self, self.tex_name, self.names, self.start_path)

        if dialog.ShowModal() == 0:
            with open(self.start_path + '\\files\\names.json', 'r')as file:
                self.names = json.load(file)

    def compare(self, event):
        compare = CompareDialog(self)

        if compare.ShowModal() == 0:
            pass

    def change_name(self, event):
        dialog = ChangeNameDialog(self, self.start_path)
        if dialog.ShowModal() == 0:
            with open(self.start_path + '\\files\\names.json', 'r')as file:
                self.names = json.load(file)

    # search
    def search_mesh(self, event):
        value = self.m_searchCtrl_mesh.GetValue()
        if value != '':
            indexes = function.find(value, self._searched_mesh)

            self.mesh_search = True

            self.search_mesh_show.clear()
            self.search_mesh_index.clear()

            for index in indexes:
                self.search_mesh_show.append(self.mesh_name_cn[index])
                self.search_mesh_index.append(index)

            self.m_listBox_mesh.Clear()
            self.m_listBox_mesh.Set(self.search_mesh_show)
        else:
            self.mesh_search = False
            self.m_listBox_mesh.Clear()
            self.m_listBox_mesh.Set(self.mesh_name_cn)

    def search_tex(self, event):
        value = self.m_searchCtrl_tex.GetValue()
        if value != '':
            indexes = function.find(value, self._searched_tex)
            self.tex_search = True

            self.search_tex_show.clear()
            self.search_tex_index.clear()

            for index in indexes:
                self.search_tex_show.append(self.tex_name_cn[index])
                self.search_tex_index.append(index)

            self.m_listBox_tex.Clear()
            self.m_listBox_tex.Set(self.search_tex_show)
        else:
            self.tex_search = False
            self.m_listBox_tex.Clear()
            self.m_listBox_tex.Set(self.tex_name_cn)

    def search_pass(self, event):
        value = self.m_searchCtrl_pass.GetValue()
        if value != '':
            indexes = function.find(value, self._search_pass)

            self.pass_search = True

            self.search_pass_index.clear()
            self.search_pass_show.clear()

            for index in indexes:
                self.search_pass_show.append(self.passed[index])
                self.search_pass_index.append(index)

            self.m_listBox_info.Clear()
            self.m_listBox_info.Set(self.search_pass_show)
        else:
            self.pass_search = False
            self.m_listBox_info.Clear()
            self.m_listBox_info.Set(self.passed)

    def search_unable(self, event):
        value = self.m_searchCtrl_unable.GetValue()
        if value != "":
            indexes = function.find(value, self._search_unable)

            self.unable_search = True

            self.search_unable_index.clear()
            self.search_unable_show.clear()

            for index in indexes:
                self.search_unable_show.append(self.disable_restore_list_show[index])
                self.search_unable_index.append(index)

            self.m_listBox_unable.Clear()
            self.m_listBox_unable.Set(self.search_unable_show)
        else:
            self.unable_search = False
            self.m_listBox_unable.Clear()
            self.m_listBox_unable.Set(self.disable_restore_list_show)

    # else

    def able_export(self):
        for name in self.mesh_name:
            if name in self.tex_name:
                self.able_restore += 1
                self.able_restore_list.append(name)
        if self.able_restore >= 1:
            num = 0
            self.disable_restore_list = []
            self.disable_restore_list_show.clear()
            for name in self.tex_name:
                if name not in self.mesh_name:
                    num += 1
                    self.disable_restore_list_show.append("%d） %s" % (num, self.names[name]))
                    self.disable_restore_list.append(name)
                    self._search_unable.append(f"{name}{self.names[name]}")

            self.m_listBox_unable.Clear()
            self.m_listBox_unable.Set(self.disable_restore_list_show)

        if len(self.tex_name) >= 1:
            self.m_menuItem_add.Enable(True)
        else:
            self.m_menuItem_add.Enable(False)

        return self.able_restore >= 1

    def restart(self):
        self.index = 0
        self.passed = []
        self.passed_list = []
        self._search_pass.clear()

        for name in self.mesh_name:
            if name in self.tex_name:
                self.able_restore += 1
                self.able_restore_list.append(name)

        self.m_staticText_all.SetLabel("总进度：%s %%" % '0')
        self.m_gauge_all.SetValue(0)

    def exit_press(self, event):
        self.Destroy()


class AddDialog(noname.MyDialog_add_new):
    def __init__(self, parent, name_list, names, start_path):
        noname.MyDialog_add_new.__init__(self, parent)

        self.name_list = name_list
        self.need_add = []
        self.need_add_show = []
        self.finish_num = 0

        self.start_path = start_path

        self.names = names

    def save_new_dic(self, event):
        with open(self.start_path + "\\files\\names.json", 'w')as file:
            json.dump(self.names, file)
        self.Destroy()

    def show_info(self, event):
        for name in self.name_list:
            if name not in self.names.keys():
                self.need_add.append(name)
                self.need_add_show.append("%s: " % name)

        self.m_listBox5.Set(self.need_add_show)

    def open_add_name(self, event):
        index = self.m_listBox5.GetSelection()
        value = self.need_add[index]
        if value in self.names.keys():
            value_cn = self.names[value]
        else:
            value_cn = ''

        writer = Writer(self, value, value_cn)
        bool_er = writer.ShowModal()
        if bool_er == 0:
            name = writer.GetValue()
            if name != '':
                self.finish_num += 1
            elif value in self.names.keys() and name == '':
                self.finish_num -= 1
            self.names[value] = name
            self.need_add_show[index] = "%s：%s" % (self.need_add[index], name)

            self.m_listBox5.Clear()
            self.m_listBox5.Set(self.need_add_show)
        scale = function.re_int(100 * (self.finish_num / len(self.need_add)))
        self.m_gauge5.SetValue(scale)

    def close_save(self, event):

        with open(self.start_path + "\\files\\names.json", 'w')as file:
            json.dump(self.names, file)
        self.Destroy()


class Writer(noname.MyDialog_enter_name):

    def __init__(self, parent, name, name_cn):
        noname.MyDialog_enter_name.__init__(self, parent)

        self.name = name
        self.name_cn = name_cn

    def show_name(self, event):
        self.m_staticText8.SetLabel("%s: " % self.name)
        self.m_textCtrl2.SetValue(self.name_cn)

    def save_name(self, event):
        self.name_cn = self.m_textCtrl2.GetValue()
        self.Destroy()

    def GetValue(self):
        return self.name_cn


class CompareDialog(noname.MyDialog_compare):
    def __init__(self, parent):
        noname.MyDialog_compare.__init__(self, parent)

        self.old_fold = ''
        self.new_fold = ''

        self.old_fold_list = []
        self.new_fold_list = []

        self._new_add = []
        self._new_add_show = []

    def close_the_tool(self, event):
        self.Destroy()

    def writer_into(self, event):
        index = self.m_listBox9.GetSelection()

        info = self._new_add[index]

        win32clipboard.OpenClipboard()

        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, info)
        win32clipboard.CloseClipboard()

    def test(self, event):
        if self.m_dirPicker6.GetPath() != '':
            self.new_fold = self.m_dirPicker6.Path
            self.new_fold_list = function.all_file_path(self.new_fold)
        if self.m_dirPicker_old.GetPath() != '':
            self.old_fold = self.m_dirPicker_old.GetPath()
            self.old_fold_list = function.all_file_path(self.old_fold)

        if self.new_fold != '' and self.old_fold != '':
            self.compare()

            self.m_timer2.Stop()

    def compare(self):
        num = 0
        for name in self.old_fold_list[0]:
            name_old = name
            name = name[len(self.old_fold) + 1:]
            name = "%s\\%s" % (self.new_fold, name)

            if name not in self.new_fold_list[0]:
                num += 1
                if name not in self._new_add:
                    self._new_add.append(name_old)
                    self._new_add_show.append("%d） %s" % (num, name_old))
                    self.m_listBox9.Clear()
                    self.m_listBox9.Set(self._new_add_show)


class ChangeNameDialog(noname.MyDialog_change_name):
    def __init__(self, parent, start_path):
        noname.MyDialog_change_name.__init__(self, parent)

        self.start_path = start_path

        with open("%s\\files\\names.json" % self.start_path, 'r')as file:
            self.names = json.load(file)

        self.show_list = []
        self.key_list = []
        self.searched_list = []

        self.searched_show = []
        self.search_list = []

        self.searched = False

    def show_all(self, event):
        num = 0
        for index in self.names.keys():
            num += 1
            self.show_list.append("%d）\t%s：%s" % (num, index, self.names[index]))
            self.key_list.append(index)
            self.searched_list.append("%s%s" % (index, self.names[index]))
        self.m_listBox7.Clear()
        self.m_listBox7.Set(self.show_list)

    def change_name(self, event):
        index = self.m_listBox7.GetSelection()
        if not self.searched:
            name = self.key_list[index]
        else:
            name = self.search_list[index]
        name_cn = self.names[name]

        writer = Writer(self, name, name_cn)

        if writer.ShowModal() == 0:
            name_cn = writer.GetValue()

            self.names[name] = name_cn
            num = 0
            self.show_list.clear()
            self.key_list.clear()
            for index in self.names.keys():
                num += 1
                self.show_list.append("%d）\t%s：%s" % (num, index, self.names[index]))
                self.key_list.append(index)
            self.m_listBox7.Clear()
            self.m_listBox7.Set(self.show_list)

    def searching(self, event):
        value = self.m_searchCtrl2.GetValue()
        if value != '':
            indexes = function.find(value, self.searched_list)
            self.searched_show.clear()
            self.search_list.clear()
            for index in indexes:
                self.searched_show.append(self.show_list[index])
                self.search_list.append(self.key_list[index])

        else:
            self.searched_show = self.show_list
            self.search_list = self.key_list
        self.searched = True
        self.m_listBox7.Clear()
        self.m_listBox7.Set(self.searched_show)

    def save_change(self, event):
        with open(f"{self.start_path}\\files\\names", 'w')as file:
            json.dump(self.names, file)

        self.Destroy()

    def close_save(self, event):
        with open(f"{self.start_path}\\files\\names", 'w')as file:
            json.dump(self.names, file)

        self.Destroy()


def main_part():
    app = wx.App(False)
    frame = CaleFrame(None)
    frame.Show()

    app.MainLoop()
