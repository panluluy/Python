list1 = ['Jerry',[11,22]]
list2 = list1 # 只是赋值操作不叫拷贝操作
# 二者无法分开，list1的更改list2同时也跟着修改，因为指向的是同一个地址
print(list2)
print(id(list1),id(list2))

print("=======浅拷贝=======")
list3 = list1.copy()
list1[0]="louis"
print(list1[0],list3[0])
print(id(list1[0]),id(list3[0]))  # 浅拷贝时如果修改的是不可变类型，拷贝后的内存地址与原地址不一致

list1[1][0]="test"
print(list1[1][0],list3[1][0])  # 浅拷贝时如果修改的是可变类型，拷贝后的内存地址与原地址一致
print(id(list1[1][0]),id(list3[1][0]))

print("=======深拷贝=======")
import copy
list4 = copy.deepcopy(list1)
list1[1][0]="abc"
print(list1[1][0],list4[1][0])  # 深拷贝时如果修改的是可变类型，拷贝后的内存地址与原地址不一致
print(id(list1[1][0]),id(list4[1][0]))