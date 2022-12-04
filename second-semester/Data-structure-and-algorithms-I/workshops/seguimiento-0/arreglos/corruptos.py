def mascorrupto(corruptos):
    arr = corruptos
    highest_corrupt_money = arr[1]
    highest_corrupt = arr[0]

    for i in range(1, len(arr),2):
        if highest_corrupt_money < arr[i]:
            highest_corrupt = arr[i-1]
    
    return highest_corrupt
        


def run():
    corruptos = ["Calvarini",100,"Pinturosky",200,"Tajardini",400]
    print(mascorrupto(corruptos))


if __name__ == '__main__':
    run()