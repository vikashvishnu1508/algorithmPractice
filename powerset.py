def powerset(array):
    # Write your code here.
    result = [[]]
    for i in range(len(array)):
        for k in range(len(result)):
            result.append(result[k] + [array[i]])
    return result


print(powerset([1, 2, 3]))