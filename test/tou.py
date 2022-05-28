import multiprocessing as multip
import time
import json
import random

def reset():
        with open("save.txt","w") as multip_folder:
            dic={"quantity": 3,"SECOND_author":"multip zhao ting","THIRD_author":"save"}
            json.dump(dic, multip_folder)

def author():
        multip = [87, 90, 84, 76, 79, 86, 69, 68, 71, 89]
        for i in multip:  print(chr(i), end=' ')

def check(name):
        with open("save.txt", "r") as f_read:
            dic = json.load(f_read)
            time.sleep(0.5)
            print("%s 用户登录时剩余[%s]张票" % (name, dic["quantity"]))

def pur_votes( name):

        with open("save.txt", "r") as f_read:
            dic = json.load(f_read)

            if dic["quantity"] > 0:
                dic["quantity"] -= 1
                time.sleep(0.5)
                with open("save.txt", "w") as f_write:
                    json.dump(dic, f_write)
                    print("\n%s 用户抢票成功！" % name)
                    print("剩余[ %s ]张票" % dic["quantity"])
            else:
                print("\n当前没有票\n")

def start(name, multip_lock):
        check(name)
        multip_lock.acquire()
        pur_votes(name)
        multip_lock.release()

if __name__ == "__main__":

    multip_lock=multip.Lock()
    reset()
    ran_dom = []
    sum_cus = int(input("有多少人参与："))
    for num in range(0, sum_cus):
        nums = int(input("输入他们的代号： "))
        ran_dom.append(nums)

    for i in range(0,len(ran_dom)):
        ii=random.choice(ran_dom)
        p1 = multip.Process(target=start, args=("ID：%s" % ii, multip_lock))
        p1.start()
