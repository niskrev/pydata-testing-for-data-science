"""
This exercise is about writing a property-based unit test using hypothesis
"""
import json
from hypothesis.strategies import fixed_dictionaries, from_regex
from hypothesis import given
from src.transformers import CategoriesExtractor

import pytest

@given(fixed_dictionaries({'slug': from_regex("/")}).map(json.dumps))
def test_extract_categories(json_string):
    """
    Use hypothesis to generate test cases for CategoriesExtractor.extract_categories.
    Think about an appropriate property to test against.
    You should be able to find a bug and fix the implementation accordingly
    :param json_string:
    :return:
    """
    ce = CategoriesExtractor()

    result = ce.extract_categories(json_string, False)

    assert len(result) == 2


