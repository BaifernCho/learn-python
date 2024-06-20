
print(f"การคำนวณเกรด")


subject_all = ["THAI", "MATH", "ENGLISH", "SCIENCE", "SPORT"]
grade_all =[]

for subject in subject_all:
  grade = float(input())
  grade_all.append(grade)

for subject, grade in zip (subject_all, grade_all):
    print(f"{subject} = {grade}")

print("---")

gpa = sum(grade_all)/len(grade_all)

print(f"GPA = {gpa}")


