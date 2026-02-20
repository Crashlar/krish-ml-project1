import shutil
import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from dotenv import load_dotenv
import pickle
import pandas as pd 
import kagglehub


import numpy as np

# Load environment variables
load_dotenv()



def fetch_kaggle_datasets():
    try:
        path = kagglehub.dataset_download("bhavikjikadara/student-study-performance")
        print("Path to dataset files:", path)

        # Find the first CSV file in the downloaded folder
        csv_file = None
        for file in os.listdir(path):
            if file.endswith(".csv"):
                csv_file = os.path.join(path, file)
                break

        if not csv_file:
            raise FileNotFoundError("No CSV file found in downloaded dataset")

        # Load into DataFrame
        df = pd.read_csv(csv_file)
        return df

    except Exception as ex:
        raise CustomException(ex, sys)



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

