#acepta cualquie dato
my_tuple = (1, 'strings', 4.5, True) #puede usarse sin parentesis pero siempre es mejor usarlos
print(my_tuple[1])
#dice el tipo de cosa q es
print(type(my_tuple))
#obtiene donde esta un dato en el tuple
print(my_tuple.count('stings'))
#obtiene donde esta el dato tmbn
print(my_tuple.index(4.5))
#imprime los valores del tuple
for x in my_tuple:
    print(x)
#los tuples no se cambian
my_tuple[0] = 5

