# employees = {
#     "emp1": {"name": "Priya", "salary": 30000},
#     "emp2": {"name": "Arun", "salary": 45000},
#     "emp3": {"name": "Kumar", "salary": 25000},
#     "emp4": {"name": "Divya", "salary": 50000}
# }
# result={emp_id:details for emp_id , details in employees.items() if details["salary"]>30000}
# print(result)
# numbers = [10, 15, 20, 25, 30, 35, 40]
# result={num :num //10 for num in numbers if num % 10 ==0}
# print(result)
# numbers = [1, 2, 3, 4, 5]
# result={num:num**2  for num in numbers}
# print(result)
# employees = [
#     {"name": "Priya", "salary": 30000},
#     {"name": "Arun", "salary": 45000},
#     {"name": "Kumar", "salary": 25000},
#     {"name": "Divya", "salary": 50000},
#     {"name": "Ravi", "salary": 35000}
# ]

# # Create a dictionary directly using key: value syntax
# result = {details['name']: round(details['salary'] * 1.10, 2) for details in employees if details["salary"] >= 35000}

# print(result)

# employees = [
#     {"name": "Priya", "salary": 30000},
#     {"name": "Arun", "salary": 45000},
#     {"name": "Kumar", "salary": 25000},
#     {"name": "Divya", "salary": 50000},
#     {"name": "Ravi", "salary": 35000}
# ]

# result=[details["name"] for details in employees if details["salary"]>30000]
# print(result)
# names = ["priya", "arun", "kumar", "divya", "ravi"]
# result=[char.upper() for char in names if len(char) > 4]
# print(result)

# numbers = [10, 15, 20, 25, 30, 35, 40]
# result=[num //10 for num in numbers if num % 10 ==0]
# print(result)

# numbers = [1, 2, 3, 4, 5, 6]
# squares=[num ** 2 for num in numbers if num > 3 ]
# print(squares)