import numpy as np

class TickerSelector:
    def __init__ (self,
                  tickers = list[tuple[str, np.array]] 
                  ) -> None:
        
        self.tickers_predictions = tickers

    def pick_one(self) -> list[tuple[str, int]]:
        # help cointainer
        list_of_predictions: list[tuple[str, int]] = []
        #print(self.tickers_predictions)
        for ticker_tuple in self.tickers_predictions:
            #print(ticker_tuple)
            ticker = (ticker_tuple[0], ticker_tuple[1].iloc[-1])
            list_of_predictions.append(ticker)

        print(list_of_predictions)