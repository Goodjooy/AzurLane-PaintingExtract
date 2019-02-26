import ctypes
import sys
import winreg


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def deal_dir_key(path, dir_menu=False, bg=False):
    path = path
    key = winreg.OpenKey(key=winreg.HKEY_CLASSES_ROOT, sub_key='Directory', access=winreg.KEY_CREATE_SUB_KEY)

    if is_admin():
        if dir_menu:
            key_dir = winreg.CreateKey(key, 'shell\\AzurLane')
            winreg.SetValue(key_dir, 'command', winreg.REG_SZ, path + "\\dist\\main.exe %1")

            winreg.SetValueEx(key_dir, 'Icon', 0, winreg.REG_SZ, path + "\\dist\\main.exe")
            winreg.SetValueEx(key_dir, None, 0, winreg.REG_SZ, "导入碧蓝航线立绘还原工具")
        if not dir_menu:
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\AzurLane\\command')
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\AzurLane')

        if not bg:
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\AzurLane\\command')
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\AzurLane')
        if bg:
            key_dir = winreg.CreateKey(key, 'Background\\shell\\AzurLane')
            winreg.SetValue(key_dir, 'command', winreg.REG_SZ, path + "\\dist\\main.exe %1")

            winreg.SetValueEx(key_dir, 'Icon', 0, winreg.REG_SZ, path + "\\dist\\main.exe")
            winreg.SetValueEx(key_dir, None, 0, winreg.REG_SZ, "导入碧蓝航线立绘还原工具")


    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


def del_dir_key(dir_menu=False, bg=False):
    if is_admin():
        if not dir_menu:
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\AzurLane\\command')
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\AzurLane')
        if not bg:
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\AzurLane\\command')
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\AzurLane')


    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


if __name__ == '__main__':
    del_key()
    input()
