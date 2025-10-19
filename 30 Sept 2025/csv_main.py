import csv

Slist = [['Faruq',60],
         ['Jalila',90],
         ['Kyaw',100]]

with open('student_data.csv','w') as file:
    writer = csv.writer(file)
    writer.writerows(Slist)

students = []
with open('student_data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        students.append([row[0],int(row[1])])
    
print(students)

