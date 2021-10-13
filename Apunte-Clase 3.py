import os                   #Nos permite operar Tareas sobre el SO

"""
print(os.listdir('/home/juan/PycharmProjects/battle'))#NOS MUESTRA LO QUE CONTIENE ARCHIVOS COMO LISTA ·

os.makedirs('/home/juan/PycharmProjects/NewAge')             Crear directorioso/carpetas desde Python
os.path.exist('/home/juan/PycharmProjects/NewAge')      Existe el archivo?
os.path.abspath('Google Chrome')      Devuelve la ruta del nombre archivo
os.path/Get.size('Google Chrome')      Devuelve la ruta del nombre archivo
os..('Google Chrome')      Devuelve la ruta del nombre archivo


archivo = open('home/juan/Escritorio/Facu/Datos-/constancia-cuil')
leer1=archivo.read()
print(leer1)
archivo.close



archivo.write()
archivo=open(direcc)
leer2=archivo.readlines() COnvierte el archivo en elementos de una lista

os.getcwd -----donde se ejecuta el programa
len(leer2)
"""
#       Hay que tener cuidado respecto a la eliminacion de programas PQ no van a la paapelera ·

archivo = open('/home/juan/Descargas/archivito')
leer1=archivo.read()
archivo.close
print(leer1)
archivo=open('/home/juan/Descargas/archivito')
archivo.write('Camila')

archivo.close


