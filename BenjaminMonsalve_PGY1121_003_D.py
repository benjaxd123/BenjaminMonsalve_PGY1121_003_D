from os import system

asientos=["1","2","3","4","5","6","7","8","9","10"
          ,"11","12","13","14","15","16","17","18","19"
          ,"20","21","22","23","24","25","26","27","28","29"
          ,"30","31","32","33","34","35","36","37","38","39"
          ,"40","41","42","43","44","45","46","47","48","49"
          ,"50","51","52","53","54","55","56","57","58","59"
          ,"60","61","62","63","64","65","66","67","68","69"
          ,"70","71","72","73","74","75","76","77","78","79"
          ,"80","81","82","83","84","85","86","87","88","89"
          ,"90","91","92","93","94","95","96","97","98","99"
          ,"100"]
reservar=[None]*100
registros=[]
total = 0
platinum = 120000
gold = 80000
silver = 50000

def pasua():
    input("Precione una telca para continuar.....")
    system("cls")

def menu():
    print(asientos)
    print("""
        [1]. Comprar Entradas.
        [2]. Mostrar ubicaciones disponibles.
        [3]. Ver listado de asistentes
        [4]. Mostrar ganancias.
        [5]. Salir.
        """)

def comprar_entrada(entrada):
    while True:
        if entr in "12345678910" and len(entr)==1 or 2 and asientos(int(entr))!="x":
            asientos[int(entr)-1 or 2 or 3]="X"
            reservar[int(entr)-1 or 2 or 3]=entrada
            print("Entrada comprada!")
            return
        else:
            print("Numero no valido o entrada ocupada...")

def disponibilidad():
    for i in range(len(asientos)):
        if reservar[i]!=None:
            print(f"{i + 1} - persona: {reservar[i]}")

def ver_listado_asis():
    print(f"El listado de asistentes va asi Número y Rut:{entrada}")



def ganancias_totales(registros):
    suma = 0
    for elementos in registros:
        suma += elementos
    return suma

def salir():
    pasua()

while True:
    menu()
    op=str(input("Ingrese una opcion: "))
    match op:
        case "1":
            entr=str(input("Ingrese la cantidad de entradas que desea: "))
            en = int(input("Reingrese la cantidad de entradas:"))
            rut=int(input("Ingrese su rut: "))
            entrada=[entr, rut]
            print("[1]-Platinium: $120.000 (Asiento del 1 al 21)\n[2]-Gold: 80.000 (Asiento del 21 al 50)\n[3]-Silver: 50.000 (Asieto del 51 al 100)\n¿Que tipo de asiento desea?")
            op = input("Ingrese una opción:")
            match op:   
                case "1":
                    print("El total a pagar es de: ==> $",en * platinum)
                case "2":
                    print("El total a pagar es de: ==> $",en * gold)
                case "3":
                    print("El total a pagar es de: ==> $",en * silver)
            comprar_entrada(entrada)
        case "2":
            print(asientos)
            disponibilidad()
        case "3":
            ver_listado_asis()
            pass
        case "4":
            print(registros)
            print(ganancias_totales(registros))
        case "5":
            salir()