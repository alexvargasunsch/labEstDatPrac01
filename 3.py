def decimal_binario(entero):
    binario=0
    i=0
    if entero ==0:
        return 0
    while (entero>0):
        digito  = entero%2
        entero = int(entero//2)
        binario = binario+digito*(10**i)
        i = i + 1
    return 

numero = int(input("ingrese un numero entero que se convertira a binario: "))
resultado= decimal_binario(numero)
print('el numero ', numero ,' en binario es: ', resultado)