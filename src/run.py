from dataCollector.data_collector import DataCollector
from datasetBuilder.dataset_builder import DatasetBuilder

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT"]
    data_collector = DataCollector(tickers)
    data = data_collector.collect_data()

    dataset_builder = DatasetBuilder(data)
    dataset = dataset_builder.build_dataset()
    #print(dataset)

