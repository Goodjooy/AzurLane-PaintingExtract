# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GirlsFrontLine", pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"RGB文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem6 )

		self.m_menuItem7 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Alpha文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem7 )

		self.m_menu1.AppendSubMenu( self.m_menu11, u"导入文件" )

		self.m_menu1.AppendSeparator()

		self.m_menu21 = wx.Menu()
		self.m_menuItem8 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"RGB && Alpha文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem8 )

		self.m_menuItem9 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"RGB文件夹", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem9 )

		self.m_menuItem10 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"Alpha文件夹", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem10 )

		self.m_menu1.AppendSubMenu( self.m_menu21, u"导入目录" )

		self.m_menu1.AppendSeparator()

		self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem5 )

		self.m_menubar1.Append( self.m_menu1, u"文件" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem_all = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"导出全部", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem_all )

		self.m_menuItem_choice = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"导出选择项", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem_choice )

		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"直接拷贝不符合", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"导出筛选项", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem4 )

		self.m_menubar1.Append( self.m_menu2, u"导出" )

		self.SetMenuBar( self.m_menubar1 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RGB" ), wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_gauge_RGB_load = wx.Gauge( sbSizer1.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_RGB_load.SetValue( 0 )
		bSizer6.Add( self.m_gauge_RGB_load, 1, wx.ALL, 5 )

		self.m_staticText_RGB_load = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"就绪", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_RGB_load.Wrap( -1 )

		bSizer6.Add( self.m_staticText_RGB_load, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		sbSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer1, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Alpha" ), wx.VERTICAL )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_gauge_alpha_load = wx.Gauge( sbSizer2.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_alpha_load.SetValue( 0 )
		bSizer61.Add( self.m_gauge_alpha_load, 1, wx.ALL, 5 )

		self.m_staticText_alpha_load = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"就绪", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_alpha_load.Wrap( -1 )

		bSizer61.Add( self.m_staticText_alpha_load, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		sbSizer2.Add( bSizer61, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer2, 0, wx.EXPAND, 5 )

		self.m_listbook1 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel1 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_searchCtrl_RGB = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_RGB.ShowSearchButton( True )
		self.m_searchCtrl_RGB.ShowCancelButton( False )
		bSizer3.Add( self.m_searchCtrl_RGB, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox_RGBChoices = []
		self.m_listBox_RGB = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_RGBChoices, 0 )
		bSizer3.Add( self.m_listBox_RGB, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		self.m_listbook1.AddPage( self.m_panel1, u"RGB", True )
		self.m_panel2 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_searchCtrl_alpha = wx.SearchCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_alpha.ShowSearchButton( True )
		self.m_searchCtrl_alpha.ShowCancelButton( False )
		bSizer4.Add( self.m_searchCtrl_alpha, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox_alphaChoices = []
		self.m_listBox_alpha = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_alphaChoices, 0 )
		bSizer4.Add( self.m_listBox_alpha, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer4 )
		self.m_panel2.Layout()
		bSizer4.Fit( self.m_panel2 )
		self.m_listbook1.AddPage( self.m_panel2, u"Alpha", False )

		bSizer2.Add( self.m_listbook1, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
		bSizer7.Add( self.m_listBox3, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer7 )
		self.m_panel3.Layout()
		bSizer7.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"skiped", False )
		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		m_listBox_unableChoices = []
		self.m_listBox_unable = wx.ListBox( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_unableChoices, 0 )
		bSizer9.Add( self.m_listBox_unable, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer9 )
		self.m_panel4.Layout()
		bSizer9.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"unable", True )

		bSizer62.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_now = wx.StaticText( self, wx.ID_ANY, u"当前：None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_now.Wrap( -1 )

		bSizer62.Add( self.m_staticText_now, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText_all = wx.StaticText( self, wx.ID_ANY, u"进度：0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_all.Wrap( -1 )

		bSizer62.Add( self.m_staticText_all, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_gauge_all = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_all.SetValue( 0 )
		bSizer62.Add( self.m_gauge_all, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer1.Add( bSizer62, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.load_rgb, id = self.m_menuItem6.GetId() )
		self.Bind( wx.EVT_MENU, self.load_alpha, id = self.m_menuItem7.GetId() )
		self.Bind( wx.EVT_MENU, self.load_rgb_alpha_fold, id = self.m_menuItem8.GetId() )
		self.Bind( wx.EVT_MENU, self.load_RGB_fold, id = self.m_menuItem9.GetId() )
		self.Bind( wx.EVT_MENU, self.load_alpha_fold, id = self.m_menuItem10.GetId() )
		self.Bind( wx.EVT_MENU, self.export_all, id = self.m_menuItem_all.GetId() )
		self.Bind( wx.EVT_MENU, self.export_choice, id = self.m_menuItem_choice.GetId() )
		self.m_searchCtrl_RGB.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_rgb )
		self.m_searchCtrl_RGB.Bind( wx.EVT_TEXT, self.search_rgb )
		self.m_listBox_RGB.Bind( wx.EVT_LISTBOX, self.rgb_choice )
		self.m_listBox_RGB.Bind( wx.EVT_LISTBOX_DCLICK, self.rgb_choice )
		self.m_searchCtrl_alpha.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_alpha )
		self.m_searchCtrl_alpha.Bind( wx.EVT_TEXT, self.search_alpha )
		self.m_listBox_alpha.Bind( wx.EVT_LISTBOX, self.alpha_choice )
		self.m_listBox_alpha.Bind( wx.EVT_LISTBOX_DCLICK, self.alpha_choice )
		self.m_button1.Bind( wx.EVT_BUTTON, self.setting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def load_rgb( self, event ):
		event.Skip()

	def load_alpha( self, event ):
		event.Skip()

	def load_rgb_alpha_fold( self, event ):
		event.Skip()

	def load_RGB_fold( self, event ):
		event.Skip()

	def load_alpha_fold( self, event ):
		event.Skip()

	def export_all( self, event ):
		event.Skip()

	def export_choice( self, event ):
		event.Skip()

	def search_rgb( self, event ):
		event.Skip()


	def rgb_choice( self, event ):
		event.Skip()


	def search_alpha( self, event ):
		event.Skip()


	def alpha_choice( self, event ):
		event.Skip()


	def setting( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 958,475 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer2.Add( self.m_hyperlink1, 0, wx.ALL, 5 )

		self.m_hyperlink2 = wx.adv.HyperlinkCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer2.Add( self.m_hyperlink2, 0, wx.ALL, 5 )


		bSizer10.Add( gSizer2, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer10 )
		self.m_scrolledWindow1.Layout()
		bSizer10.Fit( self.m_scrolledWindow1 )
		self.m_notebook2.AddPage( self.m_scrolledWindow1, u"欢迎", True )
		self.m_scrolledWindow5 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		gSizer3 = wx.GridSizer( 0, 3, 0, 0 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"全局设置" ), wx.VERTICAL )

		m_radioBox_type_useChoices = [ u"使用预设方案", u"使用自定义方案" ]
		self.m_radioBox_type_use = wx.RadioBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"导入导出方案选择", wx.DefaultPosition, wx.DefaultSize, m_radioBox_type_useChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_type_use.SetSelection( 0 )
		sbSizer3.Add( self.m_radioBox_type_use, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_autoopen = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"完成后自动打开文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_autoopen.SetValue(True)
		sbSizer3.Add( self.m_checkBox_autoopen, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_check = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"开始前扫描", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_check.SetValue(True)
		sbSizer3.Add( self.m_checkBox_check, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_pass_finished = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"跳过已还原", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_pass_finished.SetValue(True)
		sbSizer3.Add( self.m_checkBox_pass_finished, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox5 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"使用中文名导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox5.SetValue(True)
		sbSizer3.Add( self.m_checkBox5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_open_temp = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"自动打开选择项", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_checkBox_open_temp, 0, wx.ALL, 5 )

		self.m_checkBox4_finish_exit = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"完成后退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_checkBox4_finish_exit, 0, wx.ALL, 5 )

		self.m_checkBox_gfl_dir = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"在导出文件夹内新建文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_gfl_dir.SetValue(True)
		sbSizer3.Add( self.m_checkBox_gfl_dir, 0, wx.ALL, 5 )


		gSizer3.Add( sbSizer3, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"预设方案" ), wx.VERTICAL )

		m_radioBox_gfl_divChoices = [ u"仅导入人形", u"导入全部" ]
		self.m_radioBox_gfl_div = wx.RadioBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"导入方案", wx.DefaultPosition, wx.DefaultSize, m_radioBox_gfl_divChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_gfl_div.SetSelection( 1 )
		sbSizer4.Add( self.m_radioBox_gfl_div, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox_gfl_exChoices = [ u"不分类", u"按人形-非人形分类", u"按人形名称分类", u"按人形原皮-皮肤分类", u"按人形-人形大破分类" ]
		self.m_radioBox_gfl_ex = wx.RadioBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"导出方案", wx.DefaultPosition, wx.DefaultSize, m_radioBox_gfl_exChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_gfl_ex.SetSelection( 4 )
		sbSizer4.Add( self.m_radioBox_gfl_ex, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer3.Add( sbSizer4, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"自定义方案" ), wx.VERTICAL )

		self.m_staticText_rgb = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"RGB文件导入限制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_rgb.Wrap( -1 )

		sbSizer5.Add( self.m_staticText_rgb, 0, wx.ALL, 5 )

		self.m_textCtrl_rgb = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, u"^pic_\\W+\\.[pP][nN][Gg]$", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_textCtrl_rgb, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Alpha文件导入限制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		sbSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrl_alpha = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, u"^pic_\\W+_[Aa]lpha\\.[pP][Nn][Gg]$", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_textCtrl_alpha, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText7 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"导出分类", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button_add = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button_add, 0, wx.ALL, 5 )

		self.m_button_del = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button_del, 0, wx.ALL, 5 )


		sbSizer5.Add( gSizer4, 0, wx.EXPAND, 5 )

		m_listBox_gl_limitChoices = [ u"1）其他：^.+&" ]
		self.m_listBox_gl_limit = wx.ListBox( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_gl_limitChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		sbSizer5.Add( self.m_listBox_gl_limit, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer3.Add( sbSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_scrolledWindow5.SetSizer( gSizer3 )
		self.m_scrolledWindow5.Layout()
		gSizer3.Fit( self.m_scrolledWindow5 )
		self.m_notebook2.AddPage( self.m_scrolledWindow5, u"导出-导入设置", False )
		self.m_scrolledWindow3 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,400 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"RGB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer14.Add( self.m_staticText8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_dirPicker_gl_rbg_dir = wx.DirPickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer14.Add( self.m_dirPicker_gl_rbg_dir, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Alpha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer14.Add( self.m_staticText9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_dirPicker_gl_alpha_dir = wx.DirPickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer14.Add( self.m_dirPicker_gl_alpha_dir, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer14.Add( self.m_staticText10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_dirPicker_export = wx.DirPickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer14.Add( self.m_dirPicker_export, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_toggleBtn_lock = wx.ToggleButton( self.m_scrolledWindow3, wx.ID_ANY, u"锁定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_toggleBtn_lock, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_scrolledWindow3.SetSizer( bSizer14 )
		self.m_scrolledWindow3.Layout()
		self.m_notebook2.AddPage( self.m_scrolledWindow3, u"默认地址", False )

		bSizer9.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer9.Add( m_sdbSizer1, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.show_choice )
		self.m_radioBox_type_use.Bind( wx.EVT_RADIOBOX, self.change )
		self.m_checkBox_autoopen.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_check.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_pass_finished.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox5.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_open_temp.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox4_finish_exit.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_gfl_dir.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_radioBox_gfl_div.Bind( wx.EVT_RADIOBOX, self.change )
		self.m_radioBox_gfl_ex.Bind( wx.EVT_RADIOBOX, self.change_div )
		self.m_textCtrl_rgb.Bind( wx.EVT_TEXT, self.change )
		self.m_textCtrl_alpha.Bind( wx.EVT_TEXT, self.change )
		self.m_dirPicker_gl_rbg_dir.Bind( wx.EVT_DIRPICKER_CHANGED, self.change )
		self.m_dirPicker_gl_alpha_dir.Bind( wx.EVT_DIRPICKER_CHANGED, self.change )
		self.m_toggleBtn_lock.Bind( wx.EVT_TOGGLEBUTTON, self.lock_address )
		self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.apply_click )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.cancel_click )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.ok_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def show_choice( self, event ):
		event.Skip()

	def change( self, event ):
		event.Skip()









	def change_div( self, event ):
		event.Skip()





	def lock_address( self, event ):
		event.Skip()

	def apply_click( self, event ):
		event.Skip()

	def cancel_click( self, event ):
		event.Skip()

	def ok_click( self, event ):
		event.Skip()


