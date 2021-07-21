#Menú Principal de opciones formado con dicc.
def callMenu():

	opciones = {
    1 : "Teléfonos y contactos útiles por covid:" ,
    2 : "Líneas telefónicas de atención en caso de situaciones de emegencia" ,
    3 : "Números de asistenciaa las 24hs" ,
    4 : "Páginas con más información",
    5 : "Salir del programa"
	}
	for i in opciones:					#Iterando e imprimiendo opciones
		print(str(i) + ") " + opciones[i])

	eleccion = str(input("Ingrese la opción deseada por su número:"))
	return eleccion[0]
def Select(sel):
			print(arreglo[sel])





def Autenticacion():
	passw = "brainstorming"
	tried = 0		#Intentos ingresando password
	while(tried < 3):
		hit = str(input('Ingrese la contraseña para ser admitido por el sistema:'))
		if (hit.__eq__(passw)):		#Usuario reconocido? entonces sale del loop, sino suma un intento
			print('Bienvenido usuario!\n')
			break
		tried = tried+1
	return tried

###Main

if (Autenticacion() == 3):
	print(" \nBloqueado\n")
	quit()

while (True):
	choice = callMenu()
	if (choice == "5"):
		quit()




