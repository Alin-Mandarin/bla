#a,b,c = 10,13,20

#first_size = a
#second_size = a+(a*30/100)
#third_size = a*2
#forth_size = c+(a*30/100)

first_size = round(float(input("How much paper was needed for the first side? \n")),4)
second_size = round(first_size+(first_size*30/100),4)
third_size = round(first_size*2,4)
forth_size = round(third_size+(third_size*30/100),4)

print(f"First side: {first_size}cm\nSecond side: {second_size}cm\nThird side: {third_size}cm\nFourth side: {forth_size}cm")