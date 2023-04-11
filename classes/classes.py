from random import randint, random
import pandas as pd

class Centroid:
    def __init__(self, id:int):
        self.id = id
        self.initialize_centroid()
        self.indexs_in_table = []

        
    def new_values(self):
        tot = len(self.indexs_in_table)
    #para cada atributo do centroid vai ser zerado
        for key in self.atributos.keys():
            self.atributos[key] = 0
    #O atributo da vez vai receber uma média da soma deste atributo em cada instancia que esta em seu agrupamento
            for i in self.indexs_in_table:
                self.atributos[key] += i.atributos[key] / tot

    def zerar_lista(self):
        self.indexs_in_table.clear()

    def initialize_centroid(self):
        self.atributos =  {
                    "Alcohol": randint(1,3),
                    "Malic_acid": randint(0,14) + random(),
                    "Ash": randint(0,5) + random(),
                    "Alcalinity_of_ash": randint(0,2) + random(),
                    "Magnesium": randint(0,30) + random(), 
                    "Total_phenols": randint(0,10),
                    "Flavanoids": randint(0,10),
                    "Nonflavanoid_phenols": randint(0,10),
                    "Proanthocyanins": randint(0,10), 
                    "Color_intensity": randint(0,10),
                    "Hue": randint(0,10),
                    "OD280/OD315_of_diluted_wines": randint(0,10),
                    "Proline":randint(0,10)}
        
class Wine:

    def __init__(self, linha:int, atributos:dict):
        self.atributos = atributos
        self.linha = linha
        self.cluster = -1

    def change_cluster(self, new_cluster:int):
        self.cluster = new_cluster
