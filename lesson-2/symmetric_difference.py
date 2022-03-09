def custom_symmetric_difference(s1, s2):
    diff = set()
    for i in s1:
        if i not in s2:
            diff.add(i)

    for i in s2:
        if i not in s1:
            diff.add(i)
    return diff


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8}

result = set1.symmetric_difference(set2)
customResult = custom_symmetric_difference(set1, set2)

print("Function result:", result)
print("My Function result:", customResult)
