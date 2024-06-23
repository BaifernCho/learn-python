
numbers =[]
count = int(input())

for i in range(count):
  number = int(input())
  numbers.append(number )
  numbers.sort(reverse=True)


for number in numbers:
  print(number)
    