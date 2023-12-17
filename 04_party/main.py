guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")

    action = input("Гость пришел или ушел? ").lower()

    if action == 'пора спать':
        print("Вечеринка закончилась, все легли спать.")
        break

    if action == 'пришел':
        if len(guests) < 6:
            name = input("Имя гостя: ")
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print("Прости, но мест нет.")
    elif action == 'ушел':
        if len(guests) > 0:
            name = input("Имя гостя: ")
            if name in guests:
                guests.remove(name)
                print(f"Пока, {name}!")
            else:
                print(f"{name} не было на вечеринке.")
        else:
            print("На вечеринке никого нет.")
    else:
        print("Некорректная команда. Введите 'пришел', 'ушел' или 'Пора спать'.")