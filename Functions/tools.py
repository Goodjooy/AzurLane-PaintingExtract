import PIL.Image as pic_tools
import Functions.function as fn


def search(rgb, alpha, list_fond, name):
    temp_1 = pic_tools.open(rgb[name]).size
    temp_2 = pic_tools.open(alpha[name]).size

    if temp_1[0] == temp_2[0] * 2 and temp_1[1] == temp_2[1] * 2:
        return alpha
    else:
        indexes = fn.find(name, list_fond)

        vales = [list_fond[val] for val in indexes]

        for val in vales:
            temp_2 = pic_tools.open(alpha[val]).size

            if temp_1[0] == temp_2[0] * 2 and temp_1[1] == temp_2[1] * 2:
                temp = alpha[name]
                alpha[name] = alpha[val]
                alpha[val] = temp

        return alpha
