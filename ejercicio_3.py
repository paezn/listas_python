# Escriba una función que reciba una lista y que devuelva como resultado una tupla almacenando el primero y el ultimo elemento de la lista.  En caso de que la lista no tenga dos o mas elementos debe indicarlo y no procesar los datos.

# Función
def obtener_primero_ultimo(lista):
    # Verificar que lista no esté vacia
    if lista:
        # Verificar que la lista tenga 2 o mas elementos
        if(len(lista)>=2):
            return (lista[0], lista[-1])
        else:
            return 'La lista no tiene elementos suficientes'
    else:
        return 'Dato no valido.  Lista vacía'
        
# Invocar función
lista_1 = []
resultado = obtener_primero_ultimo(lista_1)
print(resultado)