def sumatoria(n,p,suma):
    while n>0 :
        suma = suma + n*p
        n = n- 1
        sumatoria(n,p,suma)
    return suma      
suma= 0   
numero1=  int(input('inrese un numero: '))
numero2= int(input('inrese un numero: '))
sumatotal = sumatoria(numero1,numero2,suma)
print('la sumatoria es: ', sumatotal)
