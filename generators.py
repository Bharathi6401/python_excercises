employees = [
    {"name": "Priya", "salary": 30000},
    {"name": "Arun", "salary": 45000},
    {"name": "Kumar", "salary": 25000},
    {"name": "Divya", "salary": 50000}
]
def high_salary_employees(employee_list):
    for employee in employee_list:
        if employee["salary"] > 30000:
            yield employee["name"]

   

for name in high_salary_employees(employees):
    print(name)

# def high_salary_employees(salaries):
#     for s in salaries:
#         if s > 30000:
#             yield s


# for salary in high_salary_employees(salaries = [20000, 35000, 25000, 50000, 40000]):
#         print(salary)


# def even_numbers(n):
#     yield from range(2,n+1,2)

 
# for num in even_numbers(10):
#     print(num)

# def get_numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# result = get_numbers()

# print(next(result))
# print(next(result))
# print(next(result))