#Para dar un poco de color: Usaremos sus atributos de clase como color en el texto de la Terminal (código de color implementado cómo propiedad)
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    LB = '\033[94m' #LIGHTBLUE
    RESET = '\033[0m' #RESET COLOR


#Funciones generales al principio para ser invocadas desde el principio

def	imprimirDic(D):
	for items in D:					#Iterando e imprimiendo opciones
		print(str(items) + " " + D[items])


def generarConsejoenDic():
	indice = len(MenudeConsejos) + 1			#Asigno indice correspondiente a la opcion número N (agregando 1 que es la opcion entrante)
	indice = str(indice)						#Casting entrante: longitud del Dicc(int) a String
	indice = bcolors.OK + indice + "~" + bcolors.RESET			#Detalle de color
	item = str(input("A continuacion ingrese el consejo que desee agregar al listado:"))
	item =  bcolors.OK + item + bcolors.RESET					#Detalle de color
	MenudeConsejos[str(indice)] = item


#Proceso de llamado de menu principal
def callMenu(opciones):
	imprimirDic(opciones) #Imprime opciones del Menú principal
	eleccion = str(input("Ingrese la opción por el número correspondiente:"))
	return eleccion[0]

#Proceso de Login
def Autenticacion():
	passw = "brainstorming"
	tried = 0		#Intentos ingresando password
	while(tried < 3):
		hit = str(input(bcolors.LB + "Ingrese la contraseña para ser admitido por el sistema:" + bcolors.RESET))
		if (hit.__eq__(passw)):		#Usuario reconocido? entonces sale del loop, sino suma un intento
			print(bcolors.OK + "\nBienvenido usuario!" + bcolors.RESET)
			break
		tried = tried+1
	return tried


#	Variables creadas al principio, con el fin de ser usadas a través de parámetros, para evitar re-implementarlas en funciones

#	Genero Diccionario del menú principal
MenudeOpciones = {
    "\n1)" : " Teléfonos y contactos útiles por covid:" ,
    "2)" : " Páginas con más información" ,
    "3)" : " Consejos y recomendaciones época de pandemia" ,
    "4)" : " Agregar consejo y/0 recomendación",
    "5)" : " Salir del programa"
}

#Genero Diccionario de Teléfonos
TelefonoYContactos = {
	"Ministerio de Salud: " : "Número  " + bcolors.WARNING  + "120" + bcolors.RESET + " es gratuito y te atienden las 24 horas.",
	"Whatsapp: " : "Escribí `Hola´ (sin comillas) al número" + bcolors.WARNING  + " +54 9 11 2256-0566 " + bcolors.RESET + "y comenzá a chatear.",
	"Portal de COVID-19 (GBA): " : "Número " + bcolors.WARNING  + "148 " + bcolors.RESET + ", linea que recibe consultas, dudas y reportes de síntomas de COVID-19.",
	"Línea oficial para dudas o síntomas de coronavirus COVID-19: " :  bcolors.WARNING  + "0800-777-8476" + bcolors.RESET + "." ,
	"Servicio de videollamada para personas con discapacidad auditiva: " : "Lunes a viernes de 10 a 15 horas: " +  bcolors.WARNING  + "11-5728-4011" + bcolors.RESET + ".\n"
}

#Genero Diccionario de páginas web recomendadas
PaginasWeb = {
	"Información, recomendaciones y medidas de prevención del Ministerio de Salud de la Nación:" : "https://www.argentina.gob.ar/salud/coronavirus-COVID-19",
	"Cuidados e información útil:" : "https://www.argentina.gob.ar/salud/coronavirus/cuidarnos",
	"Teléfonos de provincias y CABA:" : "https://www.argentina.gob.ar/coronavirus/telefonos/provincias-caba \n"
}

#Genero Diccionario de Consejos
MenudeConsejos = {
    bcolors.OK + "1~" : "El barbijo tiene que cubrirte la nariz, la boca y el mentón" ,
    			 "2~" : "Mantener una buena higiene, tanto personal cómo con el medio" ,
    			 "3~" : "Evitar aglomeración de gente o lugares con frecuentados por multitud " ,
    			 "4~" : "Si no te sentís bien, quedate en casa" + bcolors.RESET
}

#Generamos una lista de diccionarios para iterar facilmente, generar mayor reusabilidad y generalización de código.
ListaOpciones = [TelefonoYContactos, PaginasWeb, MenudeConsejos]


###	Main  Script
ok = (Autenticacion() < 3)				#Boolean que indica si hubo menos de 3 intentos

if (not ok):							#Si hubo 3 intentos será bloqueado.
	print( bcolors.FAIL + " \nBloqueado\n" + bcolors.RESET)
	quit()

while (ok):								# Entramos al menú/loop principal de nuestro Script/App.
	choice = callMenu(MenudeOpciones) 	# Directamente devolvemos el numero de la opcion en el menú
	if (choice == "5"):
		print(bcolors.LB + "Bye !" + bcolors.RESET)
		quit()
	elif (choice== "1" or choice== "2" or choice== "3"):
		x = int(choice)-1                     #Restamos uno a la eleccion para acceder al índice correcto en la lista de diccionarios.
		imprimirDic(ListaOpciones[x]);		  #Accedemos a lista de diccionarios
	elif (choice == "4"):
		generarConsejoenDic()
		print(bcolors.LB + "Consejo Agregado correctamente!" + bcolors.RESET)

