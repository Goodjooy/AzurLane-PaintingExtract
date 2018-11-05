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

        self.names = {}


        with open("files\\setting.json", 'r')as file:
            setting_dic = json.load(file)
        self.setting_self = setting_dic
        self.azur_lane_div_type = setting_dic["azur_lane"]["div_type"]
        self.azur_lane_export_type = setting_dic["azur_lane"]["export_type"]
        self.azur_lane_new_dir = setting_dic["azur_lane"]["new_dir"]
        self.azur_lane_with_cn = setting_dic["azur_lane"]["export_with_cn"]

        self.open_dir_after_finish = setting_dic["full"]["open_dir"]
        self.skip_had = setting_dic["full"]["skip_had"]
        self.auto_open_choice_pic = setting_dic["full"]["auto_open"]
        self.finish_exit = setting_dic["full"]["finish_exit"]

        with open("files\\default.json", 'r')as file:
            self.default = json.load(file)

        self.azur_lane = WorkClasses.AzurLaneWork(self, setting=self.setting_self, default=self.default)

        self.m_button_gui.Enable(False)

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

    # choice
    def mesh_choice(self, event):
        self.azur_lane.mesh_choice()

    def tex_choice(self, event):
        self.azur_lane.tex_choice()

    def open_file(self, event):
        self.azur_lane.open_file()

    def open_pass(self, event):
        self.azur_lane.open_pass()

    # export
    def export_choice(self, event):
        if self.azur_lane_type and self.azur_lane.is_choice() is not None:
            self.azur_lane.export_choice()

    def export_all(self, event):
        title = '保存'
        if self.azur_lane.is_able():
            title += "-碧蓝航线"
        if self.default['lock']:
            address = self.default['export']
        else:
            address = os.getcwd()
        dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            temp = dialog.GetPath()

            if self.azur_lane_type and self.azur_lane.is_able():
                self.azur_lane.export_all(temp)

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

    def __azur_lane_load(self, open_able):
        self.m_menuItem_tex.Enable(open_able)
        self.m_menuItem_mesh.Enable(open_able)
        self.m_menuItem_mix.Enable(open_able)
        self.m_menuItem_meshonly.Enable(open_able)
        self.m_menuItem_texonly.Enable(open_able)

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

    def change_size(self, event):
        pass

    def helper(self, event):
        dialog = Pattern()
        dialog.Show()

    def setting(self, event):
        dialog = Setting(self, self.setting_self, self.default, self.start_path)
        temp = dialog.ShowModal()
        if temp == 0:
            if dialog.IsChange:
                setting_dic = dialog.GetValue()
                self.default = dialog.GetDefault()
                self.setting_self = setting_dic
                self.azur_lane_div_type = setting_dic["azur_lane"]["div_type"]
                self.azur_lane_export_type = setting_dic["azur_lane"]["export_type"]
                self.azur_lane_new_dir = setting_dic["azur_lane"]["new_dir"]

                self.open_dir_after_finish = setting_dic["full"]["open_dir"]
                self.skip_had = setting_dic["full"]["skip_had"]
                self.auto_open_choice_pic = setting_dic["full"]["auto_open"]
                self.finish_exit = setting_dic["full"]["finish_exit"]

                self.azur_lane.update_setting(self.setting_self, self.default)


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

    def __init__(self, parent, setting_dic, default, def_path):
        super().__init__(parent=parent)

        self.path = def_path
        temp = wx.Image('%s\\files\\bg_story_litang.png' % self.path, wx.BITMAP_TYPE_PNG)
        temp = temp.ConvertToBitmap()
        print(self.m_bitmap2.GetSize())
        self.m_bitmap2.SetBitmap(temp)

        self.azur_lane_div_type = setting_dic["azur_lane"]["div_type"]
        self.azur_lane_export_type = setting_dic["azur_lane"]["export_type"]
        self.azur_lane_new_dir = setting_dic["azur_lane"]["new_dir"]

        self.azur_lane_use_default = setting_dic["azur_lane"]['div_use']

        self.azur_lane_with_cn = setting_dic["azur_lane"]["export_with_cn"]

        self.azur_lane_tex_limit = setting_dic["azur_lane"]['tex_limit']
        self.azur_lane_mesh_limit = setting_dic["azur_lane"]['mesh_limit']

        self.azur_lane_divide_list = setting_dic["azur_lane"]['divide_list']

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

        self.az_div_list = []
        self.reset_az_pattern()
        self.index = len(self.az_div_list) + 1

        self.__choice = -1
        self.m_bpButton_del.Enable(False)
        self.m_bpButton_up.Enable(False)
        self.m_bpButton_down.Enable(False)

        self.m_bpButton6_default_mesh.Enable(False)
        self.m_bpButton_defualt_tex.Enable(False)

        self.default_tex_pattern = "^.+\\.[pP][Nn][Gg]$"
        self.default_mesh_pattern = "^.+-mesh\\.[oO][Bb][jJ]$"

        self.tex_work = False
        self.mesh_work = False

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
        self.az_show(event)

        self.m_checkBox_autoopen.SetValue(self.open_dir_after_finish)
        self.m_checkBox_pass_finished.SetValue(self.skip_had)
        self.m_checkBox_open_temp.SetValue(self.auto_open_choice_pic)
        self.m_checkBox4_finish_exit.SetValue(self.finish_exit)

        self.m_dirPicker_export.SetPath(self.export)

        self.m_toggleBtn_lock.SetValue(self.lock)

        self.change_div(event)

    def change_work(self):
        self.setting["azur_lane"]["div_type"] = self.m_radioBox_az_div.GetSelection()
        self.setting["azur_lane"]["export_type"] = self.m_radioBox_az_type.GetSelection()
        self.setting['azur_lane']['div_use'] = self.m_radioBox_type_use.GetSelection()

        self.setting["azur_lane"]["new_dir"] = self.m_checkBox_az_dir.GetValue()
        self.setting["azur_lane"]["export_with_cn"] = self.m_checkBox_in_cn.GetValue()

        self.setting['azur_lane']['tex_limit'] = self.m_textCtrl_tex_limit.GetValue()
        self.setting['azur_lane']['mesh_limit'] = self.m_textCtrl_mesh_limit.GetValue()
        self.setting['azur_lane']['divide_list'] = self.azur_lane_divide_list

        self.setting["full"]["open_dir"] = self.m_checkBox_autoopen.GetValue()
        self.setting["full"]["skip_had"] = self.m_checkBox_pass_finished.GetValue()
        self.setting["full"]["auto_open"] = self.m_checkBox_open_temp.GetValue()
        self.setting["full"]["finish_exit"] = self.m_checkBox4_finish_exit.GetValue()

        self.lock = self.default['lock'] = self.m_toggleBtn_lock.GetValue()

        if self.lock:
            self.default["azur_lane"]['default_tex_dir'] = self.m_dirPicker_az_tex_dir.GetPath()
            self.default["azur_lane"]['default_mesh_dir'] = self.m_dirPicker_az_mesh_dir.GetPath()

            self.default['export'] = self.m_dirPicker_export.GetPath()

    def lock_address(self, event):
        self.IsChange = True
        self.lock = self.default['lock'] = self.m_toggleBtn_lock.GetValue()

        self.m_dirPicker_export.Enable(not self.lock)

        self.m_dirPicker_az_mesh_dir.Enable(not self.lock)
        self.m_dirPicker_az_tex_dir.Enable(not self.lock)

    def az_add(self, event):
        dialog = AddPattern(self, self.index)

        dialog.ShowModal()
        if dialog.is_ok:
            self.index += 1
            index, name, dir_path, pattern = dialog.get()
            self.azur_lane_divide_list.append({'name': name, 'dir': dir_path, 'pattern': pattern})

            self.m_checkList_az_limits.Clear()
            self.reset_az_pattern()
            self.m_checkList_az_limits.Set(self.az_div_list)

    def az_del(self, event):
        self.m_checkList_az_limits.Clear()
        if self.azur_lane_divide_list[self.__choice]['name'] == 'else':
            pass
        else:
            del self.azur_lane_divide_list[self.__choice]

        self.m_bpButton_del.Enable(False)
        self.m_bpButton_up.Enable(False)
        self.m_bpButton_down.Enable(False)
        self.reset_az_pattern()
        self.m_checkList_az_limits.Set(self.az_div_list)

    def choice(self, event):
        self.__choice = self.m_checkList_az_limits.GetSelection()

        if self.__choice != 0:
            self.m_bpButton_del.Enable(True)
        if self.__choice <= 1:
            self.m_bpButton_up.Enable(False)
        else:
            self.m_bpButton_up.Enable(True)
        if self.__choice == len(self.azur_lane_divide_list) - 1 or self.__choice == 0:
            self.m_bpButton_down.Enable(False)
        else:
            self.m_bpButton_down.Enable(True)

    def change_type(self, event):
        self.change(event)

        self.az_type_use(event)

    def change_div(self, event):
        if self.m_radioBox_type_use.GetSelection() == 0:
            if self.m_radioBox_az_div.GetSelection() == 2:
                self.change(event)
                self.m_checkList_az_limits.Clear()
                self.m_checkList_az_limits.Set([
                    r'1）其他：^.+$',
                    r'2）皮肤：^[a-zA-Z0-9_]+_\d$',
                    r'3）改造：^[a-zA-Z0-9_]+_[gG]$',
                    r'4）婚纱：^[a-zA-Z0-9_]+_[hH]$',
                    r'5）原皮：^[a-zA-Z0-9_]+$',
                ])
            else:
                self.m_checkList_az_limits.Clear()

    def change_pattern(self, event):
        index_2 = self.m_checkList_az_limits.GetSelection()
        dialog = AddPattern(self, index_2 + 1, self.azur_lane_divide_list[index_2]['name'],
                            self.azur_lane_divide_list[index_2]['pattern'], self.azur_lane_divide_list[index_2]['dir'])
        dialog.ShowModal()
        if dialog.is_ok:
            index, name, dir_path, pattern = dialog.get()
            self.azur_lane_divide_list[index_2] = ({'name': name, 'dir': dir_path, 'pattern': pattern})

            self.m_checkList_az_limits.Clear()
            self.reset_az_pattern()
            self.m_checkList_az_limits.Set(self.az_div_list)

    def az_up(self, event):

        temp = self.azur_lane_divide_list[self.__choice - 1]

        self.azur_lane_divide_list[self.__choice - 1] = self.azur_lane_divide_list[self.__choice]

        self.azur_lane_divide_list[self.__choice] = temp

        self.change(event)

        self.reset_az_pattern()
        self.m_checkList_az_limits.Clear()
        self.m_checkList_az_limits.Set(self.az_div_list)

        self.__choice -= 1
        self.m_checkList_az_limits.SetSelection(self.__choice)

        self.choice(event)

    def az_down(self, event):
        temp = self.azur_lane_divide_list[self.__choice + 1]

        self.azur_lane_divide_list[self.__choice + 1] = self.azur_lane_divide_list[self.__choice]

        self.azur_lane_divide_list[self.__choice] = temp

        self.change(event)

        self.reset_az_pattern()
        self.m_checkList_az_limits.Clear()
        self.m_checkList_az_limits.Set(self.az_div_list)

        self.__choice += 1
        self.m_checkList_az_limits.SetSelection(self.__choice)

        self.choice(event)

    def default_mesh(self, event):
        self.change(event)

        self.m_textCtrl_mesh_limit.SetLabel(self.default_mesh_pattern)
        self.mesh_work = True

    def default_tex(self, event):
        self.change(event)

        self.m_textCtrl_tex_limit.SetLabel(self.default_tex_pattern)
        self.tex_work = True

    def change_reset_mesh(self, event):
        self.change(event)
        if self.mesh_work:
            self.mesh_work = False
        else:
            self.m_bpButton6_default_mesh.Enable(True)

    def change_reset_tex(self, event):
        self.change(event)
        if self.tex_work:
            self.tex_work = False
        else:
            self.m_bpButton_defualt_tex.Enable(True)

    def GetValue(self):
        return self.setting

    def GetDefault(self):
        return self.default

    def az_show(self, event):
        self.m_radioBox_az_div.SetSelection(self.azur_lane_div_type)
        self.m_radioBox_az_type.SetSelection(self.azur_lane_export_type)

        self.m_radioBox_type_use.SetSelection(self.azur_lane_use_default)

        self.m_checkBox_az_dir.SetValue(self.azur_lane_new_dir)
        self.m_checkBox_in_cn.SetValue(self.azur_lane_with_cn)

        self.m_dirPicker_az_tex_dir.SetPath(self.azur_lane_default_tex_dir)
        self.m_dirPicker_az_mesh_dir.SetPath(self.azur_lane_default_mesh_dir)

        self.m_textCtrl_tex_limit.SetLabel(self.azur_lane_tex_limit)
        self.m_textCtrl_mesh_limit.SetLabel(self.azur_lane_mesh_limit)

        self.m_checkList_az_limits.Set(self.az_div_list)

        self.az_type_use(event=event)

    def az_type_use(self, event):
        if self.m_radioBox_type_use.GetSelection() == 0:
            self.m_staticText15.Enable(False)
            self.m_staticText161.Enable(False)
            self.m_staticText171.Enable(False)

            self.m_textCtrl_mesh_limit.Enable(False)
            self.m_textCtrl_tex_limit.Enable(False)

            self.m_textCtrl_mesh_limit.SetLabel(self.default_mesh_pattern)
            self.m_textCtrl_tex_limit.SetLabel(self.default_tex_pattern)

            self.m_bpButton_del.Enable(False)
            self.m_bpButton_add.Enable(False)

            self.m_bpButton_up.Enable(False)
            self.m_bpButton_down.Enable(False)

            self.m_bpButton6_default_mesh.Enable(False)
            self.m_bpButton_defualt_tex.Enable(False)

            self.m_checkList_az_limits.Enable(False)

            ####
            self.m_radioBox_az_type.Enable(True)
            self.m_radioBox_az_div.Enable(True)

            self.change_div(event=event)

        else:
            self.m_staticText15.Enable(True)
            self.m_staticText161.Enable(True)
            self.m_staticText171.Enable(True)

            self.m_textCtrl_mesh_limit.Enable(True)
            self.m_textCtrl_tex_limit.Enable(True)

            self.m_bpButton_del.Enable(False)
            self.m_bpButton_add.Enable(True)

            self.m_bpButton_up.Enable(False)
            self.m_bpButton_down.Enable(False)

            self.m_textCtrl_mesh_limit.SetLabel(self.azur_lane_mesh_limit)
            self.m_textCtrl_tex_limit.SetLabel(self.azur_lane_tex_limit)

            if self.m_textCtrl_tex_limit.GetValue() != self.default_tex_pattern:
                self.m_bpButton_defualt_tex.Enable(True)
            else:
                self.m_bpButton_defualt_tex.Enable(False)
            if self.m_textCtrl_mesh_limit.GetValue() != self.default_mesh_pattern:
                self.m_bpButton6_default_mesh.Enable(True)
            else:
                self.m_bpButton6_default_mesh.Enable(False)

            self.m_checkList_az_limits.Enable(True)

            ####
            self.m_radioBox_az_type.Enable(False)
            self.m_radioBox_az_div.Enable(False)

            self.reset_az_pattern()
            self.m_checkList_az_limits.Clear()
            self.m_checkList_az_limits.Set(self.az_div_list)

    def reset_az_pattern(self):
        self.az_div_list.clear()
        for value in range(len(self.azur_lane_divide_list)):
            val_key = str(value + 1)
            value = self.azur_lane_divide_list[value]
            self.az_div_list.append(
                '%s)%s:\t%s' % (val_key, value['dir'], value['pattern']))


class AddPattern(noname.MyDialog_limit):
    def __init__(self, parent, index, name='', pattern='', dir_path=''):
        super().__init__(parent)

        self.index = index
        self.name = name
        if self.name == '':
            self.name = str(self.index)
        self.pattern = pattern
        self.dir = dir_path
        self.m_sdbSizer5OK.Enable(False)
        self.m_staticText_index.SetLabel("编号：%d" % self.index)
        self.sys_in = True
        self.m_textCtrl_limit.SetValue(self.pattern)
        self.m_textCtrl_name.SetValue(self.name)
        self.m_textCtrl_dir.SetValue(self.dir)
        self.sys_in = False
        if self.name == 'else':
            self.m_textCtrl_name.Enable(False)
        self.is_ok = False

    def check_ok(self, event):
        if not self.sys_in:
            self.dir = self.m_textCtrl_dir.GetValue()
            self.name = self.m_textCtrl_name.GetValue()
            self.pattern = self.m_textCtrl_limit.GetValue()

            if self.dir != '' and self.name != '' and self.pattern != '':
                self.m_sdbSizer5OK.Enable(True)

            self.is_ok = True

    def save_exit(self, event):
        self.Destroy()

    def get(self):
        return self.index, self.name, self.dir, self.pattern


class Pattern(noname.MyFrame_pattern):
    def __init__(self):
        super().__init__(None)

        info = [
            r'^ ： 匹配字符串的开头',
            r'$ ： 匹配字符串的末尾。',
            r'. ： 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。',
            r'[...] ： 用来表示一组字符,单独列出：[amk] 匹配 \'a\'，\'m\'或\'k\'',
            r'[^...] ： 不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。',
            r're* ： 匹配0个或多个的表达式。',
            r're+ ： 匹配1个或多个的表达式。',
            r're? ： 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式',
            r're{ n} ： 精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。',
            r're{ n,} ： 匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。',
            r're{ n, m} ： 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式',
            r'a| b ： 匹配a或b',
            r'(re) ： 匹配括号内的表达式，也表示一个组',
            r'(?imx) ： 正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。',
            r'(?-imx) ： 正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。',
            r'(?: re) ： 类似 (...), 但是不表示一个组',
            r'(?imx: re) ： 在括号中使用i, m, 或 x 可选标志',
            r'(?-imx: re) ： 在括号中不使用i, m, 或 x 可选标志',
            r'(?#...) ： 注释.',
            r'(?= re) ： 前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。',
            r'(?! re) ： 前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功',
            r'(?> re) ： 匹配的独立模式，省去回溯。',
            r'\w ： 匹配字母数字及下划线',
            r'\W ： 匹配非字母数字及下划线',
            r'\s ： 匹配任意空白字符，等价于 [\t\n\r\f].',
            r'\S ： 匹配任意非空字符',
            r'\d ： 匹配任意数字，等价于 [0-9].',
            r'\D ： 匹配任意非数字',
            r'\A ： 匹配字符串开始',
            r'\Z ： 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。',
            r'\z ： 匹配字符串结束',
            r'\G ： 匹配最后匹配完成的位置。',
            r'\b ： 匹配一个单词边界，也就是指单词和空格间的位置。例如， \'er\\b\' 可以匹配"never" 中的 \'er\'，但不能匹配 "verb" 中的 \'er\'。',
            r'\B ： 匹配非单词边界。\'er\B\' 能匹配 "verb" 中的 \'er\'，但不能匹配 "never" 中的 \'er\'。',
            r'\n, \t, 等. ： 匹配一个换行符。匹配一个制表符。等',
            r'\1...\9 ： 匹配第n个分组的内容。',
            r'\10 ： 匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式',

        ]
        info2 = [
            r'字符类',
            r'[Pp]ython ： 匹配 "Python" 或 "python"',
            r'rub[ye] ： 匹配 "ruby" 或 "rube"',
            r'[aeiou] ： 匹配中括号内的任意一个字母',
            r'[0-9] ： 匹配任何数字。类似于 [0123456789]',
            r'[a-z] ： 匹配任何小写字母',
            r'[A-Z] ： 匹配任何大写字母',
            r'[a-zA-Z0-9] ： 匹配任何字母及数字',
            r'[^aeiou] ： 除了aeiou字母以外的所有字符',
            r'[^0-9] ： 匹配除了数字外的字符',
            r'特殊字符类',
            r'. ： 匹配除 "\n" 之外的任何单个字符。要匹配包括 \'\n\' 在内的任何字符，请使用象 \'[.\n]\' 的模式。',
            r'\d ： 匹配一个数字字符。等价于 [0-9]。',
            r'\D ： 匹配一个非数字字符。等价于 [^0-9]。',
            r'\s ： 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。',
            r'\S ： 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。',
            r'\w ： 匹配包括下划线的任何单词字符。等价于\'[A - Za - z0 - 9_]\'。',
            r'\W ： 匹配任何非单词字符。等价于 \'[ ^ A - Za - z0 - 9_]\'',

        ]
        self.m_listBox_info.Set(info)
        self.m_listBox_info2.Set(info2)


def main_part():
    app = wx.App(False)
    frame = CaleFrame(None)
    frame.Show()

    app.MainLoop()
