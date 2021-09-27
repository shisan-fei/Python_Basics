# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5

# 我的id和秘钥.
appid = '20210927000958132'
appkey = 'm2m3NS8GkmnJMpCG0W8K'

#百度翻译api
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

#
def fanyi(salt,sign,from_lang,to_lang):
    '''
    将接受到的内容翻译
    :param salt:
    :param sign:
    :param from_lang: 接受的语言类型
    :param to_lang: 翻译的目的类型
    :return: {‘驶入内容’：‘翻译后结果’}
    '''
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    k=result['trans_result'][0]['src']
    v=result['trans_result'][0]['dst']
    return {k:v}

if __name__ == '__main__':
    num = int(input("中-->英，请按1，\n英-->中，请按2："))
    query = input('请输入要翻译内容：')
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    if num == 1:
        from_lang = 'zh'
        to_lang = 'en'
        #print(fanyi(salt, sign, from_lang, to_lang))
    elif num == 2:
        from_lang = 'en'
        to_lang = 'zh'
        #print(fanyi(salt, sign, from_lang, to_lang))
    else:
        print('请按照要求查询')
    print(fanyi(salt,sign,from_lang,to_lang))
    #print(from_lang,to_lang)




