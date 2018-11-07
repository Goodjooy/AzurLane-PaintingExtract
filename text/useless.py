def add_new(self, event):
    dialog = AddDialog(self, self.azur_lane.tex_name, self.azur_lane.names, self.start_path)

    if dialog.ShowModal() == 0:
        with open(self.start_path + '\\files\\names.json', 'r')as file:
            self.names = json.load(file)


def compare(self, event):
    compare = CompareDialog(self)

    if compare.ShowModal() == 0:
        pass


def change_name(self, event):
    dialog = ChangeNameDialog(self, self.start_path)
    if dialog.ShowModal() == 0:
        with open(self.start_path + '\\files\\names.json', 'r')as file:
            self.names = json.load(file)
