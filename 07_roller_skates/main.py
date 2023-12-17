# TODO здесь писать код

num_skates = int(input("Кол-во коньков: "))
skates_sizes = [int(input(f"Размер {i + 1} пары: ")) for i in range(num_skates)]

num_people = int(input("Кол-во людей: "))
people_foot_sizes = [int(input(f"Размер ноги {i + 1} человека: ")) for i in range(num_people)]

skates_sizes.sort()
people_foot_sizes.sort()

max_people = 0
skate_index = 0

for foot_size in people_foot_sizes:
    while skate_index < num_skates and skates_sizes[skate_index] < foot_size:
        skate_index += 1
    if skate_index < num_skates:
        max_people += 1
        skate_index += 1

print("Наибольшее кол-во людей, которые могут взять ролики:", max_people)