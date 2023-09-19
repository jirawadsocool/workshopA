def city() :
    city = input("กรอกจังหวัด : ")
    return city

def PH():
    ph = int(input("กรอกค่า PH : "))
    return ph

def phCheck() :
    city()
    ph = PH()
    if ph >= 7 or ph < 9 :
        print("Result is Normal")
    elif ph > 8 :
        print("Result is Acid")
    else :
        print("Result is Alkali")

phCheck()