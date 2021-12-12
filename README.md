[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5312652&assignment_repo_type=AssignmentRepo)
# python-first-test

Simple test program to share with pupils to engage in Github repositories, commiting, and testing code.

## Lecturas y prácticas
### variables

Una variable es un espacio que reservamos en la memoria del ordenador para guardar datos. A ese espacio le damos un nombre para poder usarlo en el programa. Lo que guardamos dentro de la variable, podemos ir cambiándolo mientras el programa funciona.

Hay varios tipos de datos: letras, palabras y frases, números enteros, números decimales, y combinaciones de ellos.

para crear una variable, basta con escribir su nombre y asignarle un valor. Esto es distinto de otros lenguajes, ya que los otros nos piden decir qué tipo de variable queremos, antes de usarla.

```python
animal = "vaca"
```
Esta variable es de tipo **String**, es decir, *cadena de texto*. Debemos encerrar el contenido entre comillas. Pueden ser comillas sencillas, triples sencillas, o comillas dobles.

Con estas variables podemos hacer diversas cosas. Entre ellas, mostrar mensajes a los usuarios. Se puede operar con las cadenas de texto: unirlas, buscar parte de su contenido, dividirlas, etc.

En **Python** se puede cambiar el tipo de variable sobre la marcha:
```python
animal = 7
```
Ahora *animal* ya no es una cadena, sino un número entero, y, por lo tanto, las operaciones que se pueden hacer son distintas.

Esta cualidad de **Python** simplifica la escritura de programas sencillos, pero suele ser también fuente de frecuentes errores, si planificamos hacer alguna operación con una variable que originalmente era de un tipo, pero que después tiene otro distinto:

```python
animal = 6
print(animal+1)
#  Aquí podrían venir muchas líneas de programa.
animal = "vaca"  #Esta línea puede ser una modificación
                 #que hemos hecho después, y que está
                 #rodeada de mucho programa antes del error.
#  Aquí podría haber muchas líneas más.
print(animal+1)
```
Resultado:
> 6
>
>---------------------------------------------------------------------------
/var/folders/k8/l3stnc1x1m5dhncb6mc96h9h0000gn/T/ipykernel_17651/3099013040.py in <module>
>      6                  #rodeada de mucho programa antes del error.
>      7 #  Aquí podrían muchas líneas más de programa.
>----> 8 print(animal+1)
>
>TypeError: can only concatenate str (not "int") to str

Puedes continuar este apartado por tu cuenta, pinchando en el enlace siguiente:

[Contenidos y ejercicios de un curso](https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/1_TiposDatos/tipos-datos.ipynb)

**Identación**

Identación es el truco de mover el texto hacia la derecha para que se entienda mejor el programa. En la práctica totalidad de los lenguajes, es algo que todo programador hace para ver claramente cosas como repeticiones, o qué trozos pertenecen a un bloque. En Python es obligatoria. Hay que usar cuatro espacios para que una línea pertenezca a un trozo que se repite, y la primera linea que da comienzo al bloque, debe terminar con dos puntos (:)

Estos bloques se usan para controlar el flujo del programa, es decir, lo que hay que repetir, o lo que hay que hacer si se cumple una condición, o trozos que queremos reutilizar en lugar de copiarlos una y otra vez.

### Listas

Una lista es un tipo especial de variable, que guarda varios datos, en lugar de uno solo. Cada dato tiene un índice, que sirve para poder acceder a leer o cambiar el contenido de ese dato. Las listas se crean usando *corchetes* [].
```python
colores = ['rojo', 'azul', 'verde', 'amarillo', 'violeta', 'naranja']
print(colores[2])
```
> verde
