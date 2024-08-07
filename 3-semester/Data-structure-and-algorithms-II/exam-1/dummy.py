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


def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()

    items_greater = []
    items_lower = []

    for item in list:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)
