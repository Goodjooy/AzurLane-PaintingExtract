from typing import overload

import PIL.Image as i
import numpy

pic1 = i.open("1.png", 'r')
pic2 = i.open("2.png", "r")
pic2 = pic2.resize(pic1.size)
l = numpy.asarray(pic2)
l = l[:, :, -1]
a = numpy.asarray(pic1)
a = a.copy()
a[:, :, -1] = l

save = i.fromarray(numpy.uint8(a))

save.save('3.png')
print(a)


