import re
import os.path as op


def file_deal(paths, set_list: list, list_search: list, list_enter: list, file_path: dict, clear_list: bool = False,
              pattern=r'^[.\n]*$', is_file=True, replace_str: str = '', names: dict = None, start: int = 0):
    """

    :param clear_list: is need clear the list
    :param start: the start index list
    :param paths: DirPicker path or FilePicker files
    :param set_list: the list save the keys
    :param list_search: the list to search
    :param list_enter: the list to show
    :param file_path: the dict of loaded files
    :param pattern: the pattern of the base_filename
    :param is_file: a bool of the load type bool True->FilePicker,False->DirPicker
    :param replace_str: the need replace string in the base filename
    :param names: the Chinese-base_name dict
    :return: if do not raise any error and worked bool->True,else bool->False
    """
    try:
        if clear_list:
            set_list.clear()
            list_enter.clear()
            list_search.clear()
        num = start
        pattern_re = re.compile(pattern)
        if not is_file:
            dict_path = paths.copy()
            paths = paths.keys()
        else:
            dict_path = {}

        if not len(paths) == 0:

            for path in paths:

                if pattern_re.match(path) is not None:
                    num += 1
                    if not is_file:
                        name = path
                        path = dict_path[name]
                        name = op.splitext(name)[0].replace(replace_str, '')
                    else:
                        name = op.splitext(op.basename(path))[0].replace(replace_str, '')
                    if name not in set_list:
                        file_path[name] = path
                        set_list.append(name)
                        try:
                            list_enter.append(f"{num}）{names[name]}——{name}")
                            list_search.append(f"{names[name]}{name}")
                        except KeyError:
                            list_enter.append(f"{num}）{name}——{name}")
                            list_search.append(f"{name}")
                else:
                    continue
        else:
            return False
    except(TypeError, KeyError, RuntimeError):
        return False
    else:
        return True
