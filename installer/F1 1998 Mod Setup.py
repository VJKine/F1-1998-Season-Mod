#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
PROGRAM INFO:
    date started: 29.04.2018. 0:23 Sunday
    date finished: ??.??.2018 ??:?? ?
    publisher: Karlo Dimjašević
    profile name: Karlito
    program name: F1 1998 Mod Setup
    modder group name: The Classic Crew
    licence: No
    style: CamelCase
    usage: Mod Installer
    ...
"""

import wx
import os
import time

# CWD = os.path.dirname(os.path.realpath('F1 1998 Mod Setup.py'))
# print(CWD)

CWP = 'E:/Users/Karlo/Race Department/Programs/F1 1998 Mod Installer v1.0'


class GUI(wx.Frame):
    
    def __init__(self, Parent, Title):
        super(GUI, self).__init__(Parent, title=Title, size=(600, 450))
        
        self.IntroduceWindow()
        self.Centre()
        self.Show()
        
        
    def IntroduceWindow(self):
        Font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        Font.SetPointSize(200)
        
        Panel = wx.Panel(self)
        VerBox = wx.BoxSizer(wx.VERTICAL)
        
        Sizer = wx.GridBagSizer(30, 30)
        
        ModImage = wx.StaticBitmap(Panel, bitmap=wx.Bitmap(u'{}{}'.format(CWP, '/gui/image.bmp')))
        Sizer.Add(ModImage, pos=(0, 0), span=(2, 0), flag=wx.EXPAND)
        
        ModTitleFont = wx.Font(18, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        ModTitle = wx.StaticText(Panel, label="Welcome to\nF1 1998 Mod Setup")
        ModTitle.SetFont(ModTitleFont)
        Sizer.Add(ModTitle, pos=(0, 1), span=(0, 2), flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=30)
        
        IntroTextMessage = """
        Here, intro text!
        """
        IntroText = wx.StaticText(Panel, label=IntroTextMessage)
        Sizer.Add(IntroText, pos=(1, 1), span=(0, 2), flag=wx.EXPAND)
        
        Line = wx.StaticLine(Panel)
        Sizer.Add(Line, pos=(2, 0), span=(0, 3), flag=wx.EXPAND, border=0)
        
        NextButton = wx.Button(Panel, label="Next >>>", size=(100, 30))
        Sizer.Add(NextButton, pos=(3, 1), flag=wx.TOP, border=-13)
        
        CloseButton = wx.Button(Panel, label="Close", size=(100, 30))
        Sizer.Add(CloseButton, pos=(3, 2), flag=wx.TOP, border=-13)
        
        VerBox.Add(Sizer, flag=wx.ALL, border=15)
        Panel.SetSizerAndFit(VerBox)
        
    
if __name__ == '__main__':
    Application = wx.App()
    GUI(None, Title='F1 1998 Mod Setup')
    Application.MainLoop()