import tkinter as tk
import os
from tkinter.constants import END, LEFT, W, Y
from tkinter.filedialog import *
from tkinter.messagebox import *

def new():
    global root,file_menu,text_pad
    root.title("未命名文件")
    file_menu = None
    text_pad.delete(1.0, END)

def open():
    global file_menu
    file_menu = askopenfilename(defaultextension=".md")
    if file_menu == "":
        file_menu = None
    else:
        root.title("记事本" + os.path.basename(file_menu))
        text_pad.insert(1.0,END)
        f = open(file_menu,"r")
        text_pad.insert(1.0, f.read())
        f.close()

def save():
    global file_menu
    try:
        f = open(file_menu,'w')
        msg = text_pad.get(1.0,'end')
        f.write(msg)
        f.close()
    except:
        save()

def sfas():
    global file_menu
    f = asksaveasfilename(initialfile="未命名.md",defaultextension=".md")
    file_menu = f
    fh = open(f,'w')
    msg = text_pad.get(2.0,END)
    fh.close()
    root.title("记事本" + os.path.basename(f))

def undo():
    global text_pad
    text_pad.event_generate("<<Undo>>")

def redo():
    global text_pad
    text_pad.event_generate("<<Redo>>")

def copy():
    global text_pad
    text_pad.event_generate("<<Copy>>")

def paste():
    global text_pad
    text_pad.event_generate("<<Paste>>")

def select_all():
    global text_pad
    text_pad.tag_add("sel","1.0","end")

def cut():
    global text_pad
    text_pad.event_generate("<<Cut>>")

def athor():
    showinfo(title="作者",message="GuoZhong-Z")

def power():
    showinfo(title="版权信息",message="this is a demo")

root = tk.Tk()
root.title('记事本')
root.geometry('800x500+100+100')

menu = tk.Menu(root,tearoff=False)

file_menu = tk.Menu(menu,tearoff=False)
file_menu.add_command(label='新建',command=new)
file_menu.add_command(label='打开',command=open)
file_menu.add_command(label='保存',command=save)
file_menu.add_command(label='另存为',command=sfas)
menu.add_cascade(label='文件', menu=file_menu)

edit_menu = tk.Menu(menu,tearoff=False)
edit_menu.add_command(label='撤销',command=undo)
edit_menu.add_command(label='全选',command=select_all)
edit_menu.add_command(label='重做',command=redo)
edit_menu.add_command(label='复制',command=copy)
edit_menu.add_command(label='粘贴',command=paste)
edit_menu.add_command(label='剪切',command=cut)
menu.add_cascade(label='编辑', menu=edit_menu)

about_menu = tk.Menu(menu,tearoff=False)
about_menu.add_command(label='作者',command=athor)
about_menu.add_command(label='版权',command=power)
menu.add_cascade(label='关于', menu=about_menu)

status_str_var = tk.StringVar()
status_str_var.set('字符数{}'.format(0))
status_lable = tk.Label(root,textvariable=status_str_var,bd=1,relief=tk.SUNKEN,anchor=tk.W)
status_lable.pack(side=tk.BOTTOM,fill=tk.X)

var_line = tk.StringVar()
line_lable = tk.Label(root,textvariable=var_line,width=1,bg='#faebd7',anchor=tk.N,font=15)
line_lable.pack(side=LEFT,fill=Y)

text_pad =tk.Text(root,font=15)
text_pad.pack(fill=tk.BOTH,expand=True)

scroll = tk.Scrollbar(text_pad)
scroll.pack(fill=Y,side=tk.RIGHT)
text_pad.config(yscrollcommand=scroll.set)
scroll.config(command=text_pad.yview)

root.config(menu=menu)
root.mainloop()
