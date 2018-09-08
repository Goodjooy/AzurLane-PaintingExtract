# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"碧蓝航线立绘还原", pos = wx.DefaultPosition, size = wx.Size( 1158,758 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar2 = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.m_menu_file = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"加载 Texture2D 文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"加载 Mesh 文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem2 )
		
		self.menu_file.AppendSubMenu( self.m_menu_file, u"加载文件" )
		
		self.m_menu_fold = wx.Menu()
		self.m_menuItem_mix = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载 混合文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_fold.AppendItem( self.m_menuItem_mix )
		
		self.m_menuItem_texonly = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载 Texture2D", u"选择贴图的文件夹", wx.ITEM_NORMAL )
		self.m_menu_fold.AppendItem( self.m_menuItem_texonly )
		
		self.m_menuItem_meshonly = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载 Mesh ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_fold.AppendItem( self.m_menuItem_meshonly )
		
		self.menu_file.AppendSubMenu( self.m_menu_fold, u"加载文件夹" )
		
		self.menu_file.AppendSeparator()
		
		self.m_menuItem_exit = wx.MenuItem( self.menu_file, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.m_menuItem_exit )
		
		self.m_menubar2.Append( self.menu_file, u"文件" ) 
		
		self.m_menu_export = wx.Menu()
		self.m_menuItem_all = wx.MenuItem( self.m_menu_export, wx.ID_ANY, u"导出全部", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_export.AppendItem( self.m_menuItem_all )
		self.m_menuItem_all.Enable( False )
		
		self.m_menuItem_choice = wx.MenuItem( self.m_menu_export, wx.ID_ANY, u"导出选择的文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_export.AppendItem( self.m_menuItem_choice )
		self.m_menuItem_choice.Enable( False )
		
		self.m_menuItem_copy_only = wx.MenuItem( self.m_menu_export, wx.ID_ANY, u"把不符合条件的文件直接导出", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_export.AppendItem( self.m_menuItem_copy_only )
		self.m_menuItem_copy_only.Enable( False )
		
		self.m_menubar2.Append( self.m_menu_export, u"导出" ) 
		
		self.m_menu_tool = wx.Menu()
		self.m_menuItem_parkage = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"打包导出文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.AppendItem( self.m_menuItem_parkage )
		self.m_menuItem_parkage.Enable( False )
		
		self.m_menuItem_add = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"添加新的舰娘名", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.AppendItem( self.m_menuItem_add )
		self.m_menuItem_add.Enable( False )
		
		self.m_menuItem_set_list = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"更改舰娘名", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.AppendItem( self.m_menuItem_set_list )
		
		self.m_menuItem_new_file = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"比较新增", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.AppendItem( self.m_menuItem_new_file )
		
		self.m_menubar2.Append( self.m_menu_tool, u"工具" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		gSizer_main = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer_load_tex = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Texture2D" ), wx.VERTICAL )
		
		gSizer_tex = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_gauge_tex_load = wx.Gauge( sbSizer_load_tex.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_tex_load.SetValue( 0 ) 
		gSizer_tex.Add( self.m_gauge_tex_load, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_load_tex = wx.StaticText( sbSizer_load_tex.GetStaticBox(), wx.ID_ANY, u"无任务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_load_tex.Wrap( -1 )
		gSizer_tex.Add( self.m_staticText_load_tex, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer_load_tex.Add( gSizer_tex, 0, 0, 5 )
		
		
		bSizer2.Add( sbSizer_load_tex, 0, wx.EXPAND, 5 )
		
		sbSizer_load_mesh = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Mesh" ), wx.VERTICAL )
		
		gSizer_mesh = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_gauge_mesh_load = wx.Gauge( sbSizer_load_mesh.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_mesh_load.SetValue( 0 ) 
		gSizer_mesh.Add( self.m_gauge_mesh_load, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText_mesh_load = wx.StaticText( sbSizer_load_mesh.GetStaticBox(), wx.ID_ANY, u"无任务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_mesh_load.Wrap( -1 )
		gSizer_mesh.Add( self.m_staticText_mesh_load, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer_load_mesh.Add( gSizer_mesh, 0, 0, 5 )
		
		
		bSizer2.Add( sbSizer_load_mesh, 0, wx.EXPAND, 5 )
		
		self.m_listbook2 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel2 = wx.Panel( self.m_listbook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_searchCtrl_tex = wx.SearchCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_tex.ShowSearchButton( True )
		self.m_searchCtrl_tex.ShowCancelButton( True )
		bSizer7.Add( self.m_searchCtrl_tex, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox_texChoices = []
		self.m_listBox_tex = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_texChoices, 0 )
		bSizer7.Add( self.m_listBox_tex, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer7 )
		self.m_panel2.Layout()
		bSizer7.Fit( self.m_panel2 )
		self.m_listbook2.AddPage( self.m_panel2, u"Texture\n", False )
		self.m_panel1 = wx.Panel( self.m_listbook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_searchCtrl_mesh = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_mesh.ShowSearchButton( True )
		self.m_searchCtrl_mesh.ShowCancelButton( True )
		bSizer71.Add( self.m_searchCtrl_mesh, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox_meshChoices = []
		self.m_listBox_mesh = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_meshChoices, 0 )
		bSizer71.Add( self.m_listBox_mesh, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer71 )
		self.m_panel1.Layout()
		bSizer71.Fit( self.m_panel1 )
		self.m_listbook2.AddPage( self.m_panel1, u"Mesh", True )
		
		bSizer2.Add( self.m_listbook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		gSizer_main.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"information" ), wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_searchCtrl_pass = wx.SearchCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_pass.ShowSearchButton( True )
		self.m_searchCtrl_pass.ShowCancelButton( False )
		gSizer5.Add( self.m_searchCtrl_pass, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_choice_passChoices = [ u"全部", u"航母", u"战列舰", u"驱逐", u"巡洋", u"潜艇", u"其他" ]
		self.m_choice_pass = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_passChoices, 0 )
		self.m_choice_pass.SetSelection( 0 )
		gSizer5.Add( self.m_choice_pass, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer6.Add( gSizer5, 0, wx.EXPAND, 5 )
		
		m_listBox_infoChoices = []
		self.m_listBox_info = wx.ListBox( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_infoChoices, 0 )
		bSizer6.Add( self.m_listBox_info, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer6 )
		self.m_panel3.Layout()
		bSizer6.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"跳过文件信息", True )
		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer72 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer51 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_searchCtrl_unable = wx.SearchCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_unable.ShowSearchButton( True )
		self.m_searchCtrl_unable.ShowCancelButton( False )
		gSizer51.Add( self.m_searchCtrl_unable, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_choice_unableChoices = [ u"全部", u"航母", u"战列舰", u"驱逐", u"巡洋", u"潜艇", u"其他" ]
		self.m_choice_unable = wx.Choice( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_unableChoices, 0 )
		self.m_choice_unable.SetSelection( 0 )
		gSizer51.Add( self.m_choice_unable, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer72.Add( gSizer51, 0, wx.EXPAND, 5 )
		
		m_listBox_unableChoices = []
		self.m_listBox_unable = wx.ListBox( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_unableChoices, 0 )
		bSizer72.Add( self.m_listBox_unable, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer72 )
		self.m_panel4.Layout()
		bSizer72.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"不符合", False )
		
		sbSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText_now = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"当前：None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_now.Wrap( -1 )
		sbSizer3.Add( self.m_staticText_now, 0, wx.ALL, 5 )
		
		self.m_gauge_now = wx.Gauge( sbSizer3.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_now.SetValue( 0 ) 
		sbSizer3.Add( self.m_gauge_now, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText_all = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"总进度：0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_all.Wrap( -1 )
		sbSizer3.Add( self.m_staticText_all, 0, wx.ALL, 5 )
		
		self.m_gauge_all = wx.Gauge( sbSizer3.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_all.SetValue( 0 ) 
		sbSizer3.Add( self.m_gauge_all, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_checkBox_pass_finished = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"跳过已还原的", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_checkBox_pass_finished.SetValue(True) 
		sbSizer3.Add( self.m_checkBox_pass_finished, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_checkBox_autoopen = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"完成后打开相应文件\\文件夹", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_checkBox_autoopen.SetValue(True) 
		sbSizer3.Add( self.m_checkBox_autoopen, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer_main.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer_main )
		self.Layout()
		self.m_timer_restore = wx.Timer()
		self.m_timer_restore.SetOwner( self, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.load_tex, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.load_Mesh, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.load_tex_and_mesh, id = self.m_menuItem_mix.GetId() )
		self.Bind( wx.EVT_MENU, self.load_tex_fold, id = self.m_menuItem_texonly.GetId() )
		self.Bind( wx.EVT_MENU, self.load_mesh_fold, id = self.m_menuItem_meshonly.GetId() )
		self.Bind( wx.EVT_MENU, self.exit_press, id = self.m_menuItem_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.export_all, id = self.m_menuItem_all.GetId() )
		self.Bind( wx.EVT_MENU, self.export_choice, id = self.m_menuItem_choice.GetId() )
		self.Bind( wx.EVT_MENU, self.copy_file, id = self.m_menuItem_copy_only.GetId() )
		self.Bind( wx.EVT_MENU, self.zip_pack, id = self.m_menuItem_parkage.GetId() )
		self.Bind( wx.EVT_MENU, self.add_new, id = self.m_menuItem_add.GetId() )
		self.Bind( wx.EVT_MENU, self.change_name, id = self.m_menuItem_set_list.GetId() )
		self.Bind( wx.EVT_MENU, self.compare, id = self.m_menuItem_new_file.GetId() )
		self.m_searchCtrl_tex.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_tex )
		self.m_listBox_tex.Bind( wx.EVT_LISTBOX_DCLICK, self.tex_choice )
		self.m_searchCtrl_mesh.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_mesh )
		self.m_listBox_mesh.Bind( wx.EVT_LISTBOX_DCLICK, self.mesh_choice )
		self.m_searchCtrl_pass.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_pass )
		self.m_listBox_info.Bind( wx.EVT_LISTBOX_DCLICK, self.open_pass )
		self.m_searchCtrl_unable.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_unable )
		self.m_listBox_unable.Bind( wx.EVT_LISTBOX_DCLICK, self.open_file )
		self.m_checkBox_pass_finished.Bind( wx.EVT_CHECKBOX, self.pass_finished )
		self.m_checkBox_autoopen.Bind( wx.EVT_CHECKBOX, self.auto_open )
		self.Bind( wx.EVT_TIMER, self.restore_way, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def load_tex( self, event ):
		event.Skip()
	
	def load_Mesh( self, event ):
		event.Skip()
	
	def load_tex_and_mesh( self, event ):
		event.Skip()
	
	def load_tex_fold( self, event ):
		event.Skip()
	
	def load_mesh_fold( self, event ):
		event.Skip()
	
	def exit_press( self, event ):
		event.Skip()
	
	def export_all( self, event ):
		event.Skip()
	
	def export_choice( self, event ):
		event.Skip()
	
	def copy_file( self, event ):
		event.Skip()
	
	def zip_pack( self, event ):
		event.Skip()
	
	def add_new( self, event ):
		event.Skip()
	
	def change_name( self, event ):
		event.Skip()
	
	def compare( self, event ):
		event.Skip()
	
	def search_tex( self, event ):
		event.Skip()
	
	def tex_choice( self, event ):
		event.Skip()
	
	def search_mesh( self, event ):
		event.Skip()
	
	def mesh_choice( self, event ):
		event.Skip()
	
	def search_pass( self, event ):
		event.Skip()
	
	def open_pass( self, event ):
		event.Skip()
	
	def search_unable( self, event ):
		event.Skip()
	
	def open_file( self, event ):
		event.Skip()
	
	def pass_finished( self, event ):
		event.Skip()
	
	def auto_open( self, event ):
		event.Skip()
	
	def restore_way( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog_change_name
###########################################################################

class MyDialog_change_name ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 427,496 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_searchCtrl2 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl2.ShowSearchButton( True )
		self.m_searchCtrl2.ShowCancelButton( True )
		bSizer11.Add( self.m_searchCtrl2, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox7Choices = []
		self.m_listBox7 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox7Choices, wx.LB_NEEDED_SB )
		self.m_listBox7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer11.Add( self.m_listBox7, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		m_sdbSizer3.Realize();
		
		bSizer11.Add( m_sdbSizer3, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_save )
		self.Bind( wx.EVT_INIT_DIALOG, self.show_all )
		self.m_searchCtrl2.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searching )
		self.m_listBox7.Bind( wx.EVT_LISTBOX_DCLICK, self.change_name )
		self.m_sdbSizer3OK.Bind( wx.EVT_BUTTON, self.save_change )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close_save( self, event ):
		event.Skip()
	
	def show_all( self, event ):
		event.Skip()
	
	def searching( self, event ):
		event.Skip()
	
	def change_name( self, event ):
		event.Skip()
	
	def save_change( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog_add_new
###########################################################################

class MyDialog_add_new ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"添加新舰娘", pos = wx.DefaultPosition, size = wx.Size( 604,540 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		m_listBox5Choices = []
		self.m_listBox5 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox5Choices, wx.LB_NEEDED_SB )
		bSizer7.Add( self.m_listBox5, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_gauge5 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge5.SetValue( 0 ) 
		bSizer7.Add( self.m_gauge5, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer7.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_save )
		self.Bind( wx.EVT_INIT_DIALOG, self.show_info )
		self.m_listBox5.Bind( wx.EVT_LISTBOX_DCLICK, self.open_add_name )
		self.m_button1.Bind( wx.EVT_BUTTON, self.save_new_dic )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close_save( self, event ):
		event.Skip()
	
	def show_info( self, event ):
		event.Skip()
	
	def open_add_name( self, event ):
		event.Skip()
	
	def save_new_dic( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog_enter_name
###########################################################################

class MyDialog_enter_name ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 357,105 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetMaxLength( 20 ) 
		gSizer4.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer9.Add( gSizer4, 0, wx.EXPAND, 5 )
		
		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Save )
		m_sdbSizer4.Realize();
		
		bSizer9.Add( m_sdbSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.show_name )
		self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, self.save_name )
		self.m_sdbSizer4Save.Bind( wx.EVT_BUTTON, self.save_name )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def show_name( self, event ):
		event.Skip()
	
	def save_name( self, event ):
		event.Skip()
	
	

###########################################################################
## Class MyDialog_compare
###########################################################################

class MyDialog_compare ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"新增文件", pos = wx.DefaultPosition, size = wx.Size( 557,429 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"新文件文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer9.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_dirPicker_old = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"新文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		bSizer9.Add( self.m_dirPicker_old, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"旧文件文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_dirPicker6 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"旧文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		bSizer9.Add( self.m_dirPicker6, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox9Choices = []
		self.m_listBox9 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox9Choices, 0 )
		bSizer9.Add( self.m_listBox9, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();
		
		bSizer9.Add( m_sdbSizer2, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		self.m_timer2 = wx.Timer()
		self.m_timer2.SetOwner( self, wx.ID_ANY )
		self.m_timer2.Start( 1000 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_dirPicker_old.Bind( wx.EVT_DIRPICKER_CHANGED, self.add_new )
		self.m_dirPicker6.Bind( wx.EVT_DIRPICKER_CHANGED, self.add_old )
		self.m_listBox9.Bind( wx.EVT_LISTBOX_DCLICK, self.writer_into )
		self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.close_the_tool )
		self.Bind( wx.EVT_TIMER, self.test, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def add_new( self, event ):
		event.Skip()
	
	def add_old( self, event ):
		event.Skip()
	
	def writer_into( self, event ):
		event.Skip()
	
	def close_the_tool( self, event ):
		event.Skip()
	
	def test( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog4
###########################################################################

class MyDialog4 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 362,89 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"进度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer10.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.m_gauge6 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge6.SetValue( 0 ) 
		bSizer10.Add( self.m_gauge6, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

