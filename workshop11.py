def inputnamephonetime ():
    name_user = input("ชื่อ : ")
    phone_user = float(input("เบอร์โทร : "))
    time_user = float(input("เวลาในการโทร : "))
    return name_user, phone_user ,time_user

name_user, phone_user , time_user = inputnamephonetime

def calculatemoney() :
    if time_user >= 1 or time_user < 16 :
        service = time_user * 5
    elif time_user >= 16 and time_user < 31 :
        service = time_user * 3
    else :
        service = time_user * 1.5 
    return service

def showtime() :
    print(f"{name_user} tel.{phone_user} you got service charge {calculatemoney()}")

showtime()
