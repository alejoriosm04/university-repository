from dummy import *
from graphing import *
from neural_network import *


def main():
    ## Create dummy data
    data = createDummies(int(input('How many data?: ')))

    ## Classify patients
    prediagnostico_patients, examenes_laboratorio_patients, tratamiento_patients, salida_patients = classification(data)

    ## Show one of the lists of patients
    print("===" * 20)
    seeList(tratamiento_patients)
    
    ## Create services and add patients according to their status
    prediagnostico = Service("Prediagnóstico", prediagnostico_patients)
    examenes_laboratorio = Service("Exámenes de Laboratorio", examenes_laboratorio_patients)
    tratamiento = Service("Tratamiento", tratamiento_patients)
    salida = Service("Salida", salida_patients)

    ## Create a list with all services
    services = [prediagnostico, examenes_laboratorio, tratamiento, salida]
    
    ## Graphing services
    graphingServices(services)

    ## Sort services
    services = quickSort(services)

    ## Sort patients in each service
    prediagnostico_patients = quickSort(prediagnostico_patients)
    examenes_laboratorio_patients = quickSort(examenes_laboratorio_patients)
    tratamiento_patients = quickSort(tratamiento_patients)
    salida_patients = quickSort(salida_patients)

    ## Show services with their information
    print("===" * 20)
    seeList(services)

    ## Substract the information of each service and add it to a list
    data_services = []
    for service in services:
        data = [service.total_time, len(service.patients), service.average_time]
        data_services.append(data)   

    ## Create a neural network or load a previous one
    neural_network_results = neural_network(data_services)

    ## Print the results of the neural network
    for result in neural_network_results:
        if result == 0:
            print("This service is in a critical situation \n \t - It has a high number of patients \n \t - It has a high average time of waiting \n \t - It is necessary to increase the number of doctors and equipment")
        elif result == 1:
            print("This service is in a normal situation \n \t - It has a normal number of patients \n \t - It has a normal average time of waiting \n \t - It is necessary to maintain the number of doctors and equipment")
        elif result <= 0.5:
            print("This service should be reviewed and put into analysis and observation \n \t - It has a low number of patients \n \t - It has a medium average time of waiting \n \t - It is necessary to increase the number of doctors and equipment")
        elif result >= 0.5:
            print("This service should be reviewed and put into analysis and observation \n \t - It has a high number of patients \n \t - It has a low average time of waiting \n \t - It is necessary to improve the distribution of doctors and equipment to have a better service")


if __name__ == '__main__':
    main()