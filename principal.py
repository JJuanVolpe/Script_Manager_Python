#Menú Principal de opciones formado con dicc.
def callMenu(opciones):

	for i in opciones:					#Iterando e imprimiendo opciones
		print(str(i) + ") " + opciones[i])
	eleccion = str(input("Ingrese la opción deseada por su número:"))
	return eleccion[0]






def Autenticacion():
	passw = "brainstorming"
	tried = 0		#Intentos ingresando password
	while(tried < 3):
		hit = str(input("Ingrese la contraseña para ser admitido por el sistema:\n"))
		if (hit.__eq__(passw)):		#Usuario reconocido? entonces sale del loop, sino suma un intento
			print("Bienvenido usuario!\n")
			break
		tried = tried+1
	return tried

"""Variables que convienen ser creada de una sola vez y ser usadas a través de parámetros , 
			ya que sino se re-implementaría con cada invocación a función"""

#Genero Diccionario del menú principal
MenudeOpciones = {
    1 : "Teléfonos y contactos útiles por covid:" ,
    2 : "Líneas telefónicas de atención en caso de situaciones de emegencia" ,
    3 : "Números de asistenciaa las 24hs" ,
    4 : "Páginas con más información",
    5 : "Salir del programa"
}

TelefonoYContactos = {
	"Ministerio de Salud" : "Llamá al 120, es gratuito desde cualquier lugar del país y te atienden las 24 horas.",
		"Whatsapp" : "Escribí `Hola´ (sin comillas) al número +54 9 11 2256-0566 y comenzá a chatear.",





}

ListaOpciones = []




###Main
ok = (Autenticacion() < 3)				#Booleano que indica si hubo menos de 3 intentos

if (not ok):							#Si hubo 3 intentos será bloqueado.
	print(" \nBloqueado\n")
	quit()

while (ok):								# Entramos al menú/loop principal de nuestro Script/App.
	choice = callMenu(MenudeOpciones)
	if (choice == "5"):
		quit()
	elif (choice== "1" or choice== "2" or choice== "3"):
		print(ListaOpciones);





