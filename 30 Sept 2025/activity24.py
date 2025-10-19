
highest_scores = [900,1000,1500,2000,2500]

with open('scores.txt','w') as file:
    for score in highest_scores:
        file.write(str(score)+ '\n');
    print("File Write Success")

with open('scores.txt','a') as file:
    file.write(str(3000)+'\n')

print("File Reading...")
with open('scores.txt','r') as file:
    print("The five highest scores")
    for line in file.readlines():
        print(line)




