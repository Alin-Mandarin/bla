import math

def cases(amount, case_one, case_two_to_four, case_more_five):
    if 19 >= amount % 100 > 10:
        case = case_more_five
    else:
        if amount % 10 == 1:
            case = case_one
        elif 4 >= amount % 10 >= 2:
            case = case_two_to_four
        else:
            case = case_more_five
    return case

try:
    money = float(input("Введите кол-во денег: "))
    money_list = str(money).split('.')
    rubles = int(math.floor(money))

    if 9 >= int(money_list[1]) >=1:
        pennies = int(money_list[1]+"0")
    else: pennies = int(money_list[1])

    if pennies > 99:
        rubles += math.floor(pennies/100)
        pennies = pennies-math.floor(pennies/100)*100

    rubles_case = cases(rubles, "рубль", "рубля", "рублей")
    pennies_case = cases(pennies, "копейка", "копейки", "копеек")

    print(f"{rubles} {rubles_case} и {pennies} {pennies_case}")
except:
    print("no")
