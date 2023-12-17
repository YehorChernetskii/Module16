# TODO здесь писать код

def last_person_standing(N, K):
    people = list(range(1, N + 1))

    index = 0
    while len(people) > 1:
        index = (index + K - 1) % len(people)
        removed_person = people.pop(index)
        print(f"Выбывает человек под номером {removed_person}")
        print(f"Текущий круг людей: {people}")

    return people[0]


N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))

result = last_person_standing(N, K)

print(f"\nОстался человек под номером {result}")