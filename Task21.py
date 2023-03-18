#Задача №21. 
#Напишите программу для печати всех уникальных
#значений в словаре.
#Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
#":" S007 "}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
#Примечание: Список словарей задан изначально.
#Пользователь его не вводит

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
res = set([value.stip() for dct lst value in dct.value])
print(*res)

res = []
for dct in lst:
    for value in dct.value():
        res.append(value.stip())
