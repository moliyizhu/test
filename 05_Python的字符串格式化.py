#通过占位的形式，完成拼接
name = "张三"
message = "%s的年龄：十七" % name
print(message)

#通过占位的形式，完成字符串和数字的拼接
time = "两年半"
name = "cxk"
perfer = "唱，跳，rap，篮球"
message = "我是练习时长%s的个人练习生：%s,喜欢%s" % (time, name, perfer)
print(message)

name = "传智播客"
setup_year  = 2006
stock_price = 19.99
message = "%s，成立于%d，今天的股价是：%f" % (name, setup_year, stock_price)
print(message)