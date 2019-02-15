"""Test classes and functions for dataframehelper.py."""

import pandas as pd
import unittest
from . import dataframehelper

df = pd.read_csv("test_data/ecoli.csv")

class TestDFHelper(unittest.TestCase):

    def test_invalid_data_values(self):
        helper = dataframehelper.DataFrameObj(df)
        helper.invalid_data_values({8: ["cp"]})
        self.assertEqual(helper.data_frame[8].isna().sum(), 143)

    def test_data_split(self):
        helper = dataframehelper.DataFrameObj(df)
        res = helper.data_split([8], 0.33, 0.33, shuffle=False)
        X_train, X_val, X_test, y_train, y_val, y_test = res
        self.assertEqual(X_train.shape, (100, 8))
        self.assertEqual(X_val.shape, (100, 8))
        self.assertEqual(X_test.shape, (136, 8))
        self.assertEqual(y_train.shape, (100, 1))
        self.assertEqual(y_val.shape, (100, 1))
        self.assertEqual(y_test.shape, (136, 1))

    def test_generate_data(self):
        helper = dataframehelper.DataFrameObj(df)
        helper.generate_data(100, n_samples=10)
        self.assertEqual(helper.data_frame.shape, (1336, 9))
        self.assertEqual(helper.data_frame.isna().sum().sum(), 0)

if __name__ == '__main__':
    unittest.main()