import os

import PIL.Image as img_pak


def girl_front_line_restore(pic_path, pic_alpha, save_path):
    pic = img_pak.open(pic_path, 'r')
    pic_a = img_pak.open(pic_alpha, 'r')

    out = img_pak.new("RGBA", pic.size, (255, 255, 255, 0))
    alpha = img_pak.new("RGBA", pic.size, 0)
    alpha_1 = img_pak.new("L", pic.size, 0)
    pic_a = pic_a.resize(pic.size, img_pak.ANTIALIAS)
    alpha.paste(pic_a, (0, 0, pic.size[0], pic.size[1]))

    out.paste(pic, (0, 0, pic.size[0], pic.size[1]))
    # alpha = alpha.rotate(90)
    # alpha = alpha.transpose(img_pak.FLIP_LEFT_RIGHT)
    date = list(alpha.getdata(3))
    d = 0
    # out.putalpha(alpha_1)
    for x in range(len(date)):
        if date[x] == 0:
            i = x
            x = i % pic.size[0]
            y = i // pic.size[0]
            temp = out.getpixel((x, y))
            out.putpixel((x, y), (temp[0], temp[1], temp[2], 0))
        else:
            index = x
            x = index % pic.size[0]
            y = index // pic.size[1]
            temp = out.getpixel((x, y))
            out.putpixel((x, y), (temp[0], temp[1], temp[2], date[index]))
            d += 1

    pic_path = pic_path.split("\\")[-1]
    pic_path = pic_path[4:]
    pic_path = pic_path.split('.')[0]

    out.save("%s\\%s.png" % (save_path, pic_path))


path = input("导入文件夹位置")
save = input("导出文件夹位置")
a = os.listdir(path)
b = {}
c = {}
for i in a:
    if i.split("_")[-1].lower() == "Alpha.png".lower():
        b[i[:-10]] = i
    elif i.split("_")[-1].lower() == "N.png".lower():
        continue
    else:
        c[i[:-4]] = i
i = 0
for keyes in b.keys():
    i += 1
    print(i)

    girl_front_line_restore(c[keyes], b[keyes], save)
