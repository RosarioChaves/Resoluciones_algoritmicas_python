def clasificar(num):
    if num<0: tipo="Negativo"
    elif num==0: tipo="Cero"
    else:tipo="Positivo"
    return tipo
numeros = []

while True:
    opci=int(input("\nMENÚ\n1. Clasificación de números\n2. Suma de números y promedio\n3. Suma Dígitos\n4. Salir\n"))

    if opci==1:
        print("___ Clasificación de Números ___")
        print("Ingrese números\nPrecione '*' para salir:  ")
        num = input()
        while num!="*":
            num=int(num)
            print(f"{num} es {clasificar(num)}")
            num = input()

    elif opci==2:
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

    elif opci==3:
        suma_digitos=0
        numero=int(input("Ingrese un número entero: "))
        for digito in str(numero):
            suma_digitos+=int(digito)
        print(f"La suma de los dígitos del número {numero} es: {suma_digitos}")

    elif opci==4:
        print("Se cerrará el programa...")
        break
    else:
        print("Opción inválida")

