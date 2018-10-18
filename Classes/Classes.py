import json
import os
import time
import win32clipboard

import win32con
import wx

from Classes import noname, SubClasses
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

        self.azur_line = SubClasses.AzurLaneWork(self)
        self.girl_front_line = SubClasses.GirlsFrontLine(self)
        self.start_path = os.getcwd()

        self.azur_lane_type = True

        self.girl_line_type = False

    # file load method
    # azur lane
    def load_tex(self, event):
        self.azur_line.load_tex()

    def load_Mesh(self, event):
        self.azur_line.load_mesh()

    def load_mesh_fold(self, event):

        self.azur_line.load_mesh_fold()

    def load_tex_fold(self, event):
        self.azur_line.load_tex_fold()

    def load_tex_and_mesh(self, event):
        self.azur_line.load_tex_and_mesh()

    # girl font line
    def load_rgb(self, event):
        self.girl_front_line.load_rgb()

    def load_alpha(self, event):
        self.girl_front_line.load_alpha()

    def load_RGB_fold(self, event):
        pass

    def load_alpha_fold(self, event):
        pass

    def load_rgb_alpha_fold(self, event):
        pass

    # choice
    def mesh_choice(self, event):
        self.azur_line.mesh_choice()

    def tex_choice(self, event):
        self.azur_line.tex_choice()

    def open_file(self, event):
        self.azur_line.open_file()

    def open_pass(self, event):
        self.azur_line.open_pass()

    # export
    def export_choice(self, event):
        if self.azur_line:
            self.azur_line.export_choice()

    def export_all(self, event):
        if self.azur_line:
            self.azur_line.export_all()

    def copy_file(self, event):
        if self.azur_line:
            self.azur_line.copy_file()

    # tools

    def add_new(self, event):
        dialog = AddDialog(self, self.azur_line.tex_name, self.names, self.start_path)

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
        self.azur_line.search_mesh()

    def search_tex(self, event):
        self.azur_line.search_tex()

    def search_pass(self, event):
        self.azur_line.search_pass()

    def search_unable(self, event):
        self.azur_line.search_unable()

    # else

    def exit_press(self, event):

        if self.azur_line.restore.is_alive():
            message = wx.MessageBox("还未全部完成，确认退出？", "警告", wx.YES_NO)

            if message == wx.YES:
                self.azur_line.restore.stop_(True)
                while self.azur_line.restore.is_alive():
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

    def close_press(self, event):

        if self.azur_line.restore.is_alive():
            message = wx.MessageBox("还未全部完成，确认退出？", "警告", wx.YES_NO)

            if message == wx.YES:
                if message == wx.YES:
                    self.azur_line.restore.stop_(True)
                    while self.azur_line.restore.is_alive():
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


class ShowPic(noname.MyDialog4):
    def __init__(self, father, pic: wx.Bitmap):
        noname.MyDialog4.__init__(self, father)

        self.pic = pic

    def show_pic(self, event):
        self.m_bitmap2.Bitmap(self, self.pic)


def main_part():
    app = wx.App(False)
    frame = CaleFrame(None)
    frame.Show()

    app.MainLoop()
