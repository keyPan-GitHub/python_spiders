import requests


def GetHtmlText(url):
    try:
        response = requests.get('options', url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "http://www.xiaoxj.com"
    print(GetHtmlText(url))
