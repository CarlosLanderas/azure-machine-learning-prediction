from __future__ import print_function
from helpers.azure_helper import AzureHelper
from helpers.dataframe_helper import DataFrameHelper
from classes.azure_rest_client_factory import AzureRestClientFactory
from enums.client_type import ClientType
from settings import AZURE_TRAINING_SETS

def main():

    azurehelper = AzureHelper()

    iris_dataframe = azurehelper.read_dataset(AZURE_TRAINING_SETS['IRIS'])
    iris_random_rows = DataFrameHelper.get_frame_random_sample(iris_dataframe, 10)

    auto_dataframe = azurehelper.read_dataset(AZURE_TRAINING_SETS['AUTO'])
    auto_random_rows = DataFrameHelper.get_frame_random_sample(auto_dataframe, 10)

    for i, (iris_row, auto_row) in enumerate(
            zip(
                DataFrameHelper.frame_json(iris_random_rows),
                DataFrameHelper.frame_json(auto_random_rows)
            )):

        raw_input("Press a key to send request number {0}\n".format(str(i+1)))
        print("Sending requests to api...\n")
        post_iris_prediction(iris_row)
        post_auto_prediction(auto_row)

    print("Finished!")

def post_iris_prediction(data):
    iris_rest_client = AzureRestClientFactory.get(ClientType.iris)
    iris_rest_client.post(data)

def post_auto_prediction(data):
    auto_rest_client = AzureRestClientFactory.get(ClientType.auto)
    auto_rest_client.post(data)

if __name__ == "__main__":
    main()