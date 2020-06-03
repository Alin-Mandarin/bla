email = input()
emails = ["gmail.com","mail.ru","yandex.ru"]
access = True

for i in email:
    if not i.isdigit() and not i.isalpha() and i != '.' and i != '@':
        access = False
        break

if access and email.count('@') == 1:
    correct = False
    email = email.split('@')

    for i in emails:
        if email[1] == i:
            correct = True
            break

    if correct:
        print("Access is allowed :)")
    else:
        print("Unknown mail")
else:
    print("Incorrect")