import pytest
from src.utils import sort_by_salary


@pytest.fixture()
def test_list_salary():
    return [{'salary': 90}, {'salary': 100000}, {'salary': 120000}, {'salary': [90000, 120000]}, {'salary': [90000, 99000]}, {'salary': [90000, 160000]}]

def test_sort_by_salary(test_list_salary):
    assert sort_by_salary(test_list_salary, '100000 - 150000') == [{'salary': 100000}, {'salary': 120000}, {'salary': [90000, 120000]}, {'salary': [90000, 160000]}]