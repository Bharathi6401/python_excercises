
def common_elements(list1,list2):
    common=[]
    list2_set=set(list2)
    seen=set()
    for item in list1:
        if item in list2_set and item not in seen:
            common.append(item)
            seen.add(item)
    return common

print(common_elements(list1 = [1, 2, 2, 3, 4, 5],list2 = [2, 2, 3, 5, 6]))

# def first_non_repeating_char(text):
#     frequency={}
#     for char in text:
#         frequency[char]=frequency.get(char,0)+1
#     for char in text:
#         if frequency[char]==1:
#             return char
#     return None

# print(first_non_repeating_char("swiss"))

# def high_earning_it_employee(employee_list):
#     unique_it_names=set()
#     for employee in employee_list:
#         if employee["department"] == 'IT' and employee["salary"] > 35000:
#             unique_it_names.add(employee["name"])
#     return list(unique_it_names)

# employees = [
#     {"name": "Priya", "department": "IT", "salary": 30000},
#     {"name": "Arun", "department": "HR", "salary": 45000},
#     {"name": "Kumar", "department": "IT", "salary": 40000},
#     {"name": "Divya", "department": "HR", "salary": 50000},
#     {"name": "Ravi", "department": "Finance", "salary": 25000},
#     {"name": "Meena", "department": "IT", "salary": 50000}
# ]
# result= high_earning_it_employee(employees)
# print(result)

# employees = [
#     {"name": "Priya", "salary": 30000},
#     {"name": "Arun", "salary": 45000},
#     {"name": "Kumar", "salary": 25000},
#     {"name": "Divya", "salary": 50000},
#     {"name": "Ravi", "salary": 40000}
# ]
# def high_salary_employees(employee_list):
#     for employee in employee_list:
#         if employee["salary"] > 35000:
#             yield employee["name"]


# for name in high_salary_employees(employees):
#     print(name)

# employees = [
#     {"name": "Priya", "department": "IT", "salary": 30000},
#     {"name": "Arun", "department": "HR", "salary": 25000},
#     {"name": "Kumar", "department": "IT", "salary": 40000},
#     {"name": "Divya", "department": "HR", "salary": 35000},
#     {"name": "Ravi", "department": "Finance", "salary": 50000}
# ]
# department_count={}
# department_salary={}
# for details in employees:
#     department=details["department"]
#     salary=details["salary"]
#     department_salary[department]=department_salary.get(department,0)+salary
#     department_count[department]=department_count.get(department,0)+1

# department_average={}
# for department, total in department_salary.items():
#     average=total / department_count[department]
#     department_average[department]=average

# print(department_average)
# def group_employees(employees):
#     department_empl = {}

#     for details in employees:
#         department = details["department"]
#         name = details["name"]

#         if department not in department_empl:
#             department_empl[department] = []

#         department_empl[department].append(name)

#     return department_empl
# employees = [
#     {"name": "Priya", "department": "IT"},
#     {"name": "Arun", "department": "HR"},
#     {"name": "Kumar", "department": "IT"},
#     {"name": "Divya", "department": "HR"},
#     {"name": "Ravi", "department": "Finance"}
# ]
# result=group_employees(employees)
# print(result)
# employees = [
#     {"name": "Priya", "department": "IT"},
#     {"name": "Arun", "department": "HR"},
#     {"name": "Kumar", "department": "IT"},
#     {"name": "Divya", "department": "HR"},
#     {"name": "Ravi", "department": "Finance"}
# ]
# department_empl={}
# for details in employees:
#     department=details["department"]
#     name=details["name"]
#     if department not in department_empl:
#         department_empl[department]=[]
#     department_empl[department].append(name)

# print(department_empl)
# def find_anagrams(str1,str2):
#     frequency={}
#     if len(str1) != len(str2):
#         return False
#     for char in str1:
#         frequency[char]=frequency.get(char,0)+1
#     for char in str2:
#         frequency[char]=frequency.get(char,0) - 1
#     return all(value==0 for value in frequency.values())

# print(find_anagrams(str1 = "listen",str2 = "silent"))
# def find_the_missing_number(numbers):
#     n = len(numbers) + 1
#     expected_total = n * (n + 1) // 2
#     missing_value=expected_total - sum(numbers)
#     return missing_value
        

# print(find_the_missing_number(numbers = [1, 2, 3, 5, 6]))
# def move_zero_to_end(numbers):
#     write_index=0
#     for num in numbers:
#         if num !=0:
#             numbers[write_index]=num
#             write_index+=1

#     while write_index < len(numbers):
#         numbers[write_index]=0
#         write_index+=1
#     return numbers

# print(move_zero_to_end(numbers = [0, 1, 0, 3, 12, 0, 5]))


# def find_second_largest(numbers):
#     largest=float('-inf')
#     second_largest=float('-inf')
#     if len(set(numbers)) < 2:
#         return None
#     for num in numbers:
#         if num > largest:
#             second_largest=largest
#             largest=num
#         elif num > second_largest and num != largest:
#             second_largest=num
#     return second_largest


# print(find_second_largest(numbers = [-10, -5, -20, -2, -5]))
# print(find_second_largest(numbers = [5, 5, 5]))


# def find_common_elements(list1,list2):
#     common=[]
#     list2_set=set(list2)
#     seen=set()

#     for item in list1:
#         if item in list2_set and item not in seen:
#             common.append(item)
#             seen.add(item)
#     return common


# print(find_common_elements(list1 = [1, 2, 3, 4, 5, 2],list2 = [2, 4, 6, 7, 4]))

# def find_first_repeated_char(text):
#     seen=set()
#     for char in text:
#         if char  in seen:
#             return char
#         seen.add(char)
#     return None

# print(find_first_repeated_char(text="programming"))

