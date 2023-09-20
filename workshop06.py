def persondetails() :
    name = input("ชื่อผู้กู้ : ")
    amount = float(input("ยอดเงินกู้ : "))
    return name,amount

def calinterest(amount):
    if amount >= 1000:
        interest = amount * 2.5 / 100 * amount
    else :
        interest = amount * 5.5 / 100 * amount
    return interest

def showinterest (name,interest):
    print(f'ชื่อผู้กู้ {name} อัตราดอกเบี้ยเงินกู้คือ {interest}')

name,amount = persondetails()
interest = calinterest(amount)
showinterest(name,interest)