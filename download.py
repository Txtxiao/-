import json
import urllib.request,urllib.parse
from urllib.request import quote, unquote
import zipfile
import os

f=open('sample.json',encoding='utf-8')
res=f.read()
data=json.loads(res)
print(data)

cases=data['3544']['cases']
print(cases)


for case in cases:
        print(case['case_id'],case['case_type'])

        filename=urllib.parse.unquote(os.path.basename(case['case_zip']))
        print(filename)
        x = quote(case['case_zip'], safe=";/?:@&=+$,", encoding="utf-8")
        urllib.request.urlretrieve(x, filename)

dir_name = 'E:\大二下自学\数据科学基础\datatest'#你保存文件的路径
extension = ".zip"
os.chdir(dir_name) # 将工作路径换到你保存文件的路径
for item in os.listdir(dir_name): # 遍历文件夹中所有文件
    if item.endswith(extension): # 寻找 ".zip" 结尾的文件
        file_name = os.path.abspath(item) # 获取带文件名的文件完整路径
        zip_ref = zipfile.ZipFile(file_name) # 创建zip 对象
        os.mkdir(file_name.replace(".zip","")) # 创建同名子文件夹
        zip_ref.extractall(file_name.replace(".zip","")) # 解压zip文件内容到子文件夹
        zip_ref.close() # 关闭zip文件
        os.remove(file_name) # 删除同名zip文件








'''
for k,y in data.items():
    cases=data[k]['cases']
    print(cases)


    for case in cases:
        print(case['case_id'],case['case_type'])

        filename=urllib.parse.unquote(os.path.basename(case['case_zip']))
        print(filename)
        x = quote(case['case_zip'], safe=";/?:@&=+$,", encoding="utf-8")
        urllib.request.urlretrieve(x, filename)
        '''





