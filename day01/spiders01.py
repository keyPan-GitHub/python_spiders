import requests

r = requests.get('https://www.baidu.com')
r.encoding = 'utf-8'
print(r.text)
print(r.status_code)
