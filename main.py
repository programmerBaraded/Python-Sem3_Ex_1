# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

def nearest_value(my_list, namber_x):
    found = my_list[0]  # принимаем допущение что ближайшее число к искомому первое в списке (с индексом 0)
    for item in my_list:  # для каждого элемента (item) из items (т.е. попеременно item=1, item=2..)
        # проверяем условие если разница между item value по модулю меньше разницы found и value, то
        if abs(item - namber_x) < abs(found - namber_x):  # если условие истинно (True)
            found = item  # меняем значение нашего допущения на item (т.е. item оказался ближе к искомому значению)
    return found  # возвращаем ближайшее значение до value в списке items

my_list = [random.randint(0, 100) for _ in range(20)]
print(my_list)
namber_x = int(input("Введите искомое число: "))
count = 0
for i in range(len(my_list)):
    if namber_x == my_list[i]:
        count += 1
if count > 0:
    print(f"Искомое число встречается в списке {count} раз")
else:
    print(f'Ближайшее число к {namber_x} в списке {my_list} является {nearest_value(my_list, namber_x)}')
