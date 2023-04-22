lat = 34.5
lon = 45.6
posicion = [lat, lon]

historial = [
    [34.5, 45.6, "2022/02/02 17:20:24"],
    [34.5, 46.3, "2022/02/02 17:20:34"],
    [35.5, 47.3, "2022/02/02 17:20:44"],
    [34.5, 47.3, "2022/02/02 17:20:55"],
    [33.5, 49.3, "2022/02/02 17:20:59"],
]

indiceFecha = 2
indiceLongitud = 0
indiceLatitud = 1

for coordenada in historial:
    print(coordenada[indiceLongitud])

for coordenada in historial:
    print(coordenada[indiceFecha])

for coordenada in historial:
    print(coordenada[indiceLatitud])

for coordenada in historial:
    print(coordenada)

"""print(historial[0][indiceFecha])
print(historial[1][indiceLatitud])"""

