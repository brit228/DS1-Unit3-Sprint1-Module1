import pandas as pd
import scipy.stats as scs

def checkData(df):
    """

    """
    print("NaN Values")
    for c in df:
        print("{:40s}: {: 10d} / {: 10d}".format(c, df[c].isna().sum(), df[c].count()))

def confusionMatrix(pred, actual, outputs=[0,1]):
    s = "{:20s}".format("")
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
        s = "{:20s}".format(C)
        for d in outputs:
            s += "{: 10d}".format(pred[(pred == c) & (actual == d)].count())
        print(s)

def dataSplit(df, ycols, train_ratio=0.5, val_ratio=0.25):
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
    for i in range(nsamples):
        df = pd.concat([df, df.sample(n=nrows)], axis=0)
    return df

def chiViz(df, col1, col2):
    cross = pd.crosstab(df[col1], df[col2])
    print(cross)
    c, p, dof, expected = scs.chi2_contingency(cross)
    print("chi2 statistic:", c)
    print("p-value statistic:", p)
    print("degrees of freedom:", dof)
    print("expected frequencies", expected)
