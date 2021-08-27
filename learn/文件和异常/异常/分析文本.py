def count_word(filename):
    '''计算文件中有多少个单词'''
    try:
        with open(filename) as test_object:
            xiaoshuo = test_object.read()
    except FileNotFoundError:
        print('this file not exit')
    else:
        list1 = xiaoshuo.split()
        num = len(list1)
        print(num)
        print("this xiaoshuo have " + str(num) + " word")
        print(list1[:20])

count_word('test')
