from patient import *
from service import *


def createDummies(total):
    try:
        if total > 0:
            list = []
            for item in range(total):
                list.append(Patient())
            return list
    except:
        return None


def seeList(list):
    i = 1
    for item in list:
        print(f'({i}) {item}')
        print("===" * 20)
        i+=1


def classification(list):
    prediagnostico_patients = []
    examenes_laboratorio_patients = []
    tratamiento_patients = []
    salida_patients = []

    for patient in list:
        if patient.status == "Prediagnóstico":
            prediagnostico_patients.append(patient)
        elif patient.status == "Exámenes de Laboratorio":
            examenes_laboratorio_patients.append(patient)
        elif patient.status == "Tratamiento":
            tratamiento_patients.append(patient)
        elif patient.status == "Salida":
            salida_patients.append(patient)

    return prediagnostico_patients, examenes_laboratorio_patients, tratamiento_patients, salida_patients


def main():
    data = createDummies(int(input('How many data?: ')))
    prediagnostico_patients, examenes_laboratorio_patients, tratamiento_patients, salida_patients = classification(data)

    prediagnostico = Service("Prediagnóstico", prediagnostico_patients)
    examenes_laboratorio = Service("Exámenes de Laboratorio", examenes_laboratorio_patients)
    tratamiento = Service("Tratamiento", tratamiento_patients)
    salida = Service("Salida", salida_patients)

    prediagnostico.quickSortPatients()
    examenes_laboratorio.quickSortPatients()
    tratamiento.quickSortPatients()
    salida.quickSortPatients()

    print("===" * 20)
    print(prediagnostico)

    seeList(data)


if __name__ == '__main__':
    main()