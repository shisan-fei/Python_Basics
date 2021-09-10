import re

url="www.baidu.com"
phone= '# 2000-28-12-34'
'''
#print(re.match('www',url))
print(re.match('www',url).span())
print(re.match('baidu',url))

print(re.search('www',url).span())
print(re.search('b.*u',url).span())
'''

'''
print(re.sub(r'#','',phone))
print(re.sub(r'\D','',phone))
'''

'''
strs='one1235twothree34four'
pattern = re.compile('\d+')
print(pattern.match(strs,3,8))

print(pattern.match(strs,3,9).group(0))
print(pattern.match(strs,3,9).start())
print(pattern.match(strs,3,9).end())
print(pattern.match(strs,3,9).span())
'''

# print(re.findall('\d+',phone))
# pattern = re.compile('\d+')
# print(pattern.findall(phone,0,10))

it = re.finditer('\d+','12a32bc43jf3')
for match in it:
    print(match)
    print(match.group())