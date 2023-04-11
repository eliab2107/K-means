from math import sqrt
import csv
from random import randint, random
from classes.classes import Wine, Centroid

centroids = []

def distance_euclidian(cent_atributo, wine_atributo):
    dist = sqrt(((cent_atributo - wine_atributo)**2))
    return dist    
    
    
def create_centroids(num_centroids:int):
    global centroids
    for i in range(num_centroids):
        cent = Centroid(i)
        centroids.append(cent)
    

def define_centroid(wine:Wine, num_centroid):
    global centroids
    distancia = [0] * num_centroid
    for centroid in centroids:    
        for att in centroid.atributos:
            distancia[centroid.id] += distance_euclidian(centroid.atributos[att], wine.atributos[att])
    id = distancia.index(min(distancia))
    centroids[id].indexs_in_table.append(wine)
    return id

vinhos = []
vinho_quality_red = {
                    "Alcohol": 0,
                    "Malic_acid": 0,
                    "Ash": 0,
                    "Alcalinity_of_ash": 0,
                    "Magnesium": 0, 
                    "Total_phenols": 0,
                    "Flavanoids": 0,
                    "Nonflavanoid_phenols": 0,
                    "Proanthocyanins": 0, 
                    "Color_intensity": 0,
                    "Hue": 0,
                    "OD280/OD315_of_diluted_wines": 0,
                    "Proline":0}
arquivo = open('databases/wine.csv')
vinhs_arqv = csv.reader(arquivo)
maior = 0
for vinho in vinhs_arqv:
    for i in range(0, len(vinho)):
        try:
            vinho[i] = int(vinho[i])
        except:
            vinho[i] = float(vinho[i])

    vinho_quality_red["Alcohol"] = vinho[0]
    vinho_quality_red["Malic_acid"] = vinho[1]
    vinho_quality_red["Ash"] = vinho[2]
    vinho_quality_red["Alcalinity_of_ash"] = vinho[3]
    vinho_quality_red["Magnesium"] = vinho[4]
    vinho_quality_red["Total_phenols"] = vinho[5]
    vinho_quality_red["Flavanoids"] = vinho[6]
    vinho_quality_red["Nonflavanoid_phenols"] = vinho[7]
    vinho_quality_red["Proanthocyanins"] = vinho[8]
    vinho_quality_red["Color_intensity"] = vinho[9]
    vinho_quality_red["Hue"] = vinho[10]
    vinho_quality_red["OD280/OD315_of_diluted_wines"] = vinho[11]
    vinho_quality_red["Proline"] = vinho[12]

    #Para definir o inicio aleatório dos centroids foi avaliado o maior valor encontrado em cada parametro para estabelecer
    #um valor limite para a inicialização aleatoria dos centroids
    if vinho_quality_red["Proline"] > maior:
        maior = vinho_quality_red["Proline"]
    vinho = Wine(len(vinhos), vinho_quality_red.copy())
    vinhos.append(vinho)
    del(vinho)

arquivo.close()
# A tabela é uma lista de dicionarios em que cada dict representa uma linha do arquivo txt
# A ideia atual é usar essa tabela para instanciar todos os elementos da classe wine dentro de uma outra lista.

num_centroid = int(input())
create_centroids(num_centroid)

for i in range(5):
    for vinho in vinhos: 
        id = define_centroid(vinho, num_centroid)
        vinho.change_cluster(id)

    for centroid in centroids:
        centroid.new_values()
        centroid.zerar_lista()
        
    q = 0
    e = 0
    w = 0
    r = 0
    t = 0
    for i in vinhos:
        if i.cluster == 0:
            q += 1
        if i.cluster == 1:
            e += 1
        if i.cluster == 2:
            w += 1
        if i.cluster == 3:
            r += 1
        if i.cluster == 4:
            t += 1

    print( q ,' ', w ,'', '', e , ' ', ' ', r, ' ', ' ', t)
#print(q, ' -> ', centroids[0].atributos, '\n', w, '->', centroids[1].atributos, '\n', w, '->', centroids[2].atributos, '\n', w, '->', centroids[3].atributos, '\n', w, '->', centroids[4].atributos)