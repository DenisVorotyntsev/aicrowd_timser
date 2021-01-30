from typing import List
import time
import pickle

import pandas as pd


def save_obj(obj, path: str):
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_obj(path: str):
    with open(path, "rb") as f:
        obj = pickle.load(f)
    return obj
