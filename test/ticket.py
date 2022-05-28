import multiprocessing as wu
import time
import json   #按格式读取文件中的票数信息
import random



def reset():
        with open("dgy.txt","w") as wu_folder:
            dic={"quantity": 3,"SECOND_author":"wu zhao ting","THIRD_author":"dgy"}
            json.dump(dic, wu_folder)

def author():
        wu = [87, 90, 84, 76, 79, 86, 69, 68, 71, 89]
        for i in wu:  print(chr(i), end=' ')

def check(name):   #模拟查票，只是查看字典里面的票数

        with open("dgy.txt", "r") as f_read:
            dic = json.load(f_read)# 将文件中的数据解码成python数据格式即为字典

            time.sleep(0.5)  # 模拟网络延时来读取数据
            print("【 %s 】the number of remaining votes that the user logs in to view is [%s]" % (name, dic["quantity"]))

def pur_votes( name):

        with open("dgy.txt", "r") as f_read:
            dic = json.load(f_read)

            if dic["quantity"] > 0:
                dic["quantity"] -= 1
                time.sleep(0.5)  #与上同


                with open("dgy.txt", "w") as f_write:

                    json.dump(dic, f_write)

                    print("\n【 %s 】 Purchase of success" % name)
                    print("the number of votes remaining is[ %s ]" % dic["quantity"])

            else:
                print("Current number of tickets is：0 sheets")


def start(name, wu_lock):
        check(name)
        wu_lock.acquire()  #锁住共享变量
        pur_votes(name)
        wu_lock.release()  #释放共享变量

if __name__ == "__main__":

    wu_lock=wu.Lock()#定义锁

    reset()  #每次都将票数的默认值重置从而不用每次重新给文件写入数据
    ran_dom = []
    sum_cus = int(input("how many custorm will join: "))

    for num in range(0, sum_cus):
        nums = int(input("please enter custorm id: "))
        ran_dom.append(nums)

    for i in range(0,len(ran_dom)):  # 模拟输入的抢票人数从而进行客户端抢票
        ii=random.choice(ran_dom)
        p1 = wu.Process(target=start, args=("ID：%s" % ii, wu_lock))
        p1.start()

#使用random模拟实现一人可能出现抢购多票的情况
