import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title('欢迎登录')
window.geometry('450x300')
tk.Label(window, text='用户名').place(x=100, y=150)
tk.Label(window, text='密  码').place(x=100, y=190)
var_usr_name = tk.StringVar()
var_usr_pwd = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            messagebox.showinfo(title='欢迎光临', message=usr_name + '：请进入个人首页，查看最新资讯')
        else:
            messagebox.showinfo(message='错误提示：密码不对，请重试')
       
    else:
        is_sign_up = messagebox.askyesno('提示', '你还没有注册，请先注册')
        print(is_sign_up)
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
            if np != npf:
                messagebox.showerror('错误提示', '密码和确认密码必须一样')
            elif nn in exist_usr_info:
                messagebox.showerror('错误提示', '用户名早就注册了！')
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                    messagebox.showinfo('欢迎', '你已经成功注册了')
                    window_sign_up.destroy()
                    
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('欢迎注册')
    window_sign_up.geometry('360x200')
    new_name = tk.StringVar()
    new_name.set('amoxiang@163.com')
    tk.Label(window_sign_up, text='用户名').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=100, y=10)
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密码').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=100, y=50)
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='确认密码').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=100, y=90)
    btn_confirm_sign_up = tk.Button(window_sign_up, text=' 注册 ', command=sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=120, y=130)

btn_login = tk.Button(window, text=' 登录 ', command=usr_login)
btn_login.place(x=150, y=230)
btn_sign_up = tk.Button(window, text=' 注册 ', command=usr_sign_up)
btn_sign_up.place(x=250, y=230)

window.mainloop()
