def detectarEtapaVacunacion(edad):
    if edad > 50:
        return 1
    elif edad >= 30:
        return 2
    else:
        return 3