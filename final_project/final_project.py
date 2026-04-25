import json
import requests
import datetime
import time

# keys for the api json 
market_key  = "market_data"
price_key   = "prices"
usd_key     = "usd"

coins = ["bitcoin", "ethereum", "litecoin", "ripple", "eos", "bitcoin-cash"]

# ChatGPT helped me with this mostly because I couldn't get my API to work for more than 5 calls for some reason and chat gave me a faster method
for coin in coins:
    url = "https://api.coingecko.com/api/v3/coins/"+coin+"/market_chart?vs_currency=usd&days=365"
    headers = {"x-cg-demo-api-key": "CG-T3VAcVRkovDN6vgF8YQ1fnb8"}
    response = requests.get(url, headers=headers)
    data = response.json()

    file = open(coin + ".csv", "w")
    file_lines = []

    for entry in data["prices"]:
        timestamp = entry[0] / 1000  # convert ms → seconds
        price = entry[1]

        date = datetime.datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y")
        file_lines.append(f"{date}, {round(price, 2)}\n")

    file.writelines(file_lines)
    file.close()

def load_prices(coin):
    prices = []
    with open(coin + ".csv", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 2:
                prices.append(float(parts[1]))
    return prices

def mean_reversion(prices, coin):
    print(f"\n{coin} Mean Reversion Strategy Output:")
    buy = 0
    first_buy = None
    total_profit = 0
    last_signal = None

    for i in range(len(prices)):
        if i > 4:
            current_price = prices[i]
            avg = sum(prices[i-5:i]) / 5

            if current_price < avg * 0.98 and buy == 0:
                buy = current_price
                last_signal = "buy"
                print(f"buying at:       {round(buy, 2)}")
                if first_buy is None:
                    first_buy = buy

            elif current_price > avg * 1.02 and buy != 0:
                print(f"selling at:      {round(current_price, 2)}")
                trade_profit = current_price - buy
                print(f"trade profit:    {round(trade_profit, 2)}")
                total_profit += trade_profit
                buy = 0
                last_signal = "sell"

    if last_signal:
        print(f"{coin}: You should {last_signal} today (Mean Reversion)")

    percent_return = (total_profit / first_buy) * 100 if first_buy else 0

    print("-----------------------")
    print(f"Total profit:    {round(total_profit, 2)}")
    print(f"First buy:       {round(first_buy, 2) if first_buy else 0}")
    print(f"Percent return:  {round(percent_return, 2)}")

    return total_profit, percent_return

def simpleMovingAverageStrategy(prices, coin):
    print(f"\n{coin} Simple Moving Average Strategy Output:")

    position = 0
    buy_price = 0
    total_profit = 0
    first_buy = None
    last_signal = None

    for i in range(1, len(prices)):
        avg = sum(prices[:i]) / i
        price = prices[i]

        if price > avg and position == 0:
            print(f"buying at: {price}")
            buy_price = price
            last_signal = "buy"
            if first_buy is None:
                first_buy = price
            position = 1

        elif price < avg and position == 1:
            print(f"selling at:      {price}")
            trade_profit = price - buy_price
            print(f"trade profit:    {trade_profit}")
            total_profit += trade_profit
            position = 0
            last_signal = "sell"

    # If still holding at the end
    if last_signal:
        print(f"{coin}: You should {last_signal} today (SMA)")

    percent_return = (total_profit / first_buy) * 100 if first_buy else 0

    print("-----------------------")
    print(f"Total profit:    {total_profit}")
    print(f"First buy:       {first_buy if first_buy else 0}")
    print(f"Percent return:  {percent_return}")

    return total_profit, percent_return

def save_results(results):
    with open("/workspaces/data_3500_homework/FinalProject/results.json", "w") as f:
        json.dump(results, f, indent=4)

results = {}

for coin in coins: 
    

    prices = load_prices(coin)
    results[coin+"_Prices"] = prices

    mr_total_profit, mr_returns = mean_reversion(prices, coin)
    results[coin+"_MR_Profit"]  = mr_total_profit
    results[coin+"_MR_Returns"] = mr_returns

    sma_total_profit, sma_returns = simpleMovingAverageStrategy(prices, coin)
    results[coin+"_SMA_Profit"]  = sma_total_profit
    results[coin+"_SMA_Returns"] = sma_returns

# ChatGPT helped me with this part
best_profit = float("-inf")
best_coin = ""
best_strategy = ""

for key in results:
    if "Profit" in key:
        if results[key] > best_profit:
            best_profit = results[key]
            best_coin = key.split("_")[0]
            best_strategy = key.split("_")[1]

results["Best_Coin"] = best_coin
results["Best_Strategy"] = best_strategy
results["Best_Profit"] = best_profit

save_results(results)