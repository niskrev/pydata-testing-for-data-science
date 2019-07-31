"""
This exercise is about refactoring a unit test to improve it's readability and maintenance
"""
import pandas as pd
from src.transformers import CountryTransformer

import pytest
def test_correct_country_returned_with_simple_df():
    """
    Refactor this unit test to apply the Given/When/Then pattern
    :return:
    """

    # Given
    df = pd.DataFrame({'country': ["CA", "GB"]})

    # When
    country_transformer = CountryTransformer()
    result_df = country_transformer.transform(df)

    # Then
    assert len(result_df.index) == 2
    assert result_df.iloc[0]['country'] == 'Canada'
    assert result_df.iloc[1]['country'] == 'UK & Ireland'