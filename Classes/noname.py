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

		self.m_menu_search = wx.Menu()
		self.m_menuItem_tex_search = wx.MenuItem( self.m_menu_search, wx.ID_ANY, u"Texture结果", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_search.Append( self.m_menuItem_tex_search )
		self.m_menuItem_tex_search.Enable( False )

		self.m_menuItem_mesh_search = wx.MenuItem( self.m_menu_search, wx.ID_ANY, u"Mesh结果", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_search.Append( self.m_menuItem_mesh_search )
		self.m_menuItem_mesh_search.Enable( False )

		self.m_menuItem_unable_search = wx.MenuItem( self.m_menu_search, wx.ID_ANY, u"不符合条件结果", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_search.Append( self.m_menuItem_unable_search )
		self.m_menuItem_unable_search.Enable( False )

		self.m_menu_export.AppendSubMenu( self.m_menu_search, u"导出搜索结果" )

		self.m_menubar2.Append( self.m_menu_export, u"导出" )

		self.SetMenuBar( self.m_menubar2 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_simplebook_input = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel12 = wx.Panel( self.m_simplebook_input, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton_quick = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_quick.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_BUTTON ) )
		self.m_bpButton_quick.SetBitmapPressed( wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_BUTTON ) )
		self.m_bpButton_quick.SetBitmapCurrent( wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_BUTTON ) )
		self.m_bpButton_quick.SetBitmapPosition( wx.LEFT )
		bSizer40.Add( self.m_bpButton_quick, 0, wx.ALL, 5 )

		self.m_staticText_qiuke = wx.StaticText( self.m_panel12, wx.ID_ANY, u"快速导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_qiuke.Wrap( -1 )

		bSizer40.Add( self.m_staticText_qiuke, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_gauge_quick = wx.Gauge( self.m_panel12, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_quick.SetValue( 0 )
		bSizer40.Add( self.m_gauge_quick, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer15.Add( bSizer40, 0, wx.EXPAND, 5 )

		sbSizer_load_mesh = wx.StaticBoxSizer( wx.StaticBox( self.m_panel12, wx.ID_ANY, u"Mesh" ), wx.HORIZONTAL )

		self.m_gauge_mesh_load = wx.Gauge( sbSizer_load_mesh.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_mesh_load.SetValue( 0 )
		sbSizer_load_mesh.Add( self.m_gauge_mesh_load, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline12 = wx.StaticLine( sbSizer_load_mesh.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer_load_mesh.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_mesh_load = wx.StaticText( sbSizer_load_mesh.GetStaticBox(), wx.ID_ANY, u"无任务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_mesh_load.Wrap( -1 )

		sbSizer_load_mesh.Add( self.m_staticText_mesh_load, 1, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer15.Add( sbSizer_load_mesh, 0, wx.EXPAND, 5 )

		sbSizer_load_tex = wx.StaticBoxSizer( wx.StaticBox( self.m_panel12, wx.ID_ANY, u"Texture2D" ), wx.HORIZONTAL )

		self.m_gauge_tex_load = wx.Gauge( sbSizer_load_tex.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_tex_load.SetValue( 0 )
		sbSizer_load_tex.Add( self.m_gauge_tex_load, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline14 = wx.StaticLine( sbSizer_load_tex.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer_load_tex.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_load_tex = wx.StaticText( sbSizer_load_tex.GetStaticBox(), wx.ID_ANY, u"无任务", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_load_tex.Wrap( -1 )

		sbSizer_load_tex.Add( self.m_staticText_load_tex, 1, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer15.Add( sbSizer_load_tex, 0, wx.EXPAND, 5 )

		self.m_listbook_in = wx.Listbook( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel2 = wx.Panel( self.m_listbook_in, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer56 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_searchCtrl_tex = wx.SearchCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_tex.ShowSearchButton( True )
		self.m_searchCtrl_tex.ShowCancelButton( True )
		bSizer56.Add( self.m_searchCtrl_tex, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline16 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer56.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )

		m_choice11Choices = [ u"全部", u"有中文名", u"无中文名" ]
		self.m_choice11 = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		bSizer56.Add( self.m_choice11, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer56, 0, wx.EXPAND, 5 )

		m_listBox_texChoices = []
		self.m_listBox_tex = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_texChoices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL )
		bSizer7.Add( self.m_listBox_tex, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer7 )
		self.m_panel2.Layout()
		bSizer7.Fit( self.m_panel2 )
		self.m_listbook_in.AddPage( self.m_panel2, u"Texture\n", False )
		self.m_panel1 = wx.Panel( self.m_listbook_in, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_searchCtrl_mesh = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl_mesh.ShowSearchButton( True )
		self.m_searchCtrl_mesh.ShowCancelButton( True )
		bSizer57.Add( self.m_searchCtrl_mesh, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline17 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer57.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )

		m_choice12Choices = [ u"全部", u"有中文名", u"无中文名" ]
		self.m_choice12 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice12Choices, 0 )
		self.m_choice12.SetSelection( 0 )
		bSizer57.Add( self.m_choice12, 0, wx.ALL, 5 )


		bSizer71.Add( bSizer57, 0, wx.EXPAND, 5 )

		m_listBox_meshChoices = []
		self.m_listBox_mesh = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_meshChoices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL )
		bSizer71.Add( self.m_listBox_mesh, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer71 )
		self.m_panel1.Layout()
		bSizer71.Fit( self.m_panel1 )
		self.m_listbook_in.AddPage( self.m_panel1, u"Mesh", True )

		bSizer15.Add( self.m_listbook_in, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel12.SetSizer( bSizer15 )
		self.m_panel12.Layout()
		bSizer15.Fit( self.m_panel12 )
		self.m_simplebook_input.AddPage( self.m_panel12, u"a page", False )
		self.m_panel_char = wx.Panel( self.m_simplebook_input, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_char, wx.ID_ANY, u"spine小人提取（仅分割）(测试)" ), wx.VERTICAL )

		sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( sbSizer17.GetStaticBox(), wx.ID_ANY, u"tex" ), wx.HORIZONTAL )

		self.m_bpButton_body = wx.BitmapButton( sbSizer18.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_body.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_BUTTON ) )
		self.m_bpButton_body.SetBitmapCurrent( wx.NullBitmap )
		sbSizer18.Add( self.m_bpButton_body, 0, wx.ALL, 5 )

		self.m_gauge7 = wx.Gauge( sbSizer18.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge7.SetValue( 0 )
		sbSizer18.Add( self.m_gauge7, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer17.Add( sbSizer18, 0, wx.EXPAND, 5 )

		sbSizer19 = wx.StaticBoxSizer( wx.StaticBox( sbSizer17.GetStaticBox(), wx.ID_ANY, u"altex" ), wx.HORIZONTAL )

		self.m_bpButton_cut_way = wx.BitmapButton( sbSizer19.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_cut_way.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_BUTTON ) )
		sbSizer19.Add( self.m_bpButton_cut_way, 0, wx.ALL, 5 )

		self.m_gauge8 = wx.Gauge( sbSizer19.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge8.SetValue( 0 )
		sbSizer19.Add( self.m_gauge8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer17.Add( sbSizer19, 0, wx.EXPAND, 5 )

		sbSizer181 = wx.StaticBoxSizer( wx.StaticBox( sbSizer17.GetStaticBox(), wx.ID_ANY, u"导出" ), wx.HORIZONTAL )

		self.m_bpButton_ex_spine = wx.BitmapButton( sbSizer181.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_ex_spine.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_BUTTON ) )
		self.m_bpButton_ex_spine.SetBitmapCurrent( wx.NullBitmap )
		sbSizer181.Add( self.m_bpButton_ex_spine, 0, wx.ALL, 5 )

		self.m_gauge_ex_spine = wx.Gauge( sbSizer181.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_ex_spine.SetValue( 0 )
		sbSizer181.Add( self.m_gauge_ex_spine, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer17.Add( sbSizer181, 0, wx.EXPAND, 5 )

		self.m_staticline6 = wx.StaticLine( sbSizer17.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer17.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_treeCtrl_boys = wx.TreeCtrl( sbSizer17.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		sbSizer17.Add( self.m_treeCtrl_boys, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button16 = wx.Button( sbSizer17.GetStaticBox(), wx.ID_ANY, u"重置", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer17.Add( self.m_button16, 0, wx.ALL, 5 )


		self.m_panel_char.SetSizer( sbSizer17 )
		self.m_panel_char.Layout()
		sbSizer17.Fit( self.m_panel_char )
		self.m_simplebook_input.AddPage( self.m_panel_char, u"a page", False )

		bSizer28.Add( self.m_simplebook_input, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer28.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer47 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_info = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.m_panel24 = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		m_listBox_logChoices = []
		self.m_listBox_log = wx.ListBox( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_logChoices, 0 )
		bSizer45.Add( self.m_listBox_log, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel24.SetSizer( bSizer45 )
		self.m_panel24.Layout()
		bSizer45.Fit( self.m_panel24 )
		self.m_notebook_info.AddPage( self.m_panel24, u"日志", False )
		self.m_panel10 = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_show = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_bitmap_show, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel10.SetSizer( bSizer22 )
		self.m_panel10.Layout()
		bSizer22.Fit( self.m_panel10 )
		self.m_notebook_info.AddPage( self.m_panel10, u"展示区", False )
		self.m_panel25 = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		m_listBox_errorsChoices = []
		self.m_listBox_errors = wx.ListBox( self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_errorsChoices, 0 )
		bSizer46.Add( self.m_listBox_errors, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel25.SetSizer( bSizer46 )
		self.m_panel25.Layout()
		bSizer46.Fit( self.m_panel25 )
		self.m_notebook_info.AddPage( self.m_panel25, u"错误列表", False )
		self.m_panel3 = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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

		m_listBox_skipChoices = []
		self.m_listBox_skip = wx.ListBox( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_skipChoices, 0 )
		bSizer6.Add( self.m_listBox_skip, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer6 )
		self.m_panel3.Layout()
		bSizer6.Fit( self.m_panel3 )
		self.m_notebook_info.AddPage( self.m_panel3, u"跳过文件信息", True )
		self.m_panel4 = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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
		self.m_notebook_info.AddPage( self.m_panel4, u"不符合", False )
		self.m_panel_else = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText23 = wx.StaticText( self.m_panel_else, wx.ID_ANY, u"好奇心总是会让人去点这个按钮\n→", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "@微软雅黑" ) )

		bSizer26.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self.m_panel_else, wx.ID_ANY, u"点我呀", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel_else.SetSizer( bSizer26 )
		self.m_panel_else.Layout()
		bSizer26.Fit( self.m_panel_else )
		self.m_notebook_info.AddPage( self.m_panel_else, u"其他", False )

		bSizer47.Add( self.m_notebook_info, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_gauge_all = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_all.SetValue( 0 )
		bSizer47.Add( self.m_gauge_all, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText_now = wx.StaticText( self, wx.ID_ANY, u"当前：None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_now.Wrap( -1 )

		bSizer47.Add( self.m_staticText_now, 0, wx.ALL, 5 )

		self.m_staticText_all = wx.StaticText( self, wx.ID_ANY, u"总进度：0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_all.Wrap( -1 )

		bSizer47.Add( self.m_staticText_all, 0, wx.ALL, 5 )

		gSizer19 = wx.GridSizer( 0, 4, 0, 0 )

		m_choice_typeChoices = [ u"立绘提取", u"spine提取", u"live2D" ]
		self.m_choice_type = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_typeChoices, 0 )
		self.m_choice_type.SetSelection( 0 )
		gSizer19.Add( self.m_choice_type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button_gui = wx.Button( self, wx.ID_ANY, u"教程", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_button_gui, 0, wx.ALL, 5 )

		self.m_button_help = wx.Button( self, wx.ID_ANY, u"帮助", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_button_help, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer47.Add( gSizer19, 0, wx.ALIGN_RIGHT, 5 )


		bSizer28.Add( bSizer47, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer28 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_DEFAULT_STYLE|wx.STB_SIZEGRIP, wx.ID_ANY )

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
		self.Bind( wx.EVT_MENU, self.tex_search_ex, id = self.m_menuItem_tex_search.GetId() )
		self.Bind( wx.EVT_MENU, self.mesh_search_ex, id = self.m_menuItem_mesh_search.GetId() )
		self.Bind( wx.EVT_MENU, self.unable_search_ex, id = self.m_menuItem_unable_search.GetId() )
		self.m_bpButton_quick.Bind( wx.EVT_BUTTON, self.quick_work )
		self.m_searchCtrl_tex.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_tex )
		self.m_searchCtrl_tex.Bind( wx.EVT_TEXT, self.search_tex )
		self.m_listBox_tex.Bind( wx.EVT_LISTBOX, self.tex_choice )
		self.m_listBox_tex.Bind( wx.EVT_LISTBOX_DCLICK, self.tex_choice )
		self.m_searchCtrl_mesh.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_mesh )
		self.m_searchCtrl_mesh.Bind( wx.EVT_TEXT, self.search_mesh )
		self.m_listBox_mesh.Bind( wx.EVT_LISTBOX, self.mesh_choice )
		self.m_listBox_mesh.Bind( wx.EVT_LISTBOX_DCLICK, self.mesh_choice )
		self.m_bpButton_body.Bind( wx.EVT_BUTTON, self.load_body )
		self.m_bpButton_cut_way.Bind( wx.EVT_BUTTON, self.load_cut )
		self.m_bpButton_ex_spine.Bind( wx.EVT_BUTTON, self.export_pic )
		self.m_treeCtrl_boys.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.open_pic )
		self.m_button16.Bind( wx.EVT_BUTTON, self.reset_spine )
		self.m_searchCtrl_pass.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_pass )
		self.m_listBox_skip.Bind( wx.EVT_LISTBOX_DCLICK, self.open_pass )
		self.m_searchCtrl_unable.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search_unable )
		self.m_listBox_unable.Bind( wx.EVT_LISTBOX_DCLICK, self.open_file )
		self.m_button4.Bind( wx.EVT_BUTTON, self.show_gl_win )
		self.m_choice_type.Bind( wx.EVT_CHOICE, self.change_type )
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

	def tex_search_ex( self, event ):
		event.Skip()

	def mesh_search_ex( self, event ):
		event.Skip()

	def unable_search_ex( self, event ):
		event.Skip()

	def quick_work( self, event ):
		event.Skip()

	def search_tex( self, event ):
		event.Skip()


	def tex_choice( self, event ):
		event.Skip()


	def search_mesh( self, event ):
		event.Skip()


	def mesh_choice( self, event ):
		event.Skip()


	def load_body( self, event ):
		event.Skip()

	def load_cut( self, event ):
		event.Skip()

	def export_pic( self, event ):
		event.Skip()

	def open_pic( self, event ):
		event.Skip()

	def reset_spine( self, event ):
		event.Skip()

	def search_pass( self, event ):
		event.Skip()

	def open_pass( self, event ):
		event.Skip()

	def search_unable( self, event ):
		event.Skip()

	def open_file( self, event ):
		event.Skip()

	def show_gl_win( self, event ):
		event.Skip()

	def change_type( self, event ):
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
## Class MyDialogQuick
###########################################################################

class MyDialogQuick ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"快速导出", pos = wx.DefaultPosition, size = wx.Size( 491,191 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.m_panel25 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer492 = wx.BoxSizer( wx.VERTICAL )

		m_choice_im_typeChoices = [ u"Texture2D", u"Mesh", u"Both" ]
		self.m_choice_im_type = wx.Choice( self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_im_typeChoices, 0 )
		self.m_choice_im_type.SetSelection( 0 )
		bSizer492.Add( self.m_choice_im_type, 0, wx.ALL, 5 )

		self.m_button171 = wx.Button( self.m_panel25, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer492.Add( self.m_button171, 0, wx.ALL, 5 )


		bSizer43.Add( bSizer492, 0, 0, 5 )

		self.m_staticline10 = wx.StaticLine( self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer43.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_simplebook3 = wx.Simplebook( self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_tex = wx.Panel( self.m_simplebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText25 = wx.StaticText( self.m_panel_tex, wx.ID_ANY, u"Texture", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer46.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_textCtrl_qk_tex = wx.TextCtrl( self.m_panel_tex, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.m_textCtrl_qk_tex, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer49 = wx.BoxSizer( wx.HORIZONTAL )

		m_choice_tex_typeChoices = [ u"文件", u"文件夹" ]
		self.m_choice_tex_type = wx.Choice( self.m_panel_tex, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_tex_typeChoices, wx.CB_SORT )
		self.m_choice_tex_type.SetSelection( 0 )
		bSizer49.Add( self.m_choice_tex_type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button12 = wx.Button( self.m_panel_tex, wx.ID_ANY, u"加载", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer49.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer46.Add( bSizer49, 0, wx.ALIGN_RIGHT, 5 )


		self.m_panel_tex.SetSizer( bSizer46 )
		self.m_panel_tex.Layout()
		bSizer46.Fit( self.m_panel_tex )
		self.m_simplebook3.AddPage( self.m_panel_tex, u"a page", False )
		self.m_panel_mesh = wx.Panel( self.m_simplebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer461 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText251 = wx.StaticText( self.m_panel_mesh, wx.ID_ANY, u"Mesh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )

		bSizer461.Add( self.m_staticText251, 0, wx.ALL, 5 )

		self.m_textCtrl_qk_mesh = wx.TextCtrl( self.m_panel_mesh, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer461.Add( self.m_textCtrl_qk_mesh, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer491 = wx.BoxSizer( wx.HORIZONTAL )

		m_choice_mesh_typeChoices = [ u"文件", u"文件夹" ]
		self.m_choice_mesh_type = wx.Choice( self.m_panel_mesh, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_mesh_typeChoices, wx.CB_SORT )
		self.m_choice_mesh_type.SetSelection( 0 )
		bSizer491.Add( self.m_choice_mesh_type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button121 = wx.Button( self.m_panel_mesh, wx.ID_ANY, u"加载", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer491.Add( self.m_button121, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer461.Add( bSizer491, 0, wx.ALIGN_RIGHT, 5 )


		self.m_panel_mesh.SetSizer( bSizer461 )
		self.m_panel_mesh.Layout()
		bSizer461.Fit( self.m_panel_mesh )
		self.m_simplebook3.AddPage( self.m_panel_mesh, u"a page", False )
		self.m_panel30 = wx.Panel( self.m_simplebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText28 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"both", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer55.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl_qk_ex = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer55.Add( self.m_textCtrl_qk_ex, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button15 = wx.Button( self.m_panel30, wx.ID_ANY, u"加载", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer55.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel30.SetSizer( bSizer55 )
		self.m_panel30.Layout()
		bSizer55.Fit( self.m_panel30 )
		self.m_simplebook3.AddPage( self.m_panel30, u"a page", False )

		bSizer43.Add( self.m_simplebook3, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel25.SetSizer( bSizer43 )
		self.m_panel25.Layout()
		bSizer43.Fit( self.m_panel25 )
		self.m_notebook3.AddPage( self.m_panel25, u"导入", False )
		self.m_panel27 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText29 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"导出目录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		bSizer45.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_dirPicker8 = wx.DirPickerCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, u"导出文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_CHANGE_DIR|wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST|wx.DIRP_SMALL )
		bSizer45.Add( self.m_dirPicker8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button17 = wx.Button( self.m_panel27, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.m_button17, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel27.SetSizer( bSizer45 )
		self.m_panel27.Layout()
		bSizer45.Fit( self.m_panel27 )
		self.m_notebook3.AddPage( self.m_panel27, u"导出", True )

		bSizer42.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer42 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_choice_im_type.Bind( wx.EVT_CHOICE, self.im_sele )
		self.m_button171.Bind( wx.EVT_BUTTON, self.quick_setting )
		self.m_button12.Bind( wx.EVT_BUTTON, self.quick_tex )
		self.m_button121.Bind( wx.EVT_BUTTON, self.quick_mesh )
		self.m_button15.Bind( wx.EVT_BUTTON, self.quick_both )
		self.m_dirPicker8.Bind( wx.EVT_DIRPICKER_CHANGED, self.quick_export )
		self.m_button17.Bind( wx.EVT_BUTTON, self.quick_setting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def im_sele( self, event ):
		event.Skip()

	def quick_setting( self, event ):
		event.Skip()

	def quick_tex( self, event ):
		event.Skip()

	def quick_mesh( self, event ):
		event.Skip()

	def quick_both( self, event ):
		event.Skip()

	def quick_export( self, event ):
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
## Class MyDialog_Setting
###########################################################################

class MyDialog_Setting ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 691,500 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.m_scrolledWindow4 = wx.ScrolledWindow( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow4.SetScrollRate( 5, 5 )
		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self.m_scrolledWindow4, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_MENU ), wx.DefaultPosition, wx.DefaultSize, 0 )
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
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow41 = wx.ScrolledWindow( self.m_scrolledWindow7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow41.SetScrollRate( 5, 5 )
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow41, wx.ID_ANY, u"设置" ), wx.VERTICAL )

		m_radioBox_ex_typeChoices = [ u"仅导出可还原立绘", u"导出全部（包括不可还原）" ]
		self.m_radioBox_ex_type = wx.RadioBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"导出立绘类型", wx.DefaultPosition, wx.DefaultSize, m_radioBox_ex_typeChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_ex_type.SetSelection( 0 )
		sbSizer8.Add( self.m_radioBox_ex_type, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_in_cn = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"以中文名导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_checkBox_in_cn, 0, wx.ALL, 5 )

		self.m_checkBox_add_dir = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"在导出文件夹内新建导出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_checkBox_add_dir, 0, wx.ALL, 5 )

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

		self.m_checkBox_clear = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"导入前清空列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_checkBox_clear, 0, wx.ALL, 5 )

		self.m_staticline14 = wx.StaticLine( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer8.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_menu = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"设置右键菜单", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_button_menu, 0, wx.ALL, 5 )


		self.m_scrolledWindow41.SetSizer( sbSizer8 )
		self.m_scrolledWindow41.Layout()
		sbSizer8.Fit( self.m_scrolledWindow41 )
		bSizer48.Add( self.m_scrolledWindow41, 1, wx.EXPAND |wx.ALL, 5 )


		gSizer15.Add( bSizer48, 1, wx.EXPAND, 5 )

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


		gSizer15.Add( bSizer22, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow7.SetSizer( gSizer15 )
		self.m_scrolledWindow7.Layout()
		gSizer15.Fit( self.m_scrolledWindow7 )
		self.m_notebook3.AddPage( self.m_scrolledWindow7, u"其他设置", True )
		self.m_panel20 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox_type_useChoices = [ u"使用预设的分类方案", u"使用-自定义-分类方案" ]
		self.m_radioBox_type_use = wx.RadioBox( self.m_panel20, wx.ID_ANY, u"分类方案", wx.DefaultPosition, wx.DefaultSize, m_radioBox_type_useChoices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox_type_use.SetSelection( 1 )
		self.m_radioBox_type_use.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer32.Add( self.m_radioBox_type_use, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_simplebook_io = wx.Simplebook( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scrolledWindow71 = wx.ScrolledWindow( self.m_simplebook_io, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow71.SetScrollRate( 5, 5 )
		self.m_scrolledWindow71.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow71, wx.ID_ANY, u"预设方案" ), wx.HORIZONTAL )

		m_radioBox_imChoices = [ u"导入全部", u"仅导入皮肤", u"仅导入婚纱", u"仅导入改造", u"仅导入原皮" ]
		self.m_radioBox_im = wx.RadioBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"导入设置", wx.DefaultPosition, wx.DefaultSize, m_radioBox_imChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_im.SetSelection( 4 )
		sbSizer9.Add( self.m_radioBox_im, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline8 = wx.StaticLine( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer9.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		m_radioBox_az_divChoices = [ u"不分类", u"按舰娘名分类", u"按-皮肤-婚纱-原始皮肤分类" ]
		self.m_radioBox_az_div = wx.RadioBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"导出分类设置", wx.DefaultPosition, wx.DefaultSize, m_radioBox_az_divChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_az_div.SetSelection( 0 )
		sbSizer9.Add( self.m_radioBox_az_div, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow71.SetSizer( sbSizer9 )
		self.m_scrolledWindow71.Layout()
		sbSizer9.Fit( self.m_scrolledWindow71 )
		self.m_simplebook_io.AddPage( self.m_scrolledWindow71, u"a page", False )
		self.m_scrolledWindow8 = wx.ScrolledWindow( self.m_simplebook_io, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow8.SetScrollRate( 5, 5 )
		self.m_scrolledWindow8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_scrolledWindow8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		sbSizer101 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow8, wx.ID_ANY, u"自定义方案" ), wx.HORIZONTAL )

		bSizer49 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText15 = wx.StaticText( sbSizer101.GetStaticBox(), wx.ID_ANY, u"导入texture2D-限制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer49.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_tex_limit = wx.TextCtrl( sbSizer101.GetStaticBox(), wx.ID_ANY, u".+\\.[p,P][N,n][G,g]", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_textCtrl_tex_limit, 1, wx.ALL, 5 )

		self.m_bpButton_defualt_tex = wx.BitmapButton( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_defualt_tex.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_BUTTON ) )
		bSizer26.Add( self.m_bpButton_defualt_tex, 0, wx.ALL, 5 )


		bSizer49.Add( bSizer26, 0, wx.EXPAND, 5 )

		self.m_staticText161 = wx.StaticText( sbSizer101.GetStaticBox(), wx.ID_ANY, u"导入mesh-限制", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		bSizer49.Add( self.m_staticText161, 0, wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_mesh_limit = wx.TextCtrl( sbSizer101.GetStaticBox(), wx.ID_ANY, u".+-mesh\\.[o,O][B,b][J,j]", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl_mesh_limit, 1, wx.ALL, 5 )

		self.m_bpButton6_default_mesh = wx.BitmapButton( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton6_default_mesh.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_BUTTON ) )
		bSizer27.Add( self.m_bpButton6_default_mesh, 0, wx.ALL, 5 )


		bSizer49.Add( bSizer27, 0, wx.EXPAND, 5 )


		sbSizer101.Add( bSizer49, 1, wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer101.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText171 = wx.StaticText( sbSizer101.GetStaticBox(), wx.ID_ANY, u"导出分类：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		bSizer25.Add( self.m_staticText171, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer17 = wx.GridSizer( 0, 4, 0, 0 )

		self.m_bpButton_add = wx.BitmapButton( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_add.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
		gSizer17.Add( self.m_bpButton_add, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton_del = wx.BitmapButton( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_del.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
		gSizer17.Add( self.m_bpButton_del, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton_up = wx.BitmapButton( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_up.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_BUTTON ) )
		self.m_bpButton_up.SetBitmapDisabled( wx.NullBitmap )
		gSizer17.Add( self.m_bpButton_up, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton_down = wx.BitmapButton( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_down.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ) )
		gSizer17.Add( self.m_bpButton_down, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer25.Add( gSizer17, 1, 0, 5 )


		bSizer51.Add( bSizer25, 0, wx.EXPAND, 5 )

		m_checkList_az_limitsChoices = [u"其他"]
		self.m_checkList_az_limits = wx.CheckListBox( sbSizer101.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList_az_limitsChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_SINGLE )
		bSizer51.Add( self.m_checkList_az_limits, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_save_all = wx.CheckBox( sbSizer101.GetStaticBox(), wx.ID_ANY, u"当满足多种分类方案只保存至第一个符合的", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_save_all.SetValue(True)
		bSizer51.Add( self.m_checkBox_save_all, 0, wx.ALL, 5 )


		sbSizer101.Add( bSizer51, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow8.SetSizer( sbSizer101 )
		self.m_scrolledWindow8.Layout()
		sbSizer101.Fit( self.m_scrolledWindow8 )
		self.m_simplebook_io.AddPage( self.m_scrolledWindow8, u"a page", False )

		bSizer32.Add( self.m_simplebook_io, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel20.SetSizer( bSizer32 )
		self.m_panel20.Layout()
		bSizer32.Fit( self.m_panel20 )
		self.m_notebook3.AddPage( self.m_panel20, u"设置-导入导出", False )
		self.m_panel12 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer55 = wx.BoxSizer( wx.VERTICAL )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel12, wx.ID_ANY, u"添加新舰娘" ), wx.VERTICAL )

		m_listBox_newChoices = []
		self.m_listBox_new = wx.ListBox( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_newChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		sbSizer11.Add( self.m_listBox_new, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_gauge5 = wx.Gauge( sbSizer11.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge5.SetValue( 0 )
		sbSizer11.Add( self.m_gauge5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline15 = wx.StaticLine( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer11.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText30 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"添加新 键-值", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		bSizer61.Add( self.m_staticText30, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		gSizer171 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_bpButton_add_name = wx.BitmapButton( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_add_name.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
		gSizer171.Add( self.m_bpButton_add_name, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton_del_name = wx.BitmapButton( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_del_name.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
		gSizer171.Add( self.m_bpButton_del_name, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer61.Add( gSizer171, 0, wx.ALIGN_RIGHT, 5 )


		sbSizer11.Add( bSizer61, 0, wx.EXPAND, 5 )

		m_listBox_new1Choices = []
		self.m_listBox_new1 = wx.ListBox( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_new1Choices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		sbSizer11.Add( self.m_listBox_new1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer55.Add( sbSizer11, 1, wx.EXPAND, 5 )


		gSizer18.Add( bSizer55, 1, wx.EXPAND, 5 )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel12, wx.ID_ANY, u"修改舰娘名" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )


		sbSizer12.Add( bSizer11, 1, wx.EXPAND, 5 )

		self.m_searchCtrl2 = wx.SearchCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl2.ShowSearchButton( True )
		self.m_searchCtrl2.ShowCancelButton( True )
		sbSizer12.Add( self.m_searchCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox_changeChoices = []
		self.m_listBox_change = wx.ListBox( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_changeChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		self.m_listBox_change.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		sbSizer12.Add( self.m_listBox_change, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer18.Add( sbSizer12, 1, wx.EXPAND, 5 )


		self.m_panel12.SetSizer( gSizer18 )
		self.m_panel12.Layout()
		gSizer18.Fit( self.m_panel12 )
		self.m_notebook3.AddPage( self.m_panel12, u"工具", False )
		self.m_scrolledWindow9 = wx.ScrolledWindow( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow9.SetScrollRate( 5, 5 )
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_splitter2 = wx.SplitterWindow( self.m_scrolledWindow9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )

		self.m_panel231 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel231, wx.ID_ANY, u"加密" ), wx.VERTICAL )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_file = wx.Button( sbSizer20.GetStaticBox(), wx.ID_ANY, u"加载文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer36.Add( self.m_button_file, 0, wx.ALL, 5 )

		self.m_gauge_file = wx.Gauge( sbSizer20.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_file.SetValue( 0 )
		bSizer36.Add( self.m_gauge_file, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer20.Add( bSizer36, 0, wx.EXPAND, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_folder = wx.Button( sbSizer20.GetStaticBox(), wx.ID_ANY, u"加载文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.m_button_folder, 0, wx.ALL, 5 )

		self.m_gauge_dir = wx.Gauge( sbSizer20.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_dir.SetValue( 0 )
		bSizer37.Add( self.m_gauge_dir, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer20.Add( bSizer37, 0, wx.EXPAND, 5 )

		self.m_staticline81 = wx.StaticLine( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer20.Add( self.m_staticline81, 0, wx.EXPAND |wx.ALL, 5 )

		m_listBox_picsChoices = []
		self.m_listBox_pics = wx.ListBox( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_picsChoices, 0 )
		sbSizer20.Add( self.m_listBox_pics, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_gauge_works = wx.Gauge( sbSizer20.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_works.SetValue( 0 )
		bSizer42.Add( self.m_gauge_works, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_typeChoices = [ u"普通", u"标准", u"复杂" ]
		self.m_choice_type = wx.Choice( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_typeChoices, 0 )
		self.m_choice_type.SetSelection( 0 )
		bSizer42.Add( self.m_choice_type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_star = wx.Button( sbSizer20.GetStaticBox(), wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_button_star, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer20.Add( bSizer42, 0, wx.EXPAND, 5 )


		self.m_panel231.SetSizer( sbSizer20 )
		self.m_panel231.Layout()
		sbSizer20.Fit( self.m_panel231 )
		self.m_panel241 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer201 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel241, wx.ID_ANY, u"解密" ), wx.VERTICAL )

		bSizer361 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_file_in = wx.Button( sbSizer201.GetStaticBox(), wx.ID_ANY, u"加载文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer361.Add( self.m_button_file_in, 0, wx.ALL, 5 )

		self.m_gauge_file_in = wx.Gauge( sbSizer201.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_file_in.SetValue( 0 )
		bSizer361.Add( self.m_gauge_file_in, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer201.Add( bSizer361, 0, wx.EXPAND, 5 )

		bSizer371 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_folder_in = wx.Button( sbSizer201.GetStaticBox(), wx.ID_ANY, u"加载文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer371.Add( self.m_button_folder_in, 0, wx.ALL, 5 )

		self.m_gauge_fold_in = wx.Gauge( sbSizer201.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_fold_in.SetValue( 0 )
		bSizer371.Add( self.m_gauge_fold_in, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer201.Add( bSizer371, 0, wx.EXPAND, 5 )

		self.m_staticline811 = wx.StaticLine( sbSizer201.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer201.Add( self.m_staticline811, 0, wx.EXPAND |wx.ALL, 5 )

		m_listBox_pic_inChoices = []
		self.m_listBox_pic_in = wx.ListBox( sbSizer201.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_pic_inChoices, 0 )
		sbSizer201.Add( self.m_listBox_pic_in, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer421 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_gauge_work_in = wx.Gauge( sbSizer201.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_work_in.SetValue( 0 )
		bSizer421.Add( self.m_gauge_work_in, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_type_inChoices = [ u"普通", u"标准", u"复杂" ]
		self.m_choice_type_in = wx.Choice( sbSizer201.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_type_inChoices, 0 )
		self.m_choice_type_in.SetSelection( 0 )
		bSizer421.Add( self.m_choice_type_in, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_star_in = wx.Button( sbSizer201.GetStaticBox(), wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer421.Add( self.m_button_star_in, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer201.Add( bSizer421, 0, wx.EXPAND, 5 )


		self.m_panel241.SetSizer( sbSizer201 )
		self.m_panel241.Layout()
		sbSizer201.Fit( self.m_panel241 )
		self.m_splitter2.SplitVertically( self.m_panel231, self.m_panel241, 0 )
		bSizer33.Add( self.m_splitter2, 0, wx.EXPAND, 5 )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow9, wx.ID_ANY, u"比较新增" ), wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"新文件文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer9.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_dirPicker_old = wx.DirPickerCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"新文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		bSizer9.Add( self.m_dirPicker_old, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"旧文件文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_dirPicker6 = wx.DirPickerCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"旧文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		bSizer9.Add( self.m_dirPicker6, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox_defferChoices = []
		self.m_listBox_deffer = wx.ListBox( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_defferChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		bSizer9.Add( self.m_listBox_deffer, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer13.Add( bSizer9, 1, wx.EXPAND, 5 )


		bSizer33.Add( sbSizer13, 0, wx.EXPAND, 5 )


		self.m_scrolledWindow9.SetSizer( bSizer33 )
		self.m_scrolledWindow9.Layout()
		bSizer33.Fit( self.m_scrolledWindow9 )
		self.m_notebook3.AddPage( self.m_scrolledWindow9, u"其他工具", False )

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
		self.Bind( wx.EVT_CLOSE, self.close )
		self.Bind( wx.EVT_INIT_DIALOG, self.initial )
		self.m_notebook3.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.change_page )
		self.m_radioBox_ex_type.Bind( wx.EVT_RADIOBOX, self.change )
		self.m_checkBox_in_cn.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_add_dir.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_autoopen.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_pass_finished.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_open_temp.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox4_finish_exit.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_checkBox_clear.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_button_menu.Bind( wx.EVT_BUTTON, self.menu_setting )
		self.m_toggleBtn_lock.Bind( wx.EVT_TOGGLEBUTTON, self.lock_address )
		self.m_radioBox_type_use.Bind( wx.EVT_RADIOBOX, self.change_type )
		self.m_radioBox_im.Bind( wx.EVT_RADIOBOX, self.change_input )
		self.m_radioBox_az_div.Bind( wx.EVT_RADIOBOX, self.change_div )
		self.m_textCtrl_tex_limit.Bind( wx.EVT_TEXT, self.change_in_tex )
		self.m_textCtrl_tex_limit.Bind( wx.EVT_TEXT_ENTER, self.change )
		self.m_bpButton_defualt_tex.Bind( wx.EVT_BUTTON, self.default_tex )
		self.m_textCtrl_mesh_limit.Bind( wx.EVT_TEXT, self.change_in_mesh )
		self.m_textCtrl_mesh_limit.Bind( wx.EVT_TEXT_ENTER, self.change )
		self.m_bpButton6_default_mesh.Bind( wx.EVT_BUTTON, self.default_mesh )
		self.m_bpButton_add.Bind( wx.EVT_BUTTON, self.az_add )
		self.m_bpButton_del.Bind( wx.EVT_BUTTON, self.az_del )
		self.m_bpButton_up.Bind( wx.EVT_BUTTON, self.az_up )
		self.m_bpButton_down.Bind( wx.EVT_BUTTON, self.az_down )
		self.m_checkList_az_limits.Bind( wx.EVT_LISTBOX, self.choice )
		self.m_checkList_az_limits.Bind( wx.EVT_LISTBOX_DCLICK, self.change_pattern )
		self.m_checkBox_save_all.Bind( wx.EVT_CHECKBOX, self.change )
		self.m_listBox_new.Bind( wx.EVT_LISTBOX_DCLICK, self.open_add_name )
		self.m_bpButton_add_name.Bind( wx.EVT_BUTTON, self.name_add )
		self.m_bpButton_del_name.Bind( wx.EVT_BUTTON, self.name_del )
		self.m_listBox_new1.Bind( wx.EVT_LISTBOX, self.choice_add )
		self.m_listBox_new1.Bind( wx.EVT_LISTBOX_DCLICK, self.edit_add_name )
		self.m_searchCtrl2.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searching )
		self.m_searchCtrl2.Bind( wx.EVT_TEXT, self.searching )
		self.m_listBox_change.Bind( wx.EVT_LISTBOX_DCLICK, self.change_name )
		self.m_button_file.Bind( wx.EVT_BUTTON, self.in_file )
		self.m_button_folder.Bind( wx.EVT_BUTTON, self.in_fold )
		self.m_button_star.Bind( wx.EVT_BUTTON, self.in_start )
		self.m_button_file_in.Bind( wx.EVT_BUTTON, self.out_file )
		self.m_button_folder_in.Bind( wx.EVT_BUTTON, self.out_fold )
		self.m_button_star_in.Bind( wx.EVT_BUTTON, self.out_start )
		self.m_dirPicker_old.Bind( wx.EVT_DIRPICKER_CHANGED, self.add_new )
		self.m_dirPicker6.Bind( wx.EVT_DIRPICKER_CHANGED, self.add_old )
		self.m_listBox_deffer.Bind( wx.EVT_LISTBOX_DCLICK, self.writer_into )
		self.m_sdbSizer4Apply.Bind( wx.EVT_BUTTON, self.apply_click )
		self.m_sdbSizer4Cancel.Bind( wx.EVT_BUTTON, self.cancel_click )
		self.m_sdbSizer4OK.Bind( wx.EVT_BUTTON, self.ok_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		event.Skip()

	def initial( self, event ):
		event.Skip()

	def change_page( self, event ):
		event.Skip()

	def change( self, event ):
		event.Skip()








	def menu_setting( self, event ):
		event.Skip()

	def lock_address( self, event ):
		event.Skip()

	def change_type( self, event ):
		event.Skip()

	def change_input( self, event ):
		event.Skip()

	def change_div( self, event ):
		event.Skip()

	def change_in_tex( self, event ):
		event.Skip()


	def default_tex( self, event ):
		event.Skip()

	def change_in_mesh( self, event ):
		event.Skip()


	def default_mesh( self, event ):
		event.Skip()

	def az_add( self, event ):
		event.Skip()

	def az_del( self, event ):
		event.Skip()

	def az_up( self, event ):
		event.Skip()

	def az_down( self, event ):
		event.Skip()

	def choice( self, event ):
		event.Skip()

	def change_pattern( self, event ):
		event.Skip()


	def open_add_name( self, event ):
		event.Skip()

	def name_add( self, event ):
		event.Skip()

	def name_del( self, event ):
		event.Skip()

	def choice_add( self, event ):
		event.Skip()

	def edit_add_name( self, event ):
		event.Skip()

	def searching( self, event ):
		event.Skip()


	def change_name( self, event ):
		event.Skip()

	def in_file( self, event ):
		event.Skip()

	def in_fold( self, event ):
		event.Skip()

	def in_start( self, event ):
		event.Skip()

	def out_file( self, event ):
		event.Skip()

	def out_fold( self, event ):
		event.Skip()

	def out_start( self, event ):
		event.Skip()

	def add_new( self, event ):
		event.Skip()

	def add_old( self, event ):
		event.Skip()

	def writer_into( self, event ):
		event.Skip()

	def apply_click( self, event ):
		event.Skip()

	def cancel_click( self, event ):
		event.Skip()

	def ok_click( self, event ):
		event.Skip()

	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 0 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )


###########################################################################
## Class MyDialog_menu
###########################################################################

class MyDialog_menu ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置添加的类型", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer47 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox_dir = wx.CheckBox( self, wx.ID_ANY, u"文件夹右键", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer47.Add( self.m_checkBox_dir, 0, wx.ALL, 5 )

		self.m_checkBox_bg = wx.CheckBox( self, wx.ID_ANY, u"文件夹内右键", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer47.Add( self.m_checkBox_bg, 0, wx.ALL, 5 )

		m_sdbSizer5 = wx.StdDialogButtonSizer()
		self.m_sdbSizer5OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer5.AddButton( self.m_sdbSizer5OK )
		self.m_sdbSizer5Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Cancel )
		m_sdbSizer5.Realize();

		bSizer47.Add( m_sdbSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer47 )
		self.Layout()
		bSizer47.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_checkBox_dir.Bind( wx.EVT_CHECKBOX, self.use_dir )
		self.m_checkBox_bg.Bind( wx.EVT_CHECKBOX, self.use_bg )
		self.m_sdbSizer5OK.Bind( wx.EVT_BUTTON, self.ok_change )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def use_dir( self, event ):
		event.Skip()

	def use_bg( self, event ):
		event.Skip()

	def ok_change( self, event ):
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


###########################################################################
## Class MyDialog_add_name
###########################################################################

class MyDialog_add_name ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"添加新名", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer58 = wx.BoxSizer( wx.VERTICAL )

		bSizer59 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"键", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer59.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl_key = wx.TextCtrl( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer59.Add( self.m_textCtrl_key, 1, wx.ALL, 5 )


		bSizer58.Add( bSizer59, 1, wx.EXPAND, 5 )

		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"值", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		bSizer60.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl_var = wx.TextCtrl( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_textCtrl_var, 1, wx.ALL, 5 )


		bSizer58.Add( bSizer60, 1, wx.EXPAND, 5 )

		m_sdbSizer5 = wx.StdDialogButtonSizer()
		self.m_sdbSizer5OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer5.AddButton( self.m_sdbSizer5OK )
		self.m_sdbSizer5Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Cancel )
		m_sdbSizer5.Realize();

		bSizer58.Add( m_sdbSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer58 )
		self.Layout()
		bSizer58.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer5OK.Bind( wx.EVT_BUTTON, self.ok_work )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ok_work( self, event ):
		event.Skip()


