def inputyear():
    year = int(input("คุณอยู่ปีอะไร : "))
    return year

year = inputyear()

def number() :
    if year == 1 :
        sau = print("Welcome Freshman")
    elif year == 2 :
        sau = print("Welcome Sophomore")
    elif year == 3 :
        sau = print("Welcome Junior")
    elif year == 4 :
        sau = print("Welcome Senior")    
    else :
        sau = print("------------")
    return sau

def show():
    print(number())

show()