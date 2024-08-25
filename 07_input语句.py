""""
演示Python中的input语句
获取键盘信息
"""
name = input("请告诉我你是谁?")
print("我知道了，你是：%s" % name)


# input()语句获取的是字符串类型
num = input("请告诉我你的银行卡密码：")
print("你的银行卡密码类型是：",type(num))
num = int(num)
print("你的银行卡密码类型是：",type(num))
