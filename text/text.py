if self.frame.m_radioBox_type_use.GetSelection() == 0:

    self.frame.m_textCtrl_mesh_limit.SetLabel(self.default_mesh_pattern)
    self.frame.m_textCtrl_tex_limit.SetLabel(self.default_tex_pattern)


    self.change_input(event)
    self.change_div(event=event)

else:
    self.frame.m_staticText15.Enable(True)
    self.frame.m_staticText161.Enable(True)
    self.frame.m_staticText171.Enable(True)

    self.frame.m_textCtrl_mesh_limit.Enable(True)
    self.frame.m_textCtrl_tex_limit.Enable(True)

    self.frame.m_bpButton_del.Enable(False)
    self.frame.m_bpButton_add.Enable(True)

    self.frame.m_bpButton_up.Enable(False)
    self.frame.m_bpButton_down.Enable(False)

    self.frame.m_textCtrl_mesh_limit.SetLabel(self.azur_lane_mesh_limit)
    self.frame.m_textCtrl_tex_limit.SetLabel(self.azur_lane_tex_limit)

    self.frame.m_radioBox_im.Enable(False)

    if self.frame.m_textCtrl_tex_limit.GetValue() != self.default_tex_pattern:
        self.frame.m_bpButton_defualt_tex.Enable(True)
    else:
        self.frame.m_bpButton_defualt_tex.Enable(False)
    if self.frame.m_textCtrl_mesh_limit.GetValue() != self.default_mesh_pattern:
        self.frame.m_bpButton6_default_mesh.Enable(True)
    else:
        self.frame.m_bpButton6_default_mesh.Enable(False)

    self.frame.m_checkList_az_limits.Enable(True)

    ####

    self.frame.m_radioBox_az_div.Enable(False)

    self.reset_az_pattern()
    self.frame.m_checkList_az_limits.Clear()
    self.frame.m_checkList_az_limits.Set(self.az_div_list)