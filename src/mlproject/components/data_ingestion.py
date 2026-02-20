import pandas as pd 
import numpy as np 
import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from src.mlproject.utils import fetch_kaggle_datasets
from sklearn.model_selection import train_test_split


from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join("artifact" , "train.csv")
    test_data_path : str = os.path.join("artifact" , "test.csv")
    raw_data_path : str = os.path.join("artifact" , "raw.csv")

class DataIngestion:
    def __init__(self ):
        self.ingestion_config = DataIngestionConfig()

    def intiate_data_ingestion(self):
        try:
            # reading code 
            df = fetch_kaggle_datasets()
            logging.info("Reading completed from kaggle database")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) , exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path , index = False , header=True)

            train_set , test_set = train_test_split(df , test_size=0.2 , random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path , index = False , header=True)
            test_set.to_csv(self.ingestion_config.test_data_path , index = False , header=True)

            logging.info("Data Ingestion is Completed")

            return(
                self.ingestion_config.test_data_path,
                self.ingestion_config.train_data_path
            )
        except Exception as e:
            raise CustomException(e , sys)
        

    

        
