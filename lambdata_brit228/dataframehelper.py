import pandas as pd
import scipy.stats as scs

def checkData(df):
    """Prints NaN values for a Pandas DataFrame.

    Args:
        df: pandas dataframe

    Returns:
        None
    """
    print("NaN Values")
    for c in df:
        print("{:40s}: {: 10d} / {: 10d}".format(c, df[c].isna().sum(), df[c].count()))

def confusionMatrix(pred, actual, outputs=[0,1]):
    """Prints confusion matrix for predicted vs actual series.

    Args:
        pred: predicted values [pandas series]
        actual: actual values [pandas series]
        outputs: unique categories/values of pred and actual (default [0, 1])

    Returns:
        None
    """
    print("{:20s} || Actual".format(""))
    s = "{:20s} || ".format("Predicted")
    for c in outputs:
        C = str(c)
        if len(C) > 10:
            C = C[:7] + "..."
        s += "{:>10s}".format(C)
    print(s)
    for c in outputs:
        C = str(c)
        if len(C) > 20:
            C = C[:17] + "..."
        s = "{:20s} || ".format(C)
        for d in outputs:
            s += "{: 10d}".format(pred[(pred == c) & (actual == d)].count())
        print(s)

def dataSplit(df, ycols, train_ratio=0.5, val_ratio=0.25):
    """Splits data into depednent and independent training, validation, and testing datasets.

    Args:
        df: pandas dataframe
        ycols: list of column values or column value for df which represent the depedent data
        train_ratio: fraction of df for training (default 0.5)
        val_ratio: fraction of df for validation (default 0.25)

    Returns:
        (X[training], X[validation], X[testing], y[training], y[validation], y[testing])
            *** pandas dataframes/series
    """
    df_train = df.sample(frac=train_ratio)
    df = df.drop(df_train.index)
    df_val = df.sample(frac=val_ratio)
    df_test = df.drop(df_val.index)

    return (df_train[[c for c in df if c not in ycols]],
            df_val[[c for c in df if c not in ycols]],
            df_test[[c for c in df if c not in ycols]],
            df_train[ycols],
            df_val[ycols],
            df_test[ycols])

def generateData(df, nrows, nsamples=1):
    """Returns a dataframe with randomly copied rows copied a number of times.

    Args:
        df: pandas dataframe
        nrows: number of rows to sample
        nsamples: number of times to sample dataframe (default 1)

    Returns:
        pandas dataframe
    """
    for i in range(nsamples):
        dfn = pd.concat([df, df.sample(n=nrows)], axis=0)
    return dfn

def chiViz(df, col1, col2):
    """Prints contingency table and chi-squared statistics for it.

    Args:
        df: pandas dataframe
        col1: column name in dataframe
        col2: column name in dataframe

    Returns:
        None
    """
    cross = pd.crosstab(df[col1], df[col2])
    print(cross)
    print()
    c, p, dof, expected = scs.chi2_contingency(cross)
    print("chi2 statistic:", c)
    print("p-value statistic:", p)
    print("degrees of freedom:", dof)
    print("expected frequencies", expected)
