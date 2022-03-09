def filter_out_odd(numbers):
    return [x for x in numbers if (x % 2 == 0)]


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(filter_out_odd(data))
