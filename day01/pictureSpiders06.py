import requests
import os

url = 'https://xiaoxj.com/data/attachment/forum/202504/23/190918ut1v40as040ztre0.png'
root = 'D://VS Code//python_spiders//Picture//'
path = root + url.split('/')[-1]  # Extract the filename from the URL
try:
    kv = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Use the headers parameter to set the User-Agent
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r = requests.get(url, headers=kv)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print('爬取成功')
    else:
        print('文件已存在')
except:
    print("爬取失败")  # Print the HTML content of the page
