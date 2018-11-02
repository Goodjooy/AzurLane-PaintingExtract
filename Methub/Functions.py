import PIL.Image
import numpy


def girl_font_line_restore(pic_path, pic_alpha, save_path, is_one=False):
    pic = PIL.Image.open(pic_path, 'r')
    pic_a = PIL.Image.open(pic_alpha, 'r')

    out = PIL.Image.new("RGBA", pic.size, (255, 255, 255, 0))
    alpha = PIL.Image.new("RGBA", pic.size, 0)

    pic_a = pic_a.resize(pic.size, PIL.Image.ANTIALIAS)
    alpha.paste(pic_a, (0, 0, pic.size[0], pic.size[1]))

    out.paste(pic, (0, 0, pic.size[0], pic.size[1]))

    alpha_list = numpy.asarray(alpha)
    alpha_list = alpha_list[:, :, -1]
    temp = numpy.asarray(out)
    temp = temp.copy()
    temp[:, :, -1] = alpha_list

    out = PIL.Image.fromarray(numpy.uint8(temp))

    pic_path = pic_path.split("\\")[-1]

    pic_path = pic_path.split('.')[0]
    if is_one:
        out.save(save_path)
    else:
        out.save("%s\\%s.png" % (save_path, pic_path))



