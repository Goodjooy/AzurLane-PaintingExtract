import json
import os
import time
import win32clipboard

import win32con
import wx

from Classes import noname, WorkClasses
from Functions import function


class CaleFrame(noname.MyFrame1):

    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)

        try:
            icon = wx.Icon("files\\icon.ico")
        except FileNotFoundError:
            pass
        else:
            self.SetIcon(icon)

        self.start_path = os.getcwd()

        self.start_path = os.getcwd()
        self.names = {}
        self.azur_lane_type = True

        self.girl_line_type = False

        with open("files\\setting.json", 'r')as file:
            setting_dic = json.load(file)
        self.setting_self = setting_dic
        self.azur_lane_div_type = setting_dic["azur_lane"]["div_type"]
        self.azur_lane_export_type = setting_dic["azur_lane"]["export_type"]
        self.azur_lane_new_dir = setting_dic["azur_lane"]["new_dir"]
        self.azur_lane_with_cn = setting_dic["azur_lane"]["export_with_cn"]

        self.girl_line_div_type = setting_dic["girl_line"]["div_type"]
        self.girl_line_export_type = setting_dic["girl_line"]["export_type"]
        self.girl_line_new_dir = setting_dic["girl_line"]["new_dir"]
        self.girl_line_check = setting_dic["girl_line"]["check_before_start"]

        self.open_dir_after_finish = setting_dic["full"]["open_dir"]
        self.skip_had = setting_dic["full"]["skip_had"]
        self.auto_open_choice_pic = setting_dic["full"]["auto_open"]
        self.finish_exit = setting_dic["full"]["finish_exit"]

        with open("files\\default.json", 'r')as file:
            self.default = json.load(file)

        self.azur_lane = WorkClasses.AzurLaneWork(self, setting=self.setting_self, default=self.default)
        self.girl_front_line = WorkClasses.GirlsFrontLine(self, setting=self.setting_self, default=self.default)

    # file load method
    # azur lane
    def load_tex(self, event):
        self.azur_lane.load_tex()

    def load_Mesh(self, event):
        self.azur_lane.load_mesh()

    def load_mesh_fold(self, event):

        self.azur_lane.load_mesh_fold()

    def load_tex_fold(self, event):
        self.azur_lane.load_tex_fold()

    def load_tex_and_mesh(self, event):
        self.azur_lane.load_tex_and_mesh()

    # girl font line
    def load_rgb(self, event):
        self.girl_front_line.load_rgb()

    def load_alpha(self, event):
        self.girl_front_line.load_alpha()

    def load_RGB_fold(self, event):
        self.girl_front_line.load_rgb_f()

    def load_alpha_fold(self, event):
        self.girl_front_line.load_alpha_f()

    def load_rgb_alpha_fold(self, event):
        self.girl_front_line.load_rgb_alpha_f()

    # choice
    def mesh_choice(self, event):
        self.azur_lane.mesh_choice()

    def tex_choice(self, event):
        self.azur_lane.tex_choice()

    def rgb_choice(self, event):
        self.girl_front_line.rgb_choice()

    def alpha_choice(self, event):
        self.girl_front_line.alpha_choice()

    def open_file(self, event):
        self.azur_lane.open_file()

    def open_pass(self, event):
        self.azur_lane.open_pass()

    # export
    def export_choice(self, event):
        if self.azur_lane_type and self.azur_lane.is_choice() is not None:
            self.azur_lane.export_choice()
        if self.girl_line_type and self.girl_front_line.is_choice() is not None:
            self.girl_front_line.export_choice()

    def export_all(self, event):
        title = '保存'
        if self.azur_lane.is_able():
            title += "-碧蓝航线"
        if self.girl_front_line.is_able():
            title += '-少女前线'
        if self.default['lock']:
            address = self.default['export']
        else:
            address = os.getcwd()
        dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            temp = dialog.GetPath()

            if self.azur_lane_type and self.azur_lane.is_able():
                self.azur_lane.export_all(temp)
            if self.girl_line_type and self.girl_front_line.is_able():
                self.girl_front_line.export_all(temp)
        else:
            pass

    def copy_file(self, event):
        if self.azur_lane_type:
            self.azur_lane.copy_file()

    # tools

    def add_new(self, event):
        dialog = AddDialog(self, self.azur_lane.tex_name, self.names, self.start_path)

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
        self.azur_lane.search_mesh()

    def search_tex(self, event):
        self.azur_lane.search_tex()

    def search_rgb(self, event):
        self.girl_front_line.search_rgb()

    def search_alpha(self, event):
        self.girl_front_line.search_alpha()

    def search_pass(self, event):
        self.azur_lane.search_pass()

    def search_unable(self, event):
        self.azur_lane.search_unable()

    # else

    def exit_press(self, event):

        self.exit()

    def close_press(self, event):

        self.exit()

    def azurlane_type(self, event):
        type_bool = not self.azur_lane_type
        self.m_menuItem_azurlane.Check(type_bool)
        self.azur_lane_type = type_bool
        self.__azur_lane_load(type_bool)

    def girl_line_type(self, event):

        type_bool = not self.girl_line_type
        self.m_menuItem_girl_line.Check(type_bool)
        self.girl_line_type = type_bool
        self.__girl_line_load(type_bool)

    def __azur_lane_load(self, open_able):
        self.m_menuItem_tex.Enable(open_able)
        self.m_menuItem_mesh.Enable(open_able)
        self.m_menuItem_mix.Enable(open_able)
        self.m_menuItem_meshonly.Enable(open_able)
        self.m_menuItem_texonly.Enable(open_able)

    def __girl_line_load(self, open_able):
        self.m_menuItem_rgb.Enable(open_able)
        self.m_menuItem_alpha.Enable(open_able)
        self.m_menuItem_rgb_a.Enable(open_able)
        self.m_menuItem_rgb_f.Enable(open_able)
        self.m_menuItem_alpha_f.Enable(open_able)

    def exit(self):
        with open("%s\\files\\setting.json" % self.start_path, 'w')as file_save:
            json.dump(self.setting_self, file_save)
            with open("%s\\files\\default.json" % self.start_path, 'w')as file_:
                json.dump(self.default, file_)
        if self.azur_lane.restore.is_alive():
            message = wx.MessageBox("还未全部完成，确认退出？", "警告", wx.YES_NO)

            if message == wx.YES:
                if message == wx.YES:
                    self.azur_lane.restore.stop_(True)
                    while self.azur_lane.restore.is_alive():
                        time.sleep(1)
                self.Destroy()
            else:
                pass
        else:
            message = wx.MessageBox("确认退出？", "提示", wx.YES_NO)
            if message == wx.YES:
                self.Destroy()
            elif message == wx.CANCEL:
                pass

    def setting(self, event):
        dialog = Setting(self, self.setting_self, self.default)
        temp = dialog.ShowModal()
        if temp == 0:
            if dialog.IsChange:
                setting_dic = dialog.GetValue()
                self.default = dialog.GetDefault()
                self.setting_self = setting_dic
                self.azur_lane_div_type = setting_dic["azur_lane"]["div_type"]
                self.azur_lane_export_type = setting_dic["azur_lane"]["export_type"]
                self.azur_lane_new_dir = setting_dic["azur_lane"]["new_dir"]

                self.girl_line_div_type = setting_dic["girl_line"]["div_type"]
                self.girl_line_export_type = setting_dic["girl_line"]["export_type"]
                self.girl_line_new_dir = setting_dic["girl_line"]["new_dir"]

                self.open_dir_after_finish = setting_dic["full"]["open_dir"]
                self.skip_had = setting_dic["full"]["skip_had"]
                self.auto_open_choice_pic = setting_dic["full"]["auto_open"]
                self.finish_exit = setting_dic["full"]["finish_exit"]

                self.azur_lane.update_setting(self.setting_self, self.default)
                self.girl_front_line.update_setting(self.setting_self, self.default)


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
        with open(f"{self.start_path}\\files\\names.json", 'w')as file:
            json.dump(self.names, file)

        self.Destroy()

    def close_save(self, event):
        with open(f"{self.start_path}\\files\\names.json", 'w')as file:
            json.dump(self.names, file)

        self.Destroy()


class Setting(noname.MyDialog_Setting):
    lock: bool

    def __init__(self, parent, setting_dic, default):
        super().__init__(parent=parent)

        self.azur_lane_div_type = setting_dic["azur_lane"]["div_type"]
        self.azur_lane_export_type = setting_dic["azur_lane"]["export_type"]
        self.azur_lane_new_dir = setting_dic["azur_lane"]["new_dir"]
        self.azur_lane_with_cn = setting_dic["azur_lane"]["export_with_cn"]

        self.girl_line_div_type = setting_dic["girl_line"]["div_type"]
        self.girl_line_export_type = setting_dic["girl_line"]["export_type"]
        self.girl_line_new_dir = setting_dic["girl_line"]["new_dir"]
        self.girl_line_check = setting_dic["girl_line"]["check_before_start"]

        self.open_dir_after_finish = setting_dic["full"]["open_dir"]
        self.skip_had = setting_dic["full"]["skip_had"]
        self.auto_open_choice_pic = setting_dic["full"]["auto_open"]
        self.finish_exit = setting_dic["full"]["finish_exit"]

        self.setting = setting_dic
        self.default = default

        self.azur_lane_default_tex_dir = self.default["azur_lane"]['default_tex_dir']
        self.azur_lane_default_mesh_dir = self.default["azur_lane"]['default_mesh_dir']

        self.girl_line_default_rgb_dir = self.default["girl_line"]['default_rgb_dir']
        self.girl_line_default_alpha_dir = self.default["girl_line"]['default_alpha_dir']

        self.IsChange = False
        self.lock = self.default["lock"]
        self.export = self.default["export"]

    def ok_click(self, event):
        self.change_work()
        self.IsChange = True
        self.Destroy()

    def apply_click(self, event):
        self.change_work()
        self.IsChange = True
        self.m_sdbSizer4Apply.Enable(False)

    def change(self, event):
        self.m_sdbSizer4Apply.Enable(True)

    def cancel_click(self, event):
        self.IsChange = False
        self.Destroy()

    def show_choice(self, event):
        self.m_radioBox_az_div.SetSelection(self.azur_lane_div_type)
        self.m_radioBox_az_type.SetSelection(self.azur_lane_export_type)
        self.m_checkBox_az_dir.SetValue(self.azur_lane_new_dir)
        self.m_checkBox_in_cn.SetValue(self.azur_lane_with_cn)

        self.m_dirPicker_az_tex_dir.SetPath(self.azur_lane_default_tex_dir)
        self.m_dirPicker_az_mesh_dir.SetPath(self.azur_lane_default_mesh_dir)

        self.m_radioBox_gfl_div.SetSelection(self.girl_line_div_type)
        self.m_radioBox_gfl_ex.SetSelection(self.girl_line_export_type)
        self.m_checkBox_gfl_dir.SetValue(self.girl_line_new_dir)
        self.m_checkBox_check.SetValue(self.girl_line_check)

        self.m_dirPicker_gl_alpha_dir.SetPath(self.girl_line_default_rgb_dir)
        self.m_dirPicker_gl_rbg_dir.SetPath(self.girl_line_default_alpha_dir)

        self.m_checkBox_autoopen.SetValue(self.open_dir_after_finish)
        self.m_checkBox_pass_finished.SetValue(self.skip_had)
        self.m_checkBox_open_temp.SetValue(self.auto_open_choice_pic)
        self.m_checkBox4_finish_exit.SetValue(self.finish_exit)

        self.m_dirPicker_export.SetPath(self.export)

        self.m_toggleBtn_lock.SetValue(self.lock)

    def change_work(self):
        self.setting["azur_lane"]["div_type"] = self.m_radioBox_az_div.GetSelection()
        self.setting["azur_lane"]["export_type"] = self.m_radioBox_az_type.GetSelection()
        self.setting["azur_lane"]["new_dir"] = self.m_checkBox_az_dir.GetValue()
        self.setting["azur_lane"]["export_with_cn"] = self.m_checkBox_in_cn.GetValue()

        self.setting["girl_line"]["div_type"] = self.m_radioBox_gfl_div.GetSelection()
        self.setting["girl_line"]["export_type"] = self.m_radioBox_gfl_ex.GetSelection()
        self.setting["girl_line"]["new_dir"] = self.m_checkBox_gfl_dir.GetValue()
        self.setting["girl_line"]["check_before_start"] = self.m_checkBox_check.GetValue()

        self.setting["full"]["open_dir"] = self.m_checkBox_autoopen.GetValue()
        self.setting["full"]["skip_had"] = self.m_checkBox_pass_finished.GetValue()
        self.setting["full"]["auto_open"] = self.m_checkBox_open_temp.GetValue()
        self.setting["full"]["finish_exit"] = self.m_checkBox4_finish_exit.GetValue()

        self.lock = self.default['lock'] = self.m_toggleBtn_lock.GetValue()

        if self.lock:
            self.default["azur_lane"]['default_tex_dir'] = self.m_dirPicker_az_tex_dir.GetPath()
            self.default["azur_lane"]['default_mesh_dir'] = self.m_dirPicker_az_mesh_dir.GetPath()

            self.default["girl_line"]['default_rgb_dir'] = self.m_dirPicker_gl_rbg_dir.GetPath()
            self.default["girl_line"]['default_alpha_dir'] = self.m_dirPicker_gl_alpha_dir.GetPath()

            self.default['export'] = self.m_dirPicker_export.GetPath()

    def lock_address(self, event):
        self.IsChange = True
        self.lock = self.default['lock'] = self.m_toggleBtn_lock.GetValue()

        self.m_dirPicker_export.Enable(not self.lock)

        self.m_dirPicker_az_mesh_dir.Enable(not self.lock)
        self.m_dirPicker_az_tex_dir.Enable(not self.lock)

        self.m_dirPicker_gl_rbg_dir.Enable(not self.lock)
        self.m_dirPicker_gl_alpha_dir.Enable(not self.lock)

    def GetValue(self):
        return self.setting

    def GetDefault(self):
        return self.default


def main_part():
    app = wx.App(False)
    frame = CaleFrame(None)
    frame.Show()

    app.MainLoop()
