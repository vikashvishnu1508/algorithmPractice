def getPermutations(array):
    # Write your code here.
    n = len(array)
    permutationsCount = 1
    for i in range(1, n + 1):
        permutationsCount *= i
    print(permutationsCount)
    result = [ ]
    print(result)
    i = 1
    

print(getPermutations([1,2,3]))
