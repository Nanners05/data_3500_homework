import json
import random
def load_prices(ticker):
    with open(f"/workspaces/data_3500_homework/hw5/{ticker}.txt") as file:
        prices = [round(float(line.strip()), 2) for line in file if line.strip()]
    return prices

def mean_reversion(prices, ticker):
    print(f"\n{ticker} Mean Reversion Strategy Output:")

    buy = 0
    first_buy = None
    total_profit = 0

    for i in range(len(prices)):
        if i > 4:
            current_price = prices[i]
            avg = sum(prices[i-5:i]) / 5

            if current_price < avg * 0.98 and buy == 0:
                buy = current_price
                print(f"buying at:       {round(buy, 2)}")
                if first_buy is None:
                    first_buy = buy

            elif current_price > avg * 1.02 and buy != 0:
                print(f"selling at:      {round(current_price, 2)}")
                trade_profit = current_price - buy
                print(f"trade profit:    {round(trade_profit, 2)}")
                total_profit += trade_profit
                buy = 0

    if buy != 0:
        print(f"buying at:       {round(buy, 2)}")

    percent_return = (total_profit / first_buy) * 100 if first_buy else 0

    print("-----------------------")
    print(f"Total profit:    {round(total_profit, 2)}")
    print(f"First buy:       {round(first_buy, 2) if first_buy else 0}")
    print(f"Percent return:  {round(percent_return, 2)}")

    return total_profit, percent_return
def simpleMovingAverageStrategy(prices, ticker):
    print(f"\n{ticker} Simple Moving Average Strategy Output:")

    position = 0
    buy_price = 0
    total_profit = 0
    first_buy = None

    for i in range(1, len(prices)):
        avg = sum(prices[:i]) / i
        price = prices[i]

        if price > avg and position == 0:
            print(f"buying at: {price}")
            buy_price = price
            if first_buy is None:
                first_buy = price
            position = 1

        elif price < avg and position == 1:
            print(f"selling at:      {price}")
            trade_profit = price - buy_price
            print(f"trade profit:    {trade_profit}")
            total_profit += trade_profit
            position = 0

    # If still holding at the end
    if position == 1:
        print(f"buying at: {buy_price}")

    percent_return = (total_profit / first_buy) * 100 if first_buy else 0

    print("-----------------------")
    print(f"Total profit:    {total_profit}")
    print(f"First buy:       {first_buy if first_buy else 0}")
    print(f"Percent return:  {percent_return}")

    return total_profit, percent_return

def save_results(results):
    json.dump(results, open("/workspaces/data_3500_homework/hw5/results.json", "w"), indent=4)

# main body of code

tickers = ["ADBE", "AMZN", "AAPL", "BA", "CMCSA", "CVX", "GOOG", "JPM", "TSLA", "V"]
results = {}

for ticker in tickers: 
    

    prices = load_prices(ticker)
    results[ticker+"_Prices"] = prices

    mr_total_profit, mr_returns = mean_reversion(prices, ticker)
    results[ticker+"_MR_Profit"]  = mr_total_profit
    results[ticker+"_MR_Returns"] = mr_returns

    sma_total_profit, sma_returns = simpleMovingAverageStrategy(prices, ticker)
    results[ticker+"_SMA_Profit"]  = sma_total_profit
    results[ticker+"_SMA_Returns"] = sma_returns
    

save_results(results)