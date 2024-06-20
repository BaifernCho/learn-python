# ข้อความที่ได้รับมา
sentence = input("")

# แยกประโยคออกเป็นคำ ๆ โดยใช้ช่องว่างเป็นตัวแบ่ง
words = sentence.split()

# สลับตำแหน่งคำในประโยค
reversed_words = words[::-1]

# รวมคำกลับเป็นประโยคเดียวกัน
reversed_sentence = ' '.join(reversed_words)

# แสดงผลลัพธ์
print(reversed_sentence)
