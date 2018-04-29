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

# CWD = os.path.dirname(os.path.realpath('F1 1998 Mod Setup.py'))  # fix !
# print(CWD)

CWP = 'E:/Users/Karlo/Race Department/Programs/F1-1998-Season-Mod'  # temp !


class GUI(wx.Frame):
    
    def __init__(self, Parent, Title):
        super(GUI, self).__init__(Parent, title=Title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER, size=(600, 450))
        
        self.Panel = wx.Panel(self)
        
        self.MainBox = wx.BoxSizer(wx.VERTICAL)
        self.MainSizer = wx.GridBagSizer(10, 10)
        
        self.ImageBox = wx.BoxSizer(wx.HORIZONTAL)
        self.ImageSizer = wx.GridBagSizer(0, 0)
        self.TitleBox = wx.BoxSizer(wx.HORIZONTAL)
        self.TitleSizer = wx.GridBagSizer(0, 0)
        self.InterFaceBox = wx.BoxSizer(wx.HORIZONTAL)
        self.InterFaceSizer = wx.GridBagSizer(0, 0)
        self.ButtonsBox = wx.BoxSizer(wx.HORIZONTAL)
        self.ButtonsSizer = wx.GridBagSizer(0, 0)
        
        self.IntroduceWindow()
        
        self.SetMinSize((600, 450))
        self.SetMaxSize((600, 450))
        self.Centre()
        self.Show()        

    def IntroduceWindow(self):        
        ModImage = wx.StaticBitmap(self.Panel, bitmap=wx.Bitmap(u'{}{}'.format(CWP, '/installer/gui/image.bmp')))        
        ModTitleFont = wx.Font(18, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        ModTitle = wx.StaticText(self.Panel, label="{}\n{}".format("Welcome to", "F1 1998 Mod Setup"))
        ModTitle.SetFont(ModTitleFont)         
        IntroText = wx.StaticText(self.Panel, label="Intro Text Here")        
        Line = wx.StaticLine(self.Panel)
        NextButton = wx.Button(self.Panel, label="Next >>>", size=(100, 30))
        CloseButton = wx.Button(self.Panel, label="Close", size=(100, 30))
        BackButton = wx.Button(self.Panel, label="Back <<<", size=(100, 30))

        self.ImageSizer.Add(ModImage, pos=(0, 0))
        self.TitleSizer.Add(ModTitle, pos=(0, 0))
        self.InterFaceSizer.Add(IntroText, pos=(0, 0), flag=wx.ALL, border=20)        
        self.ButtonsSizer.Add(Line, pos=(0, 0), span=(0, 3), flag=wx.EXPAND)
        self.ButtonsSizer.Add(BackButton, pos=(1, 0), flag=wx.RIGHT, border=254)
        self.ButtonsSizer.Add(CloseButton, pos=(1, 2))
        self.ButtonsSizer.Add(NextButton, pos=(1, 1), flag=wx.RIGHT, border=10)
        
        self.ImageBox.Add(self.ImageSizer)
        self.TitleBox.Add(self.TitleSizer, flag=wx.LEFT|wx.RIGHT, border=45)
        self.InterFaceBox.Add(self.InterFaceSizer)
        self.ButtonsBox.Add(self.ButtonsSizer)
        
        self.MainSizer.Add(self.ImageBox, pos=(0, 0), span=(2, 0))
        self.MainSizer.Add(self.TitleBox, pos=(0, 1))
        self.MainSizer.Add(self.InterFaceBox, pos=(1, 1))
        self.MainSizer.Add(self.ButtonsBox, pos=(2, 0), span=(0, 2))
        
        self.MainBox.Add(self.MainSizer, flag=wx.ALL, border=10)
        
        self.Panel.SetSizerAndFit(self.MainBox)
        
        self.Bind(wx.EVT_BUTTON, self.OnNextIW, NextButton)
        self.Bind(wx.EVT_BUTTON, self.OnClose, CloseButton)

    def DirInputWindow(self):
        pass
        
    def OnClose(self, Evt):
        self.Close()
    
    def OnNextIW(self, Evt):
        self.DirInputWindow()
        
    
if __name__ == '__main__':
    Application = wx.App()
    GUI(None, Title='F1 1998 Wizard')
    Application.MainLoop()