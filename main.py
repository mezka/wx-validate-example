import wx
import re

class InputValidator(wx.Validator):
    def __init__(self, rexp):
        super(InputValidator, self).__init__()
        self._rexp = rexp
        self._crexp = re.compile(rexp)

    def Validate(self, win):

        txt = self.GetWindow()

        if self._crexp.search(txt.GetValue()):
            txt.BackgroundColour = wx.NullColour
            txt.ForegroundColour = wx.NullColour
            return True
        else:
            txt.BackgroundColour = wx.RED
            txt.ForegroundColour = wx.WHITE

        txt.Refresh()
        return False
    
    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True
        
    def Clone(self):
        return InputValidator(self._rexp)



class Frame(wx.Frame):

    def __init__(self, *args, **kw):

        super(Frame, self).__init__(*args, **kw)
        self.CreateStatusBar()

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        verticalSizer = wx.BoxSizer(wx.VERTICAL)

        nameTextCtrl = wx.TextCtrl(self, validator=InputValidator(r"[a-zA-Z]{6,}"))
        passwdTextCtrl = wx.TextCtrl(self, validator=InputValidator(r"^[0-9]{5,}"))

        postButton = wx.Button(self, label="Post")
        postButton.Bind(event=wx.EVT_BUTTON, handler=self.post)

        verticalSizer.Add(wx.StaticText(self, label="Name: "))
        verticalSizer.Add(nameTextCtrl)
        verticalSizer.Add(wx.StaticText(self, label="Password: "))
        verticalSizer.Add(passwdTextCtrl)
        verticalSizer.Add(postButton)

        sizer.Add(verticalSizer)

        self.SetSizerAndFit(sizer)

    
    def post(self, event):
        self.Validate()

if __name__ == '__main__':
    app = wx.App()
    frm = Frame(None, title='wxValidate Example', style=wx.WS_EX_VALIDATE_RECURSIVELY)
    frm.Show()
    app.MainLoop()