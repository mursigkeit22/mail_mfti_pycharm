import random
our_number = random.randint(0, 101)

while True:

    your_number = input('Enter your number: ')
    if not your_number or your_number == "exit()":
        print('Good bye!')
        break
    if not your_number.isdigit():
        print("Only integers, please")
        # Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла
        continue

    users_number = int(your_number)

    if users_number > our_number:
        print('Your number is too big')
    elif users_number < our_number:
        print('Your number is too small')
    elif users_number == our_number:
        print('You are right!')
        break
