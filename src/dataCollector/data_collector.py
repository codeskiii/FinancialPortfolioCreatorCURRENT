import yfinance as yf

class DataCollector:
    def __init__(self,
                tickers: list[str],
                wanted_data_from_ticer: list[str] = None
                ) -> None:
        
        self.wanted_tickers = tickers
        

    def collect_data(self):
        downloaded_ticers = (yf.Tickers(self.wanted_tickers))
        downloaded_ticers_list = [downloaded_ticers.tickers[(ticer_name)] for ticer_name in downloaded_ticers.tickers]
        to_dump = []

        for ticker in downloaded_ticers_list:
            filtered = dict()
            
            filtered["stock_symbol"] = ticker.info["symbol"]
            filtered["stock_history"] = ticker.history(period="max")
            filtered["quarterly_income_stmt"] = ticker.quarterly_income_stmt
            filtered["quarterly_cashflow"] = ticker.quarterly_cashflow

            to_dump.append(filtered)

        return to_dump