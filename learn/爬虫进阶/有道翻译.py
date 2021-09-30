'''
请求url  https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
请求方法： post

Request URL: https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
Request Method: POST
data = {
        doctype: json
        i: 要翻译的东西
}
'''
import requests

def get_youdao(kw):
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    data = {
        'i': kw,
        'doctype': 'json'
    }
    res = requests.post(url=url,headers=headers,data=data)
    if res.status_code == 200:
        resdata = res.json()
        if resdata['errorCode'] == 0:
            print('翻译结果：'+resdata['translateResult'][0][0]['tgt'])
        else:
            print('请求翻译失败')

if __name__ == '__main__':
    jiemian = '''
    #########################
    #####请输入要翻译的内容#####
    ########退出请输入q########
    #########################
    '''
    print(jiemian)
    while True:
        kw = input('请输入要翻译的内容：')
        if kw == 'q':
            break
        else:
            get_youdao(kw)
