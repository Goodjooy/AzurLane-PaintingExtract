import PIL.Image
import os
import threading
import tempfile

import function


class RestoreThread(threading.Thread):

    def __init__(self, id_thread, name, list_pic, form, name_dic, mesh_list_path_dir, tex_list_path_dir, save_path):
        threading.Thread.__init__(self)
        self.threadID = id_thread

        self.name = name

        self.index = 0

        self.list = list_pic

        self.format = form
        self.names = name_dic

        self.mesh_list_path_dir = mesh_list_path_dir
        self.tex_list_path_dir = tex_list_path_dir
        self.save_path = save_path

        self.stop = False

    def run(self):
        for self.index in range(len(self.list)):
            if self.index < len(self.list) and not self.stop:
                name = self.list[self.index]
                self.format.m_staticText_now.SetLabel("当前：%s" % self.names[name])
                self.format.m_gauge_now.SetValue(0)

                function.restore_tool(name, self.names, self.mesh_list_path_dir, self.tex_list_path_dir, self.save_path)
                self.format.m_gauge_now.SetValue(100)
                val_percent = str(round(100 * (self.index / len(self.list)), 2))
                val = function.re_int(100 * (self.index / len(self.list)))
                self.format.m_staticText_all.SetLabel("总进度：%s %%" % val_percent)
                self.format.m_gauge_all.SetValue(val)
                self.index += 1

        self.format.m_staticText_all.SetLabel("总进度：%s %%" % '100')
        self.format.start = False

        if self.format.m_checkBox_autoopen.GetValue():
            os.system(r"start %s" % self.save_path)

    def stop_(self, stop: bool):
        self.stop = stop

    def add_save_path(self, save_path: str):
        self.save_path = save_path

    def update_list(self, restore_list):
        self.list = restore_list


class QuickRestore(threading.Thread):

    def __init__(self, index, list_tex, list_mesh, father, work_path):
        threading.Thread.__init__(self)

        self.tex = list_tex[index]
        self.mesh = list_mesh[index]
        self.father = father

        self.path = work_path

    def run(self):
        pic = function.restore_tool_no_save(self.mesh, self.tex)

        pic.save("%s\\temp.png" % self.path)

        os.system(r"start %s\temp.png" % self.path)
