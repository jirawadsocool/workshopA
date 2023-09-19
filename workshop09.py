def inputpersondetails() :
    id = int(input("รหัสพนังาน : "))
    name = input("ชื่อพนังงาน : ")
    sales = float(input("ยอดขาย : "))
    return id,name,sales

def calcommission():
    if sales < 1000 :
        commission = 0
    elif sales < 2001 :
        commission = sales + (sales * 1 / 100)
    elif sales < 3001 :
        commission = sales + (sales * 3 / 100)
    else :
        commission = sales + (sales * 5 / 100)
    return commission

id, name, sales = inputpersondetails()
def showcommission() :
    print(f"รหัสพนังงาน : {id} ชื่อ : {name} ค่าคอมมิชชั่นเป็น {calcommission()} บาท ")

showcommission()
