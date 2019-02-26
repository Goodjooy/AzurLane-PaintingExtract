import json
import os
import sys
import time

import wx

from Classes import noname, WorkClasses, Threads, InfoClasses


class MainFrame(noname.MyFrame1):

    def __init__(self, parent, start_path):
        noname.MyFrame1.__init__(self, parent)
        self.start_path = start_path

        try:

            self.open_give = sys.argv[1]
            self.is_open_give = True

        except:
            self.open_give = ''
            self.is_open_give = False
        try:
            icon = wx.Icon(os.path.join(self.start_path, "files\\icon.ico"))
        except FileNotFoundError:
            pass
        else:
            self.SetIcon(icon)

        with open(os.path.join(self.start_path, "files\\setting.json"), 'r')as file:
            setting_dic = json.load(file)
        self.setting_self = setting_dic

        with open(os.path.join(self.start_path, "files\\default.json"), 'r')as file:
            self.default = json.load(file)

        self.painting = WorkClasses.PaintingWork(self, setting=self.setting_self, default=self.default,
                                                 start_path=self.start_path)
        # self.spine_cut = WorkClasses.SpineDivideWork(self, self.start_path)

        self.m_button_gui.Enable(False)

        self.setting_page = 0

        # self.m_simplebook_input.SetSelection(0)
        # self.m_choice_type.SetSelection(0)

        self.m_notebook_info.SetSelection(0)
        self.m_listbook_in.SetSelection(0)

        self.choice = 0

        self.drop_load_tex = WorkClasses.FileDropLoad(self.painting, self)
        self.drop_load_mesh = WorkClasses.FileDropLoad(self.painting, self)
        self.m_listBox_tex.SetDropTarget(self.drop_load_tex)
        self.m_listBox_mesh.SetDropTarget(self.drop_load_mesh)

        self.error_list = []

        if self.is_open_give:
            self.painting.open_give(self.open_give)

    # def append_error(self, error_info):
    #    self.m_listBox_errors.Append(error_info)
    #    self.error_list.append(error_info)

    def any_error(self):
        return self.error_list != []

    # file load method
    # azur lane
    def load_tex(self, event):
        self.painting.load_tex()

    def load_Mesh(self, event):
        self.painting.load_mesh()

        # def load_body(self, event):
        #    self.spine_cut.load_body()
        #
        # def load_cut(self, event):
        # self.spine_cut.load_cuter()

    def load_mesh_fold(self, event):
        self.painting.load_mesh_fold()

    def load_tex_fold(self, event):
        self.painting.load_tex_fold()

    def load_tex_and_mesh(self, event):
        self.painting.load_tex_and_mesh()

    # choice
    def mesh_choice(self, event):
        self.painting.mesh_choice()

    def tex_choice(self, event):
        self.painting.tex_choice()

    def open_file(self, event):
        self.painting.open_file()

    def open_pass(self, event):
        self.painting.open_pass()

    # def open_pic(self, event):
    #    self.spine_cut.pic_open()

    # export
    # def export_pic(self, event):
    #    self.spine_cut.export_pic()

    def export_choice(self, event):
        if self.painting.is_choice() is not None:
            self.painting.export_choice()

    def export_all(self, event):
        title = '保存'
        if self.painting.is_able():
            title += "-碧蓝航线"
        if self.default['lock']:
            address = self.default['export']
        else:
            address = os.getcwd()
        dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            temp = dialog.GetPath()

            if self.painting.is_able():
                self.painting.export_all(temp, self.painting.able)

        else:
            pass

    def copy_file(self, event):

        self.painting.copy_file()

    def tex_search_ex(self, event):
        title = '保存'
        if self.painting.is_able():
            title += "-碧蓝航线-Texture搜索"
        if self.default['lock']:
            address = self.default['export']
        else:
            address = os.getcwd()
        dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            temp = dialog.GetPath()

            if self.painting.is_able():
                self.painting.export_all(temp, self.painting.search_tex_val)

        else:
            pass

    def mesh_search_ex(self, event):
        title = '保存'
        if self.painting.is_able():
            title += "-碧蓝航线"
        if self.default['lock']:
            address = self.default['export']
        else:
            address = os.getcwd()
        dialog = wx.DirDialog(self, title, address, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

        if dialog.ShowModal() == wx.ID_OK:
            temp = dialog.GetPath()

            if self.painting.is_able():
                self.painting.export_all(temp, self.painting.search_mesh_val)

        else:
            pass

    def unable_search_ex(self, event):
        pass

    # tools
    def quick_work(self, event):
        quick = QuickWork(self, self, self.painting)
        quick.ShowModal()

    # search
    def search_mesh(self, event):
        self.painting.search_mesh()

    def search_tex(self, event):
        self.painting.search_tex()

    def search_pass(self, event):
        self.painting.search_pass()

    def search_unable(self, event):
        self.painting.search_unable()

    # else

    def exit_press(self, event):

        self.exit()

    def close_press(self, event):

        self.exit()

    # def reset_spine(self, event):
    #    self.spine_cut.reset()

    def exit(self, thread_exit=False):

        with open("%s\\files\\setting.json" % self.start_path, 'w')as file_save:
            json.dump(self.setting_self, file_save)
        with open("%s\\files\\default.json" % self.start_path, 'w')as file_:
            json.dump(self.default, file_)

        if thread_exit:
            time.sleep(2)
            self.Destroy()
            sys.exit()
        else:
            if self.painting.restore.is_alive():
                message = wx.MessageBox("还未全部完成，确认退出？", "警告", wx.YES_NO)

                if message == wx.YES:
                    if message == wx.YES:
                        self.painting.restore.stop_(True)
                        while self.painting.restore.is_alive():
                            time.sleep(1)

                    self.Destroy()
                    sys.exit()
                else:
                    pass
            else:

                message = wx.MessageBox("确认退出？", "提示", wx.YES_NO, )
                if message == wx.YES:

                    self.Destroy()
                    sys.exit()
                elif message == wx.CANCEL:
                    pass

    def change_size(self, event):
        pass

    def helper(self, event):
        dialog = Pattern()
        dialog.Show()

    def setting(self, event):
        dialog = SettingFrame(self, self.setting_self, self.default, self.start_path, self.painting.info,
                              self.painting.is_able_add(),
                              self.setting_page)
        temp = dialog.ShowModal()
        if temp == 0:
            if dialog.IsChange:
                thread = Threads.BackInfo(self.painting)
                thread.start()

                self.default = dialog.GetDefault()
                self.setting_self = dialog.GetValue()

                self.painting.update_setting(self.setting_self, self.default)

        self.setting_page = dialog.GetSelection()

    # def show_gl_win(self, event):
    #    dialog = noname.MyDialog7(self)


#
#    dialog.ShowModal()
#
# def change_type(self, event):
#    choice = self.m_choice_type.GetSelection()
#    if choice == 2:
#        self.m_choice_type.SetSelection(self.choice)
#
#        message = wx.MessageBox("将启动AzurLaneLive2DExtract所在文件夹，\n运行并直接将live2D文件拖入即可。", '信息', wx.YES_NO)
#        if message == wx.YES:
#            # os.system(r'start %s\\files\\lived\\AzurLaneLive2DExtract.exe' % self.start_path)
#            os.system(r'start "%s\\files\\lived"' % self.start_path)
#        else:
#            pass
#    else:
#        self.choice = choice
#        self.m_simplebook_input.SetSelection(choice)


class Writer(noname.MyDialog_enter_name):

    def __init__(self, parent, info: InfoClasses.PerEdit):
        noname.MyDialog_enter_name.__init__(self, parent)

        self.info = info
        self.ok = False

    def show_name(self, event):
        self.m_staticText8.SetLabel("%s: " % self.info.name)
        self.m_textCtrl2.SetValue(self.info.val)

    def save_name(self, event):
        if self.info.name == self.m_textCtrl2.GetValue():
            self.ok = False
            if self.m_checkBox_real.GetValue():
                self.ok = True
                self.info.has_cn = True
        else:
            self.info.val = self.m_textCtrl2.GetValue()
            self.ok = True
            self.info.has_cn = True
        self.Destroy()

    def save_key(self, event):
        print(event)

    def is_able(self):
        return self.ok

    def GetValue(self):
        return self.info

    def is_real(self):
        return self.m_checkBox_real.GetValue()


class SettingFrame(noname.MyDialog_Setting):

    def __init__(self, parent, setting_dic, default, def_path, info, able_add, setting_select):
        super().__init__(parent)

        self._is_change = False

        self.info = info
        self.path = def_path

        self.var = {}

        temp = wx.Image('%s\\files\\bg_story_litang.png' % self.path, wx.BITMAP_TYPE_PNG)
        temp = temp.ConvertToBitmap()
        self.m_bitmap2.SetBitmap(temp)
        if not isinstance(setting_dic, dict):
            setting_dic = setting_dic.exit()[0]
        self.set_val = WorkClasses.Setting(self, setting_dic, default, def_path, able_add)

        self.edit_name = WorkClasses.EditName(self, self.info, self.path)

        # self.compare = WorkClasses.Compare(self)

        self.pattern_edit: InfoClasses.PattenEdit = self.set_val.azur_lane_setting.divide_list

        # self.encrypt = WorkClasses.EncryptImage(self)
        # self.crypt = WorkClasses.CryptImage(self)

        self.page = setting_select
        self.m_notebook3.SetSelection(self.page)

    @property
    def IsChange(self):
        return self._is_change

    @IsChange.setter
    def IsChange(self, value: bool):
        self._is_change = value

    @property
    def setting_select(self):
        return self.m_notebook3.GetSelection()

    # 初始化
    def initial(self, event):
        self.set_val.initial()

        self.edit_name.initial()

        self.m_sdbSizer4Apply.SetLabel('应用')
        self.m_sdbSizer4Cancel.SetLabel('取消')
        self.m_sdbSizer4OK.SetLabel('确认')

        self.m_simplebook_io.SetSelection(self.set_val.azur_lane_setting.export_type.val)

    def change_page(self, event):
        self.page = self.m_notebook3.GetSelection()

    # ok,apply,cancel键处理
    def ok_click(self, event):
        self.set_val.change_work()
        self._is_change = True
        self.close()

    def apply_click(self, event):
        self.set_val.change_work()
        self._is_change = True
        self.m_sdbSizer4Apply.Enable(False)

    def cancel_click(self, event):
        self._is_change = False
        self.close()

    # 名称编辑，添加部分
    def edit_add_name(self, event):
        self.edit_name.edit_name(self.m_listBox_new1.GetSelection())

    def name_add(self, event):
        self.edit_name.add_new()

    def name_del(self, event):
        self.edit_name.del_name(self.m_listBox_new1.GetSelection())

    def open_add_name(self, event):
        self.edit_name.open_add_name()

    def change_name(self, event):
        self.edit_name.change_name()

    def searching(self, event):
        self.edit_name.searching()

    # 设置选项
    def change(self, event):
        self.m_sdbSizer4Apply.Enable(True)

    def change_type(self, event):
        self._is_change = False
        selection = self.m_radioBox_type_use.GetSelection()
        self.m_simplebook_io.SetSelection(selection)
        self.change(event)
        self.set_val.io_type_change(selection)

    def change_input(self, event):
        self.set_val.change_input()
        self.change(event)

    def menu_setting(self, event):
        self.change(event)
        dialog = MenuChoice(self, self.path)

        dialog.Show()

    def lock_address(self, event):
        self.change(event)
        self.set_val.lock_address()

    # 正则表达式的方法
    # 导出正则表达式方法
    def choice(self, event):
        index = self.m_checkList_az_limits.GetSelection()
        # 无选择
        if index == -1:
            self.m_bpButton_del.Enable(False)
            self.m_bpButton_up.Enable(False)
            self.m_bpButton_down.Enable(False)
        elif index == 0:
            # 自定义第一项不可删除,不可移动
            if index == 0:
                self.m_bpButton_del.Enable(False)
                self.m_bpButton_up.Enable(False)
                self.m_bpButton_down.Enable(False)
            else:
                self.m_bpButton_del.Enable(True)
                self.m_bpButton_up.Enable(True)
                self.m_bpButton_down.Enable(True)
        else:
            self.m_bpButton_del.Enable(True)
            self.m_bpButton_up.Enable(True)
            self.m_bpButton_down.Enable(True)
            # 自定义不可第一项被移动
            if index == 1:
                self.m_bpButton_up.Enable(False)
            else:
                self.m_bpButton_up.Enable(True)

            if index == len(self.pattern_edit.val) - 1:
                self.m_bpButton_down.Enable(False)
            else:
                self.m_bpButton_down.Enable(True)

    def az_add(self, event):
        self.choice(event)
        dialog = AddPattern(self, len(self.pattern_edit), )
        dialog.ShowModal()
        if dialog.is_ok:
            self.change(event)
            var = {"name": dialog.name, "dir": dialog.dir, "pattern": dialog.pattern}
            self.pattern_edit.append(var)

            self.m_checkList_az_limits.Append(self.pattern_edit.format_work(self.pattern_edit.val[-1]))

    def az_del(self, event):
        self.choice(event)

        def format_work(x):
            return f"名称：{x['name']}\n," \
                f"文件夹：{x['dir']},\n" \
                f"格式：{x['pattern']}\n."

        index = self.m_checkList_az_limits.GetSelection()
        dialog = wx.MessageBox(f"你确实要删除导入限制{format_work(self.pattern_edit[index])}吗？", '提示', wx.YES_NO)

        if dialog == wx.YES:
            self.change(event)
            index = self.pattern_edit.delete(index)
            self.pattern_edit.set_value()
            self.m_checkList_az_limits.SetSelection(index)

    def az_down(self, event):
        self.choice(event)
        self.change(event)
        index = self.m_checkList_az_limits.GetSelection()
        val = self.pattern_edit.move_down(index)

        self.m_checkList_az_limits.SetString(val, self.pattern_edit.
                                             format_work(self.pattern_edit[val]))

        self.m_checkList_az_limits.SetString(index, self.pattern_edit.
                                             format_work(self.pattern_edit[index]))
        self.m_checkList_az_limits.SetSelection(val)

    def az_up(self, event):
        self.choice(event)
        self.change(event)
        index = self.m_checkList_az_limits.GetSelection()
        val = self.pattern_edit.move_up(index)

        self.m_checkList_az_limits.SetString(val, self.pattern_edit.
                                             format_work(self.pattern_edit[val]))

        self.m_checkList_az_limits.SetString(index, self.pattern_edit.
                                             format_work(self.pattern_edit[index]))
        self.m_checkList_az_limits.SetSelection(val)

    # 导入的正则表达式方法
    # 检查方法
    def change_in_tex(self, event):
        self.change(event)
        if self.m_textCtrl_tex_limit.GetValue() == "^.+\\.[pP][Nn][Gg]$":
            self.m_bpButton_defualt_tex.Enable(False)
        else:
            self.m_bpButton_defualt_tex.Enable(True)

    def change_in_mesh(self, event):
        self.change(event)
        if self.m_textCtrl_mesh_limit.GetValue() == "^.+-mesh\\.[oO][Bb][jJ]$":
            self.m_bpButton6_default_mesh.Enable(False)
        else:
            self.m_bpButton6_default_mesh.Enable(True)

    def default_tex(self, event):
        self.change(event)
        self.m_textCtrl_tex_limit.SetLabel("^.+\\.[pP][Nn][Gg]$")

    def default_mesh(self, event):
        self.change(event)
        self.m_textCtrl_mesh_limit.SetLabel("^.+-mesh\\.[oO][Bb][jJ]$")

    # 获取值的方法
    def GetValue(self):
        return {
            'azur_lane': self.set_val.azur_lane_setting.to_dict(),
            'full': self.set_val.full_setting.to_dict()
        }

    def GetDefault(self):
        return self.set_val.default

    def GetSelection(self):
        return self.page

    def GetNames(self):
        return self.var

    # 退出
    def close(self, event=None):
        self.set_val.azur_lane_setting.divide_list = self.pattern_edit

        self.var = self.edit_name.exit()

        self.Destroy()


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


class QuickWork(noname.MyDialogQuick):
    def __init__(self, parent, frame: noname.MyFrame1, az: WorkClasses.PaintingWork):
        super(QuickWork, self).__init__(parent)

        self.az = az
        self.frame = frame
        self.start = False
        self.m_choice_im_type.SetSelection(0)
        self.m_choice_tex_type.SetSelection(0)
        self.m_choice_mesh_type.SetSelection(0)

        self.m_notebook3.SetSelection(0)

    def im_sele(self, event):
        choice = self.m_choice_im_type.GetSelection()
        self.m_simplebook3.SetSelection(choice)
        self.able_work()

    def quick_tex(self, event):
        select = self.m_choice_tex_type.GetSelection()
        if select == 0:
            txt = self.az.load_tex()
        else:
            txt = self.az.load_tex_fold()
        if not isinstance(txt, str):
            txt = json.dumps(txt)
        self.m_textCtrl_qk_tex.SetLabel(txt)
        self.able_work()

    def quick_mesh(self, event):
        select = self.m_choice_mesh_type.GetSelection()
        if select == 0:
            txt = self.az.load_mesh()
        else:
            txt = self.az.load_mesh_fold()
        if not isinstance(txt, str):
            txt = json.dumps(txt)
        self.m_textCtrl_qk_mesh.SetLabel(txt)

        self.able_work()

    def quick_setting(self, event):
        self.frame.setting(event)

    def quick_both(self, event):

        txt = self.az.load_tex_and_mesh()

        self.m_textCtrl_qk_ex.SetLabel(txt)
        self.able_work()

    def quick_export(self, event):
        temp = self.m_dirPicker8.GetPath()

        if self.az.is_able():
            self.az.export_all(temp)
        self.start = True
        self.able_work()

    def able_work(self):
        if self.az.is_able() and self.start:
            self.frame.m_gauge_quick.SetValue(100)
            self.Destroy()


class MenuChoice(noname.MyDialog_menu):
    def __init__(self, parent, start_path):
        super(MenuChoice, self).__init__(parent)

        self.path = start_path
        self.info = ''

    def ok_change(self, event):
        path = os.path.join(self.path, 'files\\menu_ctrl.ini')

        self.info = info = [self.m_checkBox_dir.GetValue(), self.m_checkBox_bg.GetValue()]

        with open(path, 'w')as file:
            json.dump(info, file)

        self.m_sdbSizer5OK.Enable(False)
        self.m_sdbSizer5Cancel.Enable(False)
        os.system(r'"%s"' % os.path.join(self.path, 'files\\menu_ctrl.exe'))
        self.m_sdbSizer5OK.Enable(True)
        self.m_sdbSizer5Cancel.Enable(True)


class AddNewName(noname.MyDialog_add_name):
    def __init__(self, parent, key: str = '', value: str = ''):
        super(AddNewName, self).__init__(parent)
        self.key = key
        self.value = value

        if self.key != '':
            self.m_textCtrl_key.SetLabel(self.key)
        if self.value != '':
            self.m_textCtrl_var.SetLabel(self.value)

        self.work = False

    def ok_work(self, event):
        self.key = self.m_textCtrl_key.GetValue()
        self.value = self.m_textCtrl_var.GetValue()
        self.Destroy()
        if self.key == '' or self.value == '':
            self.work = False
        else:
            self.work = True

    def get_value(self):
        return self.key, self.value


