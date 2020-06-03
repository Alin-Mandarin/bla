
while True:
    try:
        first_numerator,first_denominator = int(input("Введите первую дробь (1): \nЧислитель: ")),int(input("Знаменатель: "))
        second_numerator,second_denominator = int(input("\nВведите вторую дробь (2): \nЧислитель: ")),int(input("Знаменатель: "))

        if 109 >= first_numerator >= -109 and 109 >= second_numerator >= -109 and first_denominator > 0 and second_denominator > 0:
            break
        else:
            print("\nНеверный ввод\n")
            continue
    except:
        print("\nНеверный ввод\n")
        continue

def compare(numerator1, numerator2, denominator1, denominator2):
    if numerator1>numerator2:
        print(f"{numerator1}/{denominator1} (1) > {numerator2}/{denominator2} (2)")
    elif first_numerator<second_numerator:
        print(f"{numerator1}/{denominator1} (1) < {numerator2}/{denominator2} (2)")
    else:
        print(f"{numerator1}/{denominator1} (1) = {numerator2}/{denominator2} (2)")

if second_denominator % first_denominator == 0:
    if second_denominator > first_denominator:
        first_denominator *= (second_denominator/first_numerator)
    elif second_denominator < first_denominator:
        second_denominator *= (first_numerator/second_denominator)
    compare(first_numerator,second_numerator,first_denominator,second_denominator)
else:
    main_denominator = first_denominator*second_denominator
    first_numerator *= int(main_denominator/first_denominator)
    second_numerator *= int(main_denominator/second_denominator)
    print(f"\nОбщий знаменатель: {main_denominator} =>")
    compare(first_numerator,second_numerator,main_denominator,main_denominator)