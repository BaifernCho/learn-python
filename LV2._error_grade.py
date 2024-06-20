while True:
    try:
        score = float(input(""))

        if score < 0:
            raise ValueError("Error : Value must be greater than or equal to 0.")
        elif score > 100:
            raise ValueError("Error : Value must be less than or equal to 100.")
        else:
            if score >= 90:
                print("A")
            elif score >= 85:
                print("B+")
            elif score >= 80:
                print("B")
            elif score >= 75:
                print("C+")
            elif score >= 70:
                print("C")
            elif score >= 65:
                print("D+")
            elif score >= 60:
                print("D")
            else:
                print("F")
        break

    except ValueError as err:
        print(err)
        break
