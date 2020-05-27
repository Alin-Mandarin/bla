main_string = str(input())
even_elements_of_the_main_string = ''

for i in range(0,len(main_string),2):
    even_elements_of_the_main_string += main_string[i]

print(even_elements_of_the_main_string)