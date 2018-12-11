import ctypes
import os
import sys
import winreg


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def append_dir_key():
    path = os.path.split(os.path.realpath(sys.argv[0]))[0]
    key = winreg.OpenKey(key=winreg.HKEY_CLASSES_ROOT, sub_key='Directory\\shell', access=winreg.KEY_CREATE_SUB_KEY)

    if is_admin():
        key = winreg.CreateKey(key, 'AzurLane')
        winreg.SetValue(key, 'command', winreg.REG_SZ, path + "\\dist\\main.exe %1")

        winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, path + "\\dist\\main.exe")
        winreg.SetValueEx(key, None, 0, winreg.REG_SZ, "碧蓝航线")

    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)




def del_key():
    if is_admin():

        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\AzurLane\\command')
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\shell\\AzurLane')


    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


if __name__ == '__main__':
    del_key()
    input()
