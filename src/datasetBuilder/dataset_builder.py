import pandas as pd 

class DatasetBuilder:
    def __init__(self, tickers: list[dict]) -> None:
        self.tickers_to_analyze = tickers

    def build_dataset(self) -> pd.DataFrame:
        a = self.tickers_to_analyze[0]["stock_history"]
        b = pd.melt(self.tickers_to_analyze[0]["quarterly_income_stmt"]).set_index('variable')
        c = pd.melt(self.tickers_to_analyze[0]["quarterly_cashflow"]).set_index('variable')

        a = a.set_index(a.index.normalize().tz_localize(None)) 
        b = b.set_index(b.index.normalize().tz_localize(None)) 
        c = c.set_index(c.index.normalize().tz_localize(None)) 
    
        a = a[~a.index.duplicated(keep='first')]
        b = b[~b.index.duplicated(keep='first')]
        c = c[~c.index.duplicated(keep='first')]

        out_concat = pd.concat([a, b, c], axis=1)
        out_concat_cleaned = out_concat.dropna(axis=1, how='all')

        ready_ticker = out_concat_cleaned.fillna(0)
        ready_ticker.to_csv("ready_ticker.csv") 

        return pd.DataFrame()
