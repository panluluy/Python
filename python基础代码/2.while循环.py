username = "pan"
password = '123456'

# 方式一：使用tag标签
tag = True
while tag:
    inp_user = input("请输入你的用户名：")
    inp_pass = input("请输入你的密码：")
    if inp_user == username and inp_pass == password:
        print("{x:-^20}".format(x="登录成功"))
        while tag:
            cmd = input(">>>>>>>")
            if cmd == 'q':
                tag = False
            else:
                print("正在执行{}命令".format(cmd))
        tag = False
    else:
        print("\033[0;30;41m用户名或密码错误！\033[0m")

# 方式二：使用break
while True:
    inp_user = input("请输入你的用户名：")
    inp_pass = input("请输入你的密码：")
    if inp_user == username and inp_pass == password:
        print("{x:-^20}".format(x="登录成功"))
        while True:
            cmd = input(">>>>")
            if cmd == "q":
                break  # 退出内层循环
            else:
                print("正在执行{}命令".format(cmd))
        break  # 退出外层循环
    else:
        print("\033[0;30;41m用户名或密码错误！\033[0m")