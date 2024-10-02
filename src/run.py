from dataCollector.data_collector import DataCollector
from datasetBuilder.dataset_builder import DatasetBuilder
from modelProcessor.sequentail_processor import SequentialProcessor

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT"]
    data_collector = DataCollector(tickers)
    data = data_collector.collect_data()

    dataset_builder = DatasetBuilder(data)
    dataset = dataset_builder.build_tickers_datsets()
    #print(dataset)

    sequential_processor = SequentialProcessor(dataset).process_tickers()
    output_predictions = SequentialProcessor(dataset).process_tickers