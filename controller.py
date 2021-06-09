import wx
import interface as ui
import modal as md
from imgGen import ImageGenerator as img
from datetime import datetime
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.pyplot as plt 
import numpy as np


class Login(ui.login):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))

    def login( self, event ):
        username = self.login_input.GetValue()
        password = self.login_input2.GetValue()
        if username == "" and password == "":
            wx.MessageBox('Harap Mengisi Username dan Password Terlebih Dahulu', 'Peringatan', wx.OK | wx.ICON_WARNING)
        elif username != "admin" and password != "12345":
            wx.MessageBox('Username dan Password Salah', 'Peringatan', wx.OK | wx.ICON_WARNING)
        elif username != "admin":
            wx.MessageBox('Username Salah', 'Peringatan', wx.OK | wx.ICON_WARNING)
        elif password != "12345":
            wx.MessageBox('Password Salah', 'Peringatan', wx.OK | wx.ICON_WARNING)
        else:
            self.subframe = Dashboard(parent=None)
            self.subframe.Show()
            self.Destroy()

class Dashboard(ui.dashboard):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        self.new_obj = md.Connection()
        self.graph_income.figure = plt.figure(figsize=(3,1))
        self.graph_income.axes = self.graph_income.figure.add_subplot(1,1,1)
        self.graph_income.canvas = FigureCanvas(self.graph_income, -1, self.graph_income.figure)
        self.graph_income.sizer = wx.BoxSizer(wx.VERTICAL)
        self.graph_income.sizer.Add(self.graph_income.canvas, 1, wx.CENTER)
        self.graph_income.SetSizer(self.graph_income.sizer)
        self.graph_outcome.figure = plt.figure(figsize=(3,1))
        self.graph_outcome.axes = self.graph_outcome.figure.add_subplot(1,1,1)
        self.graph_outcome.canvas = FigureCanvas(self.graph_outcome, -1, self.graph_outcome.figure)
        self.graph_outcome.sizer = wx.BoxSizer(wx.VERTICAL)
        self.graph_outcome.sizer.Add(self.graph_outcome.canvas, 1, wx.CENTER)
        self.graph_outcome.SetSizer(self.graph_outcome.sizer)
    
    def monthly_report( self, event ):
        self.graph_income.figure.set_canvas(self.graph_income.canvas)
        self.graph_income.axes.clear()
        self.graph_outcome.figure.set_canvas(self.graph_outcome.canvas)
        self.graph_outcome.axes.clear()
        now = datetime.now()
        bulan_now = int(now.strftime("%m"))
        query ="select tanggal, nominal from pemasukan"
        data = self.new_obj.select(query)
        tanggal = []
        nominal = []
        for row in range(len(data)):
            if int(data[row][0][5:7]) == bulan_now:
                hari = int(data[row][0][8:10])
                if len(tanggal) == 0:
                    tanggal.append(hari)
                    total = data[row][1]
                elif hari == tanggal[-1]:
                    total = total + data[row][1]
                else:
                    nominal.append(total)
                    tanggal.append(hari)
                    total = data[row][1]
            if row == len(data)-1:
                nominal.append(total)

        x = tanggal
        y = [int(str(nom)[:-3]) for nom in nominal]
        x.insert(0,0)
        y.insert(0,0)
        self.graph_income.axes.plot(x,y)
        self.graph_income.canvas.draw()
        self.graph_income.axes.set_title('PEMASUKAN')

        query2 ="select tanggal, nominal from pengeluaran"
        data2 = self.new_obj.select(query2)
        tanggal2 = []
        nominal2 = []
        for row in range(len(data2)):
            if int(data2[row][0][5:7]) == bulan_now:
                hari = int(data2[row][0][8:10])
                if len(tanggal2) == 0:
                    tanggal2.append(hari)
                    total = data2[row][1]
                elif hari == tanggal2[-1]:
                    total = total + data2[row][1]
                else:
                    nominal2.append(total)
                    tanggal2.append(hari)
                    total = data2[row][1]
            if row == len(data2)-1:
                nominal2.append(total)

        x2 = tanggal2
        y2 = [int(str(nom)[:-3]) for nom in nominal2]
        x2.insert(0,0)
        y2.insert(0,0)
        self.graph_outcome.axes.plot(x2,y2)
        self.graph_outcome.canvas.draw()
        self.graph_outcome.axes.set_title('PENGELUARAN')

    def annual_report( self, event ):
        self.graph_income.figure.set_canvas(self.graph_income.canvas)
        self.graph_income.axes.clear()
        self.graph_outcome.figure.set_canvas(self.graph_outcome.canvas)
        self.graph_outcome.axes.clear()
        now = datetime.now()
        tahun_now = int(now.strftime("%Y"))
        query ="select tanggal, nominal from pemasukan"
        data = self.new_obj.select(query)
        bulan = []
        nominal = []
        for row in range(len(data)):
            if int(data[row][0][0:4]) == tahun_now:
                nama_bulan = int(data[row][0][5:7])
                if len(bulan) == 0:
                    bulan.append(nama_bulan)
                    total = data[row][1]
                elif nama_bulan == bulan[-1]:
                    total = total + data[row][1]
                else:
                    nominal.append(total)
                    bulan.append(nama_bulan)
                    total = data[row][1]
            if row == len(data)-1:
                nominal.append(total)
        x = bulan
        y = [int(str(nom)[:-3]) for nom in nominal]
        x.insert(0,0)
        y.insert(0,0)
        self.graph_income.axes.plot(x,y)
        self.graph_income.canvas.draw()
        self.graph_income.axes.set_title('PEMASUKAN')

        query2 ="select tanggal, nominal from pengeluaran"
        data2 = self.new_obj.select(query2)
        bulan2 = []
        nominal2 = []
        for row in range(len(data2)):
            if int(data2[row][0][0:4]) == tahun_now:
                nama_bulan = int(data2[row][0][5:7])
                if len(bulan2) == 0:
                    bulan2.append(nama_bulan)
                    total = data2[row][1]
                elif nama_bulan == bulan2[-1]:
                    total = total + data2[row][1]
                else:
                    nominal2.append(total)
                    bulan2.append(nama_bulan)
                    total = data2[row][1]
            if row == len(data2)-1:
                nominal2.append(total)
        x2 = bulan2
        y2 = [int(str(nom)[:-3]) for nom in nominal2]
        x2.insert(0,0)
        y2.insert(0,0)
        
        self.graph_outcome.axes.plot(x2,y2)
        self.graph_outcome.canvas.draw()
        self.graph_outcome.axes.set_title('PENGELUARAN')

    def dbtoincome( self, event ):
        self.subframe = Income(parent=None)
        self.subframe.Show()
        self.Destroy()
    
    def dbtooutcome( self, event ):
        self.subframe = Outcome(parent=None)
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

class Income(ui.income):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        self.obj = md.Connection()
        self.datatable()
    
    def datatable(self):
        total = 0
        col_label = ["ID", "Tanggal", "Keterangan", "Nominal", " ", " "]
        self.income_data.AppendCols(len(col_label))
        self.income_data.SetColSize( 0, 30 )
        self.income_data.SetColSize( 1, 100 )
        self.income_data.SetColSize( 2, 240 )
        self.income_data.SetColSize( 3, 140 )
        self.income_data.SetColSize( 4, 30 )
        self.income_data.SetColSize( 5, 30 )
        query = """select * from pemasukan"""
        data = self.obj.select(query)

        for row in range(len(data)):
            self.income_data.AppendRows(1)
            for col in range(len(data[0])):
                if row == 0:
                    self.income_data.SetColLabelValue(col, col_label[col])
                if col == 3:
                    nom = int(data[row][col])
                    total = total + nom
                val = str(data[row][col])
                self.income_data.SetCellValue(row,col,val)
        self.income_data.SetColLabelValue(4, col_label[4])
        self.income_data.SetColLabelValue(5, col_label[5])
        self.editdelbutton()
        self.income_display.SetLabelText(f"{total}")
    
    def getcellpos( self, event ):
        col = event.GetCol()
        row = event.GetRow()
        if col == 4:
            self.new_obj = EditIncome(None, row, col, self.income_data.GetCellValue(row,0), self.income_data.GetCellValue(row,2), self.income_data.GetCellValue(row,3))
            self.new_obj.Show()
            self.Destroy()  
        elif col == 5:
            button = wx.MessageBox('Hapus Data?', 'Konfirmasi', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_WARNING)
            if button == wx.YES:
                query = f"delete from pemasukan where id = {self.income_data.GetCellValue(row,0)}"
                self.obj.exec(query)
                self.subframe = Income(parent=None)
                self.subframe.Show()
                self.Destroy() 
            elif button == wx.NO:
                self.subframe = Income(parent=None)
                self.subframe.Show()
                self.Destroy()

    def editdelbutton( self ):
        editimg = wx.Bitmap("pen.jpeg", wx.BITMAP_TYPE_JPEG)
        delimg = wx.Bitmap("trash.jpeg", wx.BITMAP_TYPE_JPEG)
        editcol = 4
        delcol = 5
        self.edit = img(editimg)
        self.delete  = img(delimg)
        for row in range (self.income_data.GetNumberRows()):
            self.income_data.SetCellRenderer(row, editcol, self.edit)
            self.income_data.SetRowSize(row, editimg.GetHeight())
            self.income_data.SetColSize(editcol, editimg.GetWidth())
            self.income_data.SetCellRenderer(row, delcol, self.delete)
            self.income_data.SetRowSize(row, delimg.GetHeight())
            self.income_data.SetColSize(delcol, delimg.GetWidth())
        self.income_data.SetSize(self.income.GetSize())
        

    def intodb( self, event ):
        self.subframe = Dashboard(parent=None)
        self.subframe.Show()
        self.Destroy()
    
    def intoout( self, event ):
        self.subframe = Outcome(parent=None)
        self.subframe.Show()
        self.Destroy()

    def intostock( self, event ):
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy()

    def intologout( self, event ):
        self.subframe = Login(parent=None)
        self.subframe.Show()
        self.Destroy()
    
    def add_income( self, event ):
        self.subframe = AddIncome(parent=None)
        self.subframe.Show()
        self.Destroy()

class Outcome(ui.outcome):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        self.obj = md.Connection()
        self.obj = md.Connection()
        self.datatable()
    
    def datatable(self):
        total = 0
        col_label = ["ID", "Tanggal", "Keterangan", "Nominal", " ", " "]
        self.outcome_data.AppendCols(len(col_label))
        self.outcome_data.SetColSize( 0, 30 )
        self.outcome_data.SetColSize( 1, 100 )
        self.outcome_data.SetColSize( 2, 240 )
        self.outcome_data.SetColSize( 3, 140 )
        self.outcome_data.SetColSize( 4, 30 )
        self.outcome_data.SetColSize( 5, 30 )
        query = """select * from pengeluaran"""
        data = self.obj.select(query)

        for row in range(len(data)):
            self.outcome_data.AppendRows(1)
            for col in range(len(data[0])):
                if row == 0:
                    self.outcome_data.SetColLabelValue(col, col_label[col])
                if col == 3:
                    nom = int(data[row][col])
                    total = total + nom
                val = str(data[row][col])
                self.outcome_data.SetCellValue(row,col,val)
        self.outcome_data.SetColLabelValue(4, col_label[4])
        self.outcome_data.SetColLabelValue(5, col_label[5])
        self.editdelbutton()
        self.outcome_display.SetLabelText(f"{total}")
    
    def getcellpos( self, event ):
        col = event.GetCol()
        row = event.GetRow()
        if col == 4:
            self.new_obj = EditOutcome(None, row, col, self.outcome_data.GetCellValue(row,0), self.outcome_data.GetCellValue(row,2), self.outcome_data.GetCellValue(row,3))
            self.new_obj.Show()
            self.Destroy()  
        elif col == 5:
            button = wx.MessageBox('Hapus Data?', 'Konfirmasi', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_WARNING)
            if button == wx.YES:
                query = f"delete from pengeluaran where id = {self.outcome_data.GetCellValue(row,0)}"
                self.obj.exec(query)
                self.subframe = Outcome(parent=None)
                self.subframe.Show()
                self.Destroy() 
            elif button == wx.NO:
                self.subframe = Outcome(parent=None)
                self.subframe.Show()
                self.Destroy()

    def editdelbutton( self ):
        editimg = wx.Bitmap("pen.jpeg", wx.BITMAP_TYPE_JPEG)
        delimg = wx.Bitmap("trash.jpeg", wx.BITMAP_TYPE_JPEG)
        editcol = 4
        delcol = 5
        self.edit = img(editimg)
        self.delete  = img(delimg)
        for row in range (self.outcome_data.GetNumberRows()):
            self.outcome_data.SetCellRenderer(row, editcol, self.edit)
            self.outcome_data.SetRowSize(row, editimg.GetHeight())
            self.outcome_data.SetColSize(editcol, editimg.GetWidth())
            self.outcome_data.SetCellRenderer(row, delcol, self.delete)
            self.outcome_data.SetRowSize(row, delimg.GetHeight())
            self.outcome_data.SetColSize(delcol, delimg.GetWidth())
        self.outcome_data.SetSize(self.outcome.GetSize())
        
    def outtodb( self, event ):
        self.subframe = Dashboard(parent=None)
        self.subframe.Show()
        self.Destroy()

    def outtoin( self, event ):
        self.subframe = Income(parent=None)
        self.subframe.Show()
        self.Destroy()

    def outtostock( self, event ):
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy()

    def outtologout( self, event ):
        self.subframe = Login(parent=None)
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
        self.obj = md.Connection()
        self.datatable()
        self.editdelbutton()
    
    def getcellpos( self, event ):
        col = event.GetCol()
        row = event.GetRow()
        if col == 5:
            self.new_obj = EditStock(None, row, col, self.st_data.GetCellValue(row,0), self.st_data.GetCellValue(row,1), self.st_data.GetCellValue(row,2), self.st_data.GetCellValue(row,3), self.st_data.GetCellValue(row,4))            
            self.new_obj.Show()
            self.Destroy() 
        elif col == 6:
            button = wx.MessageBox('Hapus Data?', 'Konfirmasi', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_WARNING)
            if button == wx.YES:
                query = f"delete from produk where id_produk = {self.st_data.GetCellValue(row,0)}"
                self.obj.exec(query)
                self.subframe = Stock(parent=None)
                self.subframe.Show()
                self.Destroy() 
            elif button == wx.NO:
                self.subframe = Stock(parent=None)
                self.subframe.Show()
                self.Destroy()

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
    
    def datatable(self):
        col_label = ["Kode Produk", "Nama Produk", "Jenis Produk", "Stok", "Terjual", " ", " "]
        self.st_data.AppendCols(len(col_label))
        self.st_data.SetColSize( 0, 90 )
        self.st_data.SetColSize( 1, 160 )
        self.st_data.SetColSize( 2, 160 )
        self.st_data.SetColSize( 3, 50 )
        self.st_data.SetColSize( 4, 50 )
        self.st_data.SetColSize( 5, 30 )
        self.st_data.SetColSize( 6, 30 )
        query = "select * from produk"
        data = self.obj.select(query)

        for row in range(len(data)):
            self.st_data.AppendRows(1)
            for col in range(len(data[0])):
                if row == 0:
                    self.st_data.SetColLabelValue(col, col_label[col])
                val = str(data[row][col])
                self.st_data.SetCellValue(row,col,val)
        self.st_data.SetColLabelValue(5, col_label[5])
        self.st_data.SetColLabelValue(6, col_label[6])


    def stocktodb( self, event ):
        self.subframe = Dashboard(parent=None)
        self.subframe.Show()
        self.Destroy()

    def stocktoin( self, event ):
        self.subframe = Income(parent=None)
        self.subframe.Show()
        self.Destroy()

    def stocktoout( self, event ):
        self.subframe = Outcome(parent=None)
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
        self.obj = md.Connection()
    
    def unadd_stock( self, event ):
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy()

    def added_stock( self, event ):
        nama = self.stock_input.GetValue()
        jenis = self.stock_input2.GetValue()
        new_obj = md.Produk(nama,jenis,'0','0')
        query = """insert into produk (nama_produk, jenis_produk, stok, terjual) values (?,?,?,?)"""
        param = (new_obj.getNama(), new_obj.getJenis(), int(new_obj.getStok()), int(new_obj.getTerjual()))
        self.obj.update_insert(query,param)
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy()

class AddIncome(ui.add_income):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        self.obj = md.Connection()
    
    def unadd_income( self, event ):
        self.subframe = Income(parent=None)
        self.subframe.Show()
        self.Destroy()

    def add_income( self, event ):
        now = datetime.now()
        tanggal = now.strftime("%Y-%m-%d")
        ket = self.income_input.GetValue()
        nom = self.income_input2.GetValue()
        new_obj = md.Moneyin(tanggal,ket,nom)
        query = """insert into pemasukan (tanggal, keterangan, nominal) values (?,?,?)"""
        param = (new_obj.getTanggal(), new_obj.getKeterangan(), int(new_obj.getNominal()))
        self.obj.update_insert(query,param)
        self.subframe = Income(parent=None)
        self.subframe.Show()
        self.Destroy()

class AddOutcome(ui.add_outcome):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        self.obj = md.Connection()
    
    def unadd_outcome( self, event ):
        self.subframe = Outcome(parent=None)
        self.subframe.Show()
        self.Destroy()

    def add_outcome( self, event ):
        now = datetime.now()
        tanggal = now.strftime("%Y-%m-%d")
        ket = self.outcome_input.GetValue()
        nom = self.outcome_input2.GetValue()
        new_obj = md.Moneyout(tanggal,ket,nom)
        query = """insert into pengeluaran (tanggal, keterangan, nominal) values (?,?,?)"""
        param = (new_obj.getTanggal(), new_obj.getKeterangan(), int(new_obj.getNominal()))
        self.obj.update_insert(query,param)
        self.subframe = Outcome(parent=None)
        self.subframe.Show()
        self.Destroy()

class EditStock(ui.edit_stock):
    def __init__(self, parent, row, col, id, nama, jenis, stok, terjual):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        self.row = row
        self.col = col
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.stock = stok
        self.terjual = terjual
        self.obj = md.Connection()
        self.stock_input.SetLabelText(f"{self.nama}")
        self.stock_input2.SetLabelText(f"{self.jenis}")
        self.stock_input31.SetLabelText(f"{self.stock}")
        self.stock_input32.SetLabelText(f"{self.terjual}")
        
    def edited_stock( self, event ):
        query = """update produk set nama_produk = ?, jenis_produk = ?, stok = ?, terjual = ? where id_produk = ?"""
        param = (self.stock_input.GetValue(), self.stock_input2.GetValue(), int(self.stock_input31.GetValue()), int(self.stock_input32.GetValue()), int(self.id))
        self.obj.update_insert(query,param)
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy() 

    def unedit_stock( self, event ):
        self.subframe = Stock(parent=None)
        self.subframe.Show()
        self.Destroy() 

class EditIncome(ui.edit_income):
    def __init__(self, parent, row, col, id, keterangan, nominal):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        self.row = row
        self.col = col
        self.id = id
        self.ket = keterangan
        self.nominal = nominal
        self.obj = md.Connection()
        self.income_input.SetLabelText(f"{self.ket}")
        self.income_input2.SetLabelText(f"{self.nominal}")
        
    def add_income( self, event ):
        query = """update pemasukan set keterangan = ?, nominal = ? where id = ?"""
        param = (self.income_input.GetValue(), int(self.income_input2.GetValue()), int(self.id))
        self.obj.update_insert(query,param)
        self.subframe = Income(parent=None)
        self.subframe.Show()
        self.Destroy() 

    def unadd_income( self, event ):
        self.subframe = Income(parent=None)
        self.subframe.Show()
        self.Destroy() 

class EditOutcome(ui.edit_outcome):
    def __init__(self, parent, row, col, id, keterangan, nominal):
        super().__init__(parent)
        self.SetIcon(wx.Icon("logo.ico"))
        self.row = row
        self.col = col
        self.id = id
        self.ket = keterangan
        self.nominal = nominal
        self.obj = md.Connection()
        self.outcome_input.SetLabelText(f"{self.ket}")
        self.outcome_input2.SetLabelText(f"{self.nominal}")
    
    def add_outcome( self, event ):
        query = """update pengeluaran set keterangan = ?, nominal = ? where id = ?"""
        param = (self.outcome_input.GetValue(), int(self.outcome_input2.GetValue()), int(self.id))
        self.obj.update_insert(query,param)
        self.subframe = Outcome(parent=None)
        self.subframe.Show()
        self.Destroy() 

    def unadd_outcome( self, event ):
        self.subframe = Outcome(parent=None)
        self.subframe.Show()
        self.Destroy() 