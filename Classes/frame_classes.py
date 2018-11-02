import json
import os

import wx

from Classes import noname, WorkClasses


class MainFrame(noname.MyFrame1):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent=parent)
        with open("files\\setting.json", 'r')as file:
            file = json.load(file)
        self.setting = file
        with open('files\\default.json', 'r')as file:
            self.default = json.load(file)

        self.girl_line_div_type = self.setting["girl_line"]["div_type"]
        self.girl_line_export_type = self.setting["girl_line"]["export_type"]
        self.girl_line_new_dir = self.setting["girl_line"]["new_dir"]
        self.girl_line_check = self.setting["girl_line"]["check_before_start"]

        self.open_dir_after_finish = self.setting["full"]["open_dir"]
        self.skip_had = self.setting["full"]["skip_had"]
        self.auto_open_choice_pic = self.setting["full"]["auto_open"]
        self.finish_exit = self.setting["full"]["finish_exit"]

        self.girl_front_line = WorkClasses.GirlsFrontLine(self, self.setting, self.default)

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

    def rgb_choice(self, event):
        self.girl_front_line.rgb_choice()

    def alpha_choice(self, event):
        self.girl_front_line.alpha_choice()

    def search_rgb(self, event):
        self.girl_front_line.search_rgb()

    def search_alpha(self, event):
        self.girl_front_line.search_alpha()

    def export_all(self, event):
        title = '保存'

        if self.girl_front_line.is_able():
            title += '-少女前线'
        if self.default['lock']:
            address = self.default['export']
        else:
            address = os.getcwd()
        dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            temp = dialog.GetPath()

            self.girl_front_line.export_all(temp)
        else:
            pass

    def export_choice(self, event):
        self.girl_front_line.export_choice()

    def setting(self, event):
        dialog = Setting(self, self.setting, self.default)
        temp = dialog.ShowModal()
        if temp == 0:
            if dialog.IsChange:
                setting_dic = dialog.GetValue()
                self.default = dialog.GetDefault()
                self.setting = setting_dic
                self.girl_line_div_type = setting_dic["girl_line"]["div_type"]
                self.girl_line_export_type = setting_dic["girl_line"]["export_type"]
                self.girl_line_new_dir = setting_dic["girl_line"]["new_dir"]

                self.open_dir_after_finish = setting_dic["full"]["open_dir"]
                self.skip_had = setting_dic["full"]["skip_had"]
                self.auto_open_choice_pic = setting_dic["full"]["auto_open"]
                self.finish_exit = setting_dic["full"]["finish_exit"]

                self.girl_front_line.update_setting(self.setting, self.default)


class Setting(noname.MyDialog1):

    def __init__(self, parent, setting_dic, default):
        super(Setting, self).__init__(parent=parent)

        self.setting = setting_dic
        self.default = default

        self.girl_line_div_type = setting_dic["girl_line"]["div_type"]
        self.girl_line_export_type = setting_dic["girl_line"]["export_type"]
        self.girl_line_new_dir = setting_dic["girl_line"]["new_dir"]
        self.girl_line_check = setting_dic["girl_line"]["check_before_start"]

        self.girl_line_divide_list = setting_dic["girl_line"]['divide_list']

        self.girl_line_default_rgb_dir = self.default["girl_line"]['default_rgb_dir']
        self.girl_line_default_alpha_dir = self.default["girl_line"]['default_alpha_dir']

        self.open_dir_after_finish = setting_dic["full"]["open_dir"]
        self.skip_had = setting_dic["full"]["skip_had"]
        self.auto_open_choice_pic = setting_dic["full"]["auto_open"]
        self.finish_exit = setting_dic["full"]["finish_exit"]

        self.girl_line_use_type = setting_dic["girl_line"]["use_type"]

        self.IsChange = False

        self.IsChange = False
        self.lock = self.default["lock"]
        self.export = self.default["export"]

        self.gl_div_list = []
        self.reset_gl_pattern()
        self.index = len(self.gl_div_list) + 1

        self.__choice = None
        self.m_button_del.Enable(False)

    def gl_show(self):
        self.m_radioBox_gfl_div.SetSelection(self.girl_line_div_type)
        self.m_radioBox_gfl_ex.SetSelection(self.girl_line_export_type)
        self.m_checkBox_gfl_dir.SetValue(self.girl_line_new_dir)
        self.m_checkBox_check.SetValue(self.girl_line_check)

        self.m_dirPicker_gl_alpha_dir.SetPath(self.girl_line_default_rgb_dir)
        self.m_dirPicker_gl_rbg_dir.SetPath(self.girl_line_default_alpha_dir)

        self.m_radioBox_type_use.SetSelection(self.girl_line_use_type)

    def change_work(self):
        self.setting["girl_line"]["div_type"] = self.m_radioBox_gfl_div.GetSelection()
        self.setting["girl_line"]["export_type"] = self.m_radioBox_gfl_ex.GetSelection()
        self.setting["girl_line"]["new_dir"] = self.m_checkBox_gfl_dir.GetValue()
        self.setting["girl_line"]["check_before_start"] = self.m_checkBox_check.GetValue()

        self.setting["girl_line"]["use_type"]=self.m_radioBox_type_use.GetSelection()

        self.setting["full"]["open_dir"] = self.m_checkBox_autoopen.GetValue()
        self.setting["full"]["skip_had"] = self.m_checkBox_pass_finished.GetValue()
        self.setting["full"]["auto_open"] = self.m_checkBox_open_temp.GetValue()
        self.setting["full"]["finish_exit"] = self.m_checkBox4_finish_exit.GetValue()

        self.lock = self.default['lock'] = self.m_toggleBtn_lock.GetValue()

        if self.lock:
            self.default["girl_line"]['default_rgb_dir'] = self.m_dirPicker_gl_rbg_dir.GetPath()
            self.default["girl_line"]['default_alpha_dir'] = self.m_dirPicker_gl_alpha_dir.GetPath()

            self.default['export'] = self.m_dirPicker_export.GetPath()

    def show_choice(self, event):
        self.gl_show()

        self.m_checkBox_autoopen.SetValue(self.open_dir_after_finish)
        self.m_checkBox_pass_finished.SetValue(self.skip_had)
        self.m_checkBox_open_temp.SetValue(self.auto_open_choice_pic)
        self.m_checkBox4_finish_exit.SetValue(self.finish_exit)

        self.m_dirPicker_export.SetPath(self.export)

        self.m_toggleBtn_lock.SetValue(self.lock)

        self.change_div(event)

    def lock_address(self, event):
        self.IsChange = True
        self.lock = self.default['lock'] = self.m_toggleBtn_lock.GetValue()

        self.m_dirPicker_export.Enable(not self.lock)

        self.m_dirPicker_gl_rbg_dir.Enable(not self.lock)
        self.m_dirPicker_gl_alpha_dir.Enable(not self.lock)

    def reset_gl_pattern(self):
        self.gl_div_list.clear()
        for value in range(len(self.girl_line_divide_list)):
            val_key = str(value + 1)
            value = self.girl_line_divide_list[value]
            self.gl_div_list.append(
                '%s)%s:\t%s' % (val_key, value['dir'], value['pattern']))

    def change_div(self, event):
        types = ([
                     r'1）其他：^.+$',
                     r'2）人形：^[Pp]ic_[\S ]+_\d+(_D)*$',
                     r'3）人形皮肤：^[Pp]ic_[\S ]+(_D)*$',
                 ],
                 [
                     r'1）其他：^.+$',
                     r'2）人形：^[Pp]ic_[\S ]+?_*[^D][1-9]*$',
                     r'3）人形大破：^[pP]ic_[\S ]+?_*[1-9]*_D$'
                 ],
                 [
                     r'1）其他：^.+$',
                     r'2）人形：^pic_.+$',

                 ])
        a = self.m_radioBox_type_use.GetSelection()
        if self.m_radioBox_type_use.GetSelection() == 0:
            self.m_listBox_gl_limit.Clear()
            if self.m_radioBox_gfl_ex.GetSelection() == 1:
                self.change(event)

                self.m_listBox_gl_limit.Set(types[2])

            elif self.m_radioBox_gfl_ex.GetSelection() == 3:
                self.change(event)

                self.m_listBox_gl_limit.Set(types[0])

            elif self.m_radioBox_gfl_ex.GetSelection() == 4:
                self.change(event)

                self.m_listBox_gl_limit.Set(types[1])
            else:
                pass

    def change(self, event):
        self.m_sdbSizer1Apply.Enable(True)

    def ok_click(self, event):
        self.change_work()
        self.IsChange = True
        self.Destroy()

    def apply_click(self, event):
        self.change_work()
        self.IsChange = True
        self.m_sdbSizer1Apply.Enable(False)

    def cancel_click(self, event):
        self.IsChange = False
        self.Destroy()

    def GetValue(self):
        return self.setting

    def GetDefault(self):
        return self.default
