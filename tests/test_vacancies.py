import pytest
from src.vacancies import Vacancy

data = [{'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 30000,"to": 44000,"currency": "RUR"},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        },
        {'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 30000, "currency": "RUR"},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        },
        {'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        }]

@pytest.fixture()
def vacancy():
    return Vacancy(data[0])

@pytest.fixture()
def vacancy_2():
    return Vacancy(data[1])

@pytest.fixture()
def vacancy_3():
    return Vacancy(data[2])

def test_init_vacancy(vacancy, vacancy_2, vacancy_3):
    assert vacancy.name == 'яндекс'
    assert vacancy.url == 'ссылка'
    assert vacancy.salary == [30000, 44000]
    assert vacancy.currency == 'RUR'
    assert vacancy.requirement == 'Способен работать в команде.'
    assert vacancy.responsibility == 'Работать с клиентами или партнерами.'
    assert vacancy_2.salary == 30000
    assert vacancy_3.salary == 0
    assert vacancy_3.currency == 'валюта не указана'


