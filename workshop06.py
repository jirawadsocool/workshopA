def persondetails() :
    name = input("ชื่อผู้กู้ : ")
    amount = float(input("ยอดเงินกู้ : "))
    return name,amount

def calinterest(amount):
    if amount >= 1000:
        interest = amount * 2.5
    else :
        interest = amount * 5.5
    return interest

def showinterest (name,amount):
    print(f'ชื่อผู้กู้ {name} อัตราดอกเบี้ยเงินกู้คือ {amount}')

name,amount = persondetails()
interest = calinterest(amount)
showinterest(name,interest)