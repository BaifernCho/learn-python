import random
import string

# สร้างรายการ
cards = ['หมาป่า','ลูกหมาป่า','ผู้หยั่งรู้','องครักษ์','จอมเวทย์(ชู่)']

# แสดงรายการให้ผู้ใช้เห็น
print("ตัวละครทั้งหมด:", cards)

# สร้างรายการเก็บตัวอักษรที่ผู้ใช้เลือก
selected_cards = []

# ให้ผู้ใช้เลือกตัวละคร ตามจำนวนผู้เล่น
while len(selected_cards) < 2:
    user_input = input("กรุณาเลือกตัวละคร : ")
    if user_input in  user_input not in selected_cards:
        selected_cards.append(user_input)
    else:
        print("ตัวอักษรนี้ถูกเลือกไปแล้วหรือไม่อยู่ในช่วง A-Z กรุณาเลือกใหม่")

# แสดงผลตัวอักษรที่ผู้ใช้เลือก
print("ตัวอักษรที่คุณเลือก:", selected_cards)

# ให้ผู้ใช้กด Enter เพื่อทำการสุ่มตัวอักษร จนกว่าจะครบทุกตัว
randomized_cards = []

while selected_cards:
    input("กด Enter เพื่อทำการสุ่มตัวอักษร:")
    if not selected_cards:
        print("ตัวอักษรในรายการที่เลือกหมดแล้ว ไม่สามารถสุ่มได้อีก")
        break
    random_selection = random.choice(selected_cards)
    selected_cards.remove(random_selection)
    randomized_cards.append(random_selection)
    print(f"ตัวอักษรที่สุ่มได้: {random_selection}")

# แสดงผลลัพธ์การสุ่มทั้งหมด
print("ผลลัพธ์การสุ่มทั้งหมด:", randomized_cards)
