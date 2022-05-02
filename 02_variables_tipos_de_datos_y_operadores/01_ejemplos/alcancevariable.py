contador = 0

def saludar(lista_nombres):
    contador = 0
    for nombre in lista_nombres:
        contador += 1
        print(f'Hola {nombre}!')
    print(f'Hemos saludado a {contador} personas\n')

def acceso_variable_global():
    print(f'El valor del contador global es {contador}')

def modificacion_variable_global(nuevo_valor):
    global contador
    contador = nuevo_valor

def main():
    contador = 0
    cursos = {
        'python3iniciorapido': ['Luis', 'Sara', 'Juan', 'Alicia'],
        'otrocursodepython' : ['Estudiante Despistado']
        }
        
    for nombre_curso, alumnos in cursos.items():
        contador += 1
        print(f'Vamos a saludar a los alumnos del curso {nombre_curso}')
        saludar(alumnos)
    
    print(f'Hemos saludado a los alumnos de {contador} cursos')

    acceso_variable_global()
    modificacion_variable_global(37)
    acceso_variable_global()

if __name__ == '__main__':
    main()
