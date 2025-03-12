# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 10
# Resumen: Crear los datos de una agenda con
# nombre apellido y numero de telfono y mostrarlos 
# Topicos nuevos: Listas, for recorriendo listas
# Creditos 
# Fecha JCSP 2025 01 13
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

LAgenda = [['Jose', 'Santamaria', 678367722], # cada persona es a su vez una lista de 3 datos
           ['Juan', 'Gonzalez', 683201745],
           ['Leo', 'Soria', 621095349],
           ['Carlos', 'Lopez', 687523082]
           ]
    
# listar los datos de la agenda, 1 linea por persona
for pers in LAgenda:
    for dato in pers:
        print(dato, end=' ')
        
    print() 
