# -*- coding:utf-8 -*-
import requests

res = requests.get('https://www.seejav.bid')
# print(res.text)
print(res.encoding)
print(res.status_code)
# print(res.cookies)
# print(res.content)


