"""
This exercise is about writing a unit test using py test
"""

from src.transformers import CategoriesExtractor

def test_extract_categories():
    """
    Write a unit test for CategoriesExtractor.extract_categories(json_string, False)
    :return:
    """
    json_string = '{"urls":{"web":{"discover":"http://www.kickstarter.com/discover/categories/music/pop"}},"color":10878931,"parent_id":14,"name":"Pop","id":42,"position":14,"slug":"music/pop"}'
    result = CategoriesExtractor.extract_categories(json_string, False)
    assert result == ['music', 'pop']