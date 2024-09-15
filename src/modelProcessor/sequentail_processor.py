# TO DO
import pandas as pd
import keras

class SequentialProcessor:
    def __init__(self, tickers: list[pd.DataFrame]) -> None:
        self.tickers = tickers

    def future_builder(self, ticker: pd.DataFrame) -> None:
        pass

    def process_tickers(self) -> None:
        for ticker in self.tickers:
            self.process_ticker(ticker)