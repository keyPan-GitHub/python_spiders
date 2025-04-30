import re
# 提取字符串
# 替换
# 搜索

info = "姓名:bobby 生日:1987年10月1日 本科：2005年9月1日"
# print(re.findall("\d{4}", info))
# print(re.match(".*生日.*\d{4}", info))
# print(re.search("生日.*\d{4}", info))
match = re.match(".*生日.*?(\d{4}).*本科.*?(\d{4})", info)
print(match.group(1))
print(match.group(2))

sub = re.sub("\d{4}", "2019", info)
print(sub)

# name = 'my name is Bobby'
name = """my name is 
bobby   
"""
print(re.match('.*bobby', name, re.DOTALL).group())
