customers = []
now_year = 2017

# ระบุจำนวนลูกค้า
num_customer = int(input())

# วนตามจำนวนลูกค้าเพื่อใส่รายละเอียด
def customer_detail():
    for i in range(num_customer):
        full_name = input()
        birth_year = int(input())
        gender = input()
        customers.append((full_name, birth_year, gender))

# คำนวณอายุ
def cal_age():
    for i in range(num_customer):
        customer = customers[i]
        full_name, birth_year, gender = customer
        age = now_year - birth_year
        customers[i] = (full_name, age, gender)

customer_detail()
cal_age()

# แสดงข้อมูลลูกค้า
def display():
    print(f"--Customers Information--")
    for customer in customers:
        full_name, age, gender = customer
        print(f"{full_name} (age : {age})")

display()
