# with open("/workspaces/data_3500_homework/hw4/TSLA.txt") as file:
#     lines = file.readlines()

# prices = []
# for line in lines:
#     line = float(line)
#     prices.append(line)

# print(prices)

daily_prices = [float(line) for line in open("/workspaces/data_3500_homework/hw4/TSLA.txt").readlines()]

print(daily_prices)

i = 0
holding = False # The code was buying multiple times in a row so ChatGPT helpped with this part
buy = 0
total_profit = 0
first_buy = 0

for price in daily_prices:
    if i > 5:
        moving_avg = (daily_prices[i-1] + daily_prices[i-2] + daily_prices[i-3] + daily_prices[i-4] + daily_prices[i-5])/5

    

        if price < moving_avg * 0.98 and not holding:
            buy = price
            holding = True
            print(f"Bought at {price}")

            if first_buy == 0:
                first_buy = price

        
        elif price > moving_avg * 1.02 and holding:
            sell = price
            profit = sell - buy
            total_profit += profit
            holding = False
            print(f"Sold at {price}\nProfit: {profit}")

        else:
            pass

    i += 1

print("Total Profit:", total_profit)
print("First Buy:", first_buy)
final_profit_percentage = ( total_profit / first_buy ) * 100

print("% Return:", final_profit_percentage)