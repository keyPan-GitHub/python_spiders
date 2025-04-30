import requests
url = 'https://item.jd.com/10125122409922.html'
try:
    kv = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Use the headers parameter to set the User-Agent
    r = requests.get(url, headers=kv)
    r.raise_for_status()  # Check for HTTP errors
    r.encoding = r.apparent_encoding  # Set encoding to apparent encoding
    print(r.text)
except:
    print("爬取失败")  # Print the HTML content of the page
