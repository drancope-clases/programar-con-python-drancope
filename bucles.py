
# Bucles, explicación y ejemplos

# bucle:
#    hace lo que hay aquí hasta que el bucle termina de alguna forma

#
#
# for variable in range:
#     Hace esto hasta que termina range
#
# función range:     range(desde, hasta)

print("Ejemplo for")
for i in range(10): # números del 0 al 10
    print(i)

# while
#    # 1. while condición:
#    # 2.    Hace esto mientras condición resulta verdadero

print("Ejemplo while")
a = 1
b = 10
while a < b:
    print(a)
    a += 1

#Tu turno:

#tareas:
#    propia rama del repositorio
# 2. Resuelve el problema de la tabla de multiplicar.
# 3. Puedes hacer "commit & push" para guardar los cambios en GitHub

numero = int(input("Pon un número")) #pon aquí el número del que quieres hacer la tabla
print("tabla de multiplicar del ", numero)
i=1
while i<11:
    print(numero, "por", i, "=", numero*i)
    i= i+1
    