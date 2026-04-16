import json
import requests

def initial_data_pull(ticker):
    url = "https://api.openweathermap.org/data/2.5/weather?zip="+ticker+",1&appid=4c3b45d12f72163e1e4d671b6f145594"

    request = requests.get(url)
    stock_dictionary = json.loads(request.text)

    # keys i need
    time = "Time Series (Daily)"
    # key2 = "2026-04-06"
    price = "4. close"

    file = open("stock_market_trading_project/" + ticker + ".csv", "w")

    for date in list(stock_dictionary[time].keys())[::-1]:
        # print(date, stock_dictionary[time][date][price])
        file.write(date + ", " + stock_dictionary[time][date][price] + "\n")

    file.close()