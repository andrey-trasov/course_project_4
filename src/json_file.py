import json
from abc import ABC, abstractmethod
from src.vacancies import Vacancy

class FileWorker(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def write_vacancies(self, vacancies):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONWorker(FileWorker):
    """
    добавления вакансий в файл
    получения данных из файла по указанным критериям
    удаления информации о вакансиях
    """
    def __init__(self, path):
        self.path = path

    def write_vacancies(self, vacancies):
        """
        записывает вакансии в файл
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            for_add = []
            for vacancy in vacancies:
                for_add.append(vacancy.__dict__)
            json.dump(for_add, file, ensure_ascii=False, indent=4)

    def read_vacancies(self):
        """
        считывает вакансии из файла и преобразует их в список объектов
        """
        with open(self.path, "r", encoding='utf-8') as file:
            new_list = json.load(file)
            vacancies = Vacancy.vacancies_from_file(new_list)
            return vacancies

    def delete_vacancies(self):
        """
        удаляет ваканси из файла
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            # json.dump('', file, ensure_ascii=False, indent=4)
            file.truncate(0)








