def powerset(array):
    # Write your code here.
    result = []
    for i in range(len(array)):
        result.append([array[i]])
        for j in range(i):
            result.append([array[j], array[i]])
    for i in range(1, len(array) + 1):
        tempArr = setHelper(array[:i])
        for k in tempArr:
            if k not in result:
                result.append(k)
    return result


def setHelper(array):
    result = []
    for i in range(len(array) + 1):
        result.append( [array[k] for k in range(len(array)) if k != i ] )
    return result

print(powerset([1, 2, 3, 4,5]))