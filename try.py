import wx
import os
class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Launch Scripts")
        panel = wx.Panel(self, wx.ID_ANY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        buttonA = wx.Button(panel, id=wx.ID_ANY, label="App A", name="mario")
        buttonB = wx.Button(panel, id=wx.ID_ANY, label="App B", name="gesturecontrol")
        buttonC = wx.Button(panel, id=wx.ID_ANY, label="App C", name="dinosaur")
        buttons = [buttonA, buttonB, buttonC]

        for button in buttons:
            self.buildButtons(button, sizer)

        panel.SetSizer(sizer)

    def buildButtons(self, btn, sizer):
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, wx.ALL, 5)

    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed, taking the script from it's name
        """
        button = event.GetEventObject()

        os.system('python {}.py'.format(button.GetName()))

        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        print( "The button you pressed was labeled: " + button_by_id.GetLabel())
        print("The button's name is " + button_by_id.GetName())


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()