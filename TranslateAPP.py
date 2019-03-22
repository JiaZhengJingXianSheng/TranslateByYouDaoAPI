from tkinter import *
import hashlib
import requests
import random
import urllib
import json
import tkinter.messagebox
url = 'https://openapi.youdao.com/api'
appKey = '48b7097834ad226e'
secretKey = 'ZmuDobuZe6X1bgovrtvzPbKCPHlsKMlN'
fromLang = 'zh-CHS'
toLang = 'EN'
salt = random.randint(1, 65536)
class demo:
    def __init__(self):
        self.window = Tk()
        self.window.title("中英互译")
        self.window.geometry('600x400')
        titleImage = PhotoImage(file = "./image/welcome.gif")
        frame1 = Frame(self.window)
        frame1.pack()
        Label(frame1,image = titleImage).pack(side = 'top')
        frame2 = Frame(self.window)
        frame2.pack()
        label1 = Label(frame2 , text = "请输入中文",font=('Arial', 16),width = 10 )
        self.val = StringVar()
        entryVal = Entry(frame2,bd = 5,width = 40,textvariable = self.val)
        label1.pack(side = LEFT)
        entryVal.pack(side = LEFT)
        frame3 = Frame(self.window)
        frame3.pack()
        start = Button(frame3,text = "翻译",font=('Arial', 16),width = 15,bg='MintCream',command=self.run)
        start.pack()        
        self.window.mainloop()
    def run(self):
        self.q = self.val.get()
        sign = appKey+self.q+str(salt)+secretKey
        m = hashlib.md5(sign.encode(encoding='utf-8')).hexdigest()
        myurl = url+'?appKey='+appKey+'&q='+urllib.parse.unquote(self.q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+m
        
        try:
            r = requests.get(myurl)
            if r.status_code == 200:
                
                w = json.loads(r.text)
                text = w['web']
                self.b = ''
                for values in text:
                    self.b = self.b + str(values['key']) +'\n'
                    for trans in values['value'] :    
                        self.b = self.b + str(trans) +'\n'
            else:
                self.b = '网络错误'
            tkinter.messagebox.showinfo('结果', self.b)
        except:
            tkinter.messagebox.showerror('ERROR', '产生异常')

demo()
