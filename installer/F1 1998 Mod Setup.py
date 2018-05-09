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

PANEL_TITLE_1 = "             Welcome to\n       F1 1998 Mod Setup"

PANEL_TITLE_2 = "               Path Input"

PANEL_TITLE_3 = "    Confirm Installation"

MESSAGE_INFO_1 = """Here goes info text!"""

MESSAGE_INFO_2 = """Browse your EEA and Game path. By default,
mod will be installed into game, but you can
always select other path that you might prefer
more by selecting 'Install somewhere else...'."""


class CreateWidgets(object):
    
    def ModImage(parent):        
        Image = wx.StaticBitmap(parent, bitmap=wx.Bitmap(u'{}{}'.format(CWP, '/installer/gui/image.bmp')))
        return Image

    def PanelTitle(parent, label):
        Font = wx.Font(18, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        Title = wx.StaticText(parent, label=label)
        Title.SetFont(Font)
        return Title
        
    def InfoText(parent, label):
        Text = wx.StaticText(parent, label=label)
        return Text
        
    def Line(parent):
        Line = wx.StaticLine(parent)
        return Line
        
    def NextButton(parent):
        Button = wx.Button(parent, label="Next >", size=(100, 30))
        return Button
        
    def CloseButton(parent):
        Button = wx.Button(parent, label="Close", size=(100, 30))
        return Button
        
    def BackButton(parent):
        Button = wx.Button(parent, label="< Back", size=(100, 30))
        return Button
        
    def HelpButton(parent):
        Button = wx.Button(parent, label="Help", size=(100, 30))
        return Button

        
class MyFrame(wx.Frame):
    
    def __init__(self, Parent, Title):
        super(MyFrame, self).__init__(Parent, title=Title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER, size=(600, 450))
        
        # MainPanel = wx.Panel(self)
        # MainPanel.SetBackgroundColour('#ededed') # '#ededed' '#4f5049'
        
        self.PanelOne = self.LoadPanelOne(self)
        self.PanelTwo = self.LoadPanelTwo(self)
        
        self.PanelTwo.Hide()
        
        self.MainBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.MainBoxSizer.Add(self.PanelOne, proportion=1, flag=wx.EXPAND)
        self.MainBoxSizer.Add(self.PanelTwo, proportion=1, flag=wx.EXPAND)
        self.SetSizer(self.MainBoxSizer)
        
        
        self.SetMinSize((600, 450))
        # self.SetMaxSize((600, 450))
        self.Centre()
        
    def LoadPanelOne(self, Parent):
        MainPanel = wx.Panel(Parent)
        
        ImagePanel = wx.Panel(MainPanel)
        TitlePanel = wx.Panel(MainPanel)
        InfoPanel = wx.Panel(MainPanel)
        BottomPanel = wx.Panel(MainPanel)
        
        MainGrid = wx.GridBagSizer(5, 5)
        MainBox = wx.BoxSizer(wx.HORIZONTAL)
        
        BottomGrid = wx.GridBagSizer(5, 5)
        
        ImageBox = wx.BoxSizer(wx.HORIZONTAL)
        TitleBox = wx.BoxSizer(wx.HORIZONTAL)
        InfoBox = wx.BoxSizer(wx.HORIZONTAL)
        BottomBox = wx.BoxSizer(wx.HORIZONTAL)
        
        ModImage = CreateWidgets.ModImage(ImagePanel)
        PanelTitle = CreateWidgets.PanelTitle(TitlePanel, PANEL_TITLE_1)
        InfoText = CreateWidgets.InfoText(InfoPanel, MESSAGE_INFO_1)
        Line = CreateWidgets.Line(BottomPanel)
        HelpButton = CreateWidgets.HelpButton(BottomPanel)
        NextButton = CreateWidgets.NextButton(BottomPanel)
        CloseButton = CreateWidgets.CloseButton(BottomPanel)
        
        HelpButton.Bind(wx.EVT_BUTTON, self.OnHelp)
        NextButton.Bind(wx.EVT_BUTTON, self.OnNextPanel)
        CloseButton.Bind(wx.EVT_BUTTON, self.OnClose)
        
        BottomGrid.Add(Line, pos=(0, 0), span=(1, 4), flag=wx.EXPAND)
        BottomGrid.Add(HelpButton, pos=(1, 0), span=(1, 1), flag=wx.ALIGN_LEFT)
        BottomGrid.Add(NextButton, pos=(1, 2), span=(1, 1), flag=wx.ALIGN_RIGHT)
        BottomGrid.Add(CloseButton, pos=(1, 3), span=(1, 1))
        
        BottomGrid.AddGrowableCol(0, 0)
        BottomGrid.AddGrowableCol(1, 0)
        BottomGrid.AddGrowableCol(2, 0)
        BottomGrid.AddGrowableCol(3, 0)
        
        ImageBox.Add(ModImage, proportion=1, flag=wx.EXPAND)
        TitleBox.Add(PanelTitle, proportion=1, flag=wx.EXPAND)
        InfoBox.Add(InfoText, proportion=1, flag=wx.EXPAND)
        BottomBox.Add(BottomGrid, proportion=1, flag=wx.EXPAND)
        
        ImagePanel.SetSizer(ImageBox)
        TitlePanel.SetSizer(TitleBox)
        InfoPanel.SetSizer(InfoBox)
        BottomPanel.SetSizer(BottomBox)
        
        MainGrid.Add(ImagePanel, pos=(0, 0), span=(6, 2), flag=wx.EXPAND)
        MainGrid.Add(TitlePanel, pos=(0, 2), span=(2, 3), flag=wx.EXPAND)
        MainGrid.Add(InfoPanel, pos=(2, 2), span=(4, 3), flag=wx.EXPAND)
        MainGrid.Add(BottomPanel, pos=(6, 0), span=(2, 5), flag=wx.EXPAND)
        
        # MainGrid.AddGrowableRow(0, 0)
        # MainGrid.AddGrowableRow(1, 0)
        # MainGrid.AddGrowableRow(2, 0)
        # MainGrid.AddGrowableRow(3, 0)
        # MainGrid.AddGrowableRow(4, 0)
        # MainGrid.AddGrowableRow(5, 0)
        # MainGrid.AddGrowableRow(6, 0)
        # MainGrid.AddGrowableRow(7, 0)
        # MainGrid.AddGrowableCol(0, 0)
        # MainGrid.AddGrowableCol(1, 0)
        # MainGrid.AddGrowableCol(2, 0)
        # MainGrid.AddGrowableCol(3, 0)
        # MainGrid.AddGrowableCol(4, 0)
        
        MainBox.Add(MainGrid, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
        
        MainPanel.SetSizer(MainBox)
        
        
        
        return MainPanel
        
        
        
    def LoadPanelTwo(self, Parent):
        MainPanel = wx.Panel(Parent)
        
        ButtonPanel = wx.Panel(MainPanel)
        
        Box = wx.BoxSizer(wx.HORIZONTAL)
        BackButton = CreateWidgets.BackButton(ButtonPanel)
        BackButton.Bind(wx.EVT_BUTTON, self.OnBackPanel)
        Box.Add(BackButton, flag=wx.EXPAND)
        
        ButtonPanel.SetSizer(Box)
        
        Box2 = wx.BoxSizer(wx.HORIZONTAL)
        Box2.Add(ButtonPanel)
        
        MainPanel.SetSizer(Box2)
        
        return MainPanel
        
        
        
    def LoadPanelThree(self, Parent):
        MainPanel = wx.Panel(Parent)
        BackButton = CreateWidgets.BackButton(MainPanel)
        BackButton.Bind(wx.EVT_BUTTON, self.OnBackPanel)
        
        
        
        return MainPanel
        
    
    
    def OnNextPanel(self, Event):
        print("Next Panel!")
        self.PanelOne.Hide()
        self.PanelTwo.Show()
        self.Layout()
        
    def OnBackPanel(self, Event):
        print("Back Panel!")
        self.PanelOne.Show()
        self.PanelTwo.Hide()
        self.Layout()

        

        
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

    
    def OnHelp(self, Event):
        print("Help!")
 
    def OnClose(self, Event):
        self.Close()
    
def Main():
    App = wx.App()
    Frame = MyFrame(None, Title='F1 1998 Wizard')
    Frame.Show()
    App.MainLoop()

    
if __name__ == '__main__':
    Main()