import wx
from Infernalwhileloop import Worker
import popupsub as ps
import threading
import Queue
import random
import time


class TestFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Program')
        self.thread1 = Worker()

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        # Create panel one
        self.panel_one = ps.TestPanel(self)
        sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btn.Bind(wx.EVT_BUTTON,self.onShowPopup)
        # create panel two
        self.panel_two = ps.ShowyPanel(self)
        sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.btn.Bind(wx.EVT_BUTTON, self.hide_panel_two)
        self.panel_two.Hide()

        self.panel3 = ps.NicePanel(self)
        sizer.Add(self.panel3,1,wx.EXPAND)
        self.panel3.Hide()

        # create frame
        self.SetSize((450, 350))
        self.Centre()
        self.Show()

    """function for hiding panel one"""

    def hide_panel_one(self,event):
        one = self.panel_one
        two = self.panel_two
        two.label.SetLabel(one.patentry.GetValue()+"yoloswag")
        # self.panel_one.label.SetLabel(self.panel_one.txtentry.GetValue() + " woopwoop")
        one.Hide()
        two.Show()
        self.Layout()

    """function for hiding panel two"""
    def hide_panel_two(self,event):
        one = self.panel_one
        two = self.panel_two
        three = self.panel3
        two.label.SetLabel(u'Dry-Eye')
        two.Hide()
        three.Show()
        self.Layout()

    def onShowPopup(self,event):
        """"""
        one = self.panel_one
        if one.patentry.GetValue().lower() == 'yes':

            self.win = ps.TestPopup(self.GetTopLevelParent(), wx.SIMPLE_BORDER,one.patentry.GetValue().lower())
            self.panel_one.Hide()

            btn = event.GetEventObject()
            pos = btn.ClientToScreen( (-230,-150) )
            sz =  btn.GetSize()
            self.win.Position(pos, (0, sz[1]))
            # self.win.stbut.Bind(wx.EVT_BUTTON,self.startprogram)

            self.win.Show(True)







    def startprogram(self):
        self.thread1.start()
        self.thread1.join()
        print ' tesstone'
        # self.thread1.join()
        self.win.Destroy()
        self.panel_two.Show()
        self.Layout()


    #
    # def DestroyPopupReturn(self,event):
    #     self.win.Destroy()
    #     self.panel_one.Show()
    #     self.thread1.stop = True



#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = TestFrame()
    app.MainLoop()
