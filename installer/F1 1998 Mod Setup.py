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

SLIDER_TITLE_1 = "     Welcome to\n     F1 1998 Mod Setup"

SLIDER_TITLE_2 = "            Path Input"

SLIDER_TITLE_3 = "    Confirm Installation"

MESSAGE_INFO_1 = """Here goes info text!"""

MESSAGE_INFO_2 = """Browse your EEA and Game path. By default,
mod will be installed into game, but you can
always select other path that you might prefer
more by selecting 'Install somewhere else...'."""


class GUI(wx.Frame):
    
    def __init__(self, Parent, Title):
        # super(GUI, self).__init__(Parent, title=Title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER, size=(573, 450))
        super(GUI, self).__init__(Parent, title=Title, size=(573, 450))
            
        self.GetPanel()
        
        self.FrameOne()
        
        #self.SetMinSize((573, 450))
        #self.SetMaxSize((573, 450))
        self.Centre()
        self.Show()    

    def FrameOne(self):
        self.GetMainSizers()
        self.GetSubSizers()
        
        self.CreateModImage()
        self.CreateSliderTitle(SLIDER_TITLE_1)
        self.CreateInfoText(MESSAGE_INFO_1)
        self.CreateLine()
        self.CreateNextButton("F2")
        self.CreateCloseButton()
        
        self.MainGrid.AddGrowableCol(4, 1)
        
        self.SetSubToMain()
        self.SetBoxToPanel()
        
    def FrameTwo(self):
        self.GetMainSizers()
        self.GetSubSizers()
        
        self.CreateModImage()
        self.CreateSliderTitle(SLIDER_TITLE_2)
        self.CreateDirInputBox(MESSAGE_INFO_2)
        self.CreateLine()
        self.CreateNextButton("F3")
        self.CreateCloseButton()
        self.CreateBackButton("F1")
        
        self.MainGrid.AddGrowableCol(4, 1)
        
        self.SetSubToMain()
        self.SetBoxToPanel()
        
    def FrameThree(self):
        self.GetMainSizers()
        self.GetSubSizers()
        
        self.CreateModImage()
        self.CreateSliderTitle(SLIDER_TITLE_3)
        self.CreateConfInstBox(MESSAGE_INFO_1, "")
        self.CreateLine()
        self.CreateNextButton("F4")
        self.CreateCloseButton()
        self.CreateBackButton("F2")
        
        self.SetSubToMain()
        self.SetBoxToPanel()
        
        

    def GetPanel(self):
        self.Panel = wx.Panel(self)
        
    def GetMainSizers(self):
        self.MainBox = wx.BoxSizer(wx.VERTICAL)
        self.MainGrid = wx.GridBagSizer(5, 5)
        
    def GetSubSizers(self):
        self.SubBox = wx.BoxSizer(wx.HORIZONTAL)
        self.SubGrid = wx.GridBagSizer(20, 10)

    def SetSubToMain(self):
        self.SubBox.Add(self.SubGrid, flag=wx.ALL, border=20)
        self.MainGrid.Add(self.SubBox, pos=(1, 2), span=(3, 5))
        
    def SetBoxToPanel(self):
        self.MainBox.Add(self.MainGrid, proportion=1, flag=wx.ALL, border=10)
        self.Panel.SetSizerAndFit(self.MainBox)
        
    def ResetMainGrid(self):
        for Item in range(len(self.MainGrid.GetChildren())):
            Window = self.MainGrid.GetItem(0).GetWindow()
            print(Window)
            if not Window == None:
                Window.Destroy()
            
            # self.MainGrid.GetItem(0).GetWindow().Destroy()
            
    def ResetSubGrid(self):
        for Item in range(len(self.SubGrid.GetChildren())):
            Window = self.SubGrid.GetItem(0).GetWindow()
            print(Window)
            Window.Destroy()
            
            # self.SubGrid.GetItem(0).GetWindow().Destroy()
        
    def CreateModImage(self):
        Image = wx.StaticBitmap(self.Panel, bitmap=wx.Bitmap(u'{}{}'.format(CWP, '/installer/gui/image.bmp')))
        self.MainGrid.Add(Image, pos=(0, 0), span=(4, 2))
        
    def CreateSliderTitle(self, Label):
        Font = wx.Font(18, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        Title = wx.StaticText(self.Panel, label=Label)
        Title.SetFont(Font)
        self.MainGrid.Add(Title, pos=(0, 2), span=(0, 4))
        
    def CreateInfoText(self, Label):
        Text = wx.StaticText(self.Panel, label=Label)
        self.SubGrid.Add(Text, pos=(0, 0))
        
    def CreateLine(self):
        Line = wx.StaticLine(self.Panel)
        self.MainGrid.Add(Line, pos=(4, 0), span=(0, 7), flag=wx.EXPAND)
        
    def CreateNextButton(self, Win):
        Button = wx.Button(self.Panel, label="Next >>>", size=(100, 30))
        self.MainGrid.Add(Button, pos=(5, 3))
        self.Bind(wx.EVT_BUTTON, self.GetNextWindowDict(Win), Button)
        
    def CreateCloseButton(self):
        Button = wx.Button(self.Panel, label="Close", size=(100, 30))
        self.MainGrid.Add(Button, pos=(5, 4))
        self.Bind(wx.EVT_BUTTON, self.OnClose, Button)
        
    def CreateBackButton(self, Win):
        Button = wx.Button(self.Panel, label="<<< Back", size=(100, 30))
        self.MainGrid.Add(Button, pos=(5, 0))
        self.Bind(wx.EVT_BUTTON, self.GetBackWindowDict(Win), Button)
        
    def CreateDirInputBox(self, Label):        
        Font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        Text = wx.StaticText(self.Panel, label=Label)
        EEALabel = wx.StaticText(self.Panel, label="EEA:")
        EEALabel.SetFont(Font)
        GameLabel = wx.StaticText(self.Panel, label="Game:")
        GameLabel.SetFont(Font)
        InstLabel = wx.StaticText(self.Panel, label="Install:")
        InstLabel.SetFont(Font)
        EEAInput = wx.TextCtrl(self.Panel)
        GameInput = wx.TextCtrl(self.Panel)
        InstInput = wx.TextCtrl(self.Panel)        
        EEAButton = wx.Button(self.Panel, label="Browse...", size=(75, 24))
        GameButton = wx.Button(self.Panel, label="Browse...", size=(75, 24))
        InstButton = wx.Button(self.Panel, label="Browse...", size=(75, 24))        
        CheckButton = wx.CheckBox(self.Panel, label="Install somewhere else...")
        
        self.SubGrid.Add(Text, pos=(0, 0), span=(0, 3))
        self.SubGrid.Add(EEALabel, pos=(1, 0))
        self.SubGrid.Add(GameLabel, pos=(2, 0))
        self.SubGrid.Add(InstLabel, pos=(4, 0))
        self.SubGrid.Add(EEAInput, pos=(1, 1))
        self.SubGrid.Add(GameInput, pos=(2, 1))
        self.SubGrid.Add(InstInput, pos=(4, 1))
        self.SubGrid.Add(EEAButton, pos=(1, 2))
        self.SubGrid.Add(GameButton, pos=(2, 2))
        self.SubGrid.Add(InstButton, pos=(4, 2))
        self.SubGrid.Add(CheckButton, pos=(3, 0), span=(0, 3))

    def CreateConfInstBox(self, Label1, Label2):
        Text = wx.StaticText(self.Panel, label=Label1)
        InstText = wx.TextCtrl(self.Panel, size=(250, 100), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
        InstText.AppendText(Label2)
        CheckButton = wx.CheckBox(self.Panel, label="I read whole instructions and I\nunderstood how Installation works")
        
        self.SubGrid.Add(Text, pos=(0, 0), span=(0, 2))
        self.SubGrid.Add(InstText, pos=(1, 0), span=(2, 2))
        self.SubGrid.Add(CheckButton, pos=(3, 0))
        
    def OnClose(self, Evt):
        self.Close()
    
    def OnNextF2(self, Evt):
        self.ResetMainGrid()        
        self.ResetSubGrid()
        self.FrameTwo()
        
    def OnNextF3(self, Evt):
        self.ResetMainGrid()
        self.ResetSubGrid()
        self.FrameThree()
       
    def OnBackF1(self, Evt):
        self.ResetMainGrid()
        self.ResetSubGrid()
        self.FrameOne()

    def OnBackF2(self, Evt):
        self.ResetMainGrid()
        self.ResetSubGrid()
        self.FrameTwo()
    
    def GetNextWindowDict(self, Key):
        if Key == "F2":
            return self.OnNextF2
        elif Key == "F3":
            return self.OnNextF3
        
    def GetBackWindowDict(self, Key):
        if Key == "F1":
            return self.OnBackF1
        elif Key == "F2":
            return self.OnBackF2


            
if __name__ == '__main__':
    Application = wx.App()
    GUI(None, Title='F1 1998 Wizard')
    Application.MainLoop()