# You are given an array. Each element represents the price of a stock on that particular day.
# Calculate and return the maximum profit you can make from buying and selling that stock only once.

# For example: [9, 11, 8, 5, 7, 10]

# Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).

# Here's your starting point:
import math
def buy_and_sell(arr):
    stock_price_list_size = len(arr)
    if stock_price_list_size < 2:
        return None

    maxProfit = -math.inf
    for i in range(stock_price_list_size-1):
        for j in range(i,stock_price_list_size):
            diff = abs(arr[j] - arr[i])
            if diff > maxProfit:
                maxProfit = diff
    return maxProfit

  #Fill this in.
  
print(buy_and_sell([9, 11,20, 8, 5, 7, 10]))
# 5