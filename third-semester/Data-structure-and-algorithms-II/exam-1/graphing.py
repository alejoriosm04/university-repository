import matplotlib.pyplot as plt


def graphingServices(services):
    ## Create 4 subplots for each service
    ## On each plot, show the evolution of duration time with each patient according to their status

    fig, axs = plt.subplots(4)
    fig.suptitle('Evolution of the times of each service')
    i = 0

    ## Prediagnostico
    x = []
    y = []
    for patient in services[0].patients:
        i += 1
        x.append(i)
        y.append(patient.time1)

    axs[0].plot(x, y)
    axs[0].set_title(services[0].name)

    ## Exámenes de Laboratorio
    x = []
    y = []
    for patient in services[1].patients:
        i += 1
        x.append(i)
        y.append(patient.time2)

    axs[1].plot(x, y)
    axs[1].set_title(services[1].name)

    ## Tratamiento
    x = []
    y = []

    for patient in services[2].patients:
        i += 1
        x.append(i)
        y.append(patient.time3)

    axs[2].plot(x, y)
    axs[2].set_title(services[2].name)

    ## Salida
    x = []
    y = []

    for patient in services[3].patients:
        i += 1
        x.append(i)
        y.append(patient.time4)

    axs[3].plot(x, y)
    axs[3].set_title(services[3].name)

    ## Adjust subplots
    plt.subplots_adjust(wspace=0.4, hspace=0.9)

    plt.show()


def graphingNeuralNetwork(historial):
    ## Create a plot for the neural network
    plt.xlabel("# of workouts")
    plt.ylabel("Magnitude of loss")
    plt.plot(historial.history["loss"])
    plt.show()