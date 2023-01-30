def mergeSort(data):
    if len(data) <= 1:
        return data

    if len(data) == 2:
        return sorted(data)

    middleData = len(data)//2
    return merge(mergeSort(data[:middleData]), mergeSort(data[middleData:]))


def merge(leftData, rightData):
    person1 = 0
    person2 = 0
    result = []

    while(person1 < len(leftData) and person2 < len(rightData)):
        if leftData[person1] < rightData[person2]:
            result.append(leftData[person1])
            person1+=1
        else:
            result.append(rightData[person2])
            person2+=1
        
    result += leftData[person1:] + rightData[person2:]
    return result