# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class login
###########################################################################

class login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Diyme's Manager", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		login_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,60 ) )

		login_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		sublogin_sizer = wx.BoxSizer( wx.VERTICAL )

		self.login_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.login_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.login_panel.SetMinSize( wx.Size( 360,-1 ) )
		self.login_panel.SetMaxSize( wx.Size( 360,-1 ) )

		loginpanel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self.login_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.dummy.Wrap( -1 )

		loginpanel_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.login_text = wx.StaticText( self.login_panel, wx.ID_ANY, u"Selamat Datang", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.login_text.Wrap( 100 )

		self.login_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.login_text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.login_text.SetMinSize( wx.Size( -1,35 ) )

		loginpanel_sizer.Add( self.login_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		subloginapnel_sizer = wx.FlexGridSizer( 0, 1, 10, 0 )
		subloginapnel_sizer.SetFlexibleDirection( wx.BOTH )
		subloginapnel_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		subloginapnel_sizer.SetMinSize( wx.Size( -1,40 ) )
		login_label = wx.StaticBoxSizer( wx.StaticBox( self.login_panel, wx.ID_ANY, u"username" ), wx.VERTICAL )

		login_label.SetMinSize( wx.Size( 240,-1 ) )
		self.login_input = wx.TextCtrl( login_label.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login_input.SetMinSize( wx.Size( 220,-1 ) )

		login_label.Add( self.login_input, 0, wx.ALL, 5 )


		subloginapnel_sizer.Add( login_label, 1, wx.EXPAND, 5 )

		login_label2 = wx.StaticBoxSizer( wx.StaticBox( self.login_panel, wx.ID_ANY, u"password" ), wx.VERTICAL )

		self.login_input2 = wx.TextCtrl( login_label2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.login_input2.SetMinSize( wx.Size( 220,-1 ) )

		login_label2.Add( self.login_input2, 0, wx.ALL, 5 )


		subloginapnel_sizer.Add( login_label2, 1, wx.EXPAND, 5 )

		self.dummy = wx.StaticText( self.login_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,5 ), 0 )
		self.dummy.Wrap( -1 )

		subloginapnel_sizer.Add( self.dummy, 0, wx.ALL, 5 )


		loginpanel_sizer.Add( subloginapnel_sizer, 0, wx.ALIGN_CENTER, 5 )

		self.login_button = wx.Button( self.login_panel, wx.ID_ANY, u"Masuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.login_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.login_button.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )
		self.login_button.SetMinSize( wx.Size( 120,-1 ) )

		loginpanel_sizer.Add( self.login_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.login_panel.SetSizer( loginpanel_sizer )
		self.login_panel.Layout()
		loginpanel_sizer.Fit( self.login_panel )
		sublogin_sizer.Add( self.login_panel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		login_sizer.Add( sublogin_sizer, 1, wx.EXPAND, 5 )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,60 ) )

		login_sizer.Add( self.dummy, 0, wx.ALL, 5 )


		self.SetSizer( login_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.login_button.Bind( wx.EVT_BUTTON, self.login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login( self, event ):
		event.Skip()


###########################################################################
## Class dashboard
###########################################################################

class dashboard ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Dashboard", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		self.dashboard_menubar = wx.MenuBar( 0 )
		self.dashboard_menubar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		self.dashboard_menu = wx.Menu()
		self.db_menu = wx.MenuItem( self.dashboard_menu, wx.ID_ANY, u"Pemasukan", wx.EmptyString, wx.ITEM_NORMAL )
		self.dashboard_menu.Append( self.db_menu )

		self.db_menu2 = wx.MenuItem( self.dashboard_menu, wx.ID_ANY, u"Pengeluaran", wx.EmptyString, wx.ITEM_NORMAL )
		self.dashboard_menu.Append( self.db_menu2 )

		self.db_menu3 = wx.MenuItem( self.dashboard_menu, wx.ID_ANY, u"Stok Produk", wx.EmptyString, wx.ITEM_NORMAL )
		self.dashboard_menu.Append( self.db_menu3 )

		self.db_menu4 = wx.MenuItem( self.dashboard_menu, wx.ID_ANY, u"Keluar", wx.EmptyString, wx.ITEM_NORMAL )
		self.dashboard_menu.Append( self.db_menu4 )

		self.dashboard_menubar.Append( self.dashboard_menu, u"Menu" )

		self.SetMenuBar( self.dashboard_menubar )

		dashboard_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dashboard_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.dashboard_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		dbpanel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self.dashboard_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		dbpanel_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.db_text = wx.StaticText( self.dashboard_panel, wx.ID_ANY, u"GRAFIK PEMASUKAN DAN PENGELUARAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.db_text.Wrap( -1 )

		self.db_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.db_text.SetMinSize( wx.Size( -1,35 ) )

		dbpanel_sizer.Add( self.db_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		subdbpanel_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.monthly_radio = wx.RadioButton( self.dashboard_panel, wx.ID_ANY, u"Bulanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		subdbpanel_sizer.Add( self.monthly_radio, 0, wx.ALL, 5 )

		self.dummy = wx.StaticText( self.dashboard_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		subdbpanel_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.annual_radio = wx.RadioButton( self.dashboard_panel, wx.ID_ANY, u"Tahunan", wx.DefaultPosition, wx.DefaultSize, 0 )
		subdbpanel_sizer.Add( self.annual_radio, 0, wx.ALL, 5 )


		dbpanel_sizer.Add( subdbpanel_sizer, 0, wx.ALIGN_CENTER, 5 )

		subdbpanel_sizer2 = wx.FlexGridSizer( 5, 2, 0, 10 )
		subdbpanel_sizer2.SetFlexibleDirection( wx.BOTH )
		subdbpanel_sizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.graph_income = wx.Panel( self.dashboard_panel, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 300,250 ), wx.TAB_TRAVERSAL )
		self.graph_income.SetMinSize( wx.Size( 300,250 ) )
		self.graph_income.SetMaxSize( wx.Size( 300,250 ) )

		subdbpanel_sizer2.Add( self.graph_income, 1, wx.EXPAND |wx.ALL, 5 )

		self.graph_outcome = wx.Panel( self.dashboard_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,250 ), wx.TAB_TRAVERSAL )
		self.graph_outcome.SetMinSize( wx.Size( 300,250 ) )
		self.graph_outcome.SetMaxSize( wx.Size( 300,250 ) )

		subdbpanel_sizer2.Add( self.graph_outcome, 1, wx.EXPAND |wx.ALL, 5 )


		dbpanel_sizer.Add( subdbpanel_sizer2, 1, wx.ALIGN_CENTER, 5 )


		self.dashboard_panel.SetSizer( dbpanel_sizer )
		self.dashboard_panel.Layout()
		dbpanel_sizer.Fit( self.dashboard_panel )
		dashboard_sizer.Add( self.dashboard_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( dashboard_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.dbtoincome, id = self.db_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.dbtooutcome, id = self.db_menu2.GetId() )
		self.Bind( wx.EVT_MENU, self.dbtostock, id = self.db_menu3.GetId() )
		self.Bind( wx.EVT_MENU, self.dbtologout, id = self.db_menu4.GetId() )
		self.monthly_radio.Bind( wx.EVT_RADIOBUTTON, self.monthly_report )
		self.annual_radio.Bind( wx.EVT_RADIOBUTTON, self.annual_report )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dbtoincome( self, event ):
		event.Skip()

	def dbtooutcome( self, event ):
		event.Skip()

	def dbtostock( self, event ):
		event.Skip()

	def dbtologout( self, event ):
		event.Skip()

	def monthly_report( self, event ):
		event.Skip()

	def annual_report( self, event ):
		event.Skip()


###########################################################################
## Class income
###########################################################################

class income ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pemasukan", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		self.income_menubar = wx.MenuBar( 0 )
		self.income_menu = wx.Menu()
		self.in_menu = wx.MenuItem( self.income_menu, wx.ID_ANY, u"Dashboard", wx.EmptyString, wx.ITEM_NORMAL )
		self.income_menu.Append( self.in_menu )

		self.in_menu2 = wx.MenuItem( self.income_menu, wx.ID_ANY, u"Pengeluaran", wx.EmptyString, wx.ITEM_NORMAL )
		self.income_menu.Append( self.in_menu2 )

		self.in_menu3 = wx.MenuItem( self.income_menu, wx.ID_ANY, u"Stok Produk", wx.EmptyString, wx.ITEM_NORMAL )
		self.income_menu.Append( self.in_menu3 )

		self.in_menu4 = wx.MenuItem( self.income_menu, wx.ID_ANY, u"Keluar", wx.EmptyString, wx.ITEM_NORMAL )
		self.income_menu.Append( self.in_menu4 )

		self.income_menubar.Append( self.income_menu, u"Menu" )

		self.SetMenuBar( self.income_menubar )

		income_sizer = wx.BoxSizer( wx.VERTICAL )

		self.income = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 720,480 ), wx.TAB_TRAVERSAL )
		self.income.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.income.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.income.SetMinSize( wx.Size( 720,480 ) )
		self.income.SetMaxSize( wx.Size( 720,480 ) )

		subincome_sizer = wx.FlexGridSizer( 6, 1, 0, 0 )
		subincome_sizer.SetFlexibleDirection( wx.BOTH )
		subincome_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dummy1 = wx.StaticText( self.income, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy1.Wrap( -1 )

		self.dummy1.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		subincome_sizer.Add( self.dummy1, 0, wx.ALL, 5 )

		income_sizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.in_text = wx.StaticText( self.income, wx.ID_ANY, u"Total Pemasukan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.in_text.Wrap( -1 )

		self.in_text.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		income_sizer1.Add( self.in_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.income_display = wx.TextCtrl( self.income, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		income_sizer1.Add( self.income_display, 0, wx.ALL, 5 )


		subincome_sizer.Add( income_sizer1, 1, wx.EXPAND, 5 )

		self.dummy2 = wx.StaticText( self.income, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy2.Wrap( -1 )

		self.dummy2.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		subincome_sizer.Add( self.dummy2, 0, wx.ALL, 5 )

		self.in_button = wx.Button( self.income, wx.ID_ANY, u"Tambahkan Data ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.in_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.in_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.in_button.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		subincome_sizer.Add( self.in_button, 0, wx.ALL, 5 )

		self.dummy3 = wx.StaticText( self.income, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy3.Wrap( -1 )

		self.dummy3.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		subincome_sizer.Add( self.dummy3, 0, wx.ALL, 5 )

		self.income_data = wx.grid.Grid( self.income, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.income_data.CreateGrid( 0, 0 )
		self.income_data.EnableEditing( False )
		self.income_data.EnableGridLines( True )
		self.income_data.EnableDragGridSize( False )
		self.income_data.SetMargins( 0, 0 )

		# Columns
		self.income_data.EnableDragColMove( False )
		self.income_data.EnableDragColSize( True )
		self.income_data.SetColLabelSize( 30 )
		self.income_data.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.income_data.EnableDragRowSize( True )
		self.income_data.SetRowLabelSize( 80 )
		self.income_data.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.income_data.SetLabelBackgroundColour( wx.Colour( 198, 182, 228 ) )
		self.income_data.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		# Cell Defaults
		self.income_data.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.income_data.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.income_data.SetMinSize( wx.Size( 670,-1 ) )
		self.income_data.SetMaxSize( wx.Size( -1,260 ) )

		subincome_sizer.Add( self.income_data, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.income.SetSizer( subincome_sizer )
		self.income.Layout()
		income_sizer.Add( self.income, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( income_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.intodb, id = self.in_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.intoout, id = self.in_menu2.GetId() )
		self.Bind( wx.EVT_MENU, self.intostock, id = self.in_menu3.GetId() )
		self.Bind( wx.EVT_MENU, self.intologout, id = self.in_menu4.GetId() )
		self.in_button.Bind( wx.EVT_BUTTON, self.add_income )
		self.income_data.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.getcellpos )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def intodb( self, event ):
		event.Skip()

	def intoout( self, event ):
		event.Skip()

	def intostock( self, event ):
		event.Skip()

	def intologout( self, event ):
		event.Skip()

	def add_income( self, event ):
		event.Skip()

	def getcellpos( self, event ):
		event.Skip()


###########################################################################
## Class add_income
###########################################################################

class add_income ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pemasukan", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		addincome_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,50 ) )

		addincome_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.addincome_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.addincome_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.addincome_panel.SetMinSize( wx.Size( 360,-1 ) )

		addinpanel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self.addincome_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.dummy.SetMinSize( wx.Size( -1,20 ) )

		addinpanel_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.addin_text = wx.StaticText( self.addincome_panel, wx.ID_ANY, u"PEMASUKAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addin_text.Wrap( -1 )

		self.addin_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.addin_text.SetMinSize( wx.Size( -1,55 ) )

		addinpanel_sizer.Add( self.addin_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		subpanelincome_sizer = wx.FlexGridSizer( 5, 1, 10, 0 )
		subpanelincome_sizer.SetFlexibleDirection( wx.BOTH )
		subpanelincome_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		subpanelincome_sizer.SetMinSize( wx.Size( -1,40 ) )
		income_label = wx.StaticBoxSizer( wx.StaticBox( self.addincome_panel, wx.ID_ANY, u"keterangan" ), wx.VERTICAL )

		self.income_input = wx.TextCtrl( income_label.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.income_input.SetMinSize( wx.Size( 220,-1 ) )

		income_label.Add( self.income_input, 0, wx.ALL, 5 )


		subpanelincome_sizer.Add( income_label, 1, wx.EXPAND, 5 )

		income_label2 = wx.StaticBoxSizer( wx.StaticBox( self.addincome_panel, wx.ID_ANY, u"nominal" ), wx.VERTICAL )

		self.income_input2 = wx.TextCtrl( income_label2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.income_input2.SetMinSize( wx.Size( 220,-1 ) )

		income_label2.Add( self.income_input2, 0, wx.ALL, 5 )


		subpanelincome_sizer.Add( income_label2, 1, wx.EXPAND, 5 )

		self.dummy = wx.StaticText( self.addincome_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( 1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		subpanelincome_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		addin_button = wx.StdDialogButtonSizer()
		self.addin_buttonOK = wx.Button( self.addincome_panel, wx.ID_OK )
		addin_button.AddButton( self.addin_buttonOK )
		self.addin_buttonCancel = wx.Button( self.addincome_panel, wx.ID_CANCEL )
		addin_button.AddButton( self.addin_buttonCancel )
		addin_button.Realize();

		subpanelincome_sizer.Add( addin_button, 1, wx.ALIGN_CENTER, 5 )


		addinpanel_sizer.Add( subpanelincome_sizer, 1, wx.ALIGN_CENTER, 5 )


		self.addincome_panel.SetSizer( addinpanel_sizer )
		self.addincome_panel.Layout()
		addinpanel_sizer.Fit( self.addincome_panel )
		addincome_sizer.Add( self.addincome_panel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,50 ) )

		addincome_sizer.Add( self.dummy, 0, wx.ALL, 5 )


		self.SetSizer( addincome_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.addin_buttonCancel.Bind( wx.EVT_BUTTON, self.unadd_income )
		self.addin_buttonOK.Bind( wx.EVT_BUTTON, self.add_income )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def unadd_income( self, event ):
		event.Skip()

	def add_income( self, event ):
		event.Skip()


###########################################################################
## Class outcome
###########################################################################

class outcome ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pengeluaran", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		self.outcome_menubar = wx.MenuBar( 0 )
		self.outcome_menu = wx.Menu()
		self.out_menu = wx.MenuItem( self.outcome_menu, wx.ID_ANY, u"Dashboard", wx.EmptyString, wx.ITEM_NORMAL )
		self.outcome_menu.Append( self.out_menu )

		self.out_menu2 = wx.MenuItem( self.outcome_menu, wx.ID_ANY, u"Pemasukan", wx.EmptyString, wx.ITEM_NORMAL )
		self.outcome_menu.Append( self.out_menu2 )

		self.out_menu3 = wx.MenuItem( self.outcome_menu, wx.ID_ANY, u"Stok Produk", wx.EmptyString, wx.ITEM_NORMAL )
		self.outcome_menu.Append( self.out_menu3 )

		self.out_menu4 = wx.MenuItem( self.outcome_menu, wx.ID_ANY, u"Keluar", wx.EmptyString, wx.ITEM_NORMAL )
		self.outcome_menu.Append( self.out_menu4 )

		self.outcome_menubar.Append( self.outcome_menu, u"Menu" )

		self.SetMenuBar( self.outcome_menubar )

		outcome_sizer = wx.BoxSizer( wx.VERTICAL )

		self.outcome = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 720,480 ), wx.TAB_TRAVERSAL )
		self.outcome.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.outcome.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.outcome.SetMinSize( wx.Size( 720,480 ) )
		self.outcome.SetMaxSize( wx.Size( 720,480 ) )

		suboutcome_sizer = wx.FlexGridSizer( 6, 1, 0, 0 )
		suboutcome_sizer.SetFlexibleDirection( wx.BOTH )
		suboutcome_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dummy1 = wx.StaticText( self.outcome, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy1.Wrap( -1 )

		self.dummy1.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		suboutcome_sizer.Add( self.dummy1, 0, wx.ALL, 5 )

		outcome_sizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.out_text = wx.StaticText( self.outcome, wx.ID_ANY, u"Total Pengeluaran", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.out_text.Wrap( -1 )

		self.out_text.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		outcome_sizer1.Add( self.out_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.outcome_display = wx.TextCtrl( self.outcome, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		outcome_sizer1.Add( self.outcome_display, 0, wx.ALL, 5 )


		suboutcome_sizer.Add( outcome_sizer1, 1, wx.EXPAND, 5 )

		self.dummy2 = wx.StaticText( self.outcome, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy2.Wrap( -1 )

		self.dummy2.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		suboutcome_sizer.Add( self.dummy2, 0, wx.ALL, 5 )

		self.out_button = wx.Button( self.outcome, wx.ID_ANY, u"Tambahkan Data ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.out_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.out_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.out_button.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		suboutcome_sizer.Add( self.out_button, 0, wx.ALL, 5 )

		self.dummy3 = wx.StaticText( self.outcome, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy3.Wrap( -1 )

		self.dummy3.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		suboutcome_sizer.Add( self.dummy3, 0, wx.ALL, 5 )

		self.outcome_data = wx.grid.Grid( self.outcome, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.outcome_data.CreateGrid( 0, 0 )
		self.outcome_data.EnableEditing( False )
		self.outcome_data.EnableGridLines( True )
		self.outcome_data.EnableDragGridSize( False )
		self.outcome_data.SetMargins( 0, 0 )

		# Columns
		self.outcome_data.EnableDragColMove( False )
		self.outcome_data.EnableDragColSize( True )
		self.outcome_data.SetColLabelSize( 30 )
		self.outcome_data.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.outcome_data.EnableDragRowSize( True )
		self.outcome_data.SetRowLabelSize( 80 )
		self.outcome_data.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.outcome_data.SetLabelBackgroundColour( wx.Colour( 198, 182, 228 ) )
		self.outcome_data.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		# Cell Defaults
		self.outcome_data.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.outcome_data.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.outcome_data.SetMinSize( wx.Size( 670,-1 ) )
		self.outcome_data.SetMaxSize( wx.Size( -1,260 ) )

		suboutcome_sizer.Add( self.outcome_data, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.outcome.SetSizer( suboutcome_sizer )
		self.outcome.Layout()
		outcome_sizer.Add( self.outcome, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( outcome_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.outtodb, id = self.out_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.outtoin, id = self.out_menu2.GetId() )
		self.Bind( wx.EVT_MENU, self.outtostock, id = self.out_menu3.GetId() )
		self.Bind( wx.EVT_MENU, self.outtologout, id = self.out_menu4.GetId() )
		self.out_button.Bind( wx.EVT_BUTTON, self.add_outcome )
		self.outcome_data.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.getcellpos )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def outtodb( self, event ):
		event.Skip()

	def outtoin( self, event ):
		event.Skip()

	def outtostock( self, event ):
		event.Skip()

	def outtologout( self, event ):
		event.Skip()

	def add_outcome( self, event ):
		event.Skip()

	def getcellpos( self, event ):
		event.Skip()


###########################################################################
## Class add_outcome
###########################################################################

class add_outcome ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pengeluaran", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		addoutcome_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,50 ) )

		addoutcome_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.addoutcome_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.addoutcome_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.addoutcome_panel.SetMinSize( wx.Size( 360,-1 ) )

		addoutpanel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self.addoutcome_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.dummy.SetMinSize( wx.Size( -1,20 ) )

		addoutpanel_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.addout_text = wx.StaticText( self.addoutcome_panel, wx.ID_ANY, u"PENGELUARAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addout_text.Wrap( -1 )

		self.addout_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.addout_text.SetMinSize( wx.Size( -1,55 ) )

		addoutpanel_sizer.Add( self.addout_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		subpaneloutcome_sizer = wx.FlexGridSizer( 5, 1, 10, 0 )
		subpaneloutcome_sizer.SetFlexibleDirection( wx.BOTH )
		subpaneloutcome_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		subpaneloutcome_sizer.SetMinSize( wx.Size( -1,40 ) )
		outcome_label = wx.StaticBoxSizer( wx.StaticBox( self.addoutcome_panel, wx.ID_ANY, u"keterangan" ), wx.VERTICAL )

		self.outcome_input = wx.TextCtrl( outcome_label.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.outcome_input.SetMinSize( wx.Size( 220,-1 ) )

		outcome_label.Add( self.outcome_input, 0, wx.ALL, 5 )


		subpaneloutcome_sizer.Add( outcome_label, 1, wx.EXPAND, 5 )

		outcome_label2 = wx.StaticBoxSizer( wx.StaticBox( self.addoutcome_panel, wx.ID_ANY, u"nominal" ), wx.VERTICAL )

		self.outcome_input2 = wx.TextCtrl( outcome_label2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.outcome_input2.SetMinSize( wx.Size( 220,-1 ) )

		outcome_label2.Add( self.outcome_input2, 0, wx.ALL, 5 )


		subpaneloutcome_sizer.Add( outcome_label2, 1, wx.EXPAND, 5 )

		self.dummy = wx.StaticText( self.addoutcome_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( 1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		subpaneloutcome_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		addout_button = wx.StdDialogButtonSizer()
		self.addout_buttonOK = wx.Button( self.addoutcome_panel, wx.ID_OK )
		addout_button.AddButton( self.addout_buttonOK )
		self.addout_buttonCancel = wx.Button( self.addoutcome_panel, wx.ID_CANCEL )
		addout_button.AddButton( self.addout_buttonCancel )
		addout_button.Realize();

		subpaneloutcome_sizer.Add( addout_button, 1, wx.ALIGN_CENTER, 5 )


		addoutpanel_sizer.Add( subpaneloutcome_sizer, 1, wx.ALIGN_CENTER, 5 )


		self.addoutcome_panel.SetSizer( addoutpanel_sizer )
		self.addoutcome_panel.Layout()
		addoutpanel_sizer.Fit( self.addoutcome_panel )
		addoutcome_sizer.Add( self.addoutcome_panel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,50 ) )

		addoutcome_sizer.Add( self.dummy, 0, wx.ALL, 5 )


		self.SetSizer( addoutcome_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.addout_buttonCancel.Bind( wx.EVT_BUTTON, self.unadd_outcome )
		self.addout_buttonOK.Bind( wx.EVT_BUTTON, self.add_outcome )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def unadd_outcome( self, event ):
		event.Skip()

	def add_outcome( self, event ):
		event.Skip()


###########################################################################
## Class stock
###########################################################################

class stock ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Stok Produk", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		self.stock_menubar = wx.MenuBar( 0 )
		self.stock_menu = wx.Menu()
		self.st_menu = wx.MenuItem( self.stock_menu, wx.ID_ANY, u"Dashboard", wx.EmptyString, wx.ITEM_NORMAL )
		self.stock_menu.Append( self.st_menu )

		self.st_menu2 = wx.MenuItem( self.stock_menu, wx.ID_ANY, u"Pemasukan", wx.EmptyString, wx.ITEM_NORMAL )
		self.stock_menu.Append( self.st_menu2 )

		self.st_menu3 = wx.MenuItem( self.stock_menu, wx.ID_ANY, u"Pengeluaran", wx.EmptyString, wx.ITEM_NORMAL )
		self.stock_menu.Append( self.st_menu3 )

		self.st_menu4 = wx.MenuItem( self.stock_menu, wx.ID_ANY, u"Keluar", wx.EmptyString, wx.ITEM_NORMAL )
		self.stock_menu.Append( self.st_menu4 )

		self.stock_menubar.Append( self.stock_menu, u"Menu" )

		self.SetMenuBar( self.stock_menubar )

		stock_sizer = wx.BoxSizer( wx.VERTICAL )

		self.stock_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.stock_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		stpanel_sizer = wx.FlexGridSizer( 0, 1, 0, 0 )
		stpanel_sizer.SetFlexibleDirection( wx.BOTH )
		stpanel_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dummy = wx.StaticText( self.stock_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		stpanel_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.st_text = wx.StaticText( self.stock_panel, wx.ID_ANY, u"DAFTAR PRODUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_text.Wrap( -1 )

		self.st_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.st_text.SetMinSize( wx.Size( -1,40 ) )

		stpanel_sizer.Add( self.st_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.stock_button = wx.Button( self.stock_panel, wx.ID_ANY, u"Tambahkan Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stock_button.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.stock_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.stock_button.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		stpanel_sizer.Add( self.stock_button, 0, wx.ALL, 5 )

		self.dummy = wx.StaticText( self.stock_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( 5, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		stpanel_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.st_data = wx.grid.Grid( self.stock_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.st_data.CreateGrid( 0, 0 )
		self.st_data.EnableEditing( False )
		self.st_data.EnableGridLines( True )
		self.st_data.EnableDragGridSize( False )
		self.st_data.SetMargins( 0, 0 )

		# Columns
		self.st_data.EnableDragColMove( False )
		self.st_data.EnableDragColSize( True )
		self.st_data.SetColLabelSize( 30 )
		self.st_data.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.st_data.EnableDragRowSize( True )
		self.st_data.SetRowLabelSize( 80 )
		self.st_data.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.st_data.SetLabelBackgroundColour( wx.Colour( 198, 182, 228 ) )
		self.st_data.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		# Cell Defaults
		self.st_data.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.st_data.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.st_data.SetMinSize( wx.Size( 670,-1 ) )
		self.st_data.SetMaxSize( wx.Size( -1,260 ) )

		stpanel_sizer.Add( self.st_data, 0, wx.ALL, 5 )


		self.stock_panel.SetSizer( stpanel_sizer )
		self.stock_panel.Layout()
		stpanel_sizer.Fit( self.stock_panel )
		stock_sizer.Add( self.stock_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( stock_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.stocktodb, id = self.st_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.stocktoin, id = self.st_menu2.GetId() )
		self.Bind( wx.EVT_MENU, self.stocktoout, id = self.st_menu3.GetId() )
		self.Bind( wx.EVT_MENU, self.stocktologout, id = self.st_menu4.GetId() )
		self.stock_button.Bind( wx.EVT_BUTTON, self.addnewstock )
		self.st_data.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.getcellpos )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def stocktodb( self, event ):
		event.Skip()

	def stocktoin( self, event ):
		event.Skip()

	def stocktoout( self, event ):
		event.Skip()

	def stocktologout( self, event ):
		event.Skip()

	def addnewstock( self, event ):
		event.Skip()

	def getcellpos( self, event ):
		event.Skip()


###########################################################################
## Class add_stock
###########################################################################

class add_stock ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Produk", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		addstock_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,50 ) )

		addstock_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.addstock_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.addstock_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.addstock_panel.SetMinSize( wx.Size( 360,-1 ) )

		addspanel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy = wx.StaticText( self.addstock_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.dummy.SetMinSize( wx.Size( -1,20 ) )

		addspanel_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		self.addstock_text = wx.StaticText( self.addstock_panel, wx.ID_ANY, u"Tambahkan Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addstock_text.Wrap( -1 )

		self.addstock_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.addstock_text.SetMinSize( wx.Size( -1,55 ) )

		addspanel_sizer.Add( self.addstock_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		subpanelstock_sizer = wx.FlexGridSizer( 5, 1, 10, 0 )
		subpanelstock_sizer.SetFlexibleDirection( wx.BOTH )
		subpanelstock_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		subpanelstock_sizer.SetMinSize( wx.Size( -1,40 ) )
		stock_label = wx.StaticBoxSizer( wx.StaticBox( self.addstock_panel, wx.ID_ANY, u"nama produk" ), wx.VERTICAL )

		self.stock_input = wx.TextCtrl( stock_label.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stock_input.SetMinSize( wx.Size( 220,-1 ) )

		stock_label.Add( self.stock_input, 0, wx.ALL, 5 )


		subpanelstock_sizer.Add( stock_label, 1, wx.EXPAND, 5 )

		stock_label2 = wx.StaticBoxSizer( wx.StaticBox( self.addstock_panel, wx.ID_ANY, u"jenis produk" ), wx.VERTICAL )

		self.stock_input2 = wx.TextCtrl( stock_label2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stock_input2.SetMinSize( wx.Size( 220,-1 ) )

		stock_label2.Add( self.stock_input2, 0, wx.ALL, 5 )


		subpanelstock_sizer.Add( stock_label2, 1, wx.EXPAND, 5 )

		self.dummy = wx.StaticText( self.addstock_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( 1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		subpanelstock_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		addstock_button = wx.StdDialogButtonSizer()
		self.addstock_buttonSave = wx.Button( self.addstock_panel, wx.ID_SAVE )
		addstock_button.AddButton( self.addstock_buttonSave )
		self.addstock_buttonCancel = wx.Button( self.addstock_panel, wx.ID_CANCEL )
		addstock_button.AddButton( self.addstock_buttonCancel )
		addstock_button.Realize();

		subpanelstock_sizer.Add( addstock_button, 1, wx.ALIGN_CENTER, 5 )


		addspanel_sizer.Add( subpanelstock_sizer, 1, wx.ALIGN_CENTER, 5 )


		self.addstock_panel.SetSizer( addspanel_sizer )
		self.addstock_panel.Layout()
		addspanel_sizer.Fit( self.addstock_panel )
		addstock_sizer.Add( self.addstock_panel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.add_stock = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.add_stock.Wrap( -1 )

		self.add_stock.SetMinSize( wx.Size( -1,50 ) )

		addstock_sizer.Add( self.add_stock, 0, wx.ALL, 5 )


		self.SetSizer( addstock_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.addstock_buttonCancel.Bind( wx.EVT_BUTTON, self.unadd_stock )
		self.addstock_buttonSave.Bind( wx.EVT_BUTTON, self.added_stock )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def unadd_stock( self, event ):
		event.Skip()

	def added_stock( self, event ):
		event.Skip()


###########################################################################
## Class edit_stock
###########################################################################

class edit_stock ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Produk", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		addstock_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy1.Wrap( -1 )

		self.dummy1.SetMinSize( wx.Size( -1,50 ) )

		addstock_sizer.Add( self.dummy1, 0, wx.ALL, 5 )

		self.addstock_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.addstock_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.addstock_panel.SetMinSize( wx.Size( 360,-1 ) )

		addspanel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy2 = wx.StaticText( self.addstock_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy2.Wrap( -1 )

		self.dummy2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.dummy2.SetMinSize( wx.Size( -1,10 ) )

		addspanel_sizer.Add( self.dummy2, 0, wx.ALL, 5 )

		self.addstock_text = wx.StaticText( self.addstock_panel, wx.ID_ANY, u"Edit Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addstock_text.Wrap( -1 )

		self.addstock_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.addstock_text.SetMinSize( wx.Size( -1,30 ) )

		addspanel_sizer.Add( self.addstock_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		subpanelstock_sizer = wx.FlexGridSizer( 5, 1, 10, 0 )
		subpanelstock_sizer.SetFlexibleDirection( wx.BOTH )
		subpanelstock_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		subpanelstock_sizer.SetMinSize( wx.Size( -1,40 ) )
		stock_label = wx.StaticBoxSizer( wx.StaticBox( self.addstock_panel, wx.ID_ANY, u"nama produk" ), wx.VERTICAL )

		self.stock_input = wx.TextCtrl( stock_label.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stock_input.SetMinSize( wx.Size( 220,-1 ) )

		stock_label.Add( self.stock_input, 0, wx.ALL, 5 )


		subpanelstock_sizer.Add( stock_label, 1, wx.EXPAND, 5 )

		stock_label2 = wx.StaticBoxSizer( wx.StaticBox( self.addstock_panel, wx.ID_ANY, u"jenis produk" ), wx.VERTICAL )

		self.stock_input2 = wx.TextCtrl( stock_label2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stock_input2.SetMinSize( wx.Size( 220,-1 ) )

		stock_label2.Add( self.stock_input2, 0, wx.ALL, 5 )


		subpanelstock_sizer.Add( stock_label2, 1, wx.EXPAND, 5 )

		stock_label3 = wx.BoxSizer( wx.HORIZONTAL )

		stock_label31 = wx.StaticBoxSizer( wx.StaticBox( self.addstock_panel, wx.ID_ANY, u"stok produk" ), wx.VERTICAL )

		self.stock_input31 = wx.TextCtrl( stock_label31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stock_input31.SetMinSize( wx.Size( 110,-1 ) )

		stock_label31.Add( self.stock_input31, 0, wx.ALL, 5 )


		stock_label3.Add( stock_label31, 1, 0, 5 )

		stock_label32 = wx.StaticBoxSizer( wx.StaticBox( self.addstock_panel, wx.ID_ANY, u"produk terjual" ), wx.HORIZONTAL )

		self.stock_input32 = wx.TextCtrl( stock_label32.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stock_input32.SetMinSize( wx.Size( 110,-1 ) )

		stock_label32.Add( self.stock_input32, 0, wx.ALL, 5 )


		stock_label3.Add( stock_label32, 1, 0, 5 )


		subpanelstock_sizer.Add( stock_label3, 1, wx.EXPAND, 5 )

		self.dummy = wx.StaticText( self.addstock_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetFont( wx.Font( 1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.dummy.SetMinSize( wx.Size( -1,-10 ) )

		subpanelstock_sizer.Add( self.dummy, 0, wx.ALL, 5 )

		addstock_button = wx.StdDialogButtonSizer()
		self.addstock_buttonSave = wx.Button( self.addstock_panel, wx.ID_SAVE )
		addstock_button.AddButton( self.addstock_buttonSave )
		self.addstock_buttonCancel = wx.Button( self.addstock_panel, wx.ID_CANCEL )
		addstock_button.AddButton( self.addstock_buttonCancel )
		addstock_button.Realize();

		subpanelstock_sizer.Add( addstock_button, 1, wx.ALIGN_CENTER, 5 )


		addspanel_sizer.Add( subpanelstock_sizer, 1, wx.ALIGN_CENTER, 5 )


		self.addstock_panel.SetSizer( addspanel_sizer )
		self.addstock_panel.Layout()
		addspanel_sizer.Fit( self.addstock_panel )
		addstock_sizer.Add( self.addstock_panel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.add_stock = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.add_stock.Wrap( -1 )

		self.add_stock.SetMinSize( wx.Size( -1,50 ) )

		addstock_sizer.Add( self.add_stock, 0, wx.ALL, 5 )


		self.SetSizer( addstock_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.addstock_buttonCancel.Bind( wx.EVT_BUTTON, self.unedit_stock )
		self.addstock_buttonSave.Bind( wx.EVT_BUTTON, self.edited_stock )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def unedit_stock( self, event ):
		event.Skip()

	def edited_stock( self, event ):
		event.Skip()


###########################################################################
## Class edit_outcome
###########################################################################

class edit_outcome ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Pengeluaran", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		editoutcome_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy1.Wrap( -1 )

		self.dummy1.SetMinSize( wx.Size( -1,50 ) )

		editoutcome_sizer.Add( self.dummy1, 0, wx.ALL, 5 )

		self.editoutcome_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.editoutcome_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.editoutcome_panel.SetMinSize( wx.Size( 360,-1 ) )

		editoutpanel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy2 = wx.StaticText( self.editoutcome_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy2.Wrap( -1 )

		self.dummy2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.dummy2.SetMinSize( wx.Size( -1,20 ) )

		editoutpanel_sizer.Add( self.dummy2, 0, wx.ALL, 5 )

		self.editout_text = wx.StaticText( self.editoutcome_panel, wx.ID_ANY, u"EDIT PENGELUARAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.editout_text.Wrap( -1 )

		self.editout_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.editout_text.SetMinSize( wx.Size( -1,55 ) )

		editoutpanel_sizer.Add( self.editout_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		subpaneloutcome_sizer = wx.FlexGridSizer( 5, 1, 10, 0 )
		subpaneloutcome_sizer.SetFlexibleDirection( wx.BOTH )
		subpaneloutcome_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		subpaneloutcome_sizer.SetMinSize( wx.Size( -1,40 ) )
		outcome_label = wx.StaticBoxSizer( wx.StaticBox( self.editoutcome_panel, wx.ID_ANY, u"keterangan" ), wx.VERTICAL )

		self.outcome_input = wx.TextCtrl( outcome_label.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.outcome_input.SetMinSize( wx.Size( 220,-1 ) )

		outcome_label.Add( self.outcome_input, 0, wx.ALL, 5 )


		subpaneloutcome_sizer.Add( outcome_label, 1, wx.EXPAND, 5 )

		outcome_label2 = wx.StaticBoxSizer( wx.StaticBox( self.editoutcome_panel, wx.ID_ANY, u"nominal" ), wx.VERTICAL )

		self.outcome_input2 = wx.TextCtrl( outcome_label2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.outcome_input2.SetMinSize( wx.Size( 220,-1 ) )

		outcome_label2.Add( self.outcome_input2, 0, wx.ALL, 5 )


		subpaneloutcome_sizer.Add( outcome_label2, 1, wx.EXPAND, 5 )

		self.dummy3 = wx.StaticText( self.editoutcome_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy3.Wrap( -1 )

		self.dummy3.SetFont( wx.Font( 1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		subpaneloutcome_sizer.Add( self.dummy3, 0, wx.ALL, 5 )

		editout_button = wx.StdDialogButtonSizer()
		self.editout_buttonOK = wx.Button( self.editoutcome_panel, wx.ID_OK )
		editout_button.AddButton( self.editout_buttonOK )
		self.editout_buttonCancel = wx.Button( self.editoutcome_panel, wx.ID_CANCEL )
		editout_button.AddButton( self.editout_buttonCancel )
		editout_button.Realize();

		subpaneloutcome_sizer.Add( editout_button, 1, wx.ALIGN_CENTER, 5 )


		editoutpanel_sizer.Add( subpaneloutcome_sizer, 1, wx.ALIGN_CENTER, 5 )


		self.editoutcome_panel.SetSizer( editoutpanel_sizer )
		self.editoutcome_panel.Layout()
		editoutpanel_sizer.Fit( self.editoutcome_panel )
		editoutcome_sizer.Add( self.editoutcome_panel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,50 ) )

		editoutcome_sizer.Add( self.dummy, 0, wx.ALL, 5 )


		self.SetSizer( editoutcome_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.editout_buttonCancel.Bind( wx.EVT_BUTTON, self.unadd_outcome )
		self.editout_buttonOK.Bind( wx.EVT_BUTTON, self.add_outcome )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def unadd_outcome( self, event ):
		event.Skip()

	def add_outcome( self, event ):
		event.Skip()


###########################################################################
## Class edit_income
###########################################################################

class edit_income ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Pemasukan", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 720,480 ), wx.Size( 720,480 ) )
		self.SetBackgroundColour( wx.Colour( 198, 182, 228 ) )

		editincome_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy1.Wrap( -1 )

		self.dummy1.SetMinSize( wx.Size( -1,50 ) )

		editincome_sizer.Add( self.dummy1, 0, wx.ALL, 5 )

		self.editincome_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.editincome_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.editincome_panel.SetMinSize( wx.Size( 360,-1 ) )

		editinpanel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.dummy2 = wx.StaticText( self.editincome_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy2.Wrap( -1 )

		self.dummy2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.dummy2.SetMinSize( wx.Size( -1,20 ) )

		editinpanel_sizer.Add( self.dummy2, 0, wx.ALL, 5 )

		self.editin_text = wx.StaticText( self.editincome_panel, wx.ID_ANY, u"EDIT PEMASUKAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.editin_text.Wrap( -1 )

		self.editin_text.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.editin_text.SetMinSize( wx.Size( -1,55 ) )

		editinpanel_sizer.Add( self.editin_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		subpanelincome_sizer = wx.FlexGridSizer( 5, 1, 10, 0 )
		subpanelincome_sizer.SetFlexibleDirection( wx.BOTH )
		subpanelincome_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		subpanelincome_sizer.SetMinSize( wx.Size( -1,40 ) )
		income_label = wx.StaticBoxSizer( wx.StaticBox( self.editincome_panel, wx.ID_ANY, u"keterangan" ), wx.VERTICAL )

		self.income_input = wx.TextCtrl( income_label.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.income_input.SetMinSize( wx.Size( 220,-1 ) )

		income_label.Add( self.income_input, 0, wx.ALL, 5 )


		subpanelincome_sizer.Add( income_label, 1, wx.EXPAND, 5 )

		income_label2 = wx.StaticBoxSizer( wx.StaticBox( self.editincome_panel, wx.ID_ANY, u"nominal" ), wx.VERTICAL )

		self.income_input2 = wx.TextCtrl( income_label2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.income_input2.SetMinSize( wx.Size( 220,-1 ) )

		income_label2.Add( self.income_input2, 0, wx.ALL, 5 )


		subpanelincome_sizer.Add( income_label2, 1, wx.EXPAND, 5 )

		self.dummy3 = wx.StaticText( self.editincome_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy3.Wrap( -1 )

		self.dummy3.SetFont( wx.Font( 1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		subpanelincome_sizer.Add( self.dummy3, 0, wx.ALL, 5 )

		editin_button = wx.StdDialogButtonSizer()
		self.editin_buttonOK = wx.Button( self.editincome_panel, wx.ID_OK )
		editin_button.AddButton( self.editin_buttonOK )
		self.editin_buttonCancel = wx.Button( self.editincome_panel, wx.ID_CANCEL )
		editin_button.AddButton( self.editin_buttonCancel )
		editin_button.Realize();

		subpanelincome_sizer.Add( editin_button, 1, wx.ALIGN_CENTER, 5 )


		editinpanel_sizer.Add( subpanelincome_sizer, 1, wx.ALIGN_CENTER, 5 )


		self.editincome_panel.SetSizer( editinpanel_sizer )
		self.editincome_panel.Layout()
		editinpanel_sizer.Fit( self.editincome_panel )
		editincome_sizer.Add( self.editincome_panel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.dummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dummy.Wrap( -1 )

		self.dummy.SetMinSize( wx.Size( -1,50 ) )

		editincome_sizer.Add( self.dummy, 0, wx.ALL, 5 )


		self.SetSizer( editincome_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.editin_buttonCancel.Bind( wx.EVT_BUTTON, self.unadd_income )
		self.editin_buttonOK.Bind( wx.EVT_BUTTON, self.add_income )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def unadd_income( self, event ):
		event.Skip()

	def add_income( self, event ):
		event.Skip()


