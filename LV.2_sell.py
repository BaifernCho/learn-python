num = int(input())  #i
price_all=[]

def show_price ():
  for i in range(num):
    price = int(input())
    price_all.append(price)


def cal_price():
  sum = 0
  for price in price_all:
    sum += price
  print(sum,"THB")
show_price()
cal_price()
    