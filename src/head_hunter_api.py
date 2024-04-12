from abc import ABC, abstractmethod
import requests

class Parser(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker=None):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        # super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 2: #поменять 2 на 20
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies

    # def __iter__(self):
    #     self.iter_index = len(self.vacancies)
    #
    # def __next__(self):
    #     if self.iter_index == 0:
    #         raise StopIteration
    #     self.iter_index -= 1
    #     return self.vacancies[-self.iter_index]





# a = HeadHunterAPI()
# s = a.load_vacancies('водитель')
# # with open('test.txt', 'w', encoding='utf-8') as file:
# #     print(file.write(str(s)))
#
# class Vacancy:
#     def __init__(self, vacancy_dict):
#         self.name = vacancy_dict['name']
#         self.employer = vacancy_dict['employer']['name']
#         self.experience = vacancy_dict['experience']['name']
#         self.schedule = vacancy_dict['schedule']['name']
#         self.employment = vacancy_dict['employment']['name']
#         print(self.name)
#         print(self.employer)
#         print(self.experience)
#         print(self.schedule)
#         print()
#         print()
#         print()
#         print()
#         print()
#
# w = 0
# for i in s:
#     q = Vacancy(i)
#     w += 1
#
#
#
#
#
# print('stop', w)