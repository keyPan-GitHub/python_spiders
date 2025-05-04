# 导入 requests 库，该库用于发送 HTTP 请求
import requests
# 从 bs4 库中导入 BeautifulSoup 类，用于解析 HTML 或 XML 文档
from bs4 import BeautifulSoup

# 定义要请求的目标网页的 URL
url = "https://www.xiaoxj.com/"
# 使用 requests 库的 get 方法发送 GET 请求，并将响应对象赋值给 response 变量
response = requests.get(url)
# 使用 BeautifulSoup 类对响应的文本内容进行解析，指定解析器为 html.parser
soup = BeautifulSoup(response.text, "html.parser")
# 调用 prettify 方法将解析后的 HTML 文档以格式化的形式打印输出
print(soup.prettify())
