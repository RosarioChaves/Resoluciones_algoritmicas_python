def clasificar(num):
    if num<0: tipo="Negativo"
    elif num==0: tipo="Cero"
    else:tipo="Positivo"
    return tipo

def contar_ocurrencias_letras(frase):
    contador={}
    frase=frase.lower()# Convertir a minúsculas
    for letra in frase:
        if letra.isalpha():
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
    return contador
       
numeros = []

while True:
    opci=int(input("\nMENÚ\n1. Contador de letras\n2. Clasificación de números\n3. Suma de números y promedio\n4. Suma Dígitos\n5. Salir\n"))
    if opci==1: #Contar numero de ocurrencias de cada letra del alfabeto que tiene una frase que ingrese el usuario
        print("___ Contador de Letras ___")
        frase=input("Ingrese una frase:  ")
        ocurrencias=contar_ocurrencias_letras(frase)
        print("Número de ocurrencias de cada letra:")
        for letra, cantidad in ocurrencias.items():
            print(f"{letra}: {cantidad}")

    elif opci==2:
        print("___ Clasificación de Números ___")
        print("Ingrese números\nPrecione '*' para salir:  ")
        num = input()
        while num!="*":
            num=int(num)
            print(f"{num} es {clasificar(num)}")
            num = input()

    elif opci==3:
        print("___ Suma de Números y Promedio ___")
        num=int(input("Ingrese números enteros\nPrecione '0' para salir: "))
        total=0
        promedio=0

        while num!=0:
            numeros.append(num)
            total+=num
            promedio=round(total / len(numeros),2)
            num=int(input())
        print(f"La sumatoria de los números ingresados es: {total}")
        print(f"El promedio es: {promedio}")

    elif opci==4:
        suma_digitos=0
        numero=int(input("Ingrese un número entero: "))
        for digito in str(numero):
            suma_digitos+=int(digito)
        print(f"La suma de los dígitos del número {numero} es: {suma_digitos}")

    elif opci==5:
        print("Se cerrará el programa...")
        break
    else:
        print("Opción inválida")

