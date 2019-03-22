import hashlib
import requests
import random
import urllib
import json
url = 'https://openapi.youdao.com/api'
appKey = '48b7097834ad226e'
secretKey = 'ZmuDobuZe6X1bgovrtvzPbKCPHlsKMlN'
source = ['zh-CHS','EN']
sourcee = ['中文','英语']
ending = ['zh-CHS','EN','ja','ko']
endingg = ['中文','英语','日语','韩语']
print('*******这是一个很像c语言界面的程序*******')
print('**************翻译源语言****************')
for index in range(len(source)):
    val1 = '[' + str(index) + ']' + '    ' +  sourcee[index] + '    ' + source[index] 
    print (val1)
print('*************翻译目标语言***************')
for index in range(len(ending)):
    val2 = '[' + str(index) + ']' + '    ' +  endingg[index] + '    ' + ending[index]
    print (val2)
print('***************************************')
while(1):
    s = eval(input('请输入翻译的源语言序号: '))
    e = eval(input('请输入翻译的目标语言序号: '))
    if s >= len(source) or e >= len(ending):
        print('输入序号错误，请重新输入。')
        print('***************************************')
        continue
    fromLang = source[s]
    toLang = ending[e]
    salt = random.randint(1, 65536)
    q = input("请输入要翻译的文字：")
    sign = appKey+q+str(salt)+secretKey
    m = hashlib.md5(sign.encode(encoding='utf-8')).hexdigest()
    myurl = url+'?appKey='+appKey+'&q='+urllib.parse.unquote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+m
    try:
        r = requests.get(myurl)
        w = json.loads(r.text)
        tran = str(q) + ' : ' + str(w['translation'])
        print (tran)
        print('***************************************')
        y = input('是否继续 y/n: ')
        print('***************************************')
        if y in ['y','Y']:
            continue
        if y in ['N','n']:
            break
    
        
    except:
        print("产生异常，注意网络连接。")

