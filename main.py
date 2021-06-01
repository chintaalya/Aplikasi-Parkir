import wx
import controller as cn

app = wx.App()
frame = cn.Login(parent=None)
frame.Show()
app.MainLoop()