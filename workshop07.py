def inputnumber():
    number = int(input("ใส่เลขของคุณ : "))
    return number

def process():
    true = "Correct, You are the winner"
    false = "Not Correct!!!"
    return true,false

true,false = process()

def shownumber():
    if inputnumber() == 25 :
        print(true)
    else :
        print(false)

shownumber()