def grouptour():
    leader = input("ใส่ชื่อหัวหน้าทัวร์ : ")
    leaderphone = input("ใส่เบอร์โทรหัวหน้าทัวร์ : ")
    tourist = int(input("ใส่จำนวนนักท่องเที่ยว : "))
    return leader, leaderphone, tourist

leader, leaderphone, tourist = grouptour

def caltour():
    if tourist >= 1 or tourist < 3 :
        person = tourist * 300
    elif tourist >= 3 or tourist < 6 :
        person = tourist * 250
    elif tourist >= 6 or tourist < 11 :
        person = tourist * 210
    else :
        person = tourist * 150
        return person
    
def showtour():
    print(f'หัวหน้าทัวร์ {leader} เบอร์โทร {leaderphone} แพ็คเกจท่องเที่ยวในราคา {caltour()} บาท')

showtour()