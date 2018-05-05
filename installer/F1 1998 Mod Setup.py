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

SLIDER_TITLE_1 = "             Welcome to\n       F1 1998 Mod Setup"

SLIDER_TITLE_2 = "               Path Input"

SLIDER_TITLE_3 = "    Confirm Installation"

MESSAGE_INFO_1 = """Here goes info text!"""

MESSAGE_INFO_2 = """Browse your EEA and Game path. By default,
mod will be installed into game, but you can
always select other path that you might prefer
more by selecting 'Install somewhere else...'."""


class GUI(wx.Frame):
    
    def __init__(self, Parent, Title):
        super(GUI, self).__init__(Parent, title=Title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER, size=(600, 450))
        # super(GUI, self).__init__(Parent, title=Title, size=(600, 450))
            
        self.MainPanel = self.GetMainPanel('#4f5049')
        
        self.CreateContainers()
        
        self.MainFrame()
        
        self.SetMinSize((600, 450))
        self.SetMaxSize((600, 450))
        self.Centre()
        self.Show()

    def MainFrame(self):        
        # IMAGE
        self.CreateModImage()        
        # IMAGE
        
        # TITLE
        self.TitleBox = wx.BoxSizer(wx.HORIZONTAL)
        self.CreateSliderTitle(SLIDER_TITLE_1)
        self.TitleContainer.SetSizer(self.TitleBox)
        # TITLE
        
        # INFO
        self.InfoBox = wx.BoxSizer(wx.HORIZONTAL)
        self.CreateInfoText(MESSAGE_INFO_1)
        self.InteractiveContainer.SetSizer(self.InfoBox)
        # INFO
        
        # BUTTONS + LINE
        self.BottomGrid = wx.GridBagSizer(5, 5)
        self.BottomBox = wx.BoxSizer(wx.HORIZONTAL)
        self.CreateLine()
        self.CreateNextButton("F2")
        self.CreateCloseButton()        
        self.BottomGrid.AddGrowableCol(0, 1)
        self.BottomGrid.AddGrowableCol(1, 0)
        self.BottomGrid.AddGrowableCol(2, 0)
        self.BottomGrid.AddGrowableCol(3, 0)
        self.BottomGrid.AddGrowableCol(4, 0)
        self.BottomBox.Add(self.BottomGrid, proportion=1)
        self.BottomContainer.SetSizer(self.BottomBox)
        print(self.BottomGrid.GetChildren())
        print(self.BottomBox.GetChildren())
        # BUTTONS + LINE
        
    def CreateContainers(self):
        self.ImageContainer = wx.Panel(self.MainPanel)
        self.ImageContainer.SetBackgroundColour('#ededed')
        
        self.TitleContainer = wx.Panel(self.MainPanel)
        self.TitleContainer.SetBackgroundColour('#ededed')
        
        self.InteractiveContainer = wx.Panel(self.MainPanel)
        self.InteractiveContainer.SetBackgroundColour('#ededed')
        
        self.BottomContainer = wx.Panel(self.MainPanel)
        self.BottomContainer.SetBackgroundColour('#ededed')
        
        self.MainGrid = wx.GridBagSizer(5, 5)
        self.MainBox = wx.BoxSizer(wx.VERTICAL)
        
        self.MainGrid.Add(self.ImageContainer, pos=(0, 0), span=(7, 2), flag=wx.EXPAND)
        self.MainGrid.Add(self.TitleContainer, pos=(0, 2), span=(2, 3), flag=wx.EXPAND)
        self.MainGrid.Add(self.InteractiveContainer, pos=(2, 2), span=(5, 3), flag=wx.EXPAND)
        self.MainGrid.Add(self.BottomContainer, pos=(7, 0), span=(1, 5), flag=wx.EXPAND)
        
        self.MainGrid.AddGrowableRow(0, 0)
        self.MainGrid.AddGrowableRow(1, 0)
        self.MainGrid.AddGrowableRow(2, 1)
        self.MainGrid.AddGrowableRow(3, 1)
        self.MainGrid.AddGrowableRow(4, 1)
        self.MainGrid.AddGrowableRow(5, 1)
        self.MainGrid.AddGrowableRow(6, 1)
        self.MainGrid.AddGrowableRow(7, 0)
        
        self.MainGrid.AddGrowableCol(0, 0)
        self.MainGrid.AddGrowableCol(1, 0)
        self.MainGrid.AddGrowableCol(2, 1)
        self.MainGrid.AddGrowableCol(3, 1)
        self.MainGrid.AddGrowableCol(4, 1)
        
        self.MainBox.Add(self.MainGrid, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        
        self.MainPanel.SetSizer(self.MainBox)

    def GetMainPanel(self, BG=None):
        Panel = wx.Panel(self)
        if not BG == None:
            Panel.SetBackgroundColour(BG)
        return Panel
        
    def CreateModImage(self):        
        Image = wx.StaticBitmap(self.ImageContainer, bitmap=wx.Bitmap(u'{}{}'.format(CWP, '/installer/gui/image.bmp')))        
        
    def CreateSliderTitle(self, Label):
        Font = wx.Font(18, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        
        Title = wx.StaticText(self.TitleContainer, label=Label)
        Title.SetFont(Font)
        
        self.TitleBox.Add(Title)
        
    def CreateInfoText(self, Label):
        Text = wx.StaticText(self.InteractiveContainer, label=Label)
        
        self.InfoBox.Add(Text, flag=wx.ALL, border=20)
        
    def CreateLine(self):
        Line = wx.StaticLine(self.BottomContainer)
        
        self.BottomGrid.Add(Line, pos=(0, 0), span=(0, 5), flag=wx.EXPAND)
        
    def CreateNextButton(self, Win):
        Button = wx.Button(self.BottomContainer, label="Next >>>", size=(100, 30))
        
        self.BottomGrid.Add(Button, pos=(1, 3), flag=wx.RIGHT, border=5)
        
        self.Bind(wx.EVT_BUTTON, self.GetNextWindowDict(Win), Button)
        
    def CreateCloseButton(self):
        Button = wx.Button(self.BottomContainer, label="Close", size=(100, 30))
        
        self.BottomGrid.Add(Button, pos=(1, 4), flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
        
        self.Bind(wx.EVT_BUTTON, self.OnClose, Button)
        
    def CreateBackButton(self, Win):
        Button = wx.Button(self.BottomContainer, label="<<< Back", size=(100, 30))
        print(self.BottomGrid.GetChildren())
        self.BottomGrid.Add(Button, pos=(1, 0), flag=wx.LEFT, border=10)
        print(self.BottomGrid.GetChildren())
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
        # TITLE
        self.ResetSizer(self.TitleBox)
        self.TitleBox = wx.BoxSizer(wx.HORIZONTAL)
        self.CreateSliderTitle(SLIDER_TITLE_2)
        self.TitleContainer.SetSizer(self.TitleBox)
        # TITLE
        
        # BACK BUTTON
        # self.ResetSizer(self.BottomGrid)
        self.BottomBox = wx.BoxSizer(wx.HORIZONTAL)
        print(self.BottomGrid.GetChildren())
        print(self.BottomBox.GetChildren())
        # self.CreateBackButton("F1")
        # self.BottomBox.Add(self.BottomGrid, proportion=1)
        # self.BottomContainer.SetSizer(self.BottomBox)
        
        # self.CreateNextButton("F3")
        # BACK BUTTON
        
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

    def ResetSizer(self, Sizer):
        for Item in range(len(Sizer.GetChildren())):
            Window = Sizer.GetItem(0).GetWindow()
            # print(Window)
            if not Window == None:
                Window.Destroy()
    

            
if __name__ == '__main__':
    Application = wx.App()
    GUI(None, Title='F1 1998 Wizard')
    Application.MainLoop()