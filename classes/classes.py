from random import randint, random
import pandas as pd

class centroid:
    def __int__(self, id: int, atributos: dict, clustering: list):
        self.id = randint(0, 10)
        self.atributos = atributos
        self.clustering = clustering


    def new_values(self):
        tot = len(self.clustering)
    #para cada atributo do centroid vai ser zerado
        for key in self.atributos.keys():
            self.atributos[key] = 0
    #O atributo da vez vai receber uma média da soma deste atributo em cada instancia que esta em seu agrupamento
            for i in self.clustering:
                self.atributos[key] += i[key] / tot


    def initialize_centroid(self):
        self.atributos = {"fixed_acidity": randint(0, 15) + random(), "volatile_acidity": random() + random(),
                 "citric_acid": random(), "residual_sugar": randint(0, 15) + random(), "chlorides": random(),
                 "free_sulfur_dioxide": randint(0, 100), "total_sulfur_dioxide": randint(0, 300),
                 "density": random() + random(), "pH": randint(0, 4) + random(), "sulphates": randint(0, 2) + random(),
                 "alcohol": randint(0, 15), "quality": randint(0, 9) + random()}

class wines:

    def __int__(self, atributos:dict, cluster:int):
        self.atributos = atributos
        self.cluster = -1

    def change_cluster(self, new_cluster:int):
        self.cluster = new_cluster

