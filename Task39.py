#Задача №39. 
#Даны два массива чисел. Требуется вывести те элементы
#первого массива (в том порядке, в каком они идут в первом
#массиве), которых нет во втором массиве. Пользователь вводит
#число N - количество элементов в первом массиве, затем N
#чисел - элементы массива. Затем число M - количество
#элементов во втором массиве. Затем элементы второго массива

num_1 = int(input('Введите количество элементов в первом массиве: '))
list_1 = list()

for i in range(num_1):
    x = int(input('введите элемент массива: '))
    list_1.append(x)
print(list_1)
num_2 = int(input('Введите количество элементов во втором массиве: '))
list_2 = list()

for i in range(num_2):
    x = int(input('введите элемент массива: '))
    list_2.append(x)
print(list_2)
list_new = list()

def result (list_1, list_2, list_new):
    for i in list_1:
        if i not in list_2:
            list_new.append(i)
# for j in list_2:
# if i == j:
# list_new.append(i)

    return list_new



print(result(list_1, list_2, list_new))
