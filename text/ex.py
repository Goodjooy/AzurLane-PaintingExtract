import json
with open('1.txt', 'r', encoding='utf-8')as file:
    info = file.readlines()
    print(info)
with open("2.txt", 'w', encoding='utf-8')as i:
    for e in info:
        a = 'r\'%s\',\n' % e[:-1].replace('\t',' ： ')
        print(a)
        i.write(a)
