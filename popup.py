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

        self.stop = False

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
        self.win = ps.TestPopup(self.GetTopLevelParent(), wx.SIMPLE_BORDER)
        self.panel_one.Hide()
        self.stop = False

        btn = event.GetEventObject()
        pos = btn.ClientToScreen( (-160,-150) )
        sz =  btn.GetSize()
        self.win.Position(pos, (0, sz[1]))
        self.win.stbut.Bind(wx.EVT_BUTTON,self.DestroyPopupReturn)
        self.win.Show(True)
        #
        # self.our_thread = threading.Thread(target=self.do_this)
        # self.our_thread.start()

        self.thread1 = Worker(self)
        wx.CallAfter(self.startprogram)


    def do_this(self):
        i = 0
        while i <1000000:
            i+=1
            print i
            if self.stop:
                return
        self.DestroyandContinue()





    def startprogram(self):
        self.thread1.start()
        # print self.thread1.join()

        try:
            while self.thread1.is_alive():

                self.win.Show(True)
        finally:
                self.thread1.join()
        print 'hoi'
        if not self.thread1.is_alive():
            print 'hoi'
        # self.win.Destroy()
        # self.panel_one.Show()


    def DestroyandContinue(self):
        # print self.our_thread.__dict__
        # self.our_thread.quit()
        self.win.Destroy()
        self.panel_two.Show()
        self.Layout()

    def DestroyPopupReturn(self,event):
        self.stop = True

        self.win.Destroy()
        self.panel_one.Show()

        # self.thread1 = Worker(self.win,self.panel_one)




#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = TestFrame()
    app.MainLoop()
