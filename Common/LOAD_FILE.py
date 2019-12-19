# -*- coding: utf-8 -*-
import win32con
import win32gui


class WinUpLoadFile:

    def winUpLoadFile(self, file_path, title):

        # 一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样
        dialog = win32gui.FindWindow("#32770", title)
        # 二级窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        # 四级窗口
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        # 执行操作 输入文件路径
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
        # 点击打开上传文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


if __name__ == "__main__":
    WinUpLoadFile().winUpLoadFile("C:\\Users\\S\Desktop\\html\\jquery.html", "文件上传")

