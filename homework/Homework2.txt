print("Name/Surname: Özge Nur Aydın", "Email: ozgeaydiin@gmail.com", "Homework2", sep= "\n")

import operator

#öğrencilerden ad soyad ve puan  input fonksiyonu ile bilgilerinin alınması

student1 = input("Enter the name/surname of student 1: ")
grades_s1 = [int(input(f'Enter {student1}\'s midterm score: ')), int(input(f'Enter {student1}\'s  final score: ')), int(input(f'Enter {student1}\'s  homework score: '))]

student2 = input("Enter the name/surname of student 2: ")
grades_s2 = [int(input(f'Enter {student2}\'s midterm score: ')), int(input(f'Enter {student2}\'s  final score: ')), int(input(f'Enter {student2}\'s homework score: '))]

student3 = input("Enter the name/surname of student 3: ")
grades_s3 = [int(input(f'Enter {student3}\'s midterm score: ')), int(input(f'Enter {student3}\' final score: ')), int(input(f'Enter {student3}\' homework score: '))]

student4 = input("Enter the name/surname of student 4: ")
grades_s4 = [int(input(f'Enter {student4}\'s midterm score: ')), int(input(f'Enter {student4}\'s final score: ')), int(input(f'Enter {student4}\'s homework score: '))]

student5 = input("Enter the name/surname of student 5: ")
grades_s5 = [int(input(f'Enter {student5}\'s midterm score: ')), int(input(f'Enter {student5}\'s final score: ')), int(input(f'Enter {student5}\'s homework score: '))]


#input fonksiyonu ile alınan bilgilerin iki ayrı listeye yerleştirilmesi

students = [student1,student2,student3,student4,student5]

grades = [grades_s1,grades_s2,grades_s3,grades_s4,grades_s5]

# isimler key, notlar value olacak şekilde iki listenin sözlük metodu birleştirilmesi

information = dict(zip(students, grades))



#her öğrenci için ortalama puanların bulunması ve bunun mean_grades isimli listeye aktarılması

mean_grades = []

for k,v in information.items():
  vtoplam = (v[0]+v[1]+v[2])/3
  v = vtoplam
  mean_grades.append(vtoplam)

#öğrencilerin isimlerinin bulunduğu liste ile ortalamaları bulunan liste yeni bir sözlükte birleştirildi

new_info= dict(zip(students, mean_grades))

#öğrencilerin value değerlerine göre azalan bir sıralama yapılmış ve print edilmiş ve en yüksek ortalamaya sahip öğrenci tebrik edilmiştir

dict1 = sorted(new_info.items(), reverse=True, key=operator.itemgetter(1))
new_dict = {key: value for (key, value) in dict1}

descending_order = list(new_dict)


print("The descending order according to the average score is as follows:")
print(new_dict)
print("Congrats {} !!! You are the student with the highest score average".format(descending_order[0]) )
