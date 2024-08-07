class Service():
    def __init__(self, name, patients):
        self.name = name
        self.patients = patients
        self.total_time = 0
        for patient in patients:
            if self.name == "Prediagnóstico":
                self.total_time += patient.time1
            elif self.name == "Exámenes de Laboratorio":
                self.total_time += patient.time2
            elif self.name == "Tratamiento":
                self.total_time += patient.time3
            elif self.name == "Salida":
                self.total_time += patient.time4
        try:
            self.average_time = round(self.total_time / len(self.patients), 2)
        except ZeroDivisionError:
            self.average_time = 0

    def __str__(self):
        return f'{self.name}:\n\tPersonas en Total y Tiempo Total: {len(self.patients)+1} Personas atendidas en {self.total_time} minutos\n\tTiempo promedio: {self.average_time} minutos'

    def __gt__(self, nextService):
        return self.average_time > nextService.average_time
    
    def __lt__(self, nextService):
        return self.average_time < nextService.average_time
    
    def __eq__(self, nextService):
        return self.average_time == nextService.average_time
