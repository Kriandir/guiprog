import wx

class confirmapp_wx(wx.Frame)
class simpleapp_wx(wx.Frame):
    #initializing phase
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size=(500,500))
        self.parent = parent
        self.Center()
        self.initialize()

    # needed to show the application"
    def initialize(self):
        # initialize grid
        sizer = wx.GridBagSizer()

        #initialize text entry with enter confirmation
        self.entry = wx.TextCtrl(self,-1,style = wx.TE_PROCESS_ENTER,value=u"Patient number:")
        sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)

        #initialize button with click listhener
        button = wx.Button(self,-1,label="Confirm!")
        sizer.Add(button,(0,1))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick,button)

        #add label
        self.label = wx.StaticText(self,-1,label=u'Dry-Eye')
        self.label.SetBackgroundColour(wx.BLACK)
        self.label.SetForegroundColour(wx.YELLOW)
        sizer.Add( self.label, (1,0),(1,2), wx.EXPAND )

        #perform grid
        sizer.AddGrowableCol(0)
        # self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y);
        # self.SetSizeHints(-1,self.GetSize().x,-1,self.GetSize().x);
        # self.SetSizerAndFit(sizer)
        self.SetAutoLayout(1)
        self.SetSizer(sizer)
        self.Show(True)

# when button is clicked execute:
    def OnButtonClick(self,event):
        self.label.SetLabel(self.entry.GetValue() + 'clicked le button')
        # self.label.SetLabel("you clicked?")
        # print "woop woop le click da button"

#when enter is pressed execute:
    def OnPressEnter(self,event):
        self.label.SetLabel(self.entry.GetValue() + "entered")
        # print "You pressed enter !"

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'my application')
    app.MainLoop()
