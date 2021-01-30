import sys

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA

from utils import save_obj


def train(path_to_train_data: str, path_to_save_model: str = "./models/model.pkl"):
    df_train = pd.read_csv(path_to_train_data)
    model = ARIMA(df_train['value'], order=(1, 1, 1))
    results = model.fit(disp=False)
    save_obj(results, path_to_save_model)


if __name__ == "__main__":
    args = sys.argv
    path_to_train_data = args[1]
    train(path_to_train_data)

