# Escriba una función que reciba una lista y devuelva el total de numeros positivos que contiene.

# Función
def contar_positivos(lista):
    # Verificar que lista no esté vacia
    if lista:
        positivos = 0
        for i in lista:
            if i >0:
                positivos = positivos + 1
        return positivos
    else:
        return 'Dato no valido.  Lista vacía'
        
# Invocar función
lista_1 = [1,-2,5]
resultado = contar_positivos(lista_1)
print(resultado)