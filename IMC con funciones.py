def calcularIMC(peso, altura):
    imc = peso / (altura * altura)
    return imc




#Calculadora de IMC
# IMC = Peso / (ALTURA * ALTURA)
# < 19 delgadez
# entre 20 y 25 normal
# entre 26 y 30: sobrepeso
# > de 30 obesidad

def pedirElIMC():
    peso = int(input('ingrese su peso en kg'))
    alturaEnCentimetros = int(input('ingrese su altura en centimetros'))
    altura = alturaEnCentimetros /100
    imc = calcularIMC(peso, altura)
    print('su IMC es de'+ str(imc))
    if imc < 20:
        print('Estado de delgadez')
    if imc >= 20 and imc < 26:
        print('Peso normal')
    if imc >= 26 and imc < 60:
        print('Sobrepeso')
    if imc > 30:
        print('obesidad')

pedirElIMC()