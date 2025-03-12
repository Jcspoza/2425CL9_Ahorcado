# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 10
# Resumen: Crear los datos de una agenda con
# nombre apellido y numero de telfono y mostrarlos 
# Topicos nuevos: Listas, for recorriendo listas
# Creditos 
# Fecha JCSP 2025 01 13
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

LAgenda = []
fin = False

while not fin:
    persona = []
    nombre = input('Nombre :')
    persona.append(nombre)
    apellido = input('Apellido :')
    persona.append(apellido)
    telefono = int(input('Telefono :'))
    persona.append(telefono)
    
    LAgenda.append(persona)
    
    fin = (input('Fin de intoduccion').upper()[0] == 'S')
    
# listar los datos de la agenda, 1 linea por persona
for pers in LAgenda:
    for dato in pers:
        print(dato, end=' ')
        
    print() 
