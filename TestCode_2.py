def numberOfWaysToMakeChange(n, denoms):
    result = [[0 for i in range(n)] for j in range(len(denoms))]
    answer = 0
    i = 0
    while i < len(denoms):
        j = 0
        while j < n:
            if (j+1) % (denoms[i]) == 0:
                result[i][j] = 1
            if i == len(denoms) - 1:
                k = 0
                sum = 0
                while k < len(denoms):
                    sum += result[k][j]
                    k += 1
                if j < n - 1 and sum > 1:
                    answer += sum
                if j == n - 1:
                    answer += sum
            j += 1
        i += 1
    print(result)
    return answer


print(numberOfWaysToMakeChange(7, [2, 3, 4, 7]))
