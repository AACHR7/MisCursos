#set no permite valores duplicados
set_a = {1, 2, 3, 4, 5}
print(set_a)
#no duplica
set_a = {1, 2, 3, 4, 5, 5} 
#añade
set_a.add(6)
#quita
set_a.remove(2)
set_a.discard(2)
#usando matematicas
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.union(set_b))#suma y no pone los duplicados
print(set_a | set_b) #suma tmbn
print(set_a.interseccion(set_b))#solo imprime los q se repiten
print(set_a & set_b)#l mismo q interseccion
print(set_a.difference(set_b))#estan en a no en b
print(set_a - set_b)#igual que difference
#simetrical difference o ^es igual pone lo q esta en a o b pr no en los 2 set
#set no es una secuencia no contiene index ordenado