# CL9 - Python : 'Ahorcado' : 1er programa complejo - Listas y módulos - PyR 2024_25 CMM BML

Forma parte de la serie '**Workshop about Python and micropython with Pico W in CMM Benito**' Martin Madrid

Sigue la clase en los pfd CL9 y CL10

## Clase 9 - Indice - 90 minutos

- Módulos: ¿Por qué? Ventajas

- Diseño del ‘Ahorcado’: bloques en seudocódigo

- ESTUDIAR y PROBAR:   “AhorcadoSimple” + mejoras 1 y 2

## Tutoriales y Programas que vamos a seguir

### Tutoriales resumen

Del libro 'Invent with Python ..."'

[Chapter 7 - Designing Hangman with Flowcharts](https://inventwithpython.com/invent4thed/chapter7.html)

[Chapter 8 - Writing the Hangman Code](https://inventwithpython.com/invent4thed/chapter8.html)

----

### Tabla resumen de programas

| Programa                                     | Lenguaje | Objetivo de Aprendizaje                                                            |
| -------------------------------------------- | -------- | ---------------------------------------------------------------------------------- |
| [P_ahorcadoListas.py](P_ahorcadoListas.py)   | Py       |                                                                                    |
| [P_ahorcado_Simple.py](P_ahorcado_Simple.py) | Py       | Versión funcional pero simple del ahorcado + necesita importar P_ahorcadoListas.py |
| [P_ahorcado_Mej1.py](P_ahorcado_Mej1.py)     | Py       | reemplaza rayas con las letras correctas en su posición                            |
| [P_ahorcado_Mej1y2.py](P_ahorcado_Mej1y2.py) | Py       | Expande letras falladas y correctas con 1 caracter + por cada letra                |

### Recomendaciones de estudio despues de la clase

Leer Libro de python:

[Modulos](https://ellibrodepython.com/modulos-python#m%C3%B3dulos-en-python)

Nota : **explicar `__main__`**

## Módulos: ¿Por qué? Ventajas

Los módulos en Python son una de sus características más poderosas
y versátiles, son simplemente ficheros separados que se ejecutan junto a otros

* **Organización:**

Los módulos permiten organizar el código en unidades más pequeñas, lo que mejora la legibilidad y facilita la colaboración entre desarrolladores.

* **Reusabilidad:**

Permiten agrupar funciones, clases o bloques de código relacionados en el mismo archivo.
En lugar de copiar sus definiciones en varios programas, podemos definir
nuestras funciones más utilizadas en un módulo e importarlo.

* **Mantenibilidad:**

Al separar el código en módulos, es más sencillo realizar cambios, mejoras o correcciones en áreas específicas sin afectar el resto del programa.

Por razones didácticas, vamos a separar parte del programa del Ahorcado

[P_ahorcado_Simple.py](P_ahorcado_Simple.py)

en un modulo aparte :

[P_ahorcadoListas.py](P_ahorcadoListas.py)

para entender como funcionan los módulos y sus ventajas. 

Los 2 programas con mejoras de Ahorcado_simple, también requerirán importar el modulo

## Diseño del ‘Ahorcado’: bloques en seudocódigo

![](./ahorcadoseudocogigo.png)

## Estudiar y probar:   “AhorcadoSimple” + mejoras 1 y 2

### Modulo : P_ahorcadoListas.py

Aqui vamos a incluir :

* Dibujos del ahorcado como lista

* Lista de palabras secretas -> ver uso de [split](https://ellibrodepython.com/cadenas-python#splitsepnone-maxsplit-1)

* Alfabeto : letras que se consideran validas. En una primera versión no se utilizaran acentos

* Mensaje de presentación

### Programa Principal : P_ahorcado_simple.py

Veamos un diagrama de seudocódigo con más detalle

![](./seudocodigoDet.png)

El programa en Python incluye comentarios que siguen los bloques de seudocódigo, por ejemplo

```
# BLOQUE de juego 1 - INICIALIZACION
# 1.1 presentacion de Juego
print(f'Programa del ahorcado Clase 9 - Version {VERSION}')
print(MENS_PRESENTA)

# 1.2 Inicializacion de variables de juego
letrasFalladas = ''
letrasCorrectas = ''
JuegoAcabado = False

# 1.3 Eleccion de la palabra a adivinar
IndiceAleatorio = randint(0, len(PALABRAS) - 1)
palabraSecreta = PALABRAS[IndiceAleatorio] # eleccion de la palabra a adivinar
```

Se corresponden con los 2 últimos bloques de 1-INICIO

Se explicará en la clase cada bloque, pero antes conviene estudiar el concepto de programación funcional

### Programación Funcional

ver del libro de Python [Funciones](https://ellibrodepython.com/funciones-en-python)



---

### Punto de situación en el Mapa de conceptos de Programación

 ![](./mapaConceptos_prog.png)

Hemos visto :

* Módulos : (azul oscuro)

* Programación funcional

## Preguntas sobre la Clase 9 - 10 minutos

Sección para que los alumnos pregunten sus dudas durante la clase

---

TO DO :
