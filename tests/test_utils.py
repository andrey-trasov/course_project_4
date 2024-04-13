import pytest
from src.utils import filter_by_salary, sorted_by_salary
from src.vacancies import Vacancy
from src.functions import Functions

# data = [{'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 90000, "to": 160000, "currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.", "responsibility": "Работать с клиентами или партнерами."}
#         },
#         {'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 100000, "currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
#         },
#         {'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 90000,"to": 120000,"currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
#         },
#         {'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 90000,"to": 99000,"currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
#         },
#         {'name': 'яндекс',
#          'apply_alternate_url': 'ссылка',
#          "salary": {"from": 90, "currency": "RUR"},
#          "snippet": {"requirement": "Способен работать в команде.",
#          "responsibility": "Работать с клиентами или партнерами."}
#          }]
#
#
#
#
#
#
# @pytest.fixture()
# def test_list_salary_filter():
#     return Vacancy.cast_to_object_list(data)
#
# @pytest.fixture()
# def test_list_salary_filters():
#     return [Vacancy(data[0]), Vacancy(data[1]), Vacancy(data[2])]
# def test_filter_by_salary(test_list_salary_filter):
#     instance_sorted_class = Functions.similar_vacancies(test_list_salary_filter)
#     assert instance_sorted_class[0].salary == [90000, 160000]
#     assert instance_sorted_class[1].salary == 100000
#     assert instance_sorted_class[2].salary == [90000, 120000]
#
#
#
# def test_sorted_by_salary(test_list_salary_filters):
#     instance_filter_class = sorted_by_salary(test_list_salary_filters)
#     assert instance_filter_class[0].salary == test_list_salary_filters[0].salary
#     assert instance_filter_class[1].salary == test_list_salary_filters[2].salary
#     assert instance_filter_class[2].salary == test_list_salary_filters[1].salary

#--------------------------------------

# data = [{'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 900000,"to": 160000,"currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
#         },
#         {'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 100000,"currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
#         },
#         {'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 90000,"to": 120000,"currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
#         },
#         {'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 90000,"to": 99000,"currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
#         },
#         {'name': 'яндекс',
#         'apply_alternate_url': 'ссылка',
#         "salary": {"from": 90,"currency": "RUR"},
#         "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
#         }]
#
# @pytest.fixture()
# def vacancy():
#     return Vacancy.cast_to_object_list(data)
#
# def test_filter_by_salary(vacancy):
#     instance_sorted_class = Functions.similar_vacancies(vacancy)
#     assert instance_sorted_class[0].salary == [90000, 160000]
#     assert instance_sorted_class[1].salary == 100000
#     assert instance_sorted_class[2].salary == [90000, 120000]
