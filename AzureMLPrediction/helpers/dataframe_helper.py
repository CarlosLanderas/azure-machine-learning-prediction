import json

class DataFrameHelper(object):
    """description of class"""
    @staticmethod
    def get_frame_random_sample(dataframe, number):
        return dataframe.sample(n=number)
    @staticmethod
    def frame_json(dataframe):
        return  json.loads(dataframe.to_json(orient='records'))
