# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 9
# Nombre programa : P_ahorcado_Simple.py
# Version : 1.0 panel basico
# Resumen: Juego de adivinar palabras de un conjuto (animales) , con 8 intentos, 'ahorcado'
# Topicos nuevos: Listas, estructura de juego, trocear programa por bloques + probar x bloques
# Creditos : adaptacion de JCSP basado en "Invent with python" ed4 - cap. 7 , 8 y 9
# https://inventwithpython.com/invent4thed/chapter8.html
# Fecha JCSP 2023 03 16
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

# 0.1 Carga librerias necesarias
from random import randint
# 0.2 Carga constantes del juego
from P_ahorcadoListas import *
VERSION = 'Simple'

# 0.3 Definiciones de Funciones
def muestraPanel(letrasFall, letrasCorr, palabraSec):
    """Muestra el panel del juego en texto: dibujo ahoracado e info de letras falladas y acertadas
    Version 1.0 : panel basico
    """
    # primero el dibujo del ahoracado
    print(AHORCADO_PICS[len(letrasFall)]) # con mas letras falladas mas partes del ahorcado
    print()
    # Info de letras falladas
    print(f'Letras Falladas {len(letrasFall)} de {MAXFALLOS} fallos: {letrasFall}')
    # info de letras acertadas
    huecosPsec = len(palabraSec)
    huecosXrayas = '-' * huecosPsec
    print(f'{huecosPsec} huecos en palabra secreta: {huecosXrayas} ## Letras adivinadas: {letrasCorr}')  

def adivinaLetra(yaPropuestas):
    """Devuelve la letra propuesta por el jugador y chequea que sea una letra nueva"""
    letraPropuesta = ""
    while (letraPropuesta not in ALFABETO) or letraPropuesta in yaPropuestas: 
        letraPropuesta = input('Di 1 letra nueva:').lower()[0]
       
    return letraPropuesta
        
def CheckGano(palabraSec, letrasAdiv):
    """Chequea si el jugador ha adivinado todas las letras de palabraSec """
    for letra in palabraSec:
        if letra not in letrasAdiv:
            return False
            
    return True

def CheckPerdio(letFall, maxFall):
    """Chequea que no hemos sobrepasado el maximo de fallos"""
    
    return len(letFall) >= maxFall

# Fin de las definiciones de Funciones

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


# 2- BUCLE PRINCIPAL DE JUEGO
while not JuegoAcabado:
    # Paso 2.1 - Muestra panel de situacion: dibujo del ahorcado, y aciertos
    print('----------------------- Nuevo Intento -----------------------')
    muestraPanel(letrasFalladas, letrasCorrectas, palabraSecreta)

    # Paso 2.2 - El jugador debe proponer una letra distinta a las ya dichas
    propuesta = adivinaLetra(letrasFalladas + letrasCorrectas)

    # Paso 2.3 - Dinamica de juego -> Comprueba si letra propuesta esta en palabra a adivinar
    if propuesta in palabraSecreta:
        # Paso 2.3.A si letra propuesta esta en palabra secreta
        letrasCorrectas = letrasCorrectas + propuesta

        # Chequea si el jugador ha ganado       
        todasLetrasEncontradas = CheckGano(palabraSecreta, letrasCorrectas)
            
        JuegoAcabado = todasLetrasEncontradas               
            
    else: # Paso 2.3.B NO esta
        letrasFalladas = letrasFalladas + propuesta
        # Paso 2.3.B.2 Chequea si el jugador ha pasado su numero de fallos
        JuegoAcabado = CheckPerdio(letrasFalladas, MAXFALLOS)

# Bloque 3 FIN DEL JUEGO
#3.1 Muestara ultimo panel
print('===================== FIN DE JUEGO =====================')
muestraPanel(letrasFalladas, letrasCorrectas, palabraSecreta)
# 3.2 Mensajes de Ganar o Perder
if todasLetrasEncontradas:
    print('¡Si! La palabra secreta es "' + palabraSecreta + '"¡Has ganado!')
else:
    print('¡Has agotado todos los intentos!')
    print('Despues de fallar ' + str(len(letrasFalladas)) + ' veces y acertar ' + str(len(letrasCorrectas)) + ' veces. La palabra era "' + palabraSecreta + '"')
# FIN DE PROGRAMA