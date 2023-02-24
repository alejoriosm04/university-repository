import random
from data import *


class Patient():
    def __init__(self):
        self.name = giveName()
        self.age = round(random.uniform(18, 90), 0)
        self.illness = giveIllness()
        self.status = giveStatus()
        self.time1 = round(random.uniform(1, 600), 0)
        if self.status == "Exámenes de Laboratorio":
            self.time2 = round(random.uniform(1, 600), 0)
        else:
            self.time2 = 0
        if self.status == "Tratamiento":
            self.time2 = round(random.uniform(1, 600), 0)
            self.time3 = round(random.uniform(1, 600), 0)
        else:
            self.time3 = 0
        if self.status == "Salida":
            self.time2 = round(random.uniform(1, 600), 0)
            self.time3 = round(random.uniform(1, 600), 0)
            self.time4 = round(random.uniform(1, 600), 0)
        else:
            self.time4 = 0
        self.total_time = self.time1 + self.time2 + self.time3 + self.time4

    def __str__(self):
        return f'Nombre: {self.name}\nEdad: {self.age} años \nEnfermedad: {self.illness}\nEstado: {self.status}\nTiempo 1: {self.time1} minutos \nTiempo 2: {self.time2} minutos \nTiempo 3: {self.time3} minutos \nTiempo 4: {self.time4} minutos \nTiempo Total: {self.total_time} minutos'


def giveName():
	name = random.choice(names)
	surname1 = random.choice(surnames)
	surname2 = random.choice(surnames)
	return f'{name} {surname1} {surname2}' 


def giveIllness():
    return random.choice(illnesses)


def giveStatus():
    return random.choice(statuses)
