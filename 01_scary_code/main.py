a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)

# TODO переписать программу

a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count_5_first = a.count(5)
print(f"Кол-во цифр 5 при первом объединении: {count_5_first}")

a = [i for i in a if i != 5]

a.extend(c)
count_3_second = a.count(3)
print(f"Кол-во цифр 3 при втором объединении: {count_3_second}")

print("Итоговый список:", a)