import os

import pygame


class CutSpace(object):

    def __init__(self):
        self._xy = ()
        self._size = ()
        self._orig = (0, 0)
        self._offset = (0, 0)
        self._rotate = False

    def cuter(self, pic):
        """cut every part """
        """[pygame.Surface,(x,y)]:returns"""

        cut_sp = pygame.Rect(self._xy, self._size)
        if self._rotate:
            cut_sp = pygame.Rect(self._xy, self._size[::-1])

            cut = pic.subsurface(cut_sp)
            cut = pygame.transform.rotate(cut, -90)
        else:
            cut = pic.subsurface(cut_sp)

        x, y = self._xy

        return [cut, (x, y)]

    def add_xy(self, x, y):
        self._xy = (x, y)

    def add_size(self, size_x, size_y):
        self._size = (size_x, size_y)

    def add_rotate(self, bool=False):
        self._rotate = bool

    def add_orig(self, orig_x, orig_y):
        self._orig = (orig_x, orig_y)

    def add_offset(self, offset_x, offset_y):
        self._offset = (offset_x, offset_y)

    def all_to_0(self):
        self._xy = ()
        self._size = ()
        self._orig = (0, 0)
        self._offset = (0, 0)
        self._rotate = False


def body_cut(name):
    try:
        os.makedirs("out\\" + name)
    except FileExistsError:
        pass

    pygame.init()
    pic = pygame.image.load("Texture2D\\" + name + ".png")
    space = {'body_part': {}}
    loader = CutSpace()
    in_part = None

    with open("TextAsset\\" + name + ".atlas.txt", 'r')as info:
        for line in info.readlines():

            line = line[:-1]

            if not line:
                continue

            elif line[-3:] == "png":
                space['name'] = line[:-4]

            elif line[0:4] == "size":
                line = line[5:]
                line = line.split(',')
                line = [int(line[0]), int(line[1])]
                space['size'] = line

            elif line[:6] == "format":
                space["format"] = line[8:-4]

            elif line[:6] == "filter":
                line = line[8:]
                line = line.split(',')
                space["filter"] = line

            elif line[:6] == "repeat":
                if line[8:] == 'none':
                    space['repeat'] = None
                else:
                    space['repeat'] = line[8:]

            else:
                if line[0] != ' ':
                    in_part = line
                    space['body_part'][line] = None
                    loader.all_to_0()

                elif line[0] == ' ':
                    line = line[2:]

                    if line[:6] == 'rotate':
                        line = line[8:]
                        if line == "false":
                            loader.add_rotate(False)
                        elif line == "true":
                            loader.add_rotate(True)

                    elif line[:2] == 'xy':
                        line = line[4:]
                        line = line.split(',')
                        line = [int(line[0]), int(line[1])]
                        loader.add_xy(line[0], line[1])

                    elif line[:4] == 'size':
                        line = line[6:]
                        line = line.split(',')
                        line = [int(line[0]), int(line[1])]
                        loader.add_size(line[0], line[1])

                    elif line[:4] == 'orig':
                        line = line[6:]
                        line = line.split(',')
                        line = [int(line[0]), int(line[1])]
                        loader.add_orig(line[0], line[1])

                    elif line[:6] == "offset":
                        line = line[8:]
                        line = line.split(',')
                        line = [int(line[0]), int(line[1])]
                        loader.add_offset(line[0], line[1])

                    elif line[:5] == "index":
                        space['body_part'][in_part] = loader.cuter(pic)

    i = 0
    for key in space['body_part'].keys():

        if space['body_part'][key][0] is None:
            continue

        else:

            pygame.image.save(space['body_part'][key][0], "out\\" + name + "\\" + str(i) + ".png")

        i += 1

    return True
