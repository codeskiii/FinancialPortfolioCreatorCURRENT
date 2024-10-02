
import pandas as pd
from modelBuilder.model_builder import ModelBuilder
import numpy as np
#from sklearn.preprocessing import StandardScaler

class SequentialProcessor:
    def __init__(self, tickers_datasets: list[pd.DataFrame]) -> None:
        self.model_builder = ModelBuilder()
        self.tickers_datasets = tickers_datasets
        self.output_datasets: list[tuple[str, np.array]] = []

    def build_target(self, ticker_df: pd.DataFrame,
                            target_column: str, 
                            target_frequency: int) -> pd.DataFrame:
        
        df_with_target = ticker_df.copy()
        #scaler = StandardScaler()
        
        df_with_target["Target"] = df_with_target[target_column].shift(-target_frequency)
        df_with_target = df_with_target.ffill()
        #df_with_target = scaler.fit_transform(df_with_target)

        return df_with_target

    def process_ticker(self, ticker: pd.DataFrame,
                       target_column: str = "Close", # column from df
                       target_frequency: int = 1 # in days
                       ) -> pd.DataFrame:
        
        dataset_with_target = self.build_target(ticker, target_column, target_frequency)
        model = self.model_builder.build_model(dataset_with_target)
        result = self.model_builder.result_collector(model, dataset_with_target)

        return result

    def process_tickers(self) -> None:
        for ticker in self.tickers_datasets:
            processed_array = self.process_ticker(ticker=ticker[1])
            ticker_tag: str = ticker[0]

            self.output_datasets.append((ticker_tag, processed_array))