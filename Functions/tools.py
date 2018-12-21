import os
import re
import os.path as op
import functools


def info_write_builder(is_file, dict_path, replace_str, set_list, file_path, list_enter, names, list_search):
    def info_write(path):
        num = path[1] + 1
        if not is_file:
            name = path[0]
            path = dict_path[name]
            name = op.splitext(name)[0].replace(replace_str, '')
        else:
            name = op.splitext(op.basename(path[0]))[0].replace(replace_str, '')
        if name not in set_list:
            file_path[name] = path[0]
            set_list.append(name)
            try:
                list_enter.append(f"{num}）{names[name]}——{name}")
                list_search.append(f"{names[name]}{name}")
            except KeyError:
                list_enter.append(f"{num}）{name}——{name}")
                list_search.append(f"{name}")

    return info_write


def file_deal(paths, set_list: list, list_search: list, list_enter: list, file_path: dict, clear_list: bool = False,
              pattern=r'^[.\n]*$', is_file=True, replace_str: str = '', names: dict = None):
    """

    :param clear_list: is need clear the list
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
        if names is None:
            names = {}

        pattern_re = re.compile(pattern)
        if not is_file:
            dict_path = paths.copy()
            paths = paths.keys()
            num = len(paths)
        else:
            dict_path = {}
            num = len(set_list)

        if clear_list:
            set_list.clear()
            list_enter.clear()
            list_search.clear()
            num = 0

        if not len(paths) == 0:

            path = filter(lambda x: pattern_re.match(os.path.basename(x)) is not None, paths)
            path = list(path)

            info_write = info_write_builder(is_file, dict_path, replace_str, set_list, file_path, list_enter,
                                            names, list_search)

            path_len = len(path)
            paths = zip(path, range(path_len))

            paths = list(paths)

            num += len(list(map(info_write, list(paths))))

            if path_len == 0:
                return False, '导入完成，无新增项！'
        else:
            return False, '导入失败，无导入项！'
    except (TypeError, KeyError, RuntimeError)as info:
        return False, '导入失败，发生错误！%s' % info
    else:
        return True, '导入成功！ 成功导入%d个！' % num


def pattern_builder(x, y):
    """
    change pattern only char to avoid some problems
    :param x: str
    :param y: str
    :return: str
    """
    if re.match(r'[^.|+*?^$()\]\[\\]', y):
        return f'{x}.*{y}'
    else:
        return f'{x}.*\\{y}'


def find(string: str, array_enter: list):
    """
    search
    :param string: the key words for search
    :param array_enter: a list is searched
    :return: the enable index
    """
    str_search = functools.reduce(pattern_builder, string, '^') + '.*$'

    array_found = zip(array_enter, range(len(array_enter)))
    out = filter(lambda x: re.match(str_search, x[0], re.IGNORECASE), array_found)
    try:
        return list(zip(*out))[-1]
    except IndexError:
        return ()


def build_return_list(x, y):
    x = list(x)
    x.extend(y)
    return x


def all_file(dir_name, skip_type=r'^UISprite.+$'):
    """
    a function to get all file in a dir
    :param dir_name: the path to get all files
    :param skip_type: the file name pattern which are skipped
    :return: the all files path
    """
    list_keep = os.listdir(dir_name)

    skip_pattern = re.compile(skip_type, flags=re.IGNORECASE)
    out_list = filter(lambda x: os.path.isfile(dir_name + "\\" + x) and skip_pattern.match(x) is None, list_keep)
    out_list = map(lambda x: dir_name + "\\" + x, out_list)

    dir_list = filter(lambda x: os.path.isdir(dir_name + "\\" + x), list_keep)
    dir_list = map(lambda x: dir_name + "\\" + x, dir_list)
    dir_list = map(lambda x: all_file(x, skip_type), dir_list)

    out_list = list(out_list)
    dir_list = list(dir_list)

    return_list = functools.reduce(build_return_list, dir_list, out_list)

    return_list = list(return_list)

    return return_list


def all_file_path(dir_name):
    files = all_file(dir_name)

    return files


if __name__ == '__main__' and False:
    a = ["2222", "3333", "阿贝克隆比abeikelongbi", "阿芙乐尔afuleer", "阿赫野aheye", "爱宕aidang", "爱丁堡aidingbao",
         "埃尔德里奇aierdeliqi",
         "埃克赛特aikesaite", "埃米尔贝尔汀aimierbeierding", "埃塞克斯aisaikesi", "阿贾克斯ajiakesi", "阿基里斯ajilisi", "阿卡斯塔akasita",
         "鞍山anshan", "奥利克aolike", "奥马哈aomaha", "奥斯本aosiben", "阿瑞托莎aruituosha", "阿斯托利亚asituoliya", "阿武隈awuwei",
         "白露bailu", "舰猫-白鹰baiying", "浜风bangfeng", "半人马banrenma", "北安普顿beianpudun", "贝尔法斯特beierfasite",
         "北卡罗莱纳beikaluolaina", "贝利beili", "本森bensen", "标枪biaoqiang", "宾夕法尼亚binxifaniya", "比睿birui", "俾斯麦bisimai",
         "博格boge", "舰猫-伯克喵bokemiao", "波利斯bolisi", "波特兰botelan", "布鲁克林bulukelin", "布什bushi", "不知火buzhihuo",
         "苍龙canglong", "长春changchun", "长岛changdao", "长良changliang", "长门changmen", "赤城chicheng", "舰猫-重樱chongying",
         "川内chuannei", "初春chuchun", "吹雪chuixue", "春月chunyue", "初霜chushuang", "出云chuyun", "大潮dachao",
         "大斗犬dadouquan",
         "大凤dafeng", "大黄蜂dahuangfeng", "丹佛danfo", "大青花鱼daqinghuayu", "德意志deyizhi", "电dian", "独角兽dujiaoshou",
         "敦刻尔克dunkeerke", "舰猫-朵朵丸duoduowan", "多塞特郡duosaitejun", "俄克拉荷马ekelahema", "反击fanji", "斐济feiji",
         "飞龙feilong",
         "菲尼克斯feinikesi", "绯樱feiying", "凤祥fengxiang", "福尔班fuerban", "弗莱彻fulaiche", "扶桑fusang", "抚顺fushun",
         "福特fute",
         "高雄-和谐gaoxiong-hx", "高雄gaoxiong", "格里德利gelideli", "哥伦比亚gelunbiya", "格奈森瑙genaisennao", "紫布里gin",
         "光辉guanghui",
         "光荣guangrong", "谷风gufeng", "古鹰guying", "海伦娜hailunna", "海王星haiwangxing", "哈曼haman", "涅普顿HDN101",
         "诺瓦露HDN201",
         "布兰HDN301", "贝露HDN401", "黑暗界heianjie", "黑潮heichao", "heizewude", "潢潮huangchao", "舰猫-皇家huangjia",
         "皇家方舟huangjiafangzhou", "华盛顿huashengdun", "胡德hude", "胡蜂hufeng", "彗星huixing", "霍比huobi", "火奴鲁鲁huonululu",
         "火枪手huoqiangshou", "狐提huti", "伊-19i19", "伊-26i26", "伊-58i58", "加古jiagu", "加贺jiahe", "加拉蒂亚jialadiya",
         "加利福尼亚jialifuniya", "江风jiangfeng", "杰金斯jiejinsi", "肌风jifeng", "金刚jingang", "竞技神jingjishen", "君主junzhu",
         "卡尔斯鲁厄kaersilue", "凯旋kaixuan", "kangkede", "卡辛kaxin", "柯尔克keerke", "舰猫-克雷喵keleimiao", "克雷文keleiwen",
         "克利夫兰kelifulan", "科隆-uikelong-ui", "科隆kelong", "科罗拉多keluoladuo", "科尼斯堡-uikenisibao-ui", "科尼斯堡kenisibao",
         "肯特-和谐kente-hx", "肯特kente", "金布里kin", "恐怖kongbu", "昆西kunxi", "拉德福特ladefute", "拉菲lafei", "莱比锡laibixi",
         "兰利lanli", "雷lei", "勒马尔lemaer", "利安得liande", "列克星敦liekexingdun", "利根ligen", "凌波lingbo", "黎塞留lisailiu",
         "里士满lishiman", "陆奥luao", "鲁莽lumang", "伦敦lundun", "罗德尼luodeni", "罗恩luoen", "罗利luoli", "路易九世luyijiushi",
         "麦考尔maikaoer", "马里兰malilan", "满朝manchao", "卯月maoyue", "马萨诸塞masazhusai", "蒙彼利埃mengbiliai",
         "孟菲斯mengfeisi",
         "妙高miaogao", "明尼阿波利斯mingniabolisi", "明石mingshi", "命运女神mingyunnvshen", "莫里moli", "摩耶moye", "睦月muyue",
         "纳尔逊naerxun", "南达科他nandaketa", "那支nazhi", "内华达neihuada", "鸟海niaohai", "尼古拉斯nigulasi", "宁海ninghai",
         "纽卡斯尔niukasier", "诺福克nuofuke", "女将nvjiang", "欧根ougen", "欧若拉ouruola", "彭萨科拉pengsakela", "平海pinghai",
         "蒲风pufeng", "齐柏林qibolin", "亲潮qinchao", "晴野qingye", "丘比特qiubite", "企业qiye", "让.巴尔rangbaer", "热心rexin",
         "日向rixiang", "瑞鹤ruihe", "若叶ruoye", "如月ruyue", "萨福克safuke", "萨拉托加salatuojia", "三笠sanli", "三日月sanriyue",
         "叄魏sanwei", "撒切尔saqieer", "沙恩霍斯特shaenhuosite", "山城shancheng", "神风shenfeng", "圣地亚哥shengdiyage",
         "胜利shengli",
         "圣路易斯shengluyisi", "圣女贞德shengnvzhende", "声望shengwang", "神通shentong", "什罗普郡shiluopujun", "时雨shiyu",
         "舰猫-水手shuishou", "水无月shuiwuyue", "斯佩伯爵sipeibojue", "斯彭斯sipengsi", "松风songfeng", "隼鹰sunying",
         "苏塞克斯susaikesi",
         "太原taiyuan", "唐斯tangsi", "天后tianhou", "田纳西tiannaxi", "鲦鱼tiaoyu", "提尔比茨tierbici", "舰猫-铁血tiexue",
         "突击者tujizhe",
         "U-47U47", "U-557U557", "U-81U81", "罄UISprite", "未知舰娘unknown", "观察者αunknown1", "观察者βunknown2",
         "进化者unknown3",
         "塞壬-零unknown4", "威尔士亲王weiershiqinwang", "威奇塔weiqita", "文森斯wensensi", "雯月wenyue", "雾岛wudao", "无敌wudi",
         "五十铃wushiling", "翔凤xiangfeng", "翔鹤xianghe", "西奥xiao", "小猎兔犬xiaolietuquan", "小天鹅xiaotiane", "肖月xiaoyue",
         "谢菲尔特xiefeierde", "西弗吉尼亚xifujiniya", "夕立xili", "夕暮ximu", "西姆斯ximusi", "新月xinyue",
         "希佩尔海军上将xipeierhaijunshangjiang", "休斯顿xiusidun", "吸血鬼xixuegui", "夕张xizhang", "雪风xuefeng", "絮库夫xukufu",
         "亚利桑那yalisangna", "牙买加yamaijia", "阳炎yangyan", "盐湖城yanhucheng", "厌战yanzhan", "亚特兰大yatelanda", "野分yefen",
         "伊吹yichui", "伊利yili", "伊丽莎白yilishabai", "萤火虫yinghuochong", "伊势yishi", "逸仙yixian", "幽冥youming",
         "舰猫-约翰喵yuehanmiao", "约克yueke", "约克城yuekecheng", "约克公爵yuekegongjue", "z1z1", "z18z18", "Z19Z19",
         "Z20Z20",
         "Z21Z21", "Z23Z23", "z25z25", "z35z35", "Z46Z46", "女灶神zaoshen", "泽西zexi", "朝潮zhaochao", "榛名zhenming",
         "芝加哥zhijiage", "朱诺zhunuo", "最上zuishang"]
    b = find('ww.', a)
    print(b)
    print(a[b[0]])

if __name__ == '__main__':
    for d in all_file('E:\\jacky\\az2\\Texture2D'):
        print(d)
