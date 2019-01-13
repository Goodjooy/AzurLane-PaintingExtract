import json

val=None
with open ('names.json','r')as file:
    val=json.load(file)

key=input('请输入键：\t')
name=input('请输入值：\t')

if name in val.keys():
    print('注意，该操作将会覆盖原有的%s的值：%s'%(key,val[key]))
    if input('确认继续？（y/n）')=='y':
        val[key]=name
else:
    cal[key]=name
with open('names.json','w')as file:
    json.dump(val,file)
print('done')
input()