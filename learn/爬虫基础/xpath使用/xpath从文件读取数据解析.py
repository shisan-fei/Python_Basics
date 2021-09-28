'''
/ 当前元素子节点
// 当前元素子节点或孙子节点
'''
from lxml import etree
#读取html文件解析
html = etree.parse('test.html',etree.HTMLParser())    #返回一个html对象
# print(html)

#提取数据
res = html.xpath('/html/body/div/ul/li/a/text()')     #使用单斜线
res1= html.xpath('//li/a/text()')   #提取所有li下的a标签
res2 = html.xpath
print(res1)