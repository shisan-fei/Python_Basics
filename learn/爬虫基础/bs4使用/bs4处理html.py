'''
BeautifulSoup(html文本,'解析器')
    通过tag标签对象获取文档数据
        bs4对象.标签
        bs4对象.标签['内容']
    通过搜索获取页面中元素
        bs4对象.find('元素')  找到以一个元素
        bs4对象.find_all()    找到所有元素返回元祖
'''
from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html>
 <head> 
  <meta charset="utf-8" /> 
  <meta name="description" content="牛客网是互联网求职神器，C++、Java、前端、产品、运营技能学习/备考/求职题库，在线进行百度阿里腾讯网易等互联网名企笔试面试模拟考试练习,和牛人一起讨论经典试题,全面提升你的技术能力" /> 
  <meta name="keywords" content="牛客网,C++笔试面试，Java笔试面试，计算机笔试,计算机面试, IT笔试,笔试题库,笔试练习,IT面试,在线编程,编程学习,牛客网" /> 
  <title>小萝卜112的个人主页_牛客网</title> 
 </head>
 <body> 
  <div class="nk-container    "> 
     <a class="nowcoder-logo" href="/" title="牛客网"></a> 
     <ul class="nowcoder-navbar"> 
      <li data-type="home"><a href="/">首页</a></li> 
      <li data-type="tiku"> <a href="https://www.nowcoder.com/contestRoom">题库</a> 
       <ul class="sub-nav" data-type="tiku"> 
        <li><a href="https://www.nowcoder.com/contestRoom">公司真题</a></li> 
        <li><a href="https://www.nowcoder.com/intelligentTest">专项练习</a></li> 
        <li><a href="https://www.nowcoder.com/activity/oj">在线编程</a></li> 
        <li><a href="https://www.nowcoder.com/activity/topics">精华专题</a></li> 
        <li><a href="https://www.nowcoder.com/questionCenter">试题广场</a></li> 
       </ul> </li> 
     </ul>
  </div>
 </body>
</html>
'''
#创建bs4对象，指定lxml解析器
soup = BeautifulSoup(html,'lxml')

#通过tag标签对象获取文档数据
r = soup.li
# print(r)    #----><li data-type="home"><a href="/">首页</a></li>
# print(r.text)   #--->获取标签中文本
# print(r['data-type'])
#获取标签对象指定数据
# print(soup.a)        #----><a class="nowcoder-logo" href="/" title="牛客网"></a>
# print(soup.a['title'])   #牛客网

# print(soup.title.text)   #--->小萝卜112的个人主页_牛客网
# print(soup.title.parent.name)   #--->head,获取标签名
#
# 通过搜索获取页面中元素
# res = soup.find('a')  #返回第一个找到的a标签
# res = soup.find('a')["class"]

res = soup.find_all('a')   #返回所有a标签的集合
for i in res:
    print(i['href'])