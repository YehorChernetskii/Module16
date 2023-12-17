# TODO здесь писать код

first_list = []

for i in range(3):
    num = int(input(f"Введите число {i + 1} для первого списка: "))
    first_list.append(num)

second_list = []

for i in range(7):
    num = int(input(f"Введите число {i + 1} для второго списка: "))
    second_list.append(num)

first_list.extend(second_list)

first_list = list(set(first_list))

print("Первый список:", first_list)
print("Второй список:", second_list)
print("Новый первый список с уникальными элементами:", first_list)