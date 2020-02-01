def count(coins, m, n): 
	combinations = [0 for k in range(n+1)] 
	combinations[0] = 1
	for i in range(0,m): 
		for j in range(coins[i],n+1): 
			combinations[j] += combinations[j-coins[i]] 
	return combinations[n] 
coins = [1,2,5]
m = len(coins) 
amount = 12
x = count(coins, m, amount) 
print (x) 

import sys 
def minCoins(coins, m, n): 
	combinations = [0 for i in range(n + 1)] 
	combinations[0] = 0
	for i in range(1, n + 1): 
		combinations[i] = sys.maxsize 
	for i in range(m): 
		for j in range(coins[i], n + 1): 
			sub_res = combinations[j - coins[i]] 
			if (sub_res != sys.maxsize and sub_res + 1 < combinations[j]): 
					combinations[j] = sub_res + 1
	return combinations[n] 

if __name__ == "__main__": 

	coins = [9, 6, 5, 1]
	m = len(coins) 
	n = 11
	print("Minimum coins required is ", 
				minCoins(coins, m, n)) 

# This code is contributed by ita_c 
