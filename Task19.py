#Задача №19. 
#Дана последовательность из N целых чисел и число
#K. Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо, K –
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]
#Примечание: Пользователь может вводить значения
#списка или список задан изначально.

a = [1, 2, 3, 4, 5 ]
k = 3
part1 = a[:k]
part2 = a[k:]
lst = part2+part1
print(lst)