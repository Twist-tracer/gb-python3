# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
from functools import reduce

companies = []
Company = namedtuple('Company', 'name, income, total_income')
for ci in range(int(input('Введите кол-во предприятий: '))):
    name = input(f'Введите название {ci + 1} компании: ')
    income = tuple(int(input(f'Введите прибыль за {qi + 1} квартал: ')) for qi in range(4))

    company = Company(
        name,
        income,
        reduce(lambda carry, item: carry + item, income)
    )

    companies.append(company)

avg_income = reduce(lambda carry, item: carry + item, [company.total_income for company in companies]) / len(companies)

print(f'Средняя прибыль компаний: {avg_income}')

companies_upper_avg, companies_lower_avg = [],[]
for company in companies:
    if company.total_income > avg_income:
        companies_upper_avg.append(company.name)
    elif company.total_income < avg_income:
        companies_lower_avg.append(company.name)

print(f'Компании у которых прибыль выше средней: {companies_upper_avg}')
print(f'Компании у которых прибыль ниже средней: {companies_lower_avg}')
