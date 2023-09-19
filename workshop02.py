def student_details() :
    student_id = int(input('รหัสนักเรียน : '))
    student_name = input('ชื่อนักเรียน : ')
    score_1 = float(input('คะแนนสอบครั้งที่ 1 : '))
    score_2 = float(input('คะแนนสอบครั้งที่ 2 : '))
    score_3 = float(input('คะแนนสอบครั้งที่ 3 : '))
    return student_id,student_name,score_1,score_2,score_3

student_id,student_name,score_1,score_2,score_3 = student_details ()

def calscroesstu() :
    return (score_1 + score_2 + score_3) / 3

def showscorestudent():
    print(f'รหัสนักเรียน : {student_id} ชื่อนักเรียน : {student_name} คะแนนเฉลี่ยของนักเรียนคือ : {calscroesstu():.2f}')

showscorestudent()