import pandas as pd
import keras
from sklearn.preprocessing import StandardScaler

class ModelBuilder:
    def __init__(self) -> None:
        self.scaler = StandardScaler()

    def result_collector(self, model: keras.Sequential, 
                         ticker_df: pd.DataFrame,
                         target_column: str = "Target"
                         ) -> pd.DataFrame:
        #print(ticker_df.drop(columns=[target_column]).columns)
        print(ticker_df)
        X = ticker_df.drop(columns=[target_column])
        X = self.scaler.fit_transform(X)
        predictions = model.predict(X)
        print(predictions)
        #print(pd.DataFrame(predictions, columns=["Predictions"]))
        return pd.DataFrame(predictions, columns=["Predictions"])
    
    def build_model(self, ticker_df: pd.DataFrame,
                    target_column: str = "Target",
                    structure: list[dict] = [
                        {"layer_type": "dense", "units": 64, "activation": "relu"},
                        {"layer_type": "dense", "units": 32, "activation": "relu"},
                        {"layer_type": "dense", "units": 1}
                    ],
                    optimizer: str = "adam",
                    loss: str = "mse",
                    epochs: int = 10
                    ) -> keras.Sequential:
        
        model = keras.Sequential()

        for layer in structure:
            if "activation" in layer:
                model.add(keras.layers.Dense(layer["units"], activation=layer["activation"]))
            else:
                model.add(keras.layers.Dense(layer["units"]))

        model.compile(optimizer=optimizer, loss=loss)
        
        X = ticker_df.drop(columns=[target_column])
        X = self.scaler.fit_transform(X)

        y = ticker_df[target_column]
        #y.bfill(inplace=True)

        model.fit(X, y, epochs=epochs)

        model.summary()
        return model
