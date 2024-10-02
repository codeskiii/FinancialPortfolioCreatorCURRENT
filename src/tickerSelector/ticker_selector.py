import numpy as np

class TickerSelector:
    def __init__ (self,
                  tickers = list[np.array] 
                  ) -> None:
        
        self.tickers_predictions = tickers

    def pick_one(self) -> list[int]:
        pass 