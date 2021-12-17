[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5312652&assignment_repo_type=AssignmentRepo)
# python: Primeros pasos

Introducción básica a **Python** y programas de prueba sencillos, para compartir con los alumnos y empezar con tareas de usar entornos de ejecución online, *notebooks*, GitHub y distintas clases de archivos.

Basic introduction to **Python** and simple test program to share with pupils to engage in accesing to online run environments, notebooks, Github, and different sort of files.

## Índice

* [Repositorios y **GitHub**](#item1)

* [Lenguajes](#item2)

* [Intérpretes](#item3)

* [Python](#item4)

<a name="item1"></a>
## Repositorios y **GitHub**

Un repositorio es una carpeta en la que guardamos un proyecto, normalmente programas, y que debe estar sincronizada entre nuestro ordenador y los ordenadores de otros colaboradores.

**GitHub** es un sitio de Internet, que permite guardar repositorios. Es uno de los más utilizados del mundo.

Para sincronizar el trabajo que se hace, se utiliza un programa, **git**, que nos obliga a trabajar de una manera especial:
- Creamos copias del repositorio original, bien para tener una copia de nuestra propiedad, o bien para hacer una copia desde Internet a nuestro ordenador.
- Modificamos el programa en el que estamos trabajando, en una **rama** distinta, para que no se mezcle con lo que ya estaba hecho antes, y creamos una "*solicitud de incorporación*" (*pull request*), para que los colaboradores la prueben, y si el cambio está bien, se incorpora a la *rama* original.

<a name="item2"></a>
## Lenguajes

Un ordenador trabaja con electricidad. Dentro, la parte más importante es el **microprocesador**. Tiene millones de circuitos electrónicos dentro. Está diseñado de manera que, uno tras otro, van pasando millonésimas de segundo en las que un cable enciende un voltaje y lo apaga, para que cada vez que se enciende, en un conjunto de cables *"pongamos"* encendidos o apagados los voltios, y según sea esta combinación de voltios, se lleven a esos circuitos electrónicos, y se produzca un resultado concreto, que aparece en forma de voltajes, encendidos o apagados, en ese mismo conjunto de cables.

Para representar el voltaje encendido, se usa normalmente el número **1**, mientras que el apagado es el **0**. De esa manera, podríamos escribir los voltajes que van ocurriendo en cada instante de manera parecida a esta:

    00101001
    01001000
    00100101
    00100110
    11001010
    10010100
    10100100
    00101001
    00100011
    etc.

En esa lista de unos y ceros, unas líneas serían el voltaje que produce que el microprocesador se *configure* para realizar una operación u otra, y otras serían el voltaje que el microprocesador produce como resultado.

Es tremendamente difícil de leer, de modo que en primer lugar nos conviene separar esas líneas en dos, una para el voltaje que entra en el microprocesador, y otra para el voltaje que sale:

    Entrada:              Salida:

    00101001
    01001000
    00100101
                          00100110
    11001010
    10010100
    10100100
                          00101001
                          00100011

    etc.                  Etc.

La parte de *Entrada* es la que nos interesa aquí. Eso es un *programa*. Y al principio se escribían así. Hace ya más de 70 años. Y es tan complicado de entender, y puede provocar tantos errores de diseño, que ya desde el principio empezaron a usarse métodos para facilitar esto.

### Códigos.

#### Hexadecimal
La primera simplificación de este sistema numérico ***binario*** es reducir cada ***palabra*** de ocho dígitos a una reducción más fácil de leer. Se trata del código ***hexadecimal***. Cada grupo de cuatro unos y ceros se puede representar con un *carácter* o *dígito* de un conjunto de 16 diferentes. Como nuestro sistema decimal numérico solamente tiene 10, lo que se hace es usar esos 10 y añadir 6 letras. Así, el grupo de voltajes 0000 representaría al número cero, y usamos ese número cero como abreviatura. El 0001 pasará a ser el número 1, y el 0010 (que es el siguiente contando en el sistema binario) será el 2, y así hasta llegar al 1001 que es el 9. El siguiente, 1010 será la letra A, el 1011 será la B, y el último, 1111 es la F.

Un ejemplo de programa ahora resultará más fácil de leer:

    ...
    23
    25
    33
    3A
    B1
    B3
    44
    etc.

Pero no es más fácil de entender. Para eso tendremos que conocer qué obliga a hacer cada número en el microprocesador. Por ejemplo podría ocurrir que el número 33 conectara los circuitos del microprocesador para leer los dos siguientes datos y sumarlos. Así, los siguientes (3A y B1) no hacen nada, son solamente los números que hay que sumar. Pero también podría ser que el número 23 que hay antes sea la instrucción de multiplicar, y entonces los dos siguientes son los números, y el 33 es un número para multiplicar y no una instrucción. Hay que diferenciar de alguna manera lo que son ***instrucciones*** y lo que son ***datos***.

#### Ascii

 En los ordenadores es casi inevitable que tengamos que guardar datos. Y es muy frecuente que se trate de documentos, que contienen texto. Por ejemplo, este documento que estás leyendo.

 En los primeros años se utilizó extensamente el código ***Ascii*** para esta tarea. En este código se hace una equivalencia entre los números binarios que representan el voltaje en el ordenador con las letras, símbolos y números necesarios para escribir texto.

 ![código Ascii](Imagenes/ascii_parte.png)

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
