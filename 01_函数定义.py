"""
函数定义：
def 函数名(传入参数)
    函数体
    return 返回值

函数应用：
函数名(参数)
"""

#函数演示

str1 = "itheima"
str2 = "electronic"

count = 0
for x in str1:
    count += 1
print(f"字符串{str1}的长度为{count}")

count = 0
for x in str2:
    count += 1;
print(f"字符串{str2}的长度为{count}")


def my_len(data):
    count = 0
    for x in data:
        count += 1
    print(f"字符串{data}的长度为{count}")

my_len(str1)
my_len(str2)