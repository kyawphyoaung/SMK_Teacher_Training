Slist = [['Faruq',60],
         ['Jalila',90],
         ['Kyaw',100]]

with open('results.txt','w') as file:
    for x in range(len(Slist)):
        file.write(Slist[x][0]+',') #row 1 column 0
        file.write(str(Slist[x][1])+'\n')#row 1 column 1

Alist = []
with open('results.txt','r') as file:
    Alist = file.read().split(',')

newlist = []
for x in range(0,len(Alist)-1,2):
    newlist.append([Alist[x],int(Alist[x+1])]) 
print("Two Dimensional Array")
print(newlist)
