import pandas as pd
from os import path
from pathlib import Path

current_path = dir_path = path.dirname(path.realpath(__file__))
data_file = Path(current_path) / 'data.csv'

dtf = pd.read_csv(data_file, encoding='UTF-8', delimiter=',')
df = dtf.copy(deep=True)

