class Service():
    def __init__(self, name, patients):
        self.name = name
        self.patients = patients
        self.total_time = 0
        for patient in patients:
            self.total_time += patient.total_time
        self.average_time = self.total_time / len(self.patients)

    def __str__(self):
        return f'{self.name}:\n\tPacientes: {self.patients}\n\tTiempo total: {self.total_time} minutos\n\tTiempo promedio: {self.average_time} minutos'

    def quickSortPatients(self):
        if len(self.patients) <= 1:
            return self.patients
        else:
            pivot = self.patients.pop()

        items_greater = []
        items_lower = []

        for item in self.patients:
            if item.total_time > pivot.total_time:
                items_greater.append(item)
            else:
                items_lower.append(item)

        return Service.quickSortPatients(items_lower) + [pivot] + Service.quickSortPatients(items_greater)
