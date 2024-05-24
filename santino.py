from os import system

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menu():
    print("Menu de Opciones")
    print("1- Ingresar 1er operando")
    print("2- Ingresar 2do operando")
    print("3- Elegir operacion")
    print("4- Resetear operandos")
    print("5- Salir")
    return input("Ingrese opcion: ")

def elegir_operacion():
    print("Elegir operación")
    print("a- Suma")
    print("b- Resta")
    print("c- División")
    print("d- Multiplicacion")
    return input("Ingrese operacion: ")
    
def sumar(a:float,b:float)->float:
    return a + b

def restar(a:float,b:float)->float:
    return a - b

def dividir(a:float,b:float)->float:
    return a / b

def multiplicar(a:float,b:float)->float:
    return a * b

def obtener_num():
    return float(input("Ingrese numero: "))
    
def pedir_confirmacion(mensaje: str) -> bool:
    rta = input(mensaje).lower()
    return rta == "s"

operando1 = None
operando2 = None
seguir = True

while seguir:
    limpiar_pantalla()
    
    opcion = menu()
    match opcion:
        case "1":
            if operando1 is None:
                operando1 = obtener_num()
            else:
                print("El numero 1 ya fue ingresado")
        case "2":
            if operando1 is not None:
                if operando2 is None:
                    operando2 = obtener_num()
                else:
                    print("El numero 2 ya fue ingresado")
            else:
                print("Primero ingresa el operando 1")
        case "3":
            if operando1 != None and operando2 is not None:
                operacion = elegir_operacion()
                match operacion:
                    case "a":
                        resultado = sumar(operando1, operando2)
                        print(f"El resultado de la suma es= {resultado}")
                    case "b":
                        resultado = restar(operando1, operando2)
                        print(f"El resultado de la resta es= {resultado}")
                    case "c":
                        if operando2 != 0:
                            resultado = dividir(operando1, operando2)
                            print(f"El resultado de la division es= {resultado}")
                        else:
                            print("Error: División por cero")
                    case "d":
                        resultado = multiplicar(operando1, operando2)
                        print(f"El resultado de la multiplicacion es= {resultado}")
                    case _:
                        print("Operación no válida")
            else:
                print("Primero ingresa ambos operandos")
        case "4":
            if pedir_confirmacion("Deseas resetear los operandos? s/n: "):
                operando1 = None
                operando2 = None
                print("Operandos reseteados.")
        case "5":
            if pedir_confirmacion("Confirma salida? s/n: "):
                seguir = False
        case _:
            print("Opción no válida")
        
    pausar()

print("Fin del programa")