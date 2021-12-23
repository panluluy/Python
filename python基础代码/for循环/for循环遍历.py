# for循环遍历
for i in range(1,10):
    print(i)

# for循环构造死循环
class MyRange():

    def __iter__(self):
        return self

    def __next__(self):
        return None

for i in MyRange():
    print("测试")