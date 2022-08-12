def mascorrupto2(arreglo, i=1):
    if i == len(arreglo)-1:
        return i
    else:
        i_dinero_mas_corrupto = mascorrupto2(arreglo, i+2)
        dinero = arreglo[i]
        dinero_mas_corrupto = arreglo[i_dinero_mas_corrupto]
        if dinero_mas_corrupto > dinero:
            return i_dinero_mas_corrupto
        else:
            return i


def mascorrupto(arreglo):
    return arreglo[mascorrupto2(arreglo)-1]


def main():
    arreglo = ["Calvarini",100,"Pinturosky",200,"Tajardini",400]
    print(mascorrupto(arreglo))


if __name__ == '__main__':
    main()