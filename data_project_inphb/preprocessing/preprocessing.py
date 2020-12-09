import pandas as pd
import numpy as np


def convert_cast(df, categorical_cols):
    """cast categorical column values into string(object)

        input :
            df (object): a pandas dataframe : 
            categorica_cals (list): list of categorical columns in df
        output:
            return the same data frame with casted columns
    """
    for col_name in categorical_cols:
        df[col_name] = df[col_name].astype("object")
    return df

def convert_cast(mapper_config=None, dataframe=None):
    """
    Convert and cast DataFrame field types.

    This function achieves the same purpose as pd.read_csv, but it is used on
    actual DataFrame obtained from SQL.
    """
    # field conversion
    for var_name, lambda_string in mapper_config['converters'].items():
        if var_name in dataframe.columns:
            func = eval(lambda_string)
            dataframe[var_name] = dataframe[var_name].apply(func)

    # field type conversion/compression
    dty = dict(dataframe.dtypes)
    for col_name, actual_type in dty.items():
        expected_type = mapper_config['columns'][col_name]['dtype']
        if actual_type != expected_type:
            dataframe[col_name] = dataframe[col_name].astype(expected_type)

    return dataframe

def input_missing_values(df):
    """remove missing values in dataframe
        
        input (object): pandas dataframe containing missing values
        
        output: return the dataframe without missing values    
    """
    for col in df.columns:
        if (df[col].dtype is float) or (df[col].dtype is int):
            df[col] = df[col].fillna(df[col].median())
        if (df[col].dtype == object):
            df[col] = df[col].fillna(df[col].mode()[0])

    return df