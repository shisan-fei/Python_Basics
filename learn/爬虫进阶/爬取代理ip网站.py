import requests
from lxml import etree

url = 'http://www.xiladaili.com/gaoni/3/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

res = requests.get(url=url,headers=headers)
if res.status_code == 200:
    datas = res.content.decode('utf-8')
    #使用xpath解析html
    res_html = etree.HTML(datas)
    trs=res_html.xpath('//table[@class="fl-table"]//tr//td[1]/text()')     #所有ip
    dailis = res_html.xpath('//table[@class="fl-table"]//tr//td[2]/text()')  #htpps还是http

    datas = list(zip(trs,dailis))
    print(datas)
    print(dailis)
    # print([i.xpath('//td[1]/text()') for i in trs])
    # print(datas)