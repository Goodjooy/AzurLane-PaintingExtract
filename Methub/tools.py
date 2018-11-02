import os

import PIL.Image as Image


def get_longest(array_enter):
    return max([len(value) for value in array_enter])


def find(string, array_enter):
    # one->index two->value
    if not array_enter:
        return array_enter
    able_next = [[], []]
    indexes = range(get_longest(array_enter))
    text_val = string[0]
    able_index = []
    array_copy = [[index, array_enter[index]] for index in range(len(array_enter))]
    pass_list = []

    for index in indexes:
        for value in range(len(array_enter)):
            try:
                val1 = (array_copy[value][1][index]).lower()
            except IndexError:
                continue

            if val1 == text_val and value not in pass_list:
                able_next[0].append(value)
                able_index.append(value)
                pass_list.append(value)
                able_next[1].append(array_enter[value][index + 1:])

    string = string[1:]
    if len(able_next) >= 1 and len(string) > 0:
        value = find(string, able_next[1])
        able_index = []
        for index in value:
            able_index.append(able_next[0][index])
        return able_index
    else:
        return able_index


def all_file(dir_name):
    had = []
    list_keep = os.listdir(dir_name)
    out_list = []
    dir_list = []
    for file in list_keep:
        if not isfile(dir_name + "\\" + file) and not (file in had):
            dir_list.append(file)
        else:
            out_list.append(file)
    for file in dir_list:
        re_1 = all_file(dir_name + "\\" + file)
        had.extend(re_1)
        out_list.extend(re_1)

    return out_list


def all_file_path(dir_name):
    had = []
    list_keep = os.listdir(dir_name)
    diction = {}
    dir_list = []
    file_name_list = []
    file_list = []
    for file in list_keep:
        if not isfile(dir_name + "\\" + file) and not (file in had):
            dir_list.append(file)
        elif file.split(' ')[0] == "UISprite":
            pass
        elif file.split(' ')[-1][0] == "#":
            temp = file.split('\\')[-1].lower().replace('.png', '').split(" ")
            if temp[0].split("_")[-1].lower() == "alpha":
                temp = '_Alpha ' + temp[-1]
                file_list.append(file)
                file_name_list.append(file.replace(temp, "_again_Alpha"))
            else:
                temp = " " + temp[-1]
                file_list.append(file)
                file = file.replace(temp, "_again")
                file_name_list.append(file)

        else:
            file_list.append(file)
            file_name_list.append(file)
    for file in dir_list:
        re = all_file_path(dir_name + "\\" + file)
        had.extend(re[0])
        file_name_list.extend(re[0])
        for keys in re[1]:
            diction[keys] = re[1][keys]
    for index in range(len(file_name_list)):
        if not file_name_list[index] in had:
            diction[file_name_list[index]] = dir_name + "\\" + file_list[index]
            file_list[index] = dir_name + "\\" + file_list[index]

    return file_list, diction


def isfile(file):
    try:
        with open(file, 'r'):
            pass
    except FileNotFoundError:
        return False
    except PermissionError:
        return False
    else:
        return True


def search(rgb, alpha, list_fond, name):
    temp_1 = Image.open(rgb[name]).size
    temp_2 = Image.open(alpha[name]).size

    if temp_1[0] == temp_2[0] * 2 and temp_1[1] == temp_2[1] * 2:
        return alpha
    else:
        indexes = find(name, list_fond)

        vales = [list_fond[val] for val in indexes]

        for val in vales:
            temp_2 = Image.open(alpha[val]).size

            if temp_1[0] == temp_2[0] * 2 and temp_1[1] == temp_2[1] * 2:
                temp = alpha[name]
                alpha[name] = alpha[val]
                alpha[val] = temp

        return alpha
