import wx

########################################################################
class TestPopup(wx.PopupWindow):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent, style,patentry):
        """Constructor"""
        wx.PopupWindow.__init__(self, parent, style)

        panel = wx.Panel(self)
        self.panel = panel
        panel.SetBackgroundColour("DARK BLUE")
        self.sttext = wx.StaticText(panel,-1,"You have entered: \n" +patentry +'\n' +"Is this okay?",pos=(100,20))
        self.sttext.SetForegroundColour(wx.Colour(255,255,255))
        self.stbut = wx.Button(panel,-1, "Cancel Measurement",pos=(102,102))
        # st = wx.StaticText(panel, -1,
        #                    "Cancel the measurement?\n",
        #                    pos=(10,10))
        sz = self.sttext.GetBestSize()
        self.SetSize( (sz.width+200, sz.height+200) )
        panel.SetSize( (sz.width+200, sz.height+200) )

        panel.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        panel.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        panel.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        # panel.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        # st.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        # st.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        # st.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        # st.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        wx.CallAfter(self.Refresh)

    def OnMouseLeftDown(self, evt):
        self.Refresh()
        self.ldPos = evt.GetEventObject().ClientToScreen(evt.GetPosition())
        self.wPos = self.ClientToScreen((0,0))
        self.panel.CaptureMouse()

    def OnMouseMotion(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            dPos = evt.GetEventObject().ClientToScreen(evt.GetPosition())
            nPos = (self.wPos.x + (dPos.x - self.ldPos.x),
                    self.wPos.y + (dPos.y - self.ldPos.y))
            self.Move(nPos)

    def OnMouseLeftUp(self, evt):
        if self.panel.HasCapture():
            self.panel.ReleaseMouse()

    # def OnRightUp(self, evt):
    #     self.Show(False)
    #     self.Destroy()


#########################################################
class PlaceholderTextCtrl(wx.TextCtrl):
    def __init__(self, *args, **kwargs):
        self.default_text = kwargs.pop("placeholder", "")
        wx.TextCtrl.__init__(self, *args, **kwargs)
        self.OnKillFocus(None)
        self.Bind(wx.EVT_SET_FOCUS, self.OnFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnFocus(self, evt):
        self.SetForegroundColour(wx.BLACK)
        if self.GetValue() == self.default_text:
            self.SetValue("")
        evt.Skip()

    def OnKillFocus(self, evt):
        if self.GetValue().strip() == "":
            self.SetValue(self.default_text)
            self.SetForegroundColour(wx.LIGHT_GREY)
        if evt:
            evt.Skip()

########################################################################
class NicePanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.initialize()

    def initialize(self):

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(4, 2, 9, 25)

        title = wx.StaticText(self, label="Title")
        author = wx.StaticText(self, label="Author")
        # review = wx.StaticText(self, label="Review")
        buttonname = wx.StaticText(self, label="Start")

        tc1 = wx.TextCtrl(self)
        tc2 = wx.TextCtrl(self)
        # tc3 = wx.TextCtrl(self)
        but = wx.Button(self)

        fgs.AddMany([(title), (tc1, 1, wx.EXPAND), (author),
            (tc2, 1, wx.EXPAND),(buttonname),(but,1)])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        self.SetSizer(hbox)

class ShowyPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.initialize()

    def initialize(self):


        sizer = wx.GridBagSizer(10,10)

        self.btn = wx.Button(self, label="Open Popup",size=(150,30))
        sizer.Add(self.btn,(6,1),(2,20),wx.ALIGN_CENTER)
        # btn.Bind(wx.EVT_BUTTON, self.onShowPopup)


        self.txtentry = PlaceholderTextCtrl(self,-1,style = wx.TE_PROCESS_ENTER, placeholder = "Patientnumber:",size =(150,50))
        sizer.Add(self.txtentry,(6,0),(2,0),wx.ALIGN_LEFT,wx.EXPAND)
        # self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.txtentry)

        self.label = wx.StaticText(self,-1,label=u'Dry-Eye')
        sizer.Add( self.label, (2,0),(0,21), wx.ALIGN_CENTER,wx.EXPAND )


        sizer.AddGrowableCol(0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer)

##########################################################################
class TestPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.initialize()

    def initialize(self):

        # initialize a grid with 5 rows and 5 columns
        sizer = wx.GridBagSizer(5,5)

        self.label = wx.StaticText(self, label=u"Dry-Eye")
        sizer.Add(self.label, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)

        # position = row,col and span = row,col
        line = wx.StaticLine(self)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        # wx.LEFT|Bottom does something I don't yet understand
        self.patlabel = wx.StaticText(self,-1,label=u'PatientNumber')
        sizer.Add( self.patlabel, pos=(2, 0), flag=wx.LEFT|wx.BOTTOM, border=10)
        self.patentry = PlaceholderTextCtrl(self,-1,style = wx.TE_PROCESS_ENTER, placeholder = "Patientnumber:",size =(150,50))
        sizer.Add(self.patentry,pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)

        self.proclabel = wx.StaticText(self,-1,label=u'Procedure')
        sizer.Add( self.proclabel,  pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)
        self.procentry = PlaceholderTextCtrl(self,-1,style = wx.TE_PROCESS_ENTER, placeholder = "Procedure:",size =(150,50))
        sizer.Add(self.procentry,pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND,
            border=5)


        self.btn = wx.Button(self, label="Open Popup",size=(150,30))
        sizer.Add(self.btn,pos=(7, 3))



        # self.label = wx.StaticText(self,-1,label=u'Dry-Eye')
        # sizer.Add(self.label,pos=(1,10),span = (1,2), flag= wx.CENTER|wx.TOP, border = 20)


        sizer.AddGrowableCol(2)
        self.SetAutoLayout(1)
        self.Layout()
        self.SetSizerAndFit(sizer)
        # self.SetSizer(sizer)

    #----------------------------------------------------------------------



"""popup call"""
    # def onShowPopup(self, event):
    #     """"""
    #     win = TestPopup(self.GetTopLevelParent(), wx.SIMPLE_BORDER)
    #
    #     btn = event.GetEventObject()
    #     pos = btn.ClientToScreen( (0,0) )
    #     sz =  btn.GetSize()
    #     win.Position(pos, (0, sz[1]))
    #
    #
    #     win.Show(True)
