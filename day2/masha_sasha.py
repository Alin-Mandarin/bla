import math

stroka = "sanya 4ccc3, masha 2dfsdf3".replace(',','').split()

correct = [0,1,2,3,4,5,6,7,8,9]

name = ''
age = ''
counter = 0;

for i in stroka:
    counter += 1
    if i.isalpha(): name = i
    else:
        for j in i:
            if j.isdigit(): age +=j
    if counter % 2 ==0:
        print("name:", name, "age:", age)
        name = ''
        age = ''