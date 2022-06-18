# -*- coding:utf-8 -*-
import requests

res = requests.get('https://www.seejav.bid/forum/forum.php?mod=forumdisplay&fid=2')
# print(res.text)
print(res.encoding)
print(res.status_code)
print(res.cookies)
print(res.text)



