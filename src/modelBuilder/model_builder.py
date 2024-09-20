import pandas as pd
import keras

class ModelBuilder:
    def __init__(self) -> None:
        pass

    def build_model(self, ticker_df: pd.DataFrame,
                    target_column: str = "Target"                    
                    
                    ) -> keras.Sequential:
        
        model = keras.Sequential([])
