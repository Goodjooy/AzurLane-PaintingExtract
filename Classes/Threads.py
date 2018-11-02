import os
import threading
import re

import Methub
from Classes import noname


class GirlSRestore(threading.Thread):

    def __init__(self, able_list: list, rgb_list: dict, alpha_list: dict, save_path: str, is_work: bool,
                 form: noname.MyFrame1,
                 setting: dict, full: dict):
        super(GirlSRestore, self).__init__()

        self.able_list = able_list
        self.rgb_list = rgb_list
        self.alpha_list = alpha_list
        self.save_path = save_path
        self.is_work = is_work

        self.form = form

        self.setting = setting
        self.full = full

    def run(self):
        length = len(self.rgb_list)
        if not self.is_work:
            pass
        else:
            i = 0
            if self.setting["check_before_start"]:
                for val in self.able_list:
                    Methub.tools.search(self.rgb_list, self.alpha_list, list(self.alpha_list.keys()), val)
                    i += 1
                    val_percent = str(round(100 * (i / len(self.able_list)), 2))
                    val = round(100 * (i / len(self.rgb_list)))
                    self.form.m_staticText_all.SetLabel("扫描进度：%s %%" % val_percent)
                    self.form.m_gauge_all.SetValue(val)
                i = 0

            for val in self.able_list:
                if self.setting["use_type"] == 0:
                    choice = self.setting["export_type"]

                    if choice == 0:
                        save_path = f"{self.save_path}"

                    elif choice == 1:
                        pattern_per = re.compile(r'^pic_.+$')

                        if pattern_per.match(val) is not None:
                            save_path = f"{self.save_path}\\人形"
                        else:
                            save_path = f"{self.save_path}\\非人形"
                    elif choice == 2:
                        pattern_per = re.compile(r'^[Pp]ic_.+$')
                        if pattern_per.match(val) is not None:
                            address = val.replace('pic_', '').replace('_D', '')
                            len_num = re.findall(r'_\d+', address)
                            if len(len_num) != 0:
                                address = address.replace(len_num[-1], '')
                            if address.lower() == '':
                                address += len_num[-1]
                            save_path = f"{self.save_path}\\人形\\{address}"

                        else:
                            save_path = f"{self.save_path}\\非人形"

                    elif choice == 3:
                        pattern_skin = re.compile(r'^[Pp]ic_[\S ]+_\d+(_D)*$')
                        pattern_per = re.compile(r'^[Pp]ic_[\S ]+(_D)*$')

                        if pattern_skin.match(val) is not None:
                            save_path = f"{self.save_path}\\皮肤"
                        elif pattern_per.match(val) is not None:
                            save_path = f"{self.save_path}\\人形"
                        else:
                            save_path = f"{self.save_path}\\其他"

                    elif choice == 4:
                        pattern_dis = re.compile(r'^[pP]ic_[\S ]+?_*[1-9]*_D$')
                        pattern_per = re.compile(r'^[Pp]ic_[\S ]+?_*[^D][1-9]*$')

                        if pattern_dis.match(val) is not None:
                            save_path = f"{self.save_path}\\大破"
                        elif pattern_per.match(val) is not None:
                            save_path = f"{self.save_path}\\人形"
                        else:
                            save_path = f"{self.save_path}\\其他"

                    else:
                        save_path = self.save_path

                else:
                    save_path = ''
                    for setting in self.setting['divide_list'][1:]:
                        pattern_er = re.compile(setting['pattern'])
                        if pattern_er.match(val) is not None:
                            save_path = f'{self.save_path}\\{setting["dir"]}'
                            break

                    if save_path == "":
                        save_path = self.save_path
                os.makedirs(save_path, exist_ok=True)
                Methub.Functions.girl_font_line_restore(self.rgb_list[val], self.alpha_list[val], save_path)
                i += 1

                val_percent = str(round(100 * (i / length), 2))
                self.form.m_staticText_now.SetLabel("当前：%s" % val)
                val = round(100 * (i / length))
                self.form.m_staticText_all.SetLabel("总进度：%s %%" % val_percent)
                self.form.m_gauge_all.SetValue(val)

            self.form.m_staticText_all.SetLabel("总进度：%s %%" % '100')
            self.form.m_gauge_all.SetValue(100)
            self.form.start = False

            if self.full["open_dir"]:
                os.system(r"start %s" % self.save_path)

    def set_value(self, rgb_list, alpha_list, save_path, able_list, setting, full):
        self.rgb_list = rgb_list
        self.alpha_list = alpha_list
        self.save_path = save_path
        self.able_list = able_list

        self.setting = setting
        self.full = full

    def set_work(self, is_work: bool):
        self.is_work = is_work
