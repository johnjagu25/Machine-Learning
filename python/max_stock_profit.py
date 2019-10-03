# Given a array of numbers representing the stock prices of a company in chronological order,

# write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5,
# since you could buy the stock at 5 dollars and sell it at 10 dollars.


def maxProfit(stock_price_list):
    stock_length = len(stock_price_list)
    if stock_length > 1:
        max_profit = 0
        buy_price = stock_price_list[0]
        for val in range(1, len(stock_price_list)):
            sell_price = stock_price_list[val]
            if buy_price > sell_price:
                buy_price = sell_price
            else:
                diff = sell_price - buy_price
                if diff > max_profit:
                    max_profit = diff
        return max_profit
    
    else:
        return 0
    


print(maxProfit([9, 11, 20,8, 5, 7, 10,100]))
print(maxProfit([9]))
