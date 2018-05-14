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

TEXT_DICT = {
    'title': ["Welcome to\nF1 1998 Mod Setup",
              "Path Input",
              "Confirm Installation",
              "..."],
    'label': ["Panel One Info Text...",
              "Browse your EEA and Game path. By default,\n" \
              "mod will be installed into game, but you can\n" \
              "always select other path that you might prefer\n" \
              "more by selecting 'Install somewhere else...'.",
              "Please read the text below. It's very important for\n" \
              "you to know how this installation works. Thanks!",
              "..."],
    'box': ["Licence Text...",
            "Installation Info Text...",
            "..."],
    'input': ["EEA",
              "Game",
              "Install",
              "..."],
    'button': ["Help",
               "< Back",
               "Next >",
               "Install",
               "Close",
               "Browse...",
               "..."],
    'cbutton': ["I Agree!",
                "Install somewhere else...",
                "I read whole instructions and\n" \
                "I understood how Installation works!",
                "..."],
}


class CreateWidgets(object):
    
    def ModImage(parent):        
        return wx.StaticBitmap(parent, bitmap=wx.Bitmap(u'{}{}'.format(CWP, '/installer/gui/image.bmp')))

    def PanelTitle(parent, label):
        Font = wx.Font(18, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        Title = wx.StaticText(parent, label=label)
        Title.SetFont(Font)
        return Title
        
    def Text(parent, label, font=None):
        Text = wx.StaticText(parent, label=label)
        try:
            Text.SetFont(font)
        except:
            pass
        return Text
        
    def Line(parent):
        return wx.StaticLine(parent)
        
    def Button(parent, label, w, h):
        return wx.Button(parent, label=label, size=(w, h))
        
    def CheckButton(parent, label):
        return wx.CheckBox(parent, label=label)
        
    def TextEntry(parent, style=None, label=None):
        if not style == None:
            TextEntry = wx.TextCtrl(parent, style=style)
        else:
            TextEntry = wx.TextCtrl(parent)
        try:
            TextEntry.AppendText(label)
        except:
            pass
        return TextEntry

        
class MyFrame(wx.Frame):
    
    def __init__(self, Parent, Title):
        super(MyFrame, self).__init__(Parent, title=Title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER, size=(600, 450))
        
        self.PanelOne = self.LoadPanelOne(self)
        self.PanelTwo = self.LoadPanelTwo(self)
        self.PanelThree = self.LoadPanelThree(self)
        
        self.MainBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.MainBoxSizer.Add(self.PanelOne, proportion=1, flag=wx.EXPAND)
        self.MainBoxSizer.Add(self.PanelTwo, proportion=1, flag=wx.EXPAND)
        self.MainBoxSizer.Add(self.PanelThree, proportion=1, flag=wx.EXPAND)
        self.SetSizer(self.MainBoxSizer)
        
        self.ControlPanels()
        
        self.SetMinSize((600, 450))
        self.SetMaxSize((600, 450))
        self.Centre()
        
    def ControlPanels(self):    
        self.PanelOne.Show()
        self.PanelTwo.Hide()
        self.PanelThree.Hide()
        
    def LoadPanelOne(self, Parent):
        MainPanel = wx.Panel(Parent)
        
        ImagePanel = wx.Panel(MainPanel)
        TitlePanel = wx.Panel(MainPanel)
        InfoPanel = wx.Panel(MainPanel)
        self.BottomPanel = wx.Panel(MainPanel)
        
        MainGrid = wx.GridBagSizer(5, 5)
        MainBox = wx.BoxSizer(wx.HORIZONTAL)
        
        TitleGrid = wx.GridBagSizer(0, 0)
        InfoGrid = wx.GridBagSizer(5, 5)
        BottomGrid = wx.GridBagSizer(5, 5)
        
        ImageBox = wx.BoxSizer(wx.HORIZONTAL)
        TitleBox = wx.BoxSizer(wx.HORIZONTAL)
        InfoBox = wx.BoxSizer(wx.HORIZONTAL)
        BottomBox = wx.BoxSizer(wx.HORIZONTAL)
        
        ModImage = CreateWidgets.ModImage(ImagePanel)
        PanelTitle = CreateWidgets.PanelTitle(TitlePanel, TEXT_DICT['title'][0])
        InfoText = CreateWidgets.Text(InfoPanel, TEXT_DICT['label'][0])
        TextLicenceStyle = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL
        TextLicence = CreateWidgets.TextEntry(InfoPanel, style=TextLicenceStyle, label=TEXT_DICT['box'][0])
        CheckButton = CreateWidgets.CheckButton(InfoPanel, TEXT_DICT['cbutton'][0])
        Line = CreateWidgets.Line(self.BottomPanel)
        HelpButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][0], 100, 30)
        NextButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][2], 100, 30)
        CloseButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][4], 100, 30)
        
        CheckButton.Bind(wx.EVT_CHECKBOX, self.OnCheck)
        
        HelpButton.Bind(wx.EVT_BUTTON, self.OnHelp)
        NextButton.Bind(wx.EVT_BUTTON, self.OnNextPanel)
        CloseButton.Bind(wx.EVT_BUTTON, self.OnClose)
        
        TitleGrid.Add(PanelTitle, pos=(0, 0), flag=wx.ALIGN_CENTER)
        InfoGrid.Add(InfoText, pos=(0, 0), span=(0, 2), flag=wx.ALIGN_CENTER)
        InfoGrid.Add(TextLicence, pos=(1, 0), span=(2, 2), flag=wx.EXPAND)
        InfoGrid.Add(CheckButton, pos=(3, 0))
        BottomGrid.Add(Line, pos=(0, 0), span=(1, 4), flag=wx.EXPAND)
        BottomGrid.Add(HelpButton, pos=(1, 0), span=(1, 1), flag=wx.ALIGN_LEFT)
        BottomGrid.Add(NextButton, pos=(1, 2), span=(1, 1), flag=wx.ALIGN_LEFT)
        BottomGrid.Add(CloseButton, pos=(1, 3), span=(1, 1), flag=wx.ALIGN_RIGHT)
        
        TitleGrid.AddGrowableRow(0, 0)
        TitleGrid.AddGrowableCol(0, 0)
        InfoGrid.AddGrowableRow(1, 0)
        InfoGrid.AddGrowableRow(2, 0)
        InfoGrid.AddGrowableCol(0, 0)
        InfoGrid.AddGrowableCol(1, 0)
        BottomGrid.AddGrowableCol(0, 0)
        BottomGrid.AddGrowableCol(1, 0)
        BottomGrid.AddGrowableCol(2, 0)
        BottomGrid.AddGrowableCol(3, 0)
        
        ImageBox.Add(ModImage, proportion=1, flag=wx.EXPAND)
        TitleBox.Add(TitleGrid, proportion=1, flag=wx.EXPAND)
        InfoBox.Add(InfoGrid, proportion=1, flag=wx.EXPAND)
        BottomBox.Add(BottomGrid, proportion=1, flag=wx.EXPAND)
        
        ImagePanel.SetSizer(ImageBox)
        TitlePanel.SetSizer(TitleBox)
        InfoPanel.SetSizer(InfoBox)
        self.BottomPanel.SetSizer(BottomBox)
        
        MainGrid.Add(ImagePanel, pos=(0, 0), span=(6, 2), flag=wx.EXPAND)
        MainGrid.Add(TitlePanel, pos=(0, 2), span=(2, 3), flag=wx.EXPAND)
        MainGrid.Add(InfoPanel, pos=(2, 2), span=(4, 3), flag=wx.EXPAND|wx.ALL, border=20)
        MainGrid.Add(self.BottomPanel, pos=(6, 0), span=(2, 5), flag=wx.EXPAND)

        MainGrid.AddGrowableCol(4, 0)
        
        MainBox.Add(MainGrid, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
        
        MainPanel.SetSizer(MainBox)
        
        return MainPanel
        
    def LoadPanelTwo(self, Parent):
        MainPanel = wx.Panel(Parent)
        
        ImagePanel = wx.Panel(MainPanel)
        TitlePanel = wx.Panel(MainPanel)
        InputPanel = wx.Panel(MainPanel)
        self.BottomPanel = wx.Panel(MainPanel)
        
        MainGrid = wx.GridBagSizer(5, 5)
        MainBox = wx.BoxSizer(wx.HORIZONTAL)
        
        TitleGrid = wx.GridBagSizer(0, 0)
        InputGrid = wx.GridBagSizer(5, 5)
        BottomGrid = wx.GridBagSizer(5, 5)
        
        ImageBox = wx.BoxSizer(wx.HORIZONTAL)
        TitleBox = wx.BoxSizer(wx.HORIZONTAL)
        InputBox = wx.BoxSizer(wx.HORIZONTAL)
        BottomBox = wx.BoxSizer(wx.HORIZONTAL)
        
        Font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        
        ModImage = CreateWidgets.ModImage(ImagePanel)
        PanelTitle = CreateWidgets.PanelTitle(TitlePanel, TEXT_DICT['title'][1])
        InfoText = CreateWidgets.Text(InputPanel, TEXT_DICT['label'][1])
        EEALabel = CreateWidgets.Text(InputPanel, TEXT_DICT['input'][0], Font)
        GameLabel = CreateWidgets.Text(InputPanel, TEXT_DICT['input'][1], Font)
        InstallationLabel = CreateWidgets.Text(InputPanel, TEXT_DICT['input'][2], Font)
        EEAInput = CreateWidgets.TextEntry(InputPanel)
        GameInput = CreateWidgets.TextEntry(InputPanel)
        InstallationInput = CreateWidgets.TextEntry(InputPanel)
        EEAButton = CreateWidgets.Button(InputPanel, TEXT_DICT['button'][5], 75, 24)
        GameButton = CreateWidgets.Button(InputPanel, TEXT_DICT['button'][5], 75, 24)
        InstallationButton = CreateWidgets.Button(InputPanel, TEXT_DICT['button'][5], 75, 24)
        CheckButton = CreateWidgets.CheckButton(InputPanel, TEXT_DICT['cbutton'][1])
        Line = CreateWidgets.Line(self.BottomPanel)
        HelpButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][0], 100, 30)
        BackButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][1], 100, 30)
        NextButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][2], 100, 30)
        CloseButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][4], 100, 30)
        
        EEAButton.Bind(wx.EVT_BUTTON, self.OnBrowse)
        GameButton.Bind(wx.EVT_BUTTON, self.OnBrowse)
        InstallationButton.Bind(wx.EVT_BUTTON, self.OnBrowse)
        HelpButton.Bind(wx.EVT_BUTTON, self.OnHelp)
        BackButton.Bind(wx.EVT_BUTTON, self.OnBackPanel)
        NextButton.Bind(wx.EVT_BUTTON, self.OnNextPanel)
        CloseButton.Bind(wx.EVT_BUTTON, self.OnClose)
        CheckButton.Bind(wx.EVT_CHECKBOX, self.OnCheck)
        
        TitleGrid.Add(PanelTitle, pos=(0, 0), flag=wx.ALIGN_CENTER)
        InputGrid.Add(InfoText, pos=(0, 0), span=(0, 3), flag=wx.EXPAND)
        InputGrid.Add(EEALabel, pos=(1, 0), flag=wx.EXPAND)
        InputGrid.Add(GameLabel, pos=(2, 0), flag=wx.EXPAND)
        InputGrid.Add(InstallationLabel, pos=(4, 0), flag=wx.EXPAND)
        InputGrid.Add(EEAInput, pos=(1, 1), flag=wx.EXPAND)
        InputGrid.Add(GameInput, pos=(2, 1), flag=wx.EXPAND)
        InputGrid.Add(InstallationInput, pos=(4, 1), flag=wx.EXPAND)
        InputGrid.Add(EEAButton, pos=(1, 2), flag=wx.ALIGN_RIGHT)
        InputGrid.Add(GameButton, pos=(2, 2), flag=wx.ALIGN_RIGHT)
        InputGrid.Add(InstallationButton, pos=(4, 2), flag=wx.ALIGN_RIGHT)
        InputGrid.Add(CheckButton, pos=(3, 0), span=(0, 3), flag=wx.EXPAND)
        BottomGrid.Add(Line, pos=(0, 0), span=(1, 4), flag=wx.EXPAND)
        BottomGrid.Add(HelpButton, pos=(1, 0), span=(1, 1), flag=wx.ALIGN_LEFT)
        BottomGrid.Add(BackButton, pos=(1, 1), span=(1, 1), flag=wx.ALIGN_RIGHT)
        BottomGrid.Add(NextButton, pos=(1, 2), span=(1, 1), flag=wx.ALIGN_LEFT)
        BottomGrid.Add(CloseButton, pos=(1, 3), span=(1, 1), flag=wx.ALIGN_RIGHT)
        
        TitleGrid.AddGrowableRow(0, 0)
        TitleGrid.AddGrowableCol(0, 0)
        InputGrid.AddGrowableRow(0, 0)
        InputGrid.AddGrowableRow(3, 0)
        InputGrid.AddGrowableCol(0, 0)
        InputGrid.AddGrowableCol(1, 1)
        InputGrid.AddGrowableCol(2, 0)
        BottomGrid.AddGrowableCol(0, 0)
        BottomGrid.AddGrowableCol(1, 0)
        BottomGrid.AddGrowableCol(2, 0)
        BottomGrid.AddGrowableCol(3, 0)
        
        ImageBox.Add(ModImage, proportion=1, flag=wx.EXPAND)
        TitleBox.Add(TitleGrid, proportion=1, flag=wx.EXPAND)
        InputBox.Add(InputGrid, proportion=1, flag=wx.EXPAND)
        BottomBox.Add(BottomGrid, proportion=1, flag=wx.EXPAND)
        
        ImagePanel.SetSizer(ImageBox)
        TitlePanel.SetSizer(TitleBox)
        InputPanel.SetSizer(InputBox)
        self.BottomPanel.SetSizer(BottomBox)
        
        MainGrid.Add(ImagePanel, pos=(0, 0), span=(6, 2), flag=wx.EXPAND)
        MainGrid.Add(TitlePanel, pos=(0, 2), span=(2, 3), flag=wx.EXPAND)
        MainGrid.Add(InputPanel, pos=(2, 2), span=(4, 3), flag=wx.EXPAND|wx.ALL, border=20)
        MainGrid.Add(self.BottomPanel, pos=(6, 0), span=(2, 5), flag=wx.EXPAND)

        MainGrid.AddGrowableCol(4, 0)
        
        MainBox.Add(MainGrid, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
        
        MainPanel.SetSizer(MainBox)        
        
        return MainPanel        
        
    def LoadPanelThree(self, Parent):
        MainPanel = wx.Panel(Parent)
        
        ImagePanel = wx.Panel(MainPanel)
        TitlePanel = wx.Panel(MainPanel)
        InfoPanel = wx.Panel(MainPanel)
        self.BottomPanel = wx.Panel(MainPanel)
        
        MainGrid = wx.GridBagSizer(5, 5)
        MainBox = wx.BoxSizer(wx.HORIZONTAL)
        
        TitleGrid = wx.GridBagSizer(0, 0)
        InfoGrid = wx.GridBagSizer(5, 5)
        BottomGrid = wx.GridBagSizer(5, 5)
        
        ImageBox = wx.BoxSizer(wx.HORIZONTAL)
        TitleBox = wx.BoxSizer(wx.HORIZONTAL)
        InfoBox = wx.BoxSizer(wx.HORIZONTAL)
        BottomBox = wx.BoxSizer(wx.HORIZONTAL)
        
        ModImage = CreateWidgets.ModImage(ImagePanel)
        PanelTitle = CreateWidgets.PanelTitle(TitlePanel, TEXT_DICT['title'][2])
        TextInfo1 = CreateWidgets.Text(InfoPanel, TEXT_DICT['label'][2])
        TextStyle = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL
        TextInfo2 = CreateWidgets.TextEntry(InfoPanel, style=TextStyle, label=TEXT_DICT['box'][1])
        CheckButton = CreateWidgets.CheckButton(InfoPanel, TEXT_DICT['cbutton'][2])
        Line = CreateWidgets.Line(self.BottomPanel)
        HelpButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][0], 100, 30)
        BackButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][1], 100, 30)
        InstallButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][3], 100, 30)
        CloseButton = CreateWidgets.Button(self.BottomPanel, TEXT_DICT['button'][4], 100, 30)
        
        CheckButton.Bind(wx.EVT_CHECKBOX, self.OnCheck)
        HelpButton.Bind(wx.EVT_BUTTON, self.OnHelp)
        BackButton.Bind(wx.EVT_BUTTON, self.OnBackPanel)
        InstallButton.Bind(wx.EVT_BUTTON, self.OnInstall)
        CloseButton.Bind(wx.EVT_BUTTON, self.OnClose)
        
        TitleGrid.Add(PanelTitle, pos=(0, 0), flag=wx.ALIGN_CENTER)
        InfoGrid.Add(TextInfo1, pos=(0, 0), span=(0, 2), flag=wx.ALIGN_CENTER)
        InfoGrid.Add(TextInfo2, pos=(1, 0), span=(2, 2), flag=wx.EXPAND)
        InfoGrid.Add(CheckButton, pos=(3, 0))
        BottomGrid.Add(Line, pos=(0, 0), span=(1, 4), flag=wx.EXPAND)
        BottomGrid.Add(HelpButton, pos=(1, 0), span=(1, 1), flag=wx.ALIGN_LEFT)
        BottomGrid.Add(BackButton, pos=(1, 1), span=(1, 1), flag=wx.ALIGN_RIGHT)
        BottomGrid.Add(InstallButton, pos=(1, 2), span=(1, 1), flag=wx.ALIGN_LEFT)
        BottomGrid.Add(CloseButton, pos=(1, 3), span=(1, 1), flag=wx.ALIGN_RIGHT)
        
        TitleGrid.AddGrowableRow(0, 0)
        TitleGrid.AddGrowableCol(0, 0)        
        InfoGrid.AddGrowableRow(1, 0)
        InfoGrid.AddGrowableRow(2, 0)
        InfoGrid.AddGrowableCol(0, 0)
        InfoGrid.AddGrowableCol(1, 0)
        BottomGrid.AddGrowableCol(0, 0)
        BottomGrid.AddGrowableCol(1, 0)
        BottomGrid.AddGrowableCol(2, 0)
        BottomGrid.AddGrowableCol(3, 0)
        
        ImageBox.Add(ModImage, proportion=1, flag=wx.EXPAND)
        TitleBox.Add(TitleGrid, proportion=1, flag=wx.EXPAND)
        InfoBox.Add(InfoGrid, proportion=1, flag=wx.EXPAND)
        BottomBox.Add(BottomGrid, proportion=1, flag=wx.EXPAND)
        
        ImagePanel.SetSizer(ImageBox)
        TitlePanel.SetSizer(TitleBox)
        InfoPanel.SetSizer(InfoBox)
        self.BottomPanel.SetSizer(BottomBox)
        
        MainGrid.Add(ImagePanel, pos=(0, 0), span=(6, 2), flag=wx.EXPAND)
        MainGrid.Add(TitlePanel, pos=(0, 2), span=(2, 3), flag=wx.EXPAND)
        MainGrid.Add(InfoPanel, pos=(2, 2), span=(4, 3), flag=wx.EXPAND|wx.ALL, border=20)
        MainGrid.Add(self.BottomPanel, pos=(6, 0), span=(2, 5), flag=wx.EXPAND)

        MainGrid.AddGrowableCol(4, 0)
        
        MainBox.Add(MainGrid, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
        
        MainPanel.SetSizer(MainBox)
        
        return MainPanel        
    
    
    def OnNextPanel(self, Event):
        print("Next Panel!")
        if self.PanelOne.IsShown():
            self.PanelTwo.Show()
            self.PanelOne.Hide()            
        elif self.PanelTwo.IsShown():
            self.PanelTwo.Hide()
            self.PanelThree.Show()
        elif self.PanelThree.IsShown():
            self.PanelThree.Hide()
            # self.PanelFour.Show()
        self.Layout()
        
    def OnBackPanel(self, Event):
        print("Back Panel!")
        if self.PanelTwo.IsShown():
            self.PanelTwo.Hide()
            self.PanelOne.Show()
        elif self.PanelThree.IsShown():
            self.PanelThree.Hide()
            self.PanelTwo.Show()
        # elif self.PanelFour.IsShown():
            # self.PanelFour.Hide()
            # self.PanelThree.Show()
        self.Layout()

    def OnBrowse(self, Event):
        print("Browse...")

    def OnCheck(self, Event):
        print("Check!")
    
    def OnHelp(self, Event):
        print("Help!")
 
    def OnClose(self, Event):
        self.Close()
    
    def OnInstall(self, Event):
        print("Install!")
    
    
def Main():
    App = wx.App()
    Frame = MyFrame(None, Title='F1 1998 Wizard')
    Frame.Show()
    App.MainLoop()

    
if __name__ == '__main__':
    Main()
    