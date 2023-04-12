def tipoCohete(cohete):
    if cohete["carga"] > 50000:
        return "Carga superpesada"
    elif cohete["carga"] > 20000:
        return "Carga pesada"
    elif cohete["carga"] > 2000:
        return "Carga media"
    elif cohete["carga"] <= 2000:
        return "Carga liviana"