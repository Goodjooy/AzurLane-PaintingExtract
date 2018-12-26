import os
import collections


class PerInfo(object):
    def __init__(self, name, name_cn):

        self.tex_path = ''
        self.mesh_path = ''
        self.save_path = ''

        self.lay_in = ''

        self.name = name
        if name == name_cn:
            self.has_cn = False
        else:
            self.has_cn = True

        self.name_cn = name_cn
        self.is_able_work = False

        self.is_skip = False

        self.set_ex_as_cn = True

    def __str__(self):
        return f'Key:{self.name}\n' \
            f'Name:{self.name_cn}\n' \
            f'Tex:{self.tex_path}\n' \
            f'Mesh:{self.mesh_path}\n' \
            f'Save at:{self.save_path}\n'

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
        name_cn = self.name_cn
        name = self.name

        if name_cn + '.png' in keys:
            self.is_skip = True
            self.lay_in = files[name_cn + '.png']
        if name + '.png' in keys:
            self.is_skip = True
            self.lay_in = files[name + '.png']

        else:
            self.is_skip = False

        return self.is_skip

    def add_save(self, save_path):
        if self.set_ex_as_cn:
            self.save_path = os.path.join(save_path, self.name_cn)
        else:
            self.save_path = os.path.join(save_path, self.name)

    def get_show(self, index=0):
        return f'{index}）:{self.name_cn}——{self.name};(@_@)'

    def get_search(self):
        return f'{self.name}{self.name_cn}'

    def update_name(self, names: dict):
        if self.name in names.keys():
            self.name_cn = names[self.name]
        else:
            self.name_cn = self.name


class KeyExistError(KeyError):
    def __init__(self, arg):
        self.arg = arg


class PerInfoList(object):
    def __init__(self, item: collections.Iterable = None):

        self._info_dict = {}

        self._info_key_list = []

        self.for_search = []

        self.for_show = []

        self.start = 0
        self.index = 0

        if isinstance(item, collections.Iterable):
            self.extend(item)

    def __delitem__(self, key):
        if isinstance(key, int):
            key = self._info_key_list[key]
        else:
            pass
        del self._info_dict[key]
        index = self._info_key_list.index(key)
        del self.for_show[index]
        del self.for_search[index]

    def __getitem__(self, item):
        """

        :param item:
        :return: PerInfo
        """
        if isinstance(item, int):
            return self._info_dict[self._info_key_list[item]]
        else:
            return self._info_dict[item]

    def __setitem__(self, key: str, value: PerInfo):
        if key in self._info_dict.keys():
            raise KeyExistError("KeyExist!")

        else:
            self._info_dict[key] = value
            self._info_key_list.append(key)
            self.for_show.append(value.get_show(len(self)))
            self.for_search.append(value.get_search())

    def __iter__(self):
        self.index = self.start
        return self

    def __next__(self):
        if self.index >= len(self._info_key_list):
            raise StopIteration
        else:
            val = self._info_dict[self._info_key_list[self.index]]

            self.index += 1

            return val

    def __str__(self):
        return str(list(zip(self._info_key_list, self._info_dict.values())))

    def __len__(self):
        return len(self._info_key_list)

    def __bool__(self):
        if len(self) <= 0:
            return False
        else:
            return True

    def __contains__(self, item):
        if isinstance(item, str):
            return item in self._info_key_list
        if isinstance(item, PerInfo):
            return item in self._info_dict.values()
        else:
            return False

    def remove(self, item: collections.Iterable):
        return PerInfoList(filter(lambda x: x in item, self))

    def append_name(self, name, names_key):

        if name in names_key.keys():
            name_cn = names_key[name]
        else:
            name_cn = name
        if name not in self._info_dict:
            self[name] = PerInfo(name, name_cn)
        else:
            pass

        return name

    def append_self(self, value):
        if isinstance(value, PerInfo):
            self[value.name] = value
        else:
            raise ValueError(f'{type(value)}is not able')

    def extend(self, values):
        if isinstance(values, collections.Iterable):
            list(map(lambda _x: self.append_self(_x), values))

    def set_tex(self, key, path):
        self._info_dict[key].add_tex(path)

    def set_mesh(self, key, path):
        self._info_dict[key].add_mesh(path)

    def set_save(self, key, path):
        self._info_dict[key].add_save(path)

    def clear(self):
        self._info_key_list.clear()
        self._info_dict.clear()
        self.for_search.clear()
        self.for_show.clear()

    def up_date_name_cn(self, name_cn: dict):
        list(map(lambda _x: _x.update_name(name_cn), self))

    def is_in_dict(self, item):
        return item not in self._info_dict.keys()

    def build_unable(self):
        val = (filter(lambda _x: not _x.is_able_work, self))
        cla = PerInfoList()

        list(map(lambda _x: cla.append_self(_x), val))

        return cla

    def build_able(self):
        val = (filter(lambda _x: _x.is_able_work, self))
        cla = PerInfoList()

        list(map(lambda _x: cla.append_self(_x), val))

        return cla

    def build_skip(self, filename):
        val = (filter(lambda _x: _x.need_skip(filename), self))
        cla = PerInfoList(val)

        return cla

    def build_search(self, indexes):
        val = (map(lambda _x: self[_x], indexes))
        cla = PerInfoList()

        list(map(lambda _x: cla.append_self(_x), val))

        return cla


if __name__ == '__main__':
    a = PerInfoList()
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
