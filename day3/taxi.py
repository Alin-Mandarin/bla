tax_numbers = ["TAX", "TBX", "TEX"]

numbers = ["7 TAX 9215", "6 TEX 9125", "a236ye 73", "21-14 BOT", "3412 0321 GR", "1 TBX 0021-7", "2-TBX 0001", "1 TBX 0000", "1 TBX 0020"]

correct = False
main_access = False

correct_numbers = list()

def check (number):
    ischeck = False
    number = number.split(' ')
    if len(number) == 3:
        if number[0].isdigit() <= 7:
            if number[1].isalpha() and len(number[1]) == 3:
                if number[2].isdigit() and len(number[2]) == 4 and number[2].count('0') != 4:
                   ischeck = True
    return ischeck

for i in range(len(numbers)):
    correct = check(numbers[i])
    numbers_split = numbers[i].split()
    if correct and int(numbers_split[0]) == 7:
        for j in tax_numbers:
            if numbers_split[1] == j:
                print(numbers[i])
    elif correct and 1 <= int(numbers_split[0]) < 7:
        for j in tax_numbers:
            if j != 'TEX' and numbers_split[1] == j:
                print(numbers[i])