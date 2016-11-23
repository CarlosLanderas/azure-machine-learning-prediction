from classes.azure_api_client import AzureApiClient
from settings import AZUREML_API
from enums.client_type import ClientType
class AzureRestClientFactory(object):
    @staticmethod
    def get(clienttype):
        if clienttype is ClientType.iris:
            return AzureApiClient(AZUREML_API['PREDICT_IRIS'])
        elif clienttype is ClientType.auto:
            return AzureApiClient(AZUREML_API['PREDICT_AUTO'])