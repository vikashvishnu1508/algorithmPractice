# # cook your dish here
# def maxProfitWithKTransactions(prices, k):
#     # Write your code here.
# 	profit = []
# 	for i in range(len(prices) - 1):
# 		for j in range(i, len(prices)):
# 			if (j == len(prices) - 1):
# 				if (prices[i] < prices[j]):
# 					profit.append(prices[j] - prices[i])
# 			else:
# 			    if ((prices[i] < prices[j]) and (prices[j] > prices[j + 1])):
# 			        profit.append(prices[j] - prices[i])
# 	profit.sort(reverse=True)
# 	return sum(profit[:k]), profit


# print(maxProfitWithKTransactions([50, 25, 12, 4, 3, 10, 1, 100], 2))

# def Descending_Order(num):
#     #Bust a move right here
#     if num == 0:
#         return 0
#     num_array = []
#     while(num%10 != 0):
#         num_array.append(str(num%10))
#         num = int(num / 10)
#     num_array.sort(reverse=True)
#     return int(''.join(num_array))

# print('ans = ',Descending_Order(0))


# def getNthFib(n):
#     # Write your code here.
# 	fibonaci = [0 , 1]
# 	if n > 2:
# 		for i in range(2, n):
# 			fibonaci.append(fibonaci[i-2] + fibonaci[i-1])
# 	return fibonaci[n-1]

# print(getNthFib(10))
import numpy as np
def riverSizes(matrix):
    # Write your code here.
    vertical = []
    horizantal = []
    answer = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                if i < len(matrix)-1:
                    if matrix[i][j] == 1 and matrix[i + 1][j] == 1:
                        vertical.append([i, i + 1, j])
                        continue
                if j < len(matrix[0])-1:
                    if matrix[i][j] == 1 and matrix[i][j + 1] == 1:
                        horizantal.append([j, j + 1, i])
                        continue
                if i != 0 and j != 0:
                    if matrix[i-1][j] == 0 and matrix[i][j-1] == 0:
                        answer.append(1)
                if i == 0:
                    if matrix[i][j-1] == 0:
                        answer.append(1)
    print("vertical array")
    print(vertical)
    ver_count = [i[2] for i in vertical]
    for i in set(ver_count):
        if ver_count.count(i) == 1:
            answer.append(2)
        else:
            answer.append(ver_count.count(i))
    return answer
    
    # print("horizantal array")
    # print(horizantal)


testInput = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ]

print(riverSizes(testInput))