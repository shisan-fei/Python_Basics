#找github上星级最高python项目
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status_code:',r.status_code)

response_dict = r.json()
print(response_dict.keys())
print("total repositories:",response_dict['total_count'])