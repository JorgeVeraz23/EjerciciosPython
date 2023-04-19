"""arreglo = ['banana', 'melon', 'sandia', 'pera']

arreglo.append('kiwi')
arreglo.reverse()
arreglo.remove('banana')

for fruta in arreglo:
    print('la fruta es: '+fruta)
print('------------------------------')
for fruta in arreglo:
    if fruta.endswith('a'):
        print("La fruta es: " + fruta)
print('------------------------------')
for fruta in arreglo:
    if fruta == 'sandia':
        break
    print("La fruta es: " + fruta)"""

texto = 'hola mundo'

for letra in texto:
    print("Letra "+letra)

for numero in range(10):
    if(numero > 5):
        print(numero)

print('-------------------------------------------')

for numero in range(6,10):
    print(numero)