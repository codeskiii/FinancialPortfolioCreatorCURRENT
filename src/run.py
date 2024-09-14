from dataCollector.data_collector import DataCollector

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "ADBE", "NFLX", "PINS"]
    data_collector = DataCollector(tickers)
    data = data_collector.collect_data()
