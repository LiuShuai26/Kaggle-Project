import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


data_train = pd.read_csv("train.csv")

fig = plt.figure()
fig.set(alpha=0.2)

# plt.subplot2grid((2, 3), (0, 0))
# data_train.Survived.value_counts().plot(kind='bar')
# plt.title("survived: 1")
# plt.ylabel("people")
#
# plt.subplot2grid((2, 3), (0, 1))
# data_train.Pclass.value_counts().plot(kind='bar')
# plt.ylabel("people")
# plt.title("Pclass")
#
# plt.subplot2grid((2, 3), (0, 2))
# plt.scatter(data_train.Survived, data_train.Age)
# plt.ylabel("age")
# plt.title("Survived: 1")
#
# plt.subplot2grid((2, 3), (1, 0), colspan=2)
# data_train.Age[data_train.Pclass == 1].plot(kind='kde')
# data_train.Age[data_train.Pclass == 2].plot(kind='kde')
# data_train.Age[data_train.Pclass == 3].plot(kind='kde')
# plt.xlabel("age")
# plt.ylabel("midu")
# plt.title("Pclass by age")
# plt.legend(('top class', 'mid class', 'low class'), loc='best')
#
# plt.subplot2grid((2, 3), (1, 2))
# data_train.Embarked.value_counts().plot(kind='bar')
# plt.title("Embarked")
# plt.ylabel("people")
#
# plt.show()

# Survived_0 = data_train.Pclass[data_train.Survived == 0].value_counts()
# Survived_1 = data_train.Pclass[data_train.Survived == 1].value_counts()
# df = pd.DataFrame({'survived': Survived_1, 'died': Survived_0})
# df.plot(kind='bar', stacked=True)
# plt.title("asdf")
# plt.xlabel("Pclass")
# plt.ylabel("people")
#
# plt.show()

Survived_m = data_train.Survived[data_train.Sex == 'male'].value_counts()
Survived_f = data_train.Survived[data_train.Sex == 'female'].value_counts()
df = pd.DataFrame({'male': Survived_m, 'female': Survived_f})
df.plot(kind='bar', stacked=True)
plt.show()
