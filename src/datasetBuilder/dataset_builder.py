import pandas as pd 

class DatasetBuilder:
    def __init__(self, tickers: list[dict]) -> None:
        self.tickers_to_analyze = tickers

    def build_tickers_datsets(self) -> list[pd.DataFrame]:
        processed_tickers = []
        for ticker in self.tickers_to_analyze:
            processed_tickers.append(self.build_dataset(ticker))

        return processed_tickers

    def build_dataset(self, ticker: dict) -> pd.DataFrame:
        a = ticker["stock_history"]
        b = pd.melt(ticker["quarterly_income_stmt"]).set_index('variable')
        c = pd.melt(ticker["quarterly_cashflow"]).set_index('variable')

        a = a.set_index(a.index.normalize().tz_localize(None)) 
        b = b.set_index(b.index.normalize().tz_localize(None)) 
        c = c.set_index(c.index.normalize().tz_localize(None)) 

        a = a[~a.index.duplicated(keep='first')]
        b = b[~b.index.duplicated(keep='first')]
        c = c[~c.index.duplicated(keep='first')]
        
        out_concat = pd.concat([a, b, c], axis=1)
        out_concat_cleaned = out_concat.dropna(axis=1, how='all')
        out_concat_cleaned.replace(0, pd.NA, inplace=True)
        out_concat_cleaned.fillna(method='ffill', inplace=True)

        ready_ticker = out_concat_cleaned.fillna(0)
        # DEBUG ONLY
        #ready_ticker.to_csv("ready_ticker.csv") 

        return pd.DataFrame()
