"""Helper utility functions for Pandas DataFrames."""

import pandas as pd
import scipy.stats as scs
import numpy as np


def invalid_data_values(data_frame, invalid_dict):
    """Replaces invalid values in a dictionary from a user-defined
    dictionary of column names corresponding to a list of invalid values.

    Args:
        data_frame: pandas dataframe
        invalid_dict: dictionary of column names to list of invalid values
    Returns:
        pandas dataframe
    """
    for key in invalid_dict:
        for val in invalid_dict[key]:
            data_frame[data_frame[key] == val][key] = np.nan
    return data_frame


def check_data(data_frame):
    """Prints NaN values for a Pandas DataFrame.

    Args:
        data_frame: pandas dataframe
    Returns:
        None
    """
    print("NaN Values")
    format_string = "{:40s}: {: 10d} / {: 10d}"
    for col_name in data_frame:
        print(format_string.format(col_name,
                                   data_frame[col_name].isna().sum(),
                                   data_frame[col_name].count()))


def confusion_matrix(pred, actual, outputs):
    """Prints confusion matrix for predicted vs actual series.

    Args:
        pred: predicted values [pandas series]
        actual: actual values [pandas series]
        outputs: unique categories/values of pred and actual
    Returns:
        None
    """
    print("{:20s} || Actual".format(""))
    temp_string = "{:20s} || ".format("Predicted")
    for out in outputs:
        out_string = str(out)
        if len(out_string) > 10:
            out_string = out_string[:7] + "..."
        temp_string += "{:>10s}".format(out_string)
    print(temp_string)
    for out1 in outputs:
        out_string = str(out1)
        if len(out_string) > 20:
            out_string = out_string[:17] + "..."
        temp_string = "{:20s} || ".format(out_string)
        for out2 in outputs:
            count = pred[(pred == out1) & (actual == out2)].count()
            temp_string += "{: 10d}".format(count)
        print(temp_string)


def data_split(data_frame, ycols, train_ratio=0.5, val_ratio=0.25):
    """Splits data into depednent and independent training, validation, and
    testing datasets.

    Args:
        data_frame: pandas dataframe
        ycols: list of column values or column value for df which represent
            the depedent data
        train_ratio: fraction of df for training (default 0.5)
        val_ratio: fraction of df for validation (default 0.25)
    Returns:
        (X[training], X[validation], X[testing],
            y[training], y[validation], y[testing])
            *** pandas dataframes/series
    """
    df_train = data_frame.sample(frac=train_ratio)
    data_frame = data_frame.drop(df_train.index)
    df_val = data_frame.sample(frac=val_ratio)
    df_test = data_frame.drop(df_val.index)

    return (df_train[[c for c in data_frame if c not in ycols]],
            df_val[[c for c in data_frame if c not in ycols]],
            df_test[[c for c in data_frame if c not in ycols]],
            df_train[ycols],
            df_val[ycols],
            df_test[ycols])


def generate_data(data_frame, nrows, nsamples=1):
    """Returns a dataframe with randomly copied rows copied a number of times.

    Args:
        data_frame: pandas dataframe
        nrows: number of rows to sample
        nsamples: number of times to sample dataframe (default 1)
    Returns:
        pandas dataframe
    """
    for _ in range(nsamples):
        dfn = pd.concat([data_frame, data_frame.sample(n=nrows)], axis=0)
    return dfn


def chi_viz(data_frame, col1, col2):
    """Prints contingency table and chi-squared statistics for it.

    Args:
        data_frame: pandas dataframe
        col1: column name in dataframe
        col2: column name in dataframe
    Returns:
        None
    """
    cross = pd.crosstab(data_frame[col1], data_frame[col2])
    print(cross)
    print()
    chi_val, p_val, dof, expected = scs.chi2_contingency(cross)
    print("chi2 statistic:", chi_val)
    print("p-value statistic:", p_val)
    print("degrees of freedom:", dof)
    print("expected frequencies", expected)
