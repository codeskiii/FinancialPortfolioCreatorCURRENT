import pandas as pd
import keras

class ModelBuilder:
    def __init__(self) -> None:
        pass

    def build_model(self, ticker_df: pd.DataFrame,
                    target_column: str = "Target",
                    structure: list[dict] = [
                        {"layer_type": "dense", "units": 64, "activation": "relu"},
                        {"layer_type": "dense", "units": 32, "activation": "relu"},
                        {"layer_type": "dense", "units": 1}
                    ],
                    optimizer: str = "adam",
                    loss: str = "mse"
                    ) -> keras.Sequential:
        
        model = keras.Sequential([])

        for layer in structure:
            if "activation" in layer:
                model.add(keras.layers.Dense(layer["units"], activation=layer["activation"]))
            else:
                model.add(keras.layers.Dense(layer["units"]))

        model.compile(optimizer=optimizer, loss=loss)
        model.fit(ticker_df.drop(columns=[target_column]), ticker_df[target_column], epochs=10)
        model.summary()

        return model
