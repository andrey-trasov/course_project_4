import pytest
from src.vacancies import Vacancy

data = {'name': 'яндекс',
        'apply_alternate_url': 'ссылка',
        "salary": {"from": 30000,"to": 44000,"currency": "RUR"},
        "snippet": {"requirement": "Способен работать в команде.","responsibility": "Работать с клиентами или партнерами."}
        }

@pytest.fixture()
def vacancy():
    return Vacancy(data)

def test_init_vacancy(vacancy):
    assert vacancy.name == 'яндекс'
    assert vacancy.url == 'ссылка'
    assert vacancy.salary == [30000, 44000]
    assert vacancy.currency == 'RUR'
    assert vacancy.requirement == 'Способен работать в команде.'
    assert vacancy.responsibility == 'Работать с клиентами или партнерами.'
    vacancy.salary = {}
    assert vacancy.salary == 'не указана'
#  assert vacancy.currency == 'валюта не указана'

