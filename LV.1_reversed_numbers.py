#รับค่า จำนวนนับที่ต้องการ
count = int(input())
numbers =[]
def num_count(count):
  return (count)


#รับค่าตัวเลขที่ต้องการ 
def put_number(count):

  for i in range(count): 
    number = int(input())
    numbers.append(number)
  return (numbers)

# แสดงผลเรียงลำดับจากหลังไปหน้า
def show_num(numbers):
    reversed_numbers = list(reversed(numbers))
    for number in reversed_numbers:
        print(number)

# ใช้งานฟังก์ชัน
num_count(count)
put_number(count)
show_num(numbers)
  
