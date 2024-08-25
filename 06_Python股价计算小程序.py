name = "传智博客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_grownth_factor = 1.2
grownth_day = 7
finally_stock = stock_price * stock_price_daily_grownth_factor ** grownth_day
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数%.1f，经过%d的增长，股价达到了：%.2f"%
      (stock_price_daily_grownth_factor,grownth_day,finally_stock) )

