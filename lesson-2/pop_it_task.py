count = {
    'фиолетовый': 0,
    'желтый': 0,
    'синий': 0,
    'зеленый': 0,
    'голубой': 0,
    'ораньжевый': 0,
}

print("Цвета:", count.keys())

while True:
    string = input()

    if string.__eq__('stop'):
        print(count)
        break

    if string in count.keys():
        count[string] = count[string] + 1

    else:
        print('Такого цвета не существует')

    print('Введите следующее значение')

