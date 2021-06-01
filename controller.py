import wx
import interface as ui

class Login(ui.login):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))

    def login( self, event ):
        self.subframe = Dashboard(parent=None)
        self.subframe.Show()
        self.Destroy()

class Dashboard(ui.dashboard):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))

    def dbtofinance( self, event ):
        self.subframe = Finance(parent=None)
        self.subframe.Show()
        self.Destroy()

    def dbtostock( self, event ):
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy()

    def dbtologout( self, event ):
        self.subframe = Login(parent=None)
        self.subframe.Show()
        self.Destroy()

class Finance(ui.finance):
    wx.SB_VERTICAL
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        
    def fintodb( self, event ):
        self.subframe = Dashboard(parent=None)
        self.subframe.Show()
        self.Destroy()

    def fintostock( self, event ):
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy()

    def fintologout( self, event ):
        self.subframe = Login(parent=None)
        self.subframe.Show()
        self.Destroy()
    
    def add_income( self, event ):
        self.subframe = AddIncome(parent=None)
        self.subframe.Show()
        self.Destroy()
    
    def add_outcome( self, event ):
        self.subframe = AddOutcome(parent=None)
        self.subframe.Show()
        self.Destroy()

class Stock(ui.stock):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))

    def stocktodb( self, event ):
        self.subframe = Dashboard(parent=None)
        self.subframe.Show()
        self.Destroy()

    def stocktofin( self, event ):
        self.subframe = Finance(parent=None)
        self.subframe.Show()
        self.Destroy()

    def stocktologout( self, event ):
        self.subframe = Login(parent=None)
        self.subframe.Show()
        self.Destroy()
    
    def addnewstock( self, event ):
        self.subframe = AddStock(parent=None)
        self.subframe.Show()
        self.Destroy()

class AddStock(ui.add_stock):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
    
    def unadd_stock( self, event ):
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy()

    def added_stock( self, event ):
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy()

class AddIncome(ui.add_income):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
    
    def unadd_income( self, event ):
        self.subframe = Finance(parent=None)
        self.subframe.Show()
        self.Destroy()

    def add_income( self, event ):
        self.subframe = Finance(parent=None)
        self.subframe.Show()
        self.Destroy()

class AddOutcome(ui.add_outcome):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
    
    def unadd_outcome( self, event ):
        self.subframe = Finance(parent=None)
        self.subframe.Show()
        self.Destroy()

    def add_outcome( self, event ):
        self.subframe = Finance(parent=None)
        self.subframe.Show()
        self.Destroy()
