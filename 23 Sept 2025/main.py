# File Write
# with open('smk.txt','w') as myFile:
#     myFile.write('Student 1'+'\n')
#     myFile.write('Student 2')

# myFile = open('smk.txt','w')
# myFile.write('Student 3'+'\n')
# myFile.write('Student 4')
# myFile.close()

# File Read
with open('smk.txt','r') as myFile:
    student_list = myFile.read()
    print(student_list)

student_list=[]
myFile = open('smk.txt','r')
student_list = myFile.read().split(',')
print(student_list)
myFile.close()