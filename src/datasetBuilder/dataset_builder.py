import pandas as pd 

class DatasetBuilder:
    def __init__(self, tickers: list[dict]) -> None:
        self.tickers_to_analyze = tickers

    def build_dataset(self) -> pd.DataFrame:
        a = self.tickers_to_analyze[0]["stock_history"]
        b = pd.melt(self.tickers_to_analyze[0]["quarterly_income_stmt"]).set_index('variable')
        c = pd.melt(self.tickers_to_analyze[0]["quarterly_cashflow"]).set_index('variable')

        out_concat = pd.concat([a, b, c])
        out_concat_cleaned = out_concat.dropna(axis=1, how='all')

        ready_ticker = out_concat_cleaned.fillna(0)
        ready_ticker.to_csv("ready_ticker.csv")

        return pd.DataFrame()
