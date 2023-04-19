#la idea de un diccionario es que a partir de un termino nos de su definicion
diccionario = {
    "Programar": "Programar es transformar el cafe en codigo",
    "POO": "Programacion Orientada a Objetos",
    "MVC": "Modelo Vista Controlador",
    "4": "cuatro",
    "5": "cinco",
    "17": "uno siete"
}
texto = input("ingrese un elemento del diccionario ")
textoFinal = ''
for letra in texto:
    textoFinal += diccionario[letra]

print(textoFinal)