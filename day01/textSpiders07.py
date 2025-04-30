import requests
import time

# 测试的URL
url = "https://www.baidu.com"

# 爬取100次网页


def test_requests_performance():
    success_count = 0
    start_time = time.time()

    for i in range(100):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                success_count += 1
        except Exception as e:
            print(f"第 {i+1} 次请求失败: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"成功爬取 {success_count} 次网页，总耗时: {elapsed_time:.2f} 秒")


if __name__ == "__main__":
    test_requests_performance()
