# cook your dish here
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
	profit = []
	for i in range(len(prices) - 1):
		for j in range(i, len(prices)):
			if (j == len(prices) - 1):
				if (prices[i] < prices[j]):
					profit.append(prices[j] - prices[i])
			else:
			    if ((prices[i] < prices[j]) and (prices[j] > prices[j + 1])):
			        profit.append(prices[j] - prices[i])
	profit.sort(reverse=True)
	return sum(profit[:k]), profit


#print(maxProfitWithKTransactions([50, 25, 12, 4, 3, 10, 1, 100], 2))

def Descending_Order(num):
    #Bust a move right here
    if num == 0:
        return 0
    num_array = []
    while(num%10 != 0):
        num_array.append(str(num%10))
        num = int(num / 10)
    num_array.sort(reverse=True)
    return int(''.join(num_array))

print('ans = ',Descending_Order(0))