# TODO здесь писать код

class1_heights = list(range(160, 177, 2))
class2_heights = list(range(162, 181, 3))

# Объединение списков и сортировка
combined_heights = class1_heights + class2_heights
combined_heights.sort()

# Вывод отсортированного списка
print("Отсортированный список ростов:", combined_heights)