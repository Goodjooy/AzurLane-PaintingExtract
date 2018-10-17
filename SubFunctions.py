import os

import wx
import function


def load_file(type_load="file_in", title="open", file_type="", format_in=None, path=os.getcwd()):
    __save_file = False
    __load_folder = False
    __save_file = False
    __load_file = False

    if type_load == 'file_in':
        __load_file = True
    elif type_load == 'file_out':
        __save_file = True
    elif type_load == 'folder_out':
        __load_folder = True
    elif type_load == 'folder_out':
        __save_file = True
    else:
        raise ValueError("not a able type")

    __title = title
    __file_type = file_type

    __format = format_in

    __open_path = path

    file_dialog = wx.FileDialog(__format, __title, __open_path, "",
                                file_type, style=wx.FD_MULTIPLE)

    if file_dialog.ShowModal() == wx.ID_OK:

        __format.m_staticText_load_tex.SetLabel("开始")
        __format.m_gauge_tex_load.SetValue(0)
        paths = file_dialog.GetPaths()
        if not len(paths) == 0:
            num = 0
            for path in paths:
                num += 1
                name = path.split('\\')[-1].split('.')[0]

                if name not in __format.tex_name:
                    __format.tex_name.append(name)
                    __format.tex_list_path_dir[name] = path
                    try:
                        __format.tex_name_cn.append(f"{num}）{__format.names[name]}——{name}")
                        __format._searched_tex.append(f"{__format.names[name]}{name}")
                    except KeyError:
                        __format.tex_name_cn.append(f"{num}）{name}——{name}")
                        __format._searched_tex.append(f"{name}")

                __format.m_gauge_tex_load.SetValue(function.re_int(100 * (num / len(paths))))
            __format.m_staticText_load_tex.SetLabel("完成")
        __format.m_listBox_tex.Set(__format.tex_name_cn)
