
"""
Comentario de varias líneas
"""
# Tipos de datos primitivos

valor_entero = -12200
valor_decimal = -10.2

valor_cadena = "Hola mundo"

booleanos = False

print(valor_cadena[2])



# Tipos de datos compuestos

lista = [1, "2", 3, 4, 5, 6, 7, False, 9, {}]
lista2 = list()

lista.append(11)
lista.pop()

tupla = (1, 2, 3, 4, 5)

diccionarios = {
    "Nombre": "Camila",
    "ID": 12345557,
    "Autenticado": False,
    "contenido": {

    }
}
# Operadores
print(2 + 2 - 2 * 2 / 2) # Aritméticos

print("2" == "2") # && || ! Lógicos

x = 10 # ++ o --
x += 1

condicion = True

numero = condicion if 10 else 2 # (condicion) ? 10 : 2

# Obtener e imprimir datos

# mensaje_usuario = int(input("Dame un numero: "))

# print(mensaje_usuario)

# Funciones
def mi_funcion(mensaje):
    print(mensaje)
    return 0

mi_funcion("Hola")

# Condicionales
condicional = 2 == 2

if condicional:
    # Hacer algo
    if condicion:
        ...
elif condicion:
    # Hacer otra cosa
    ...
else:
    # Hacer ultima cosa
    ...


# Ciclos

for i in range(10):
    print(i)
    continue

i = 0

while i < 10:
    if i == 5:
        break
    i += 1



