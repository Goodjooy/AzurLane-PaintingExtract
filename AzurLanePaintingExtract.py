import os
import sys

import Classes.FrameClasses

if __name__ == '__main__':
    path = os.path.split(os.path.realpath(sys.argv[0]))[0]

    Classes.FrameClasses.main_part(path)
