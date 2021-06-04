import wx
import interface as ui
import modal as md
from imgGen import ImageGenerator as img

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
        self.editdelbutton()
    
    def getcellpos( self, event ):
        col = event.GetCol()
        row = event.GetRow()
        print(col,row)

    def editdelbutton( self ):
        editimg = wx.Bitmap("pen.jpeg", wx.BITMAP_TYPE_JPEG)
        delimg = wx.Bitmap("trash.jpeg", wx.BITMAP_TYPE_JPEG)
        editcol = 5
        delcol = 6
        self.edit = img(editimg)
        self.delete  = img(delimg)
        for row in range (self.st_data.GetNumberRows()):
            self.st_data.SetCellRenderer(row, editcol, self.edit)
            self.st_data.SetRowSize(row, editimg.GetHeight())
            self.st_data.SetColSize(editcol, editimg.GetWidth())
            self.st_data.SetCellRenderer(row, delcol, self.delete)
            self.st_data.SetRowSize(row, delimg.GetHeight())
            self.st_data.SetColSize(delcol, delimg.GetWidth())
        self.st_data.SetSize(self.stock_panel.GetSize())
    
    def data(self):		
        koloms = ["Kode Produk", "Nama Produk", "Jenis Produk", "Stok", "Terjual", "", ""]
        lstData = [
            ['Budi', 'Jember', 'budi@gmail', '1'],
            ['Asep', 'Bogor', 'asep@gmail', '1'],
            ['Joko', 'Jogja', 'joko@gmail', '1'],	
            ['Wati', 'Banyuwangi', 'wati@gmail', '1']
        ]
        for row in range(len(lstData)):
            for col in range(len(lstData[0])):
                if row == 0:
                    self.st_data.SetColLabelValue(col, koloms[col])
                val = lstData[row][col]
                print('val: ', val)
            self.st_data.SetCellValue(row,col, val )


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
