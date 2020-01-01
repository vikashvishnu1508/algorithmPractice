def hasSingleCycle(array):
    # Write your code here.
    counter = [0 for i in array]
    i = 0
    while True:
        counter[i] += 1
        if counter[i] > 1:
            break
        currentIndex = i + array[i]
        if 0 <= currentIndex <= len(array) - 1:
            i = currentIndex
        elif currentIndex < 0:
            i = len(array) - abs(currentIndex)
        elif currentIndex > len(array) - 1:
            a = (len(array) - 1)
            i = currentIndex - (len(array) - 1) - 1
    i = 0
    for i in range(len(counter)):
        if i == 0 and counter[i] != 2:
            return False
        if i > 0 and counter[i] != 1:
            return False
    return True


print(hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 908, -26]))