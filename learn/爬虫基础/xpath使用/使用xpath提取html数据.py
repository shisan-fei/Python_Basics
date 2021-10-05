from lxml import etree

#网页源代码
text = '''
<!DOCTYPE html>
<html>
 <head> 
  <meta charset="utf-8" /> 
  <meta name="description" content="牛客网是互联网求职神器，C++、Java、前端、产品、运营技能学习/备考/求职题库，在线进行百度阿里腾讯网易等互联网名企笔试面试模拟考试练习,和牛人一起讨论经典试题,全面提升你的技术能力" /> 
  <meta name="keywords" content="牛客网,C++笔试面试，Java笔试面试，计算机笔试,计算机面试, IT笔试,笔试题库,笔试练习,IT面试,在线编程,编程学习,牛客网" /> 
  <title>小萝卜112的个人主页_牛客网</title> 
 </head>
 <body> 
  <div class="nk-container"> 
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
html = etree.HTML(text)    #使用etree解析html返回html对象
print(html)
# print(html.xpath('/html/body/div/ul/li/a/text()'))   #--->['首页', '题库']   使用xpath获取/html/body/div/ul/li/路径下a标签所有内容
#
# print(html.xpath('/html/body/div/ul/li/ul/li/a/text()'))  #--->['公司真题', '专项练习', '在线编程', '精华专题', '试题广场']
# print(html.xpath('/html/body/div/ul/li/ul/li[1]/a/text()'))   #--->['公司真题']   可以指定li标签

print(html.xpath('/html/head/meta/@content'))    #获取属性值-->@属性
item = html.xpath('//div[@class="nk-container"]')   #找到所有div并且class为nk-container
for i in item:
    # i.xpath('.//a/text()')
    # print(i)
    print(i.xpath('.//li/a/text()'))
