lista_inicio=[1,2,3,4,5,6]

def añadir_item_referencia(lista,valor):
    lista.append(valor)

def añadir_item_valor(lista,item):
    lista_funcion=lista[:]
    lista_funcion.append(item)
    return lista_funcion

añadir_item_referencia(lista_inicio,10)
print(lista_inicio)

lista_inicio=añadir_item_valor(lista_inicio,11)
print(lista_inicio)