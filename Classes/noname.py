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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"碧蓝航线立绘还原", pos = wx.DefaultPosition, size = wx.Size( 1024,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.m_menu_file = wx.Menu()
		self.m_menuItem_tex = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"加载 Texture2D 文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_tex )

		self.m_menuItem_mesh = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"加载 Mesh 文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_mesh )

		self.m_menu_file.AppendSeparator()

		self.m_menuItem_rgb = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"加载RGB通道文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_rgb )
		self.m_menuItem_rgb.Enable( False )

		self.m_menuItem_alpha = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"加载alpha通道文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.Append( self.m_menuItem_alpha )
		self.m_menuItem_alpha.Enable( False )

		self.menu_file.AppendSubMenu( self.m_menu_file, u"加载文件" )

		self.m_menu_fold = wx.Menu()
		self.m_menuItem_mix = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载 Texture2D && Mesh", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_fold.Append( self.m_menuItem_mix )

		self.m_menuItem_texonly = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载 Texture2D", u"选择贴图的文件夹", wx.ITEM_NORMAL )
		self.m_menu_fold.Append( self.m_menuItem_texonly )

		self.m_menuItem_meshonly = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载 Mesh ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_fold.Append( self.m_menuItem_meshonly )

		self.m_menu_fold.AppendSeparator()

		self.m_menuItem_rgb_a = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载RGB && Alpha", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_fold.Append( self.m_menuItem_rgb_a )
		self.m_menuItem_rgb_a.Enable( False )

		self.m_menuItem_rgb_f = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载RGB", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_fold.Append( self.m_menuItem_rgb_f )
		self.m_menuItem_rgb_f.Enable( False )

		self.m_menuItem_alpha_f = wx.MenuItem( self.m_menu_fold, wx.ID_ANY, u"加载Alpha", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_fold.Append( self.m_menuItem_alpha_f )
		self.m_menuItem_alpha_f.Enable( False )

		self.menu_file.AppendSubMenu( self.m_menu_fold, u"加载文件夹" )

		self.menu_file.AppendSeparator()

		self.m_menuItem_exit = wx.MenuItem( self.menu_file, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.m_menuItem_exit )

		self.m_menubar2.Append( self.menu_file, u"文件" )

		self.m_menu_export = wx.Menu()
		self.m_menuItem_all = wx.MenuItem( self.m_menu_export, wx.ID_ANY, u"导出全部", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_export.Append( self.m_menuItem_all )
		self.m_menuItem_all.Enable( False )

		self.m_menuItem_choice = wx.MenuItem( self.m_menu_export, wx.ID_ANY, u"导出选择的文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_export.Append( self.m_menuItem_choice )
		self.m_menuItem_choice.Enable( False )

		self.m_menuItem_copy_only = wx.MenuItem( self.m_menu_export, wx.ID_ANY, u"把不符合条件的文件直接导出", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_export.Append( self.m_menuItem_copy_only )
		self.m_menuItem_copy_only.Enable( False )

		self.m_menuItem_flex = wx.MenuItem( self.m_menu_export, wx.ID_ANY, u"导出筛选项", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_export.Append( self.m_menuItem_flex )

		self.m_menubar2.Append( self.m_menu_export, u"导出" )

		self.m_menu_tool = wx.Menu()
		self.m_menuItem_parkage = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"打包导出文件", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menuItem_parkage )
		self.m_menuItem_parkage.Enable( False )

		self.m_menuItem_add = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"添加新的舰娘名", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menuItem_add )
		self.m_menuItem_add.Enable( False )

		self.m_menuItem_set_list = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"更改舰娘名", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menuItem_set_list )

		self.m_menuItem_new_file = wx.MenuItem( self.m_menu_tool, wx.ID_ANY, u"比较新增", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_tool.Append( self.m_menuItem_new_file )

		self.m_menubar2.Append( self.m_menu_tool, u"工具" )

		self.m_menu_game_type = wx.Menu()
		self.m_menuItem_azurlane = wx.MenuItem( self.m_menu_game_type, wx.ID_ANY, u"碧蓝航线", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menuItem_azurlane.SetBitmap( wx.NullBitmap )
		self.m_menu_game_type.Append( self.m_menuItem_azurlane )
		self.m_menuItem_azurlane.Check( True )

		self.m_menuItem_girl_line = wx.MenuItem( self.m_menu_game_type, wx.ID_ANY, u"少女前线", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu_game_type.Append( self.m_menuItem_girl_line )
		self.m_menuItem_girl_line.Enable( False )

		self.m_menubar2.Append( self.m_menu_game_type, u"游戏类型" )

		self.SetMenuBar( self.m_menubar2 )

		gSizer_main = wx.GridSizer( 0, 2, 0, 0 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_azur_lane = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_azur_lane.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		sbSizer_load_mesh = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_azur_lane, wx.ID_ANY, u"Mesh" ), wx.VERTICAL )

		gSizer_mesh = wx.GridSizer( 0, 2, 0, 0 )

		self.m_gauge_mesh_load = wx.Gauge( sbSizer_load_mesh.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_mesh_load.SetValue( 0 )
		gSizer_mesh.Add( self.m_gauge_mesh_load, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText_mesh_load = wx.StaticText( sbSizer_load_mesh.GetStaticBox(), wx.ID_ANY, u"无任务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_mesh_load.Wrap( -1 )

		gSizer_mesh.Add( self.m_staticText_mesh_load, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer_load_mesh.Add( gSizer_mesh, 0, 0, 5 )


		bSizer15.Add( sbSizer_load_mesh, 0, wx.EXPAND, 5 )

		sbSizer_load_tex = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_azur_lane, wx.ID_ANY, u"Texture2D" ), wx.VERTICAL )

		gSizer_tex = wx.GridSizer( 0, 2, 0, 0 )

		self.m_gauge_tex_load = wx.Gauge( sbSizer_load_tex.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_tex_load.SetValue( 0 )
		gSizer_tex.Add( self.m_gauge_tex_load, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText_load_tex = wx.StaticText( sbSizer_load_tex.GetStaticBox(), wx.ID_ANY, u"无任务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_load_tex.Wrap( -1 )

		gSizer_tex.Add( self.m_staticText_load_tex, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer_load_tex.Add( gSizer_tex, 0, 0, 5 )


		bSizer15.Add( sbSizer_load_tex, 0, wx.EXPAND, 5 )

		self.m_listbook2 = wx.Listbook( self.m_panel_azur_lane, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
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
		self.m_listbook2.AddPage( self.m_panel2, u"Texture\n", True )
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
		self.m_listbook2.AddPage( self.m_panel1, u"Mesh", False )

		bSizer15.Add( self.m_listbook2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_azur_lane.SetSizer( bSizer15 )
		self.m_panel_azur_lane.Layout()
		bSizer15.Fit( self.m_panel_azur_lane )
		bSizer2.Add( self.m_panel_azur_lane, 1, wx.EXPAND |wx.ALL, 5 )


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
		self.m_panel9 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow6 = wx.ScrolledWindow( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow6.SetScrollRate( 5, 5 )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_show = wx.StaticBitmap( self.m_scrolledWindow6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_bitmap_show, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow6.SetSizer( bSizer22 )
		self.m_scrolledWindow6.Layout()
		bSizer22.Fit( self.m_scrolledWindow6 )
		bSizer23.Add( self.m_scrolledWindow6, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline3 = wx.StaticLine( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_slider_scale = wx.Slider( self.m_panel9, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer23.Add( self.m_slider_scale, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel9.SetSizer( bSizer23 )
		self.m_panel9.Layout()
		bSizer23.Fit( self.m_panel9 )
		self.m_notebook1.AddPage( self.m_panel9, u"展示区", False )

		sbSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_now = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"当前：None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_now.Wrap( -1 )

		sbSizer3.Add( self.m_staticText_now, 0, wx.ALL, 5 )

		self.m_staticText_all = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"总进度：0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_all.Wrap( -1 )

		sbSizer3.Add( self.m_staticText_all, 0, wx.ALL, 5 )

		self.m_gauge_all = wx.Gauge( sbSizer3.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_all.SetValue( 0 )
		sbSizer3.Add( self.m_gauge_all, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer19 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_button_gui = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"教程", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_button_gui, 0, wx.ALL, 5 )

		self.m_button_help = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"帮助", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_button_help, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer3.Add( gSizer19, 0, wx.ALIGN_RIGHT, 5 )


		gSizer_main.Add( sbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer_main )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_DEFAULT_STYLE, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_press )
		self.Bind( wx.EVT_MENU, self.load_tex, id = self.m_menuItem_tex.GetId() )
		self.Bind( wx.EVT_MENU, self.load_Mesh, id = self.m_menuItem_mesh.GetId() )
		self.Bind( wx.EVT_MENU, self.load_rgb, id = self.m_menuItem_rgb.GetId() )
		self.Bind( wx.EVT_MENU, self.load_alpha, id = self.m_menuItem_alpha.GetId() )
		self.Bind( wx.EVT_MENU, self.load_tex_and_mesh, id = self.m_menuItem_mix.GetId() )
		self.Bind( wx.EVT_MENU, self.load_tex_fold, id = self.m_menuItem_texonly.GetId() )
		self.Bind( wx.EVT_MENU, self.load_mesh_fold, id = self.m_menuItem_meshonly.GetId() )
		self.Bind( wx.EVT_MENU, self.load_rgb_alpha_fold, id = self.m_menuItem_rgb_a.GetId() )
		self.Bind( wx.EVT_MENU, self.load_RGB_fold, id = self.m_menuItem_rgb_f.GetId() )
		self.Bind( wx.EVT_MENU, self.load_alpha_fold, id = self.m_menuItem_alpha_f.GetId() )
		self.Bind( wx.EVT_MENU, self.exit_press, id = self.m_menuItem_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.export_all, id = self.m_menuItem_all.GetId() )
		self.Bind( wx.EVT_MENU, self.export_choice, id = self.m_menuItem_choice.GetId() )
		self.Bind( wx.EVT_MENU, self.copy_file, id = self.m_menuItem_copy_only.GetId() )
		self.Bind( wx.EVT_MENU, self.zip_pack, id = self.m_menuItem_parkage.GetId() )
		self.Bind( wx.EVT_MENU, self.add_new, id = self.m_menuItem_add.GetId() )
		self.Bind( wx.EVT_MENU, self.change_name, id = self.m_menuItem_set_list.GetId() )
		self.Bind( wx.EVT_MENU, self.compare, id = self.m_menuItem_new_file.GetId() )
		self.Bind( wx.EVT_MENU, self.azurlane_type, id = self.m_menuItem_azurlane.GetId() )
		self.Bind( wx.EVT_MENU, self.girl_line_type, id = self.m_menuItem_girl_line.GetId() )
		self.m_searchCtrl_tex.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_tex )
		self.m_listBox_tex.Bind( wx.EVT_LISTBOX_DCLICK, self.tex_choice )
		self.m_searchCtrl_mesh.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_mesh )
		self.m_listBox_mesh.Bind( wx.EVT_LISTBOX_DCLICK, self.mesh_choice )
		self.m_searchCtrl_pass.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_pass )
		self.m_listBox_info.Bind( wx.EVT_LISTBOX_DCLICK, self.open_pass )
		self.m_searchCtrl_unable.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_unable )
		self.m_listBox_unable.Bind( wx.EVT_LISTBOX_DCLICK, self.open_file )
		self.m_slider_scale.Bind( wx.EVT_COMMAND_SCROLL_CHANGED, self.change_size )
		self.m_button_help.Bind( wx.EVT_BUTTON, self.helper )
		self.m_button5.Bind( wx.EVT_BUTTON, self.setting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close_press( self, event ):
		event.Skip()

	def load_tex( self, event ):
		event.Skip()

	def load_Mesh( self, event ):
		event.Skip()

	def load_rgb( self, event ):
		event.Skip()

	def load_alpha( self, event ):
		event.Skip()

	def load_tex_and_mesh( self, event ):
		event.Skip()

	def load_tex_fold( self, event ):
		event.Skip()

	def load_mesh_fold( self, event ):
		event.Skip()

	def load_rgb_alpha_fold( self, event ):
		event.Skip()

	def load_RGB_fold( self, event ):
		event.Skip()

	def load_alpha_fold( self, event ):
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

	def azurlane_type( self, event ):
		event.Skip()

	def girl_line_type( self, event ):
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

	def change_size( self, event ):
		event.Skip()

	def helper( self, event ):
		event.Skip()

	def setting( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame_pattern
###########################################################################

class MyFrame_pattern ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer17 = wx.GridSizer( 0, 2, 0, 0 )

		m_listBox_infoChoices = []
		self.m_listBox_info = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_infoChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		gSizer17.Add( self.m_listBox_info, 1, wx.ALL|wx.EXPAND, 5 )

		m_listBox_info2Choices = []
		self.m_listBox_info2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_info2Choices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		gSizer17.Add( self.m_listBox_info2, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog_change_name
###########################################################################

class MyDialog_change_name ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 427,496 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_searchCtrl2 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl2.ShowSearchButton( True )
		self.m_searchCtrl2.ShowCancelButton( True )
		bSizer11.Add( self.m_searchCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox7Choices = []
		self.m_listBox7 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox7Choices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
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

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

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

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

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

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

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
## Class MyDialog_Setting
###########################################################################

class MyDialog_Setting ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 1000,500 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.m_scrolledWindow4 = wx.ScrolledWindow( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow4.SetScrollRate( 5, 5 )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self.m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"files/bg_story_litang.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_scrolledWindow4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer28.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		gSizer23 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_hyperlink4 = wx.adv.HyperlinkCtrl( self.m_scrolledWindow4, wx.ID_ANY, u"作者的bilibili账号", u"https://space.bilibili.com/14435736/", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer23.Add( self.m_hyperlink4, 0, wx.ALL, 5 )

		self.m_hyperlink5 = wx.adv.HyperlinkCtrl( self.m_scrolledWindow4, wx.ID_ANY, u"作者的GitHub", u"https://github.com/Goodjooy", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer23.Add( self.m_hyperlink5, 0, wx.ALL, 5 )


		bSizer23.Add( gSizer23, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		bSizer28.Add( bSizer23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_scrolledWindow4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer28.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow4.SetSizer( bSizer28 )
		self.m_scrolledWindow4.Layout()
		bSizer28.Fit( self.m_scrolledWindow4 )
		self.m_notebook3.AddPage( self.m_scrolledWindow4, u"欢迎", False )
		self.m_scrolledWindow7 = wx.ScrolledWindow( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow7.SetScrollRate( 5, 5 )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow7, wx.ID_ANY, u"碧蓝航线" ), wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Texture2D文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		sbSizer10.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_dirPicker_az_tex_dir = wx.DirPickerCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, u"QAQ", u"设置默认文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer10.Add( self.m_dirPicker_az_tex_dir, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Mesh文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		sbSizer10.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_dirPicker_az_mesh_dir = wx.DirPickerCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, u"QAQ", u"设置默认文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer10.Add( self.m_dirPicker_az_mesh_dir, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( sbSizer10, 0, wx.EXPAND, 5 )

		self.m_staticText18 = wx.StaticText( self.m_scrolledWindow7, wx.ID_ANY, u"导出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer22.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_dirPicker_export = wx.DirPickerCtrl( self.m_scrolledWindow7, wx.ID_ANY, u"QAQ", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer22.Add( self.m_dirPicker_export, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_toggleBtn_lock = wx.ToggleButton( self.m_scrolledWindow7, wx.ID_ANY, u"锁定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_toggleBtn_lock, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_scrolledWindow7.SetSizer( bSizer22 )
		self.m_scrolledWindow7.Layout()
		bSizer22.Fit( self.m_scrolledWindow7 )
		self.m_notebook3.AddPage( self.m_scrolledWindow7, u"默认地址", False )
		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		gSizer14 = wx.GridSizer( 0, 3, 0, 0 )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"设置" ), wx.VERTICAL )

		m_radioBox_type_useChoices = [ u"使用预设的分类方案", u"使用-自定义-分类方案" ]
		self.m_radioBox_type_use = wx.RadioBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"分类方案", wx.DefaultPosition, wx.DefaultSize, m_radioBox_type_useChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_type_use.SetSelection( 0 )
		sbSizer8.Add( self.m_radioBox_type_use, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_in_cn = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"以中文名导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_in_cn.SetValue(True)
		sbSizer8.Add( self.m_checkBox_in_cn, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_az_dir = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"在导出文件夹内新建导出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_az_dir.SetValue(True)
		sbSizer8.Add( self.m_checkBox_az_dir, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer8.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkBox_autoopen = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"完成后打开相应文件\\文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_checkBox_autoopen, 0, wx.ALL, 5 )

		self.m_checkBox_pass_finished = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"跳过已还原的", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_checkBox_pass_finished, 0, wx.ALL, 5 )

		self.m_checkBox_open_temp = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"自动打开选择的还原后图片", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_checkBox_open_temp, 0, wx.ALL, 5 )

		self.m_checkBox4_finish_exit = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"完成全部后退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_checkBox4_finish_exit, 0, wx.ALL, 5 )


		gSizer14.Add( sbSizer8, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"预设方案" ), wx.VERTICAL )

		m_radioBox_az_divChoices = [ u"不分类", u"按舰娘名分类", u"按-皮肤-婚纱-原始皮肤分类" ]
		self.m_radioBox_az_div = wx.RadioBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"分类设置", wx.DefaultPosition, wx.DefaultSize, m_radioBox_az_divChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_az_div.SetSelection( 2 )
		sbSizer9.Add( self.m_radioBox_az_div, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox_az_typeChoices = [ u"仅导出可还原立绘", u"导出全部（包括不可还原）" ]
		self.m_radioBox_az_type = wx.RadioBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"导出立绘类型", wx.DefaultPosition, wx.DefaultSize, m_radioBox_az_typeChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_az_type.SetSelection( 1 )
		sbSizer9.Add( self.m_radioBox_az_type, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer14.Add( sbSizer9, 1, wx.EXPAND, 5 )

		sbSizer101 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"自定义方案" ), wx.VERTICAL )

		self.m_staticText15 = wx.StaticText( sbSizer101.GetStaticBox(), wx.ID_ANY, u"导入texture2D-限制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		sbSizer101.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl_tex_limit = wx.TextCtrl( sbSizer101.GetStaticBox(), wx.ID_ANY, u".+\\.[p,P][N,n][G,g]", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer101.Add( self.m_textCtrl_tex_limit, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText161 = wx.StaticText( sbSizer101.GetStaticBox(), wx.ID_ANY, u"导入mesh-限制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		sbSizer101.Add( self.m_staticText161, 0, wx.ALL, 5 )

		self.m_textCtrl_mesh_limit = wx.TextCtrl( sbSizer101.GetStaticBox(), wx.ID_ANY, u".+-mesh\\.[o,O][B,b][J,j]", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer101.Add( self.m_textCtrl_mesh_limit, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer16 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText171 = wx.StaticText( sbSizer101.GetStaticBox(), wx.ID_ANY, u"导出分类", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		gSizer16.Add( self.m_staticText171, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button_add = wx.Button( sbSizer101.GetStaticBox(), wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_button_add, 0, wx.ALL, 5 )

		self.m_button_del = wx.Button( sbSizer101.GetStaticBox(), wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_button_del, 0, wx.ALL, 5 )


		sbSizer101.Add( gSizer16, 0, wx.EXPAND, 5 )

		m_checkList_az_limitsChoices = [u"其他"]
		self.m_checkList_az_limits = wx.CheckListBox( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList_az_limitsChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_SINGLE )
		sbSizer101.Add( self.m_checkList_az_limits, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer14.Add( sbSizer101, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow2.SetSizer( gSizer14 )
		self.m_scrolledWindow2.Layout()
		gSizer14.Fit( self.m_scrolledWindow2 )
		self.m_notebook3.AddPage( self.m_scrolledWindow2, u"设置-碧蓝航线", False )
		self.m_scrolledWindow71 = wx.ScrolledWindow( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow71.SetScrollRate( 5, 5 )
		self.m_notebook3.AddPage( self.m_scrolledWindow71, u"正则表达式", False )

		bSizer19.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Apply )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();

		bSizer19.Add( m_sdbSizer4, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.show_choice )
		self.m_toggleBtn_lock.Bind( wx.EVT_TOGGLEBUTTON, self.lock_address )
		self.m_radioBox_type_use.Bind( wx.EVT_RADIOBOX, self.change_type )
		self.m_checkBox_az_dir.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_autoopen.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_pass_finished.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_open_temp.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox4_finish_exit.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_radioBox_az_div.Bind( wx.EVT_RADIOBOX, self.change_div )
		self.m_radioBox_az_type.Bind( wx.EVT_RADIOBOX, self.change )
		self.m_textCtrl_tex_limit.Bind( wx.EVT_TEXT_ENTER, self.change )
		self.m_textCtrl_mesh_limit.Bind( wx.EVT_TEXT_ENTER, self.change )
		self.m_button_add.Bind( wx.EVT_BUTTON, self.az_add )
		self.m_button_del.Bind( wx.EVT_BUTTON, self.az_del )
		self.m_checkList_az_limits.Bind( wx.EVT_LISTBOX, self.choice )
		self.m_checkList_az_limits.Bind( wx.EVT_LISTBOX_DCLICK, self.change_pattern )
		self.m_sdbSizer4Apply.Bind( wx.EVT_BUTTON, self.apply_click )
		self.m_sdbSizer4Cancel.Bind( wx.EVT_BUTTON, self.cancel_click )
		self.m_sdbSizer4OK.Bind( wx.EVT_BUTTON, self.ok_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def show_choice( self, event ):
		event.Skip()

	def lock_address( self, event ):
		event.Skip()

	def change_type( self, event ):
		event.Skip()

	def change( self, event ):
		event.Skip()





	def change_div( self, event ):
		event.Skip()




	def az_add( self, event ):
		event.Skip()

	def az_del( self, event ):
		event.Skip()

	def choice( self, event ):
		event.Skip()

	def change_pattern( self, event ):
		event.Skip()

	def apply_click( self, event ):
		event.Skip()

	def cancel_click( self, event ):
		event.Skip()

	def ok_click( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog7
###########################################################################

class MyDialog7 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer241 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox_gfl_exChoices = [ u"导出全部", u"仅导出人物立绘（pic打头）" ]
		self.m_radioBox_gfl_ex = wx.RadioBox( self.m_scrolledWindow3, wx.ID_ANY, u"导出设置", wx.DefaultPosition, wx.DefaultSize, m_radioBox_gfl_exChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_gfl_ex.SetSelection( 0 )
		bSizer241.Add( self.m_radioBox_gfl_ex, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox_gfl_divChoices = [ u"不分类", u"按人形名分类", u"按是否大破分类" ]
		self.m_radioBox_gfl_div = wx.RadioBox( self.m_scrolledWindow3, wx.ID_ANY, u"分类设置", wx.DefaultPosition, wx.DefaultSize, m_radioBox_gfl_divChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_gfl_div.SetSelection( 0 )
		bSizer241.Add( self.m_radioBox_gfl_div, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_check = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"开始前先进行检查", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_check.SetValue(True)
		bSizer241.Add( self.m_checkBox_check, 0, wx.ALL, 5 )

		self.m_checkBox_gfl_dir = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"在导出文件夹内新建导出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_gfl_dir.SetValue(True)
		bSizer241.Add( self.m_checkBox_gfl_dir, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow3.SetSizer( bSizer241 )
		self.m_scrolledWindow3.Layout()
		bSizer241.Fit( self.m_scrolledWindow3 )
		bSizer24.Add( self.m_scrolledWindow3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_girls_font_line = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_girls_font_line.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		sbSizer_load_rgb = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_girls_font_line, wx.ID_ANY, u"RGB" ), wx.VERTICAL )

		gSizer_rgb = wx.GridSizer( 0, 2, 0, 0 )

		self.m_gauge_RGB_load = wx.Gauge( sbSizer_load_rgb.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_RGB_load.SetValue( 0 )
		gSizer_rgb.Add( self.m_gauge_RGB_load, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText_RGB_load = wx.StaticText( sbSizer_load_rgb.GetStaticBox(), wx.ID_ANY, u"无任务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_RGB_load.Wrap( -1 )

		gSizer_rgb.Add( self.m_staticText_RGB_load, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer_load_rgb.Add( gSizer_rgb, 0, 0, 5 )


		bSizer151.Add( sbSizer_load_rgb, 0, wx.EXPAND, 5 )

		sbSizer_load_alpha = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_girls_font_line, wx.ID_ANY, u"Alpha" ), wx.VERTICAL )

		gSizer_tex1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_gauge_alpha_load = wx.Gauge( sbSizer_load_alpha.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_alpha_load.SetValue( 0 )
		gSizer_tex1.Add( self.m_gauge_alpha_load, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText_alpha_load = wx.StaticText( sbSizer_load_alpha.GetStaticBox(), wx.ID_ANY, u"无任务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_alpha_load.Wrap( -1 )

		gSizer_tex1.Add( self.m_staticText_alpha_load, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer_load_alpha.Add( gSizer_tex1, 0, 0, 5 )


		bSizer151.Add( sbSizer_load_alpha, 0, wx.EXPAND, 5 )

		self.m_listbook21 = wx.Listbook( self.m_panel_girls_font_line, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel21 = wx.Panel( self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer73 = wx.BoxSizer( wx.VERTICAL )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_searchCtrl_RGB = wx.SearchCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_RGB.ShowSearchButton( True )
		self.m_searchCtrl_RGB.ShowCancelButton( True )
		gSizer10.Add( self.m_searchCtrl_RGB, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice_rgbChoices = [ u"全部" ]
		self.m_choice_rgb = wx.Choice( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_rgbChoices, 0 )
		self.m_choice_rgb.SetSelection( 0 )
		gSizer10.Add( self.m_choice_rgb, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer73.Add( gSizer10, 0, wx.EXPAND, 5 )

		m_listBox_RGBChoices = []
		self.m_listBox_RGB = wx.ListBox( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_RGBChoices, 0 )
		bSizer73.Add( self.m_listBox_RGB, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel21.SetSizer( bSizer73 )
		self.m_panel21.Layout()
		bSizer73.Fit( self.m_panel21 )
		self.m_listbook21.AddPage( self.m_panel21, u"RGB file", False )
		self.m_panel11 = wx.Panel( self.m_listbook21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer711 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_searchCtrl_alpha = wx.SearchCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_alpha.ShowSearchButton( True )
		self.m_searchCtrl_alpha.ShowCancelButton( True )
		gSizer11.Add( self.m_searchCtrl_alpha, 0, wx.ALL|wx.EXPAND, 5 )

		m_choice_alphaChoices = [ u"全部" ]
		self.m_choice_alpha = wx.Choice( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_alphaChoices, 0 )
		self.m_choice_alpha.SetSelection( 0 )
		gSizer11.Add( self.m_choice_alpha, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer711.Add( gSizer11, 0, wx.EXPAND, 5 )

		m_listBox_alphaChoices = []
		self.m_listBox_alpha = wx.ListBox( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_alphaChoices, 0 )
		bSizer711.Add( self.m_listBox_alpha, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel11.SetSizer( bSizer711 )
		self.m_panel11.Layout()
		bSizer711.Fit( self.m_panel11 )
		self.m_listbook21.AddPage( self.m_panel11, u"Alpha file", True )

		bSizer151.Add( self.m_listbook21, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_girls_font_line.SetSizer( bSizer151 )
		self.m_panel_girls_font_line.Layout()
		bSizer151.Fit( self.m_panel_girls_font_line )
		bSizer24.Add( self.m_panel_girls_font_line, 1, wx.EXPAND |wx.ALL, 5 )

		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"少女前线" ), wx.VERTICAL )

		self.m_staticText16 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, u"RGB文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		sbSizer111.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_dirPicker_gl_rbg_dir = wx.DirPickerCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, u"QAQ", u"设置默认文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer111.Add( self.m_dirPicker_gl_rbg_dir, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( sbSizer111.GetStaticBox(), wx.ID_ANY, u"Alpha文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		sbSizer111.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_dirPicker_gl_alpha_dir = wx.DirPickerCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, u"QAQ", u"设置默认文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer111.Add( self.m_dirPicker_gl_alpha_dir, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer24.Add( sbSizer111, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer24 )
		self.Layout()
		bSizer24.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_radioBox_gfl_ex.Bind( wx.EVT_RADIOBOX, self.change )
		self.m_radioBox_gfl_div.Bind( wx.EVT_RADIOBOX, self.change )
		self.m_checkBox_gfl_dir.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_searchCtrl_RGB.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.cancel )
		self.m_searchCtrl_RGB.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_rgb )
		self.m_listBox_RGB.Bind( wx.EVT_LISTBOX_DCLICK, self.rgb_choice )
		self.m_searchCtrl_alpha.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_alpha )
		self.m_listBox_alpha.Bind( wx.EVT_LISTBOX_DCLICK, self.alpha_choice )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def change( self, event ):
		event.Skip()



	def cancel( self, event ):
		event.Skip()

	def search_rgb( self, event ):
		event.Skip()

	def rgb_choice( self, event ):
		event.Skip()

	def search_alpha( self, event ):
		event.Skip()

	def alpha_choice( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_limit
###########################################################################

class MyDialog_limit ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"添加分类", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer171 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"分类名称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gSizer171.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gSizer171.Add( self.m_textCtrl_name, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"分类文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		gSizer171.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_textCtrl_dir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer171.Add( self.m_textCtrl_dir, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"分类限制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		gSizer171.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_textCtrl_limit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer171.Add( self.m_textCtrl_limit, 0, wx.ALL, 5 )


		bSizer25.Add( gSizer171, 1, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_index = wx.StaticText( self, wx.ID_ANY, u"编号：-1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText_index.Wrap( -1 )

		bSizer27.Add( self.m_staticText_index, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )

		m_sdbSizer5 = wx.StdDialogButtonSizer()
		self.m_sdbSizer5OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer5.AddButton( self.m_sdbSizer5OK )
		self.m_sdbSizer5Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Cancel )
		m_sdbSizer5.Realize();

		bSizer27.Add( m_sdbSizer5, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		bSizer25.Add( bSizer27, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		self.SetSizer( bSizer25 )
		self.Layout()
		bSizer25.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.exit_return )
		self.m_textCtrl_name.Bind( wx.EVT_TEXT, self.check_ok )
		self.m_textCtrl_name.Bind( wx.EVT_TEXT_ENTER, self.check_ok )
		self.m_textCtrl_dir.Bind( wx.EVT_TEXT, self.check_ok )
		self.m_textCtrl_dir.Bind( wx.EVT_TEXT_ENTER, self.check_ok )
		self.m_textCtrl_limit.Bind( wx.EVT_TEXT, self.check_ok )
		self.m_textCtrl_limit.Bind( wx.EVT_TEXT_ENTER, self.check_ok )
		self.m_sdbSizer5OK.Bind( wx.EVT_BUTTON, self.save_exit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exit_return( self, event ):
		event.Skip()

	def check_ok( self, event ):
		event.Skip()






	def save_exit( self, event ):
		event.Skip()


