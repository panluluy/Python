count = 1
while count<4:
    if count == 2:
        count += 1
        continue    # 跳出此次循环，继续下一次循环，使用continue，自增必须在前面，否则进入死循环
        print(">>>>>>>>>")  # pycharm自动识别后续的代码无效
    else:
        print("正在循环第{}次".format(count))
    count += 1