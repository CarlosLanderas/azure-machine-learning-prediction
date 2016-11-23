from azureml import Workspace
from settings import AZURE_ML_SETTINGS

class AzureHelper(object):
    """Azure ML Utils Helper"""
    @classmethod
    def read_dataset(cls, datesetname):
        workspace = Workspace(workspace_id=AZURE_ML_SETTINGS['WORKSPACE_ID'],
                              authorization_token=AZURE_ML_SETTINGS['TOKEN_ID'],
                              endpoint=AZURE_ML_SETTINGS['END_POINT'])
        dataset = workspace.datasets[datesetname]
        frame = dataset.to_dataframe()
        return frame
   