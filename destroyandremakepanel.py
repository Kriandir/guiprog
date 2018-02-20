import wx
import sys
import traceback

def show_error():
    message = ''.join(traceback.format_exception(*sys.exc_info()))
    dialog = wx.MessageDialog(None, message, 'Error!', wx.OK|wx.ICON_ERROR)
    dialog.ShowModal()

class MyPanels(wx.Panel):

    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent)
        self.parent = parent

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(1000, 480))
        self.parent = parent

        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour("grey")

        self.leftpanel = MyPanels(self.panel, 1)
        self.rightpanel = MyPanels(self.panel, 1)
        self.leftpanel.SetBackgroundColour("red")
        self.rightpanel.SetBackgroundColour("green")

        self.basicsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.basicsizer.Add(self.leftpanel, 1, wx.EXPAND)
        self.basicsizer.Add(self.rightpanel, 1, wx.EXPAND)
        self.panel.SetSizer(self.basicsizer)

        button =  wx.Button(self.leftpanel, 1, 'DIE DIE DIE', (50, 130))
        buttonres = wx.Button(self.leftpanel, 2, 'Resurrect', (50, 230))
        buttonextra = wx.Button(self.leftpanel, 3, 'Test', (50, 330))

        self.Bind(wx.EVT_BUTTON, self.destroyPanel, button)
        self.Bind(wx.EVT_BUTTON, self.CreateNewPanel, buttonres)

    def CreateNewPanel(self, event):
        self.rightpanel = MyPanels(self.panel, 1)
        self.rightpanel.SetBackgroundColour("green")
        self.basicsizer.Add(self.rightpanel, 1, wx.EXPAND)
        self.panel.Layout()

        self.Show(True)
        self.Centre()

    def destroyPanel(self, event):
        self.rightpanel.Hide()
        self.panel.Layout()

def main():
    app = wx.App()
    try:
        frame = MyFrame(None, -1, 'Die.py')
        frame.Show()
        app.MainLoop()
    except:
        show_error()

if __name__ == '__main__':
    main()
