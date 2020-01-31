def powerset(array):
    # Write your code here.
    result = [[]]
    # for i in range(len(array)):
    #     # result.append([array[i]])
    #     for j in range(i + 1):
    #         # result.append([array[j], array[i]])
    #         # if j > 1:
    #         tempArr = [array[k] for k in range(j + 1)]
    #         if tempArr not in result:
    #             result.append(tempArr)
    # for i in range(len(array)):
    #     tempArr = [array[k] for k in range(len(array))  if k != i ]
    for i in range(len(array)):
        result.append( [array[k] for k in range(len(array)) if k != i ] )
    return result
    for i in range(1, len(array) + 1):
        result.append(setHelper(array[:i]))
    return result


def setHelper(array):
    result = []
    for i in range(len(array)):
        result.append( [array[k] for k in range(len(array)) if k != i ] )
    return result

print(powerset([1, 2]))