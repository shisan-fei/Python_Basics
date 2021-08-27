'''
迭代是python访问集合元素的以种方式
迭代器是一个可以记住遍历的位置的对象
迭代器从集合第一个元素访问，直到访问完，只能前进不能后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表，元组都可以创建迭代器。
'''


list=[1,2,3,4]
it = iter(list)   #iter():创建一个迭代器对象。


def blsc():
    print("使用循环输出迭代器内容")
    for i in it:
        print(i,end=" ")  #end=意思是，在末尾添加空格而不是换行符。即不换行输出。

def nextsc():
    print("使用next输出迭代器下一个元素：")
    while True:
        try:
            print(next(it),end=" ")  #使用next()依次读取迭代器下一个内容。
        except StopIteration:        #异常处理，遇到StopIteration就退出循环。
            break


blsc()
#nextsc()

