# Tickers analyzer

## How to configure dependencies

1. Install python and pip

2. Download packages

```
pip install -r requirements.txt
```

3. Edit config.json

## How to setup config.json

# depedencies

* tickers - tickers to analyze

[!WARNING]
Tickers must be avialable in yfinance/

* model structure - currently model can be only build with dense layers ex. 

```
[
    {"layer_type": "dense", "units": 64, "activation": "relu"},
    {"layer_type": "dense", "units": 32, "activation": "relu"},
    {"layer_type": "dense", "units": 1}
]
```

* optimizer, loss, epochs - they have to be available in keras

* target_column - you can change columnt to target in datasets