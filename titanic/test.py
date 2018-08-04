import pandas as pd
import numpy as np
from pandas import Series, DataFrame


train_df = pd.read_csv("train.csv")
# print(data_train.info())
print(train_df[['SibSp', 'Survived']].groupby(['SibSp'], as_index=False).mean())
