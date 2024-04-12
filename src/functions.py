from src.utils import sorted_by_salary


class Functions:

    @staticmethod

    def request():
        """
        выводит поисковый запрос для запроса вакансий из hh.ru
        """
        return input('Введите поисковый запрос для поска вакансий: ')

    @staticmethod
    def top_vacancies(vacancies):
        """
        выдает топ N вакансий по зарплате
        """
        num = int(input('Какое количчество вакансий вам выдать? '))
        sorted_vacancies = sorted_by_salary(vacancies)
        for i in sorted_vacancies[0: num]:
            print(i)

    @staticmethod
    def similar_vacancies(vacancies):
        """
        получить вакансии с ключевым словом в описании
        """
        words = input("введите ключевые слова через пробел: ").split()
        reserve_list_vacancies = vacancies
        for word in words:
            list_vacancies = []
            for v in vacancies:
                if word.lower() in v.requirement.lower() or word.lower() in v.responsibility.lower():
                    list_vacancies.append(v)
            if len(list_vacancies) == 0:
                print("Вакансии с такими ключевыми словами не найдены")
                return reserve_list_vacancies
            else:
                vacancies = list_vacancies
        return vacancies





