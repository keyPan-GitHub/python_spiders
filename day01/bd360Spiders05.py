import requests
kr = {'wd': 'python'}
url = 'https://www.baidu.com/s'
try:
    kv = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Use the headers parameter to set the User-Agent
    r = requests.get(url, headers=kv, params=kr)
    r.raise_for_status()  # Check for HTTP errors
    r.encoding = r.apparent_encoding  # Set encoding to apparent encoding
    print(r.request.url)  # Print the URL of the request
    print(r.request.headers)  # Print the headers of the request
    print(r.status_code)  # Print the status code of the response
    print(len(r.text))  # Print the length of the response text
    print(r.text)  # Print the HTML content of the page
except:
    print("爬取失败")  # Print the HTML content of the page
