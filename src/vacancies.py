


class Vacancy:
    def __init__(self, hh_vacancies):
        self.name = hh_vacancies['name']    #название вакансии
        self.url = hh_vacancies['apply_alternate_url']    #ссылка на вакансию

        self.salary = self.get_product_price(hh_vacancies)
        self.currency = hh_vacancies.get('salary').get('currency', 'валюта не указана')  # валюта

        self.requirement = self.check_source_info(hh_vacancies['snippet']['requirement'])    #краткое описани
        self.responsibility = self.check_source_info(hh_vacancies['snippet']['responsibility'])    #краткое описани


    @staticmethod
    def check_source_info(value):
        if value:
            return value
        return 'информация не была найдена'

    @staticmethod
    def get_product_price(hh_vacancies):
        if 'salary' in hh_vacancies:
            salary_from = hh_vacancies.get('salary').get('from', None)
            salary_to = hh_vacancies.get('salary').get('to', None)
            if salary_to is None and salary_from is None:
                return 'не указана'
            elif salary_to is None:
                return salary_from
            elif salary_from is None:
                return salary_to
            else:
                return [salary_from, salary_to]
        return 'не указана'




a = {'name': 'яндекс', 'apply_alternate_url': 'ссылка', "salary": {}, "snippet": {
        "requirement": "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
        "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. Совершать звонки по их обращениям и давать письменные ответы. "
      }}
s = Vacancy(a)
print(s.salary)
print(s.currency)
