import requests
url = 'https://item.jd.com/10125122409922.html'
try:
    r = requests.get(url)
    r.raise_for_status()  # Check for HTTP errors
    r.encoding = r.apparent_encoding  # Set encoding to apparent encoding
    print(r.text)
except:
    print("爬取失败")  # Print the HTML content of the page
