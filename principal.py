#Para dar un poco de color: Usaremos sus atributos de clase como color en el texto de la Terminal (código de color implementado cómo propiedad)
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


#Funciones generales al principio para ser invocadas desde el principio

def	imprimirDic(D):
	for items in D:					#Iterando e imprimiendo opciones
		print(str(items) + " " + D[items])


def callMenu(opciones):
	imprimirDic(opciones) #Imprime opciones del Menú principal
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

"""	Variables que convienen ser creada de una sola vez y ser usadas a través de parámetros ,
			ya que sino se re-implementaría con cada invocación a función"""

#Genero Diccionario del menú principal
MenudeOpciones = {
    1 : ") Teléfonos y contactos útiles por covid:" ,
    2 : ") Páginas con más información" ,
    3 : ") Consejos y recomendaciones al azar" ,
    4 : ")Agregar consejo y recomendación",
    5 : ") Salir del programa"
}

TelefonoYContactos = {
	"Ministerio de Salud" : " número  " + bcolors.WARNING  + "148" + bcolors.RESET + " es gratuito y te atienden las 24 horas.",
	"Whatsapp" : " Escribí `Hola´ (sin comillas) al número" + bcolors.WARNING  + " +54 9 11 2256-0566 " + bcolors.RESET + "y comenzá a chatear.",
	"Portal de COVID-19 (GBA)" : "número " + bcolors.WARNING  + "148 " + bcolors.RESET + "es gratuito y te atienden las 24 horas.",
}

ListaOpciones = []




###Main
ok = (Autenticacion() < 3)				#Booleano que indica si hubo menos de 3 intentos

if (not ok):							#Si hubo 3 intentos será bloqueado.
	print( bcolors.FAIL + " \nBloqueado\n" + bcolors.RESET)
	quit()

while (ok):								# Entramos al menú/loop principal de nuestro Script/App.
	choice = callMenu(MenudeOpciones)
	if (choice == "5"):
		quit()
	elif (choice== "1" or choice== "2" or choice== "3"):
		print(ListaOpciones[choice]);




