# Bases de programación en Python

En este primer capítulo veremos conceptos generales de Python, y explicaremos la extructura y formato de los archivos que usaremos durante el curso.

## Algunos conceptos básicos sobre el lenguaje Python

* Código abierto y completamente gratuíto:
    * Tanto para fines personales o educativos como para fines comerciales.
* Lenguaje de alto nivel:
    * Abstracción de aspectos más técnicos de programación.
* Fácil de escribir y leer:
    * La sintaxis de Python permite crear programas muy fáciles de interpretar y con gran funcionalidad en pocas líneas.
* Interpretado:
    * No precisa ser compilado para su ejecución.
* Multiplataforma y Portable:
    * Windows, Linux, Mac.
* Tipado dinámico:
    * No necesitamos declarar el tipo de variables, se determinan en tiempo de ejecución.
* Orientado a objetos:
    * Paradigma de programación con foco en la reusabilidad y modularidad.
* Gran comunidad y librerías:
    * Más de 370,000 proyectos en PyPi, el índice de paquetes de Python, que podemos utilizar directamente en nuestros programas.


## PEPs (Propuestas de Mejora de Python)

### Índice 

https://peps.python.org/pep-0000/

### Zen of Python

https://peps.python.org/pep-0020/

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### Guía de estilos: **PEP8**

Enlace: https://peps.python.org/pep-0008/

#### Usa **4 espacios** para identar:

```python
def funcion(valor):
    print(valor)
```

#### Limita las líneas a **79** caracteres:

```python
# Incorrecto
def funcion(valor):
    print(f"El valor que he recibido del usuario es: {valor}")
    print("Esta línea no es correcta debido a que por exceso de texto estoy superando el ancho máximo de 79 caracteres lo que hace que el código no sea legible y va en contra de la guía de estilos de pep8")
```

```python
# Correcto
with open('/ruta/a/un/archivo/para/leer') as archivo_1, \
     open('/ruta/a/un/archivo/para/escribir', 'w') as archivo_2:
    archivo_2.write(archivo_1.read())
```

#### No uses espacios en blanco innecesarios:

```python
# Correcto
print(lista[1])
```

```python
# Incorrecto
print ( lista  [ 1 ] )
```

#### Nombres de clases, variables, constantes y funciones:

```python
class NombreDeClase:
    pass

nombre_de_variable = "Hola"

def nombre_de_funcion():
    pass

NOMBRE_DE_CONSTANTE = 5
```

#### Espacios entre operadores:

```python
# Correcto
contador = 1
contador = contador + 1
contador += 1
valor = contador*2 - 1
resultado = contador*contador + valor*valor
resultado = (valor+contador) * (valor-contador)

# Incorrecto
contador=1
contador=contador+1
contador +=1
valor = contador * 2 - 1
resultado = contador * contador + valor * valor
resultado = (valor + contador) * (valor - contador)
```

#### Imports:

```python
# Correcto
import os
import json

# Incorrecto
import os, json
```


## Ejercicio: **01_hola_mundo**
Siguiendo los ejemplos anteriores, escribe una **función** que reciba dos números y muestre en una línea el texto **"Hola Mundo"** y en la siguiente el **resultado de la suma de ambos números**. Intenta seguir las recomendaciones de estilos del **PEP8**.

## Estructura y formato de un programa Python
Un ejemplo de programa básico está disponible en:  ```01_ejemplos/programabasico.py```

## El intérprete interactivo de Python

Podemos ejecutar el intérprete interactivo de Python desde un terminal simplemente escribiendo:

```
python
```

Si solo tenemos instalada una versión de Python y no estamos usando entornos virtuales de Python (explicaremos qué son los entornos virtuales en futuruas secciones), basta con ejecutar el comando anterior. En caso contrario deberemos especificar por ejemplo la versión de Python que queremos usar para lanzar el intérprete interactivo:

```
python3
```

Una vez ejecutado, nos aparecerá una interfaz similar a la siguiente:
```bash
PS C:\Users\python\github\python3iniciorapido> python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

En estas primeras líneas veremos la versión de Python que estamos ejecutando. Para salir basta con escribir:

```
exit()
```

y pulsar Intro.