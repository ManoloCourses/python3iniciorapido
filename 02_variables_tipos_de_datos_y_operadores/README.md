# Variables, tipos de datos, operadores y funciones

En este capítulo veremos qué son las variables y cómo definirlas, los tipos y estructuras de datos más comunes en Python, operadores y funciones.

## Variables

### Declarar variables
```python
valor = 5
texto = "Hola Mundo"
contador = 0
```

### Casting
```python
valor = 5
texto = str(valor)
numero_en_texto = "5"
numero = int(numero_en_texto)
```

### Función type()
```python
valor = 5
texto = "Esto es una cadena de texto"
type(valor)
type(texto)
```

### Nombres de variables
```python
# Correcto
mi_valor = 5
valor = 5
valor_1 = 5
valor1 = 5

# Incorrecto
mi valor = 5
1valor = 5
valor-1 = 5
valor 1 = 5
```

### Asignación múltiple
```python
numero, texto = 5, "Mi texto"
```

### Imprimir variables por pantalla
```python
numero, texto = 5, "Mi texto"
print(numero)
print(texto)
```

### Palabras reservadas

Palabras reservadas:
https://docs.python.org/3/reference/lexical_analysis.html#keywords
* False
* None
* True
* class
* def
* if
* and
* with
* return
* try
* in
* raise
* and

Built-in:
https://docs.python.org/3/library/functions.html
* print
* type
* str
* float
* int
* range
* max
* min
* next
* len

Librería keyword: https://docs.python.org/3/library/keyword.html

```python
import keyword
keyword.iskeyword('False') 
```

## Tipos de datos y estructuras

### str
```python
cadena = 'Hola'
cadena_2 = "Hola Mundo"
cadena_3 = f'Esto es una f-string y aqui {cadena} usamos una variable'
cadena_4 = cadena + cadena_2
```

### bool
```python
verdadero = True
falso = False
```

### int
```python
numero = 1
```

### float 
```python
numero_decimal = 1.1
```

### list 
```python
lista_de_numeros = [1, 2, 3]
lista_de_cadenas = ["Hola", "Mundo"]
lista_mezclada = [1, "Hola"]
lista_con_list = list("Hola")
```

### tuple
```python
tupla = (1, 2, 3, "Hola", 1.2)
tupla_desde_lista = tuple([1, 2, 3])
```

### set
```python
conjunto = {1, 2, 3}
conjunto_desde_lista = set([1, 1 ,1, 2, 3, 4, 5, 6, 7, 1, 6, 5])
```

### range
```python
rango = range()
```

### dict
```python
diccionario = {'clave': 'valor'}
marcas = {1: 'Ferrari', 2: 'Aston Martin', 3: 'Lotus'}
precios = {'GT3Rs': 220000, '458Italia': 240000}
marcas_y_precios = {'marcas': marcas, 'precios': precios}
```

### NoneType
```python
variable_sin_valor = None
```

## Operadores 
https://docs.python.org/3/library/operator.html

### Asignación
```python
variable = 'Valor'
```

### Operación y asignación
```python
variable = 0
variable += 1
variable *= 2
variable /= 2
variable -= 1
```

### Suma y concatenación
```python
suma = 1 + 2
cadena_compuesta = "Hola" + " " + "Mundo"!
```

### Resta
```python
resta = 1 - 2
```

### Multiplicación
```python
multiplicacion = 2 * 2
```

### Division
```python
division = 50 / 2
division_con_decimales = 50 / 3
division_entera = 50 // 3
```

### Modulo
```python
modulo = 50 % 2
modulo_con_resto = 50 % 3
```

### Potencia
```python
potencia = 2 ** 4
```

### Mayor
```python
2 > 4
```

### Mayor o igual
```python
2 >= 4
4 >= 4
5 >= 4
```

### Menor
```python
2 < 4
```

### Menor o igual
```python
2 <= 4
4 <= 4
5 < 4
```

### Igual
```python
1 == 1
'Hola' == 'Hola'
1 == 2
'Hola' == 'Holas'
```

### Distinto
```python
1 != 1
'Hola' != 1
```

### Identidad
```python
1 is 1
1 is None
1 is 1.0
1 == 1.0
```

### And

### Or

### Not

## Funciones

### Alcance de una variable: local, enclosed, global, built-in


```python

```

