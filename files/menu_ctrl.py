import ctypes
import json
import os
import sys
import winreg


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def deal_dir_key(path_func, dir_menu=False, bg=False):
    path_func = path_func
    key = winreg.OpenKey(key=winreg.HKEY_CLASSES_ROOT, sub_key='Directory', access=winreg.KEY_CREATE_SUB_KEY)

    if is_admin():
        if dir_menu:
            key_dir = winreg.CreateKey(key, 'shell\\AzurLane')
            winreg.SetValue(key_dir, 'command', winreg.REG_SZ, path_func + "\\main.exe %1")

            winreg.SetValueEx(key_dir, 'Icon', 0, winreg.REG_SZ, path_func + "\\main.exe")
            winreg.SetValueEx(key_dir, None, 0, winreg.REG_SZ, "导入碧蓝航线立绘还原工具")
        if not dir_menu:
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\AzurLane\\command')
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\AzurLane')

        if not bg:
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\AzurLane\\command')
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\AzurLane')
        if bg:
            key_dir = winreg.CreateKey(key, 'Background\\shell\\AzurLane')
            winreg.SetValue(key_dir, 'command', winreg.REG_SZ, path_func + "\\main.exe %V")

            winreg.SetValueEx(key_dir, 'Icon', 0, winreg.REG_SZ, path_func + "\\main.exe")
            winreg.SetValueEx(key_dir, None, 0, winreg.REG_SZ, "导入碧蓝航线立绘还原工具")

    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


path = os.path.split(os.path.realpath(sys.argv[0]))[0]
print(path)
path = path.replace('\\files', '')
print(path)
info = os.path.join(path, 'files\\menu_ctrl.ini')
print(info)
with open(info, 'r')as file:
    type_dir, type_bg = json.load(file)

deal_dir_key(path, type_dir, type_bg)
