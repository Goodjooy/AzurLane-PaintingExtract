for val in self.able_list:
    if self.setting["use_type"] == 0:
        choice = self.setting["export_type"]
        pattern_skin = re.compile(r'^pic_[a-zA-Z0-9_]+_[1-9]+_(_D)*$')

        if choice == 0:
            save_path = f"{self.save_path}"

        elif choice == 1:
            pattern_per = re.compile(r'^pic_.+$')

            if pattern_per.match(val) is not None:
                save_path = f"{self.save_path}\\人形"
            else:
                save_path = f"{self.save_path}\\非人形"
        elif choice == 2:
            pattern_per = re.compile(r'^pic_.+$')
            if pattern_per.match(val) is not None:

                save_path = f"{self.save_path}\\人形"
            else:
                save_path = f"{self.save_path}\\非人形"

            save_path
