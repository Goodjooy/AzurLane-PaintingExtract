from Classes.WorkClasses import BaseWorkClass


class LogViewer(BaseWorkClass):
    def __init__(self, frame):
        super(LogViewer, self).__init__(frame)
        self.log_list = []

    def __getattr__(self, item):
        return '%s 不存在' % item

    def init_worker(self, val: str, timer: float):
        self.log_list.append(Log(self.frame, timer, val))


class Log(BaseWorkClass):
    def __init__(self, frame, time_in, string):
        super(Log, self).__init__(frame)
        self.time = time_in
        self.string = string

    def show_info(self):
        return f'{self.time}-{self.string}'
