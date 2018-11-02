import Classes.frame_classes as fc
import wx

def main_part():
    app = wx.App(False)
    frame = fc.MainFrame(None)
    frame.Show()

    app.MainLoop()

if __name__ == '__main__':
    main_part()