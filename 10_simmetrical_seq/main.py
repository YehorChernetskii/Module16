# TODO здесь писать код

def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    return num_list == reverse_list

def make_sequence_palindrome(nums):
    new_nums = []
    answer = []

    for i_nums in range(0, len(nums)):
        for j_elem in range(i_nums, len(nums)):
            new_nums.append(nums[j_elem])
        if is_palindrome(new_nums):
            for i_answer in range(0, i_nums):
                answer.append(nums[i_answer])
            answer.reverse()
            break
        new_nums = []

    return answer

nums = [int(input("Число: ")) for _ in range(int(input("Кол-во чисел: ")))]

additional_sequence = make_sequence_palindrome(nums)

print(f"Последовательность: {' '.join(map(str, nums))}")
print(f"Нужно приписать чисел: {len(additional_sequence)}")
print(f"Сами числа: {' '.join(map(str, additional_sequence))}")

