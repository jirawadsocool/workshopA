def emddetails():
    emd_id = input("ป้อนรหัสพนังงาน : ")
    emd_name = input('ชื่อพนังงาน : ')
    emd_salary = float(input("เงินเดือนพนังงาน : "))
    return emd_id,emd_name,emd_salary

emd_id,emd_name,emd_salary = emddetails()

def emdsalarycalculate():
    minus_tax = emd_salary - (emd_salary * 7 / 100) - 500
    return minus_tax

def showsalarycalculate():
    print(f"ID {emd_id} คุณ {emd_name} เงินเดือนของพนังงาน {emd_salary} เงินเดือนสุทธิ {emdsalarycalculate()} บาท")

showsalarycalculate()