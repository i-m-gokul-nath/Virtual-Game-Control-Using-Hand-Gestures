import wx
import os
import  wx.html
########################################################################
class MainPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
        self.frame = parent
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        gname=['Hill Climb Racing','Mario','Google Dino']
        script=['gesturecontrol','mario','dinosaur']
        for num in range(3):
            label = "Click To Play %s" % gname[num]
            name= "%s" % script[num]
            btn = wx.Button(self, label=label,name=name,size=(180,25))
            sizer.Add(btn, 5, wx.ALL, 5)
            btn.SetBackgroundColour((220, 20, 60, 255))
        self.Bind(wx.EVT_BUTTON, self.onButton)
        
        #buttonhtml = wx.Button(self, label="How To Play",size=(180,25))
        buttonD = wx.Button(self, id=wx.ID_ANY, label="Quit",size=(180,25))
        #buttonhtml.SetBackgroundColour((220, 20, 60, 255))
        buttonD.SetBackgroundColour((220, 20, 60, 255))
        #sizer.Add(buttonhtml,0,wx.ALL,5)
        #self.Bind(wx.EVT_BUTTON,self.onclickHTML,buttonhtml)
        sizer.Add(buttonD,0,wx.ALL,5)
        self.Bind(wx.EVT_BUTTON,self.onclick,buttonD)
        hSizer.Add((1,1), 5, wx.ALL)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1,1), 5, wx.ALL, 75)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
#####################################################################  
    
      
#######################################################################
    def onButton(self, event):
      
        button = event.GetEventObject()

        os.system('python {}.py'.format(button.GetName()))

        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        print("The button you pressed was labeled: " + button_by_id.GetLabel())
        print("The button's name is " + button_by_id.GetName())

#########################################################################
    def onclick(self,e):
        wx.Exit()

    #----------------------------------------------------------------------
    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()
                
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        #bmp=wx.Bitmap('back.jpg')
        #dc.DrawBitmap(bmp,0,0)
        cliWidth, cliHeight = self.GetClientSize()
        bmp=wx.Bitmap('photo.jpg')
        bmpWide = bmp.GetWidth()
        bmpHeight = bmp.GetHeight()
        img = bmp.ConvertToImage()
        scaleFactor = cliWidth/bmpWide
        bmp = wx.Bitmap(img.Scale(int(bmpWide * scaleFactor), int(bmpHeight * scaleFactor)))
        bmpWide = bmp.GetWidth()
        bmpHeight = bmp.GetHeight()
        xPos = (cliWidth - (bmpWide))/2
        yPos = (cliHeight - (bmpHeight))/2
    # altered by me
        dc.DrawBitmap(bmp, xPos, yPos) 


########################################################################
class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None,title="Gaming" ,size=(800,550))
        panel = MainPanel(self)        
        self.Center()
########################################################################
class Main(wx.App):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, redirect=False, filename=None):
        """Constructor"""
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = Main()
    app.MainLoop()