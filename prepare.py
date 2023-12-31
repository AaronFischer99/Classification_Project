import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

from acquire import get_telco_data

"""Function will extract 'total_charges' from the 
telco data and strip teh whitespace from teh object type
to make it easier to transfomr into float or int type.
Also will replace 'churn' yes value with 1, and no value with a 0
"""   
#Function for data prep
def telco_data_prep():
    df = get_telco_data()
    df.total_charges = df.total_charges.str.strip()
    df.total_charges = df.total_charges.replace('', 0) 
    df.churn.replace(['Yes', 'No'], [1,0], inplace = True)
    return df


#Functions for spliting data (train, test, validate)
def train_test_validate():

    train, test = train_test_split(df, test_size = .2, random_state = 123)
    train_validate, test_validate = train_test_split(train_validate, test_size = .3, random_state = 123)

    return train, validate, test


#Splitting with a 20% test data ratio for test purposes to a 33% test data ratio for model validation purposes
def train_test_validate2(df, test_size=(0.2, 0.33), random_state=123):
    train, test = train_test_split(df, test_size=test_size[0], random_state=random_state)
    train_validate, test_validate = train_test_split(train, test_size=test_size[1], random_state=random_state)
    
    return train, test, train_validate, test_validate

#Splitting with a 20% test data ratio for test purposes to a 50% test data ratio for model validation purposes
def train_test_validate2(df, test_size=(0.2, 0.5), random_state=123):
    train, test = train_test_split(df, test_size=test_size[0], random_state=random_state)
    train_validate, test_validate = train_test_split(train, test_size=test_size[1], random_state=random_state)
    
    return train, test, train_validate, test_validate




def train_test_validate3(df, target_col, test_size=(0.2, 0.3), random_state=123):
    # Splitting into train and test while stratifying on the target variable
    train, test = train_test_split(df, test_size=test_size[0], stratify=df[target_col], random_state=random_state)
    
    # Splitting train further into train and validate with stratification
    train_val, test_validate = train_test_split(train, test_size=test_size[1], stratify=train[target_col], random_state=random_state)
    
    return train, validate, test
