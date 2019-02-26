import collections.abc
import functools
import os

import wx


class KeyExistError(KeyError):
    def __init__(self, arg):
        self.arg = arg


class BasicInfo(object):
    def __init__(self, name, val):

        self.name = name
        self._val = val

    def __str__(self):
        return f'Key:{self.name}\n' f'Name:{self.val}\n'

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    def rebuild_self(self, value):

        if isinstance(value, BasicInfo):
            self._val = value.val
        else:
            raise ValueError


class BasicInfoList(object):
    def __init__(self, item: collections.abc.Iterable = None):

        self._info_dict = {}

        self._key_list = []

        self._start = 0
        self._index = 0

        if isinstance(item, collections.abc.Iterable):
            self.extend(item)

    def __delitem__(self, key):
        if isinstance(key, int):
            key = self._key_list[key]
        else:
            pass
        del self._info_dict[key]
        index = self._key_list.index(key)
        del self._key_list[index]

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._info_dict[self._key_list[item]]
        else:
            return self._info_dict[item]

    def __setitem__(self, key: str, value):
        if key in self:
            index = self._key_list.index(key)
            self._key_list[index] = key
        else:
            self._key_list.append(key)

        self._info_dict[key] = value

    def __iter__(self):
        self._index = self._start
        return self

    def __next__(self):
        if self._index >= len(self._key_list):
            raise StopIteration
        else:
            val = self._info_dict[self._key_list[self._index]]

            self._index += 1

            return val

    def __str__(self):
        return str(list(zip(self._key_list, self._info_dict.values())))

    def __len__(self):
        return len(self._key_list)

    def __bool__(self):
        if len(self) <= 0:
            return False
        else:
            return True

    def __contains__(self, item):
        if isinstance(item, str):
            return item in self._key_list
        if isinstance(item, PerWork):
            return item in self._info_dict.values()
        else:
            return False

    @staticmethod
    def form_dict(values: dict = None):

        if values is None:
            values = {}
        return BasicInfoList([BasicInfo(key_, value_) for key_, value_ in values.items()])

    def remove(self, item: collections.abc.Iterable):
        return BasicInfoList(filter(lambda x: x not in item, self))

    def get_new(self, item: collections.abc.Iterable):
        return BasicInfoList(filter(lambda x: x not in self, item))

    def append_name(self, name, val, *, has_cn=False):
        if name not in self._info_dict:
            self[name] = BasicInfo(name, val)
        else:
            pass

        return name

    def append_self(self, value):
        if isinstance(value, BasicInfo):
            self[value.name] = value
        else:
            raise ValueError(f'{type(value)}is not able')

    def extend(self, values):
        if isinstance(values, collections.abc.Iterable):
            list(map(lambda _x: self.append_self(_x), values))

    def set_self(self, key, value):
        self[key].rebuild_self(value)

    def clear(self):
        self._key_list.clear()
        self._info_dict.clear()

    def get_index(self, value):
        if isinstance(value, BasicInfo):
            try:
                return self._key_list.index(value.name)
            except ValueError:
                return None
        if isinstance(value, str):
            try:
                return self._key_list.index(value)
            except ValueError:
                return None

    def is_in_dict(self, item):
        return item not in self._info_dict.keys()


class PerWork(BasicInfo):
    def __init__(self, name, name_cn, has_cn: bool = False):
        super(PerWork, self).__init__(name, name_cn)

        self.tex_path = ''
        self.mesh_path = ''
        self.save_path = ''

        self.lay_in = ''

        self.name = name
        self.name_cn = self.val

        if has_cn or name_cn != name:
            self.has_cn = True
        else:
            self.has_cn = False

        self.is_able_work = False

        self.is_skip = False

        self.set_ex_as_cn = True

    def __str__(self):
        return f'Key:{self.name}\n' \
            f'Name:{self.name_cn}\n' \
            f'Tex:{self.tex_path}\n' \
            f'Mesh:{self.mesh_path}\n' \
            f'Save at:{self.save_path}\n'

    @property
    def name_cn(self):
        return self.val

    @name_cn.setter
    def name_cn(self, name_cn):
        self._val = name_cn

    def _able_work(self):
        if os.path.exists(self.tex_path) and os.path.exists(self.mesh_path):
            self.is_able_work = True
        else:
            self.is_able_work = False

    def add_tex(self, tex_path):
        self.tex_path = tex_path
        self._able_work()

    def add_mesh(self, mesh_path):
        self.mesh_path = mesh_path
        self._able_work()

    def need_skip(self, path_files: dict):
        keys = path_files.keys()
        files = path_files
        name_cn = self.name_cn + '.png'
        name = self.name + '.png'

        if name_cn in keys:
            self.is_skip = True
            self.lay_in = files[name_cn]
            return True
        elif name in keys:
            self.is_skip = True
            self.lay_in = files[name]
            return True
        else:
            self.is_skip = False
            return False

    def add_save(self, save_path):
        if self.set_ex_as_cn:
            self.save_path = os.path.join(save_path, self.name_cn + ".png")
        else:
            self.save_path = os.path.join(save_path, self.name + ".png")

    def get_show(self, index=0):
        return f'{index}）:{self.name_cn}——{self.name};(@_@)'

    def get_search(self):
        if self.has_cn:
            return f'{self.name}{self.name_cn}'
        else:
            return self.name

    def set_name_cn(self, name):
        if name != self.name_cn and name != '':
            self.name_cn = name
            self.has_cn = True
        else:
            self.has_cn = False

    def update_name(self, names: dict):
        if self.name in names.keys():
            self.name_cn = names[self.name]
            self.has_cn = True
        else:
            self.name_cn = self.name
            self.has_cn = False

    def rebuild_self(self, value):

        if isinstance(value, PerWork):
            self.tex_path = value.tex_path
            self.mesh_path = value.mesh_path
            self.save_path = value.save_path

            self.lay_in = value.lay_in

            self.name = value.name

            self.has_cn = value.has_cn
            self.name_cn = value.name_cn
            self.is_able_work = value.is_able_work

            self.is_skip = value.is_skip

            self.set_ex_as_cn = value.set_ex_as_cn

        else:
            raise ValueError

    def clear_tex(self):
        self.tex_path = ''

    def clear_mesh(self):
        self.mesh_path = ''


class PerWorkList(BasicInfoList):
    def __init__(self, item: collections.abc.Iterable = None):

        self.for_search = []

        self.for_show = []

        super(PerWorkList, self).__init__(item)

    def __delitem__(self, key):
        super(PerWorkList, self).__delitem__(key)
        index = self._key_list.index(key)
        del self.for_show[index]
        del self.for_search[index]

    def __setitem__(self, key: str, value: PerWork):
        if key in self._info_dict.keys():
            raise KeyExistError("KeyExist!")

        else:
            self._info_dict[key] = value
            self._key_list.append(key)
            self.for_show.append(value.get_show(len(self)))
            self.for_search.append(value.get_search())

    @staticmethod
    def form_dict(values: dict = None):

        if values is None:
            values = {}
        return PerWorkList([PerWork(key_, value_) for key_, value_ in values.items()])

    def is_all_able(self):
        return not bool(self.build_unable())

    def append_name(self, name, names_key, *, has_cn=False):
        if name in names_key.keys():
            name_cn = names_key[name]
            has_cn = True
        else:
            has_cn = False
            name_cn = name
        if name not in self._info_dict:
            self[name] = PerWork(name, name_cn, has_cn)
        else:
            pass

        return name

    def append_self(self, value):
        if isinstance(value, PerWork):
            self[value.name] = value
        else:
            raise ValueError(f'{type(value)}is not able')

    def set_tex(self, key, path):
        self._info_dict[key].add_tex(path)

    def set_mesh(self, key, path):
        self[key].add_mesh(path)

    def set_save(self, key, path):
        self[key].add_save(path)

    def set_self(self, key, value):
        self[key].rebuild_self(value)
        index = self.get_index(key)
        value = self._info_dict[key]
        self.for_show[index] = value.get_show(index + 1)
        self.for_search[index] = value.get_search()

    def clear(self):
        self._key_list.clear()
        self._info_dict.clear()
        self.for_search.clear()
        self.for_show.clear()

    def clear_tex(self):
        list(map(lambda x: x.clear_tex(), self))

    def clear_mesh(self):
        list(map(lambda x: x.clear_mesh(), self))

    def up_date_name_cn(self, name_cn: dict):
        list(map(lambda _x: _x.update_name(name_cn), self))

    def build_no_cn(self):
        val = (filter(lambda _x: not _x.has_cn, self))
        cla = PerWorkList(val)
        return cla

    def build_unable(self):
        val = (filter(lambda _x: not _x.is_able_work, self))
        cla = PerWorkList()

        list(map(lambda _x: cla.append_self(_x), val))

        return cla

    def build_able(self):
        val = (filter(lambda _x: _x.is_able_work, self))
        cla = PerWorkList(val)

        return cla

    def build_no_skip(self, filename):
        val = (filter(lambda _x: not _x.need_skip(filename), self))

        cla = PerWorkList(val)

        return cla

    def build_search(self, indexes):
        val = (map(lambda _x: self[_x], indexes))
        cla = PerWorkList(val)

        return cla

    def build_skip(self, filename):
        val = (filter(lambda _x: _x.need_skip(filename), self))

        cla = PerWorkList(val)

        return cla

    def get_new(self, item: collections.abc.Iterable):
        return PerWorkList(filter(lambda x: x not in self, item))


class PerSetting(BasicInfo):
    def __init__(self, name, val):
        super(PerSetting, self).__init__(name, val)

        self.val = self._val

        self._link_set: collections.Callable = None
        self._link_get: collections.Callable = None

    def __str__(self):
        return f"\n" \
            f"\tclass:PerHolder" \
            f"\tname：{self.name}\n" \
            f"\tval：{self.val}\n" \
            f"\tset_link：{self.set_link}\n" \
            f"\tset_link：{self.get_link}\n"

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def set_link(self):
        return self._link_set

    @set_link.setter
    def set_link(self, func: collections.abc.Callable):
        if isinstance(func, collections.abc.Callable):
            self._link_set = func

    @property
    def get_link(self):
        return self._link_get

    @get_link.setter
    def get_link(self, func):
        if isinstance(func, collections.abc.Callable):
            self._link_get = func

    @property
    def value(self):
        return self.val

    def set_value(self):
        if isinstance(self.set_link, collections.abc.Callable):
            self.set_link(self.val)

    def get_value(self):
        if isinstance(self.get_link, collections.abc.Callable):
            self.val = self.get_link()


class PattenEdit(PerSetting):
    def __init__(self, name, val):
        super(PattenEdit, self).__init__(name, val)
        if not isinstance(val, list):
            raise TypeError
        self.format_work = lambda x: f'文件夹：{x["dir"]},格式：{x["pattern"]}'
        self._value = list(map(self.format_work, val))

    def __str__(self):
        return f"\n" \
            f"\tclass:PattenEdit\n" \
            f"\tname：{self.name}\n" \
            f"\tval：{self.val}\n" \
            f"\tset_link：{self.set_link}\n" \
            f"\tset_link：{self.get_link}\n"

    def __getitem__(self, item):
        return self.val[item]

    def __len__(self):
        return len(self.val)

    def set_value(self):
        if isinstance(self.set_link, collections.abc.Callable):
            self._value = list(map(self.format_work, self.val))
            self.set_link(self._value)

    def append(self, info_dict):
        index = len(self.val)
        self.val.append(info_dict)
        self._value.append(self.format_work(info_dict))
        return index

    def delete(self, index):
        del self.val[index]
        del self._value[index]
        val = index - 1
        if val < 0:
            return 0
        else:
            return val

    def move_up(self, index):
        if index > 1:
            temp = self.val[index - 1]
            self.val[index - 1] = self.val[index]
            self.val[index] = temp

            self._value[index - 1] = self.format_work(self.val[index - 1])
            self._value[index] = self.format_work(self.val[index])
            return index - 1
        else:
            return index

    def move_down(self, index):
        if index < len(self.val):
            temp = self.val[index + 1]
            self.val[index + 1] = self.val[index]
            self.val[index] = temp

            self._value[index + 1] = self.format_work(self.val[index + 1])
            self._value[index] = self.format_work(self.val[index])
            return index + 1
        else:
            return index


class SettingHolder(object):
    def __init__(self, setting: dict = None):
        self._info_dict = {}

        self._key_list = []
        self.able = []

        if setting is not None and isinstance(setting, dict):
            self.from_dict(setting)

    def __getattr__(self, item):

        if item in self._key_list:
            return self._info_dict[item]
        else:
            raise AttributeError

    def __setattr__(self, key, value):

        if key in ['_info_dict', '_key_list', 'able']:
            super(SettingHolder, self).__setattr__(key, value)
        else:
            if key not in self._key_list:
                self._key_list.append(key)
                if isinstance(value, list):
                    self._info_dict[key] = PattenEdit(key, value)
                else:
                    self._info_dict[key] = PerSetting(key, value)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __getitem__(self, item):
        self.__getattr__(item=item)

    def __str__(self):
        val = functools.reduce(lambda x, y: f'{x}\n\t{y.name}：{y}', self._info_dict.values(), f'class:\tSettingHolder')

        return val

    def to_dict(self):
        val = self._info_dict
        var = {}
        for key in val.keys():
            var[key] = val[key].val

        return dict(var)

    def from_dict(self, setting: dict):
        keys = setting.keys()
        values = setting.values()
        list(map(self.__setattr__, keys, values))

    def link_val(self, key, link_set, link_get):
        if key in self._key_list:
            self._info_dict[key].set_link = link_set
            self._info_dict[key].get_link = link_get

    def link_dict(self, val: dict):
        list(map(lambda x: self.link_val(x, val[x][0], val[x][1]), val.keys()))

    def initial_val(self):
        val = self._key_list
        list(map(lambda x: self._info_dict[x].set_value(), val))

    def get_value(self):
        val = self._key_list
        list(map(lambda x: self._info_dict[x].get_value(), val))


class PerEdit(BasicInfo):
    def __init__(self, name, val, has_cn: bool = False):
        super(PerEdit, self).__init__(name, val)

        if val == name or has_cn:
            self.has_cn = True
        else:
            self.has_cn = False

        self.get_show = lambda x: f"{x}）键->{self.name}；值->{self.val}"
        self.get_search = lambda: f"{self.name}{self.val}"

    def set_has_cn(self, bo: bool = False):
        self.has_cn = bo


class NamesEdit(BasicInfoList):
    def __init__(self, names=None):

        self.for_show = list()
        self.for_search = list()
        super().__init__(names)

    def __setitem__(self, key, value: PerEdit):

        if key in self:

            index = self._key_list.index(key)
            self._key_list[index] = key

            self.for_show[index] = value.get_show(index + 1)
            self.for_search[index] = value.get_search()
        else:
            self._key_list.append(key)

            self.for_show.append(value.get_show(len(self)))
            self.for_search.append(value.get_search())
        self._info_dict[key] = value

    def __delitem__(self, key):
        super(NamesEdit, self).__delitem__(key)
        self.for_show = [self[index].get_show(index + 1) for index in range(len(self))]
        self.for_search = [self[index].get_search() for index in range(len(self))]

    @staticmethod
    def form_dict(values: dict = None):

        if values is None:
            values = {}
        return NamesEdit([PerEdit(key_, value_, True) for key_, value_ in values.items()])

    def extend(self, values):
        if isinstance(values, collections.abc.Iterable):
            list(map(lambda _x: self.append_self(PerEdit(_x.name, _x.val, _x.has_cn)), values))

    def for_dict(self):
        var = {}
        for key in self._key_list:
            var[key] = self[key].val
        return var

    def append(self, key, value, has_info=False):
        if key in self:
            if not has_info:
                var = wx.MessageBox(f"该键：\t{key}\t已经存在了，继续将会覆盖原有值！", '提示', wx.YES_NO)
                if var == wx.YES:
                    self.edit(key, value)
            else:
                self.edit(key, value)
            return True
        else:
            self[key] = PerEdit(key, value, True)
            return False

    def edit(self, index, value, has_cn=False):
        val: PerEdit = self[index]
        val.val = value
        val.set_has_cn(has_cn)

        self[val.name] = val

    def del_name(self, index):
        del self[index]

    def append_self(self, value):

        if isinstance(value, PerWork):
            val = PerEdit(value.name, value.val, value.has_cn)
            self[value.name] = val
        elif isinstance(value, PerEdit):
            self[value.name] = value

        else:
            raise ValueError(f'{type(value)}is not able')

    @property
    def show(self):
        return self.for_show

    def build_search(self, indexes):
        val = (self[index] for index in indexes)
        return NamesEdit(val)

    def build_cn(self):
        val = filter(lambda x: x.has_cn, self)
        return NamesEdit(val)

    def append_name(self, name, val, *, has_cn=False):
        if name not in self._info_dict:
            self[name] = PerEdit(name, val, has_cn=has_cn)
        else:
            pass

        return name

    def _mix(self, dicts: dict):
        for key in dicts.keys():
            if key in self:
                self.edit(key, dicts[key])
            else:
                self.append(key, dicts[key], True)

    def mix(self, *values):
        for value in values:
            self._mix(value)

    def build_has(self):
        var = map(lambda x: not x.has_cn, self)
        return NamesEdit(var)


class TeamWork(object):
    def __init__(self, group_t, *args):
        """

        :param group: set able work
        :param args: else need else work method keys and values
            ->key1=[method1-t,method1-f], key2=[method2-t,method2-f], ...
        """
        self.group_t = group_t

        self.args = args

    def __call__(self, val: bool):
        list(map(lambda x: x.Enable(val), self.group_t))

        if val:
            list(map(lambda x: x[0](), self.args))
        else:
            list(map(lambda x: x[1](), self.args))


if __name__ == '__main__' and False:
    a = PerWorkList()
    d = ['ass', 'asss', 'assss', 'asssss', 'assssss']
    a.append_name('ass', {})
    a.append_name('asss', {})
    a.append_name('assss', {})
    a.append_name('asssss', {})
    a.append_name('assssss', {})

    # for x in a:
    #    print(x)
    print()
    # print(a.for_search)
    # print(a.for_show)
    # print(list(filter(lambda x: x.name[0:2] == "as", a)))
    c = a.build_skip(d, )
    for gg in c:
        print(gg)

if __name__ == '__main__':
    # print(dict == list)
    b = {"open_dir": True, "skip_had": True, "auto_open": True, "finish_exit": False, "clear_list": True,
         "save_all": False, "dir_menu": False, "dir_bg": False}
    a = SettingHolder(b)
    # print(a.to_dict())
    print(a.__dict__)
    a.skip_had.set_link = lambda x: print(x)
    a.skip_had.get_value()
    print(a)
    print(a.skip_had)
    # print(a)

if __name__ == '__main__' and False:
    n = {'a': 1, 'b': 2, 'n': 3, 'c': 4, 'd': 5, }
    a = NamesEdit.form_dict(n)
    print(a.__dict__)
    print(a.for_show)
