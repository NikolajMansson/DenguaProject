
# coding: utf-8

# Getting the features for the training dataset


import pandas as pd

DENGUA_PATH = "https://s3.amazonaws.com/drivendata/data/44/public/dengue_features_train.csv"
def load_dengua_data(dengua_path=DENGUA_PATH):
    return pd.read_csv(dengua_path)

dengua = load_dengua_data()

dengua.head()

# Getting the features for the testing dataset

import pandas as pd

DENGUA_FEATURES_PATH = "https://s3.amazonaws.com/drivendata/data/44/public/dengue_features_test.csv"
def load_dengua_features_data(dengua_features_path=DENGUA_FEATURES_PATH):
    return pd.read_csv(dengua_features_path)

dengua_features = load_dengua_features_data()

dengua_features.head()

# Getting the number of dengue cases for each row in the training dataset.
import pandas as pd

DENGUA_TRAINING_PATH = "https://s3.amazonaws.com/drivendata/data/44/public/dengue_labels_train.csv"
def load_dengua_training_data(dengua_training_path=DENGUA_TRAINING_PATH):
    return pd.read_csv(dengua_training_path)

dengua_training = load_dengua_training_data()

dengua_training.head()

dengua_training.info()

dengua_training["city"].value_counts()

dengua_training.describe()

# Splitting result of dengue cases into two cities; "sj" and "iq"


dengua_training_sj = dengua_training[(dengua_training['city'] == 'sj')]


dengua_training_sj.head()


dengua_training_sj.describe()

dengua_training_iq = dengua_training[(dengua_training['city'] == 'iq')]

dengua_training_iq.head()

dengua_training_iq.describe()

total_count = 936+520

print(total_count)

