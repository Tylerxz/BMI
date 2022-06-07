import tkinter
from tkinter import *
import tkinter.messagebox as messagebox
question=tkinter.Tk()
question.withdraw()
messagebox.showinfo('提示', '此程序为xz制作，版权所有，侵权必究')

class Application():
    def __init__(self,windowName):
        self.windowName = windowName

    def windowBox(self):
        #标题和标签
        self.windowName.title("BMI计算器-高级版")
        self.windowName.geometry('605x150+550+150')
        self.LeftWindowLabel =Label(self.windowName,text="请输入身高：",padx=100)
        self.LeftWindowLabel.grid(column=0,row=0) 
        self.RightWindowLabel = Label(self.windowName,text="BMI指数")
        self.RightWindowLabel.grid(column=4,row=0)
        self.LeftDownLabel = Label(self.windowName,text="请输入体重：")
        self.LeftDownLabel.grid(column=0,row=4)

        #文本框
        self.LeftText = Text(self.windowName,width=20,height=1)
        self.LeftText.grid(column=0,row=1,rowspan=2,columnspan=2)
        self.RightText = Text(self.windowName,width=31,height=5)
        self.RightText.grid(column=4,row=1,rowspan=2,columnspan=2)
        self.LeftDownText = Text(self.windowName,width=20,height=1)
        self.LeftDownText.grid(column=0,row=7,rowspan=2,columnspan=2)

        #按钮
        self.TransButton = Button(self.windowName,text="开始计算",command=self.bmi_calculate,width=10)
        self.TransButton.grid(column=2,row=2)

    def bmi_calculate(self):
        a=float(self.LeftText.get(1.0,END))
        b=float(self.LeftDownText.get(1.0,END))
        bmi=b/((a/100)**2)
        self.RightText.delete(1.0,END)
        if bmi<18.5:
            self.RightText.insert(1.0,"你的BMI值：%s；身体状态：偏瘦"%bmi)
        elif bmi<24:
            self.RightText.insert(1.0,"你的BMI值：%s；身体状态：正常"%bmi)
        elif bmi<28:
            self.RightText.insert(1.0,"你的BMI值：%s；身体状态：偏胖"%bmi)
        else:
            self.RightText.insert(1.0,"你的BMI值：%s；身体状态：肥胖"%bmi)

def GUI():
    window = Tk()
    app = Application(window)
    app.windowBox()
    window.mainloop()

GUI()
