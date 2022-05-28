#!/bin/python3

import tkinter as tk
import pickle
from tkinter import messagebox

root = tk.Tk()
root.title('欢迎登录')
root.geometry('450x300')
tk.Label(root,text='用户名').place(x=100, y=70)
tk.Label(root,text='密  码').place(x=100, y=110)
name_val = tk.StringVar()
password_val = tk.StringVar()
into_name = tk.Entry(root, textvariable=name_val )
into_name.place(x=160, y=70)
into_password = tk.Entry(root, textvariable=password_val, show="*")
into_password.place(x=160, y=110)

def usr_login():
    usr_name = name_val.get()
    usr_password = password_val.get()
    try:
        with open("info.pickle","rb") as usr_file:
            info = pickle.load(usr_file)
    except FileExistsError:
        with open("info.pickle","wb") as usr_file:
            info = {'admin': 'admin'}
            pickle.dump(info,usr_file)

    if usr_name in info:
        if usr_password == info[usr_name]:
            messagebox.showinfo(title='Wellcome',message=usr_name+':emmmmmm...')
        else:
            messagebox.showinfo(message='Error,please try again')
    else:
        is_sign_up = messagebox.askyesno('Attention','please sign up')
        print(is_sign_up)
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sign_to():
        new_password = new_repassword_val.get()
        new_repassword = new_repassword_val.get()
        new_name = new_name_val.get()
        with open("info.pickle","rb") as usr_file:
            exit_info = pickle.load(usr_file)
            if new_password != new_repassword:
                messagebox.showerror('Error attention','new_repassword and new_password are not same')
            elif new_name in exit_info:
                messagebox.showerror('Error attention','usr is exit')
            else:
                exit_info[new_name] = new_password
                with open("info.pickle","wb") as usr_file:
                    pickle.dump(exit_info,usr_file)
                messagebox.showinfo('Wellcome','You are successful')
    middle = tk.Tk()
    middle.title('用户注册')
    middle.geometry('450x300')
    tk.Label(middle,text='用户名').place(x=100, y=70)
    tk.Label(middle,text='密  码').place(x=100, y=110)
    tk.Label(middle,text='确认密码').place(x=100, y=150)
    new_name_val = tk.StringVar()
    new_password_val = tk.StringVar()
    new_repassword_val = tk.StringVar()
    into_new_name = tk.Entry(middle,textvariable=new_name_val)
    into_new_name.place(x=160, y=70)
    into_new_password = tk.Entry(middle,textvariable=new_password_val, show='*')
    into_new_password.place(x=160 ,y=110)
    into_new_repassword = tk.Entry(middle,textvariable=new_repassword_val, show='*')
    into_new_repassword.place(x=160, y=150)
    login_in = tk.Button(middle,text='注册',command=sign_to)
    login_in.place(x=250,y=200)


login = tk.Button(root,text="登录",command=usr_login)
login.place(x=150, y=200)
sign_up = tk.Button(root,text="注册",command=usr_sign_up)
sign_up.place(x=250, y=200)

root.mainloop()
