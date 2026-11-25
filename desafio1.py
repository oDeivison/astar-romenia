#imprimir as cidades que têm exatamente 1 estrada
from mapa import mapa_romenia, heuristica_bucareste

print("Cidades com exatamente 1 estrada: ")
for cidade in mapa_romenia:
    if len(mapa_romenia[cidade]) == 1:
        print(f" {cidade}")

#cidades com h(n) menor que 200km
print("Cidades com h(n) menor que 200km: ")
for cidade in mapa_romenia:
    if heuristica_bucareste[cidade] < 200:
        print(f" {cidade}")

#estrada mais longa do mapa
print("Estrada mais longa do mapa: ")
max_custo = 0
cidade_origem = ""
cidade_destino = ""
for cidade in mapa_romenia:
    for vizinho, custo in mapa_romenia[cidade]:
        if custo > max_custo:
            max_custo = custo
            cidade_origem = cidade
            cidade_destino = vizinho
print(f" {cidade_origem} -> {cidade_destino} = {max_custo} km")
