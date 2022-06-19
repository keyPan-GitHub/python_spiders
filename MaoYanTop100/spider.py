#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   spider.py
@Time    :   2020/06/08 18:33:46
@Author  :   辛酉 
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

import requests
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return print(response.content)
        return None
    except RequestException:
        return None

def main():
    url = 'https://maoyan.com/board/4?'
    html = get_one_page(url)



if __name__ == "__main__":
    main()