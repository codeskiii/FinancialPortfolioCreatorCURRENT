from dataCollector.data_collector import DataCollector
from datasetBuilder.dataset_builder import DatasetBuilder
from modelProcessor.sequentail_processor import SequentialProcessor
from tickerSelector.ticker_selector import TickerSelector
import json

if __name__ == "__main__":
    file = open("config.json", "r")
    settings = json.load(file)

    tickers = settings["tickers"]
    data_collector = DataCollector(tickers)
    data = data_collector.collect_data()

    dataset_builder = DatasetBuilder(data)
    datasets = dataset_builder.build_tickers_datsets()
    #print(dataset)

    sequential_processor = SequentialProcessor(datasets)
    sequential_processor.process_tickers()
    output_predictions = sequential_processor.output_datasets
    #print(output_predictions[0][1])

    tk = TickerSelector(output_predictions)
    selected_tickers = tk.pick_one()

