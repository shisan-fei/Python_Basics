'''
url: http://www.xiladaili.com/gaoni/
     http://www.xiladaili.com/gaoni/2/
     http://www.xiladaili.com/gaoni/3/
     分析每页网页url区别
'''
import requests,json,time
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

def getPage(url):
    '''
    请求页面,获取网页html
    :param url: 请求的url，由于是分页，url在man函数中拼接
    :return: 返回获取到的html数据
    '''
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        html = res.content.decode('utf-8')
        return html
    else:
        return False


def parseHTML(html):
    '''
    解析html，拿到ip和可代理类型. ip形如：218.88.204.125:3256  类型形如：HTTP,HTTPS代理
    :param html:获取到的html数据
    :return:返回一个元祖-->
    '''
    try:
        # 使用xpath解析html
        res_html = etree.HTML(html)
        ip_list = res_html.xpath('//table[@class="fl-table"]//tr//td[1]/text()')  # 所有ip
        daili_list = res_html.xpath('//table[@class="fl-table"]//tr//td[2]/text()')  # htpps还是http
        ip_data = list(zip(ip_list,daili_list))
        return ip_data       #返回一个元祖--->['103.103.3.6:8080', '27.192.200.7:9000', '113.237.3.178:9999'………………]
    except:
        return False

def ip_support(ip):
    '''
    判断ip支持的类型,合成proxyip参数
    :param ip: 解析出的ip数据--->['218.88.204.125:3256','HTTP,HTTPS代理']
    :return: proxyip参数
    '''
    if ip[1] == 'HTTP,HTTPS代理':
        proxyip = {
            'http': f'http://{ip[0]}',
            'https': f'http://{ip[0]}'
        }
        return proxyip
    elif ip[1] == 'HTTPS代理':
        proxyip = {'https': f'http://{ip[0]}'}
        return proxyip
    elif ip[1] == 'HTTP代理':
        proxyip = {'http': f'http://{ip[0]}'}
        return proxyip

def testip(ip,proxyip):
    '''
    测试ip是否好用
    :param ip: 解析出的ip数据--->['218.88.204.125:3256','HTTP,HTTPS代理']
    :param proxyip:  proxyip参数
    :return: 布尔值
    '''
    url = 'http://httpbin.org/get'
    try:
        print(proxyip)
        res = requests.get(url=url, headers=headers, proxies=proxyip)
        if res.status_code == 200:
            #print('ip'+res.json()['origin']+'可用')
            print('ip'+ip+'可用')
            return True
        else:
            return False
    except:
        print('测试ip失败')

def main(num):
    '''
    完成一个页面的全部请求判断，数据写入文件的流程
    :param num: 第几页
    :return:
    '''
    #拼接url
    url = f'http://www.xiladaili.com/gaoni/{num}/'
    #调用请求
    html = getPage(url)
    if html:
        #解析html,得到ip和ip支持的类型
        ip_data=parseHTML(html)
        okip_list =[]
        for ip in ip_data:
            proxyip=ip_support(ip)      #判断ip支持的类型拼接proxyip字段
            okip = testip(ip,proxyip)   #将结果ip发起请求测试，是否好用
            if okip:
                #okip_list.append(ip)     #将可以使用的ip写入列表okip_list
                #将结果写入文件
                with open('可用代理ip.txt','a+',encoding='utf-8') as fp:
                    json.dump(ip,fp)

if __name__ == '__main__':
    for i in range(1,3):
        print(f'正在爬取第{i}页')
        main(i)
        #每抓取一个页面，停两秒
        time.sleep(2)

