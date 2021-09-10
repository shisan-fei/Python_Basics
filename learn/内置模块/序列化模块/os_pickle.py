import pickle

'''
序列化：
    吧python中数据，以文本或二进制方式进行转换，可进行反序列化返回
    一般数据在程序和网络中传输存储，要序列化，更加方便
函数：
    dumps('data')   序列化，把python任意对象序列化为二进制
    loads('data')   反序列化，将序列化后的二进制数据返回
    
    dump('data','文件对象')  吧数据进行序列化后写入文件
    load('data','文件对象')  从文件中读取序列化数据进行反序列化
'''

var = 'how are you'
var2 = [1,2,3,4]

res = pickle.dumps(var)
print(res)     #--->b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bhow are you\x94.'
print(pickle.dumps(var2))
print(pickle.loads(b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04e.'))

#将数据序列化后写入文件dump()
#用dumps() 和 loads()
with open('data.txt','ab') as data:
    data.write(res)

with open('data.txt','rb') as read_data:
    dd=read_data.read()
print(pickle.loads(dd))

#用dump() 和 loads()
with open('data2.txt','ab') as data2:
    pickle.dump(var2,data2)    #写入

with open('data2.txt','rb') as read_data2:
    nn=pickle.load(read_data2)    #读出
print(nn)