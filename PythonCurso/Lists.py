list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C']
list3 = ['hello', 1, True, 40.22]
list4 = [1,[2,3,4], 5, 6]
#imprime toda la lista
print(*list3)
#imprime separado con comas
print(list3, sep =' ')
#añade 1 numero a la lista
list3.insert(len(list3), 6)
print(list3, sep =' ')
#añade sin especificar donde
list3.append(7)
print(list3, sep =' ')
#añade mas a la lista
list3.extend([6, 7, 8, 9])
print(list3, sep =' ')
#borra especificando donde
list3.pop(4)
print(list3, sep =' ')
#borra tambien
del list3[2]
print(list3, sep =' ')
#imprime o itera
for x in list3:
    print('Value: ', x)
    