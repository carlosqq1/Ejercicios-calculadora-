
#Calculadora basica en python 

def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print(f" El resultado de: {numero1} y {numero2} es: {resultado}")
    
def restar(numero1, numero2):
    resultado = numero1 - numero2
    print(f"El resultado de: {numero1} y {numero2} es: {resultado}")
    
def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    print(f"El resultado de: {numero1} y {numero2} es: {resultado}")

def dividir(numero1, numero2):
    resultado = numero1 / numero2
    print(f"El resultado de: {numero1} y {numero2} es: {resultado}")
    

continuar = True

while continuar:
    primer_numero = int(input("Ingrese su primer numero: "))
    segundo_numero = int(input("Ingrese su segundo numero: "))
    operacion = input("Que operacion necesitas realizar: ")

    if operacion == "sumar":
        sumar(primer_numero, segundo_numero)

    elif operacion == "restar":
        restar(primer_numero, segundo_numero)

    elif operacion == "multiplicar":
        multiplicar(primer_numero, segundo_numero)
    
    elif operacion == "dividir":
        dividir(primer_numero, segundo_numero)
    
    else:
        print("Operacion invalida. Seleccione sumar,\
         restar, dividir, multiplicar ")
    
    deseas_continuar = input("Que operacion deseas realizar y/n: ")

    if deseas_continuar == "y":
        continuar = True
    elif deseas_continuar == "n":
        continuar = False
    else:
        print("Seleccion no valida")
        break
