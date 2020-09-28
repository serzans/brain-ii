import yfinance as yf
import json
import time
import random
import yaml
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_style("darkgrid")

def main():
  with open("config/tickers.yaml", "r") as yaml_file:
    config  = yaml.load(yaml_file)

  print(config)

  log_file_path = f"logs/{dt.datetime.now().isoformat()}.log"

  with open(log_file_path, "w") as log_file:
    log_file.write(f"Getting the data for tickers: ...") # TODO fix

  for ticker in config:
    yf_ticker = yf.Ticker(ticker)
  
    # TODO yf.download allows to specify period for data
    history = yf_ticker.history(period="5y")

    if not len(history):
      with open(log_file_path, "w") as log_file:
        log_file.write(f"Data for {ticker} not found")
      continue
  
    fig, ax = plt.subplots(figsize=(18,10))
    ax.plot(history["Close"])
    fig.savefig(f"figures/{ticker}_close.png")

    fig, ax = plt.subplots(figsize=(18,10))
    ax.plot(history["Volume"])
    fig.savefig(f"figures/{ticker}_volume.png")
  
    log_returns = np.log(history["Close"] / history["Close"].shift(1))
 
    fig, ax = plt.subplots(figsize=(18,10))
    ax.plot(log_returns)
    fig.savefig(f"figures/{ticker}_log_returns.png")

  # time.sleep(random.random()*5)


if __name__ == "__main__":
  main()


