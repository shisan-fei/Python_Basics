import requests
import os
from threading import Thread
def getPage(kw,num):
    '''
    指定关键字和页数，爬取照片
    :param kw: 关键字
    :param num: 页数
    :return: 页面响应信息
    '''
    url = 'https://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fimg.zcool.cn%252Fcommunity%252F012ee55649bea532f87512f623b6a6.jpg%25401280w_1l_2o_100sh.jpg%26refer%3Dhttp%253A%252F%252Fimg.zcool.cn%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1635839948%26t%3D84d663a332739c4a9c9857df921bea83&thumburl=https%3A%2F%2Fimg1.baidu.com%2Fit%2Fu%3D1104502300%2C4091485257%26fm%3D26%26fmt%3Dauto'

    #定义请求参数，放入列表
    params = []
    for i in range(30,num*30+30,30):
        params.append({
            'tn':'resultjson_com',
            'logid':'7619016436617622266',
            'ipn':'rj',
            'ct':'201326592',
            'is':'',
            'fp':'result',
            'queryWord':kw,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe':' utf-8',
            'adpicid':'',
            'st': '-1',
            'z':'',
            'ic': '0',
            'hd':'',
            'latest':'',
            'copyright':'',
            'word': kw,
            's':'',
            'se':'',
            'tab':'',
            'width':'',
            'height':'',
            'face': '0',
            'istype': '2',
            'qc':'',
            'nc':'',
            'fr':'',
            'expermode':'',
            'nojc':'',
            'pn': i,
            'rn': '30',
            'gsm': '1e',
            '1633247947918:':''
        })
    url = 'https://image.baidu.com/search/acjson'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    datalist = []
    for i in params:
        #向每个url发起请求，获取data部分
        res = requests.get(url,headers=headers,params=i).json()['data']
        datalist.append(res)
        # print(json.dumps(res,indent=2))
    return datalist

def downloadImg(datalist,dir):
    '''
    下载图片写入文件夹
    :param datalist: 获取到的页面响应信息
    :param dir: 下载到的文件夹
    :return:
    '''
    #检测文件夹是否存在
    if not os.path.exists(dir):
        os.mkdir(dir)
    #循环下载图片
    for data in datalist:
        for i in data:
             # print(i.get('thumbURL'))
             if i.get('thumbURL') != None:
                images = requests.get(i.get("thumbURL"))
                try:
                    open(f'{dir}/{i["fromPageTitleEnc"]}.jpg','wb').write(images.content)   #文件名用fromPageTitleEnc的值命名
                    print(f'下载图片: {i["fromPageTitleEnc"]}')
                except:
                    print(f'下载图片: {i["fromPageTitleEnc"]} 下载失败')

if __name__ == '__main__':
    keyword = input('要什么类型的图片：')
    num = int(input('下载几页？'))
    #调用函数进行数据爬取，可以指定关键字和下载页数，获取图片url
    datalist = getPage(keyword,num)
    downloadImg(datalist,'baidupag')
    # print(datalist)

# url='https://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fimg.zcool.cn%252Fcommunity%252F012ee55649bea532f87512f623b6a6.jpg%25401280w_1l_2o_100sh.jpg%26refer%3Dhttp%253A%252F%252Fimg.zcool.cn%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1635839948%26t%3D84d663a332739c4a9c9857df921bea83&thumburl=https%3A%2F%2Fimg1.baidu.com%2Fit%2Fu%3D1104502300%2C4091485257%26fm%3D26%26fmt%3Dauto'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
# }
# image = requests.get(url,headers=headers)
# open('1.jpg','wb').write(image.content)