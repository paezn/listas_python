# Analista del salón

nombres = ['Lucas' , 'Sofía', 'Mateo', 'Valentina', 'Martín']
edades = [15,16,15,17,14]
musica = ['Rock', 'Trap', 'Pop', 'Rock', 'Trap']

# Reto 1: promedio de edad

promedio = sum(edades) / len(edades)
print('Promedio de edad: ', promedio)

# Reto 2: Mayores de 15

# Sin list comprehension
mayores_1 = []
for i in edades:
    if i > 15:
        mayores_1.append(i)
print('Edades > 15: ', mayores_1)

# Con list comprenhension
mayores_2 = [edad for edad in edades if edad > 15]
print('Edades > 15: ', mayores_2)

# Reto 3: Fans del Rock

# Sin list comprehension
fans_rock_1= []
for i in musica:
    if i > 'Rock':
        fans_rock_1.append(i)
print('Total fans del Rock: ', len(fans_rock_1))

# Con list comprenhension
fans_rock = [gen for gen in musica if gen > 'Rock']
print('Total fans del Rock: ', len(fans_rock))