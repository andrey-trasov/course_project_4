from src.head_hunter_api import HeadHunterAPI
from src.vacancies import Vacancy
from src.utils import filter_by_salary, sorted_by_salary
import os
from config import ROOT_DIR
from src.json_file import JSONWorker
from src.functions import Functions



def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies(Functions.request())

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    while True:
        print('Кнопки управления:\n'
              '1 - вывести вакансии в терминал\n'
              '2 - отфильтровать вакансии по ключевым словам\n'
              '3 - отфильтровать вакансии по З/П\n'
              '4 - сортировать вакансии по убыванию З/П\n'
              '5 - отсортировать топ N вакансий\n'
              '6 - сохранить информацию о вакансиях в файл\n'
              '7 - считатать данные из файла\n'
              '8 - удалить аданные в файле\n'
              '"stop" или "стоп" закончить работу\n')
        answer = input()
        if answer == "стоп" or answer == "stop":
            break
        try:
            answer = int(answer)
            if 1 <= answer <= 8:    #печатает вакансии в терминал
                if answer == 1:
                    for i in vacancies_list:
                        print(i)

                elif answer == 2:    #фильтрует вакансии по ключевым словам
                     vacancies_list = Functions.similar_vacancies(vacancies_list)

                elif answer == 3:  # фильтрует вакансии по з/п
                    vacancies_list = filter_by_salary(vacancies_list)

                elif answer == 4:  # сортирует вакансии по убыванию З/П
                    vacancies_list = sorted_by_salary(vacancies_list)
                    print('\nВакансии отсортированы\n')

                elif answer == 5:  # отсортирует топ N вакансий
                    Functions.top_vacancies(vacancies_list)

                elif answer == 6:  # сохраняет информацию о вакансиях в файл
                    file_name = input('Введите название файла для сохранения данных: (Пример: file )')
                    file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                    json_saver = JSONWorker(file_path)
                    json_saver.write_vacancies(vacancies_list)

                elif answer == 7:  # считатываает данные из файла
                    file_name = input('Введите название файла для считывания данные из файла: (Пример: file )')
                    file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                    json_saver = JSONWorker(file_path)
                    vacancies_list = json_saver.read_vacancies()

                elif answer == 8:  # удаляет информацию о вакансиях из файла
                    file_name = input('Введите название файла для удаления данных: (Пример: file )')
                    file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                    json_saver = JSONWorker(file_path)
                    json_saver.delete_vacancies()




            else:
                print(f"Введите цифру от 1 до 8\n")





        except ValueError:
            print(f"Введите цифру от 1 до 8\n")



    # file_name = input('Введите название файла для сохранения данных: ')
    # file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
    # jsonsaver = JSONWorker(file_path)

    # # записать данные в файл
    # jsonsaver.write_vacancies(vacancies_list)

    # # #считать данные из файла
    # vacancies_list = jsonsaver.read_vacancies()

    # #удаляем информацию о вакансиях из файла
    # jsonsaver.delete_vacancies()






















        # break















if __name__ == "__main__":
    main()





    #вывести вакансии по ключевым словам
    # vacancies_list = Functions.similar_vacancies(vacancies_list)
