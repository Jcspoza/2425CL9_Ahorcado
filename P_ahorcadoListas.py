# Taller Programación y Robótica en CMM BML – 2023 - Clase 5
# Resumen: progrma complementario a usar con CL5 Ahoracdo 1_5
# Define todas las listas
# Fecha JCSP 2023 03 16
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

AHORCADO_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

PALABRAS = 'gato perro burro raton'.split()

ALFABETO = 'abcdefghijklmnñopqrstuvwxyz'

MAXFALLOS = len(AHORCADO_PICS) - 1 # el primer dibujo es con 0 fallos

MENS_PRESENTA = """Vamos a jugar al A H O R C A D O
Yo eleguiré una palabla de nombre de animal.
Tu dirás letras de esa palabra, y yo te diré si las letras pertenecen o no a la palabra elegida,
Tienes un maximo de """ + str(MAXFALLOS) + """ fallos. Las letras acentuadas se simplificaran a sin acento, por facilidad.
Empezamos ..."""



     
