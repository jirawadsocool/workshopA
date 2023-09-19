def studentdetails():
    s_id = input("ใส่รหัสนักเรียน : ")
    s_name = input("ใส่ชื่อนักเรียน : ")
    grade = float(input("ใส่เกรดนักเรียน : "))
    return s_name, s_id , grade

def gradecal(gradcheck):
    if gradcheck < 2.00 :
        return "สอบผ่าน"
    else :
        return "สอบไม่ผ่าน"
    
def showresult(s_id, s_name, result):
    print(f"รหัสนักเรียน: {s_id}")
    print(f"ชื่อนักเรียน: {s_name}")
    print(f"เกรดนักเรียน: {result}")

studentnumber = int(input("ใส่จำนวนนักเรียน : "))

for i in range(studentnumber):
    s_id, s_name, grade = studentdetails()
    result = gradecal(grade)
    showresult(s_id, s_name, result)
