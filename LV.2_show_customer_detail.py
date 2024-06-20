print(f"--------------LV.2-------------")

customer_detail =['fristname', 'lastname','address','gender','tel' ]
detail =[]

for i in range(len(customer_detail)):
    input_detail = input(f"")
    detail.append(input_detail)
    
for i in range (len(detail)):
    print(f"{customer_detail[i]} : {detail[i]}")

