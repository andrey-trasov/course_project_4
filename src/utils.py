




def sort_by_salary(vacancies_list, salary_range):
    """
    Фильтруем зарплаты по диапазону
    :param vacancies_list: список вакансий
    :param salary_range: диапазон зарплат
    """
    sorted_list = []
    list_salary_range= salary_range.split(' ')
    min_salary, max_salary = int(list_salary_range[0]), int(list_salary_range[-1])
    for i in vacancies_list:
        if isinstance(i['salary'], int):
            if min_salary <= i['salary'] <= max_salary:
                sorted_list.append(i)
        elif isinstance(i['salary'], list):
            min_i, max_i = i['salary']
            if min_salary <= min_i <= max_salary or min_salary <= max_i <= max_salary:
                 sorted_list.append(i)
            elif min_i <= max_salary and min_salary <= max_i:
                 sorted_list.append(i)
    return sorted_list

