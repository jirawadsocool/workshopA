def inputx():
    x = int(input('ใส่ค่า x : '))
    return x

x = inputx()

def calculate():
    y = 2 * x ** 2 + 2 * x + 1
    return y

def showcal():
    print(f'ค่าของ y คือ : {calculate()}')

showcal()