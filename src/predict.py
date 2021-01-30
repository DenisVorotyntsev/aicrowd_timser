import sys

import pandas as pd
import numpy as np

from utils import load_obj


def predict(
    path_to_sample_sub: str,
    path_to_saved_model: str = "./models/model.pkl",
    path_to_save_results: str = './output/prediction.csv'
):
    sample_sub = pd.read_csv(path_to_sample_sub)
    num_points_to_predict = sample_sub.shape[0]
    model = load_obj(path_to_saved_model)
    y_hat = model.forecast(num_points_to_predict)[0]
    y_hat = np.array(y_hat)
    sample_sub["value"] = y_hat
    sample_sub.to_csv(path_to_save_results, index=False)


if __name__ == "__main__":
    args = sys.argv
    path_to_sample_sub = args[1]
    predict(path_to_sample_sub)

