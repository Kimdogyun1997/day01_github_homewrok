# 교재 dic

subjects = {'의사소통영어' : 'A+', '오래된 미래' : 'A+', '양자역학' : 'A+'}
print(subjects['오래된 미래'])

student = ' 김도균'
subject = '오래된 미래'
print(student, '학생의', subject, '과목 성적은', subjects[subject],'입니다' )

print(f'{student}학생의 {subject} 과목 성적은 {subjects[subject]}입니다')

#old style

print('%s 학생의 %s 과목 성적은 %s입니다.' %(student, subject, subjects[subject])

