import requests
url = 'https://www.nowcoder.com/profile/110481275?noredirect=true'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Cookie':'NOWCODERUID=385AD34B5156639FA7C3D2533B31059B; NOWCODERCLINETID=7DDFBCD534BC945069424375381DF38E; t=89CA0F5038129FD533C53C78FF03B9BB; NOWCODERQUERY=%E5%8D%8E%E6%B6%A6%E9%93%B6%E8%A1%8C%3A%E5%AE%8C%E7%BE%8E%E4%B8%96%E7%95%8C%E5%86%85%E6%8E%A8%3A%E5%AE%8C%E7%BE%8E%E4%B8%96%E7%95%8C%3A%E6%90%BA%E7%A8%8B%3A%E8%B4%A7%E6%8B%89%E6%8B%89%E5%86%85%E6%8E%A8; hrId=314387; gray=0; SERVERID=f24cbffaf8c883b27da19f52fb8cda88|1632732437|1632730235'
}

res = requests.get(url=url,headers=header)

code = res.status_code
print(res.text)
print(code)



