"""
This exercise is about writing a parameterised unit test using pytest
"""
import pandas as pd
from pandas.testing import assert_frame_equal

import pytest
from src.transformers import TimeTransformer

test_time_transformer_testdata = [
    (pd.DataFrame({'deadline': [1459283229], 'created_at': [1455845363], 'launched_at': [1456694829]}),
    pd.DataFrame({'launched_to_deadline': [29], 'created_to_launched': [9]})),

    (pd.DataFrame({'deadline': [0], 'created_at': [0], 'launched_at': [0]}),
    pd.DataFrame({'launched_to_deadline': [0], 'created_to_launched': [0]})),
]

@pytest.mark.parametrize(('sample_df', 'expected_df'), test_time_transformer_testdata)
def test_time_transformer(sample_df, expected_df):
    """
    Write a parameterised unit test for TimeTransformer
    :param sample_df: sample df to test with three columns: deadline, created_at, launched_at
    :param expected_df: result with two columns: launched_to_deadline, created_to_launched
    :return:
    """

    result_df = TimeTransformer().transform(sample_df)
    assert_frame_equal(result_df, expected_df) 