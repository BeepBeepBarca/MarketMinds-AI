import pandas as pd
import matplotlib as plt
import yfinance
import xgboost as xgb
import yfinance as yt

data = pd.read_csv("indexData.csv", index_col=0)

data.head()

user = input("Choose a Stock Symbol: ")

stock = yfinance.download(user, start='2000-01-01', end='2024-01-01')

graph = plt.plot(stock)


def plot():
    plt.figure(figsize=(100, 100))
    plt.plot(stock)
    plt.title(f"{user} Stock over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

plot()