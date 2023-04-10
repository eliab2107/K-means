import csv
from random import randint, random


table = []
vinho_quality_red = {"fixed_acidity": 0, "volatile_acidity": 0, "citric_acid": 0,
                             "residual_sugar": 0, "chlorides": 0, "free_sulfur_dioxide": 0, "total_sulfur_dioxide": 0,
                             "density": 0, "pH": 0, "sulphates": 0, "alcohol": 0, "quality": 0}

arquivo = open('../databases/winequality-red.csv')
vinhos = csv.reader(arquivo)
maior = 0
for vinho in vinhos:
    vinho_atual = vinho[0].split(';')
    for i in range(0, len(vinho_atual)):
        try:
            vinho_atual[i] = int(vinho_atual[i])
        except:
            vinho_atual[i] = float(vinho_atual[i])

    vinho_quality_red["fixed_acidity"] = vinho_atual[0]
    vinho_quality_red["volatile_acidity"] = vinho_atual[1]
    vinho_quality_red["citric_acid"] = vinho_atual[2]
    vinho_quality_red["residual_sugar"] = vinho_atual[3]
    vinho_quality_red["chlorides"] = vinho_atual[4]
    vinho_quality_red["free_sulfur_dioxide"] = vinho_atual[5]
    vinho_quality_red["total_sulfur_dioxide"] = vinho_atual[6]
    vinho_quality_red["density"] = vinho_atual[7]
    vinho_quality_red["pH"] = vinho_atual[8]
    vinho_quality_red["sulphates"] = vinho_atual[9]
    vinho_quality_red["alcohol"] = vinho_atual[10]
    vinho_quality_red["quality"] = vinho_atual[11]

    #Para definir o inicio aleatório dos centroids foi avaliado o maior valor encontrado em cada parametro para estabelecer
    #um valor limite para a inicialização aleatoria dos centroids
    if vinho_quality_red["quality"] > maior:
        maior = vinho_quality_red["quality"]
    table.append(vinho_quality_red.copy())
# A tabela é uma lista de dicionarios em que cada dict representa uma linha do arquivo txt
# A ideia atual é usar essa tabela para instanciar todos os elementos da classe wine dentro de uma outra lista.
print(maior)
arquivo.close()



