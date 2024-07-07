n = int(input())
def sum_digits_recursive(n):
    if n < 10:  # กรณีฐาน: ถ้า n มีเลขเพียง 1 หลัก ให้คืนค่า n
        return n
    else:  # กรณี recursive: หาผลรวมของตัวเลขทุกตัวแล้วเรียกฟังก์ชันซ้ำ
        # แปลง n เป็นสตริง
        n_str = str(n)
        
        # สร้าง list ของตัวเลขจากแต่ละหลักของ n
        digits = []
        for digit in n_str:
            digits.append(int(digit))
        
        # หาผลรวมของตัวเลขใน list
        digit_sum = sum(digits)
        
        # เรียกฟังก์ชันซ้ำด้วยผลรวมที่ได้
        return sum_digits_recursive(digit_sum)

# ทดสอบฟังก์ชัน
print(sum_digits_recursive(n))  # ผลลัพธ์คือ 1 (1+2+3+4 = 10 -> 1+0 = 1)

