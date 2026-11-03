employee = {
    "emp1": {"name": "Priya", "age": 24, "salary": 30000, "department": "IT"},
    "emp2": {"name": "Arun", "age": 25, "salary": 35000, "department": "HR"},
    "emp3": {"name": "Kumar", "age": 23, "salary": 35000, "department": "IT"},
    "emp4": {"name": "Divya", "age": 26, "salary": 40000, "department": "IT"},
    "emp5": {"name": "Ravi", "age": 28, "salary": 28000, "department": "HR"}
}


# highest_salary = float("-inf")
# second_highest = float("-inf")
# second_highest_employees = []
# second_highest_employee=""
# highest_salary_employee =""
# for emp,details in employee.items():
#     salary=details["salary"]
#     if salary > highest_salary:
#         second_highest=highest_salary
#         highest_salary=salary
#         second_highest_employee=highest_salary_employee
#         highest_salary_employee = details["name"]
#     elif salary> second_highest and salary != highest_salary:
#         second_highest=salary
#         second_highest_employee=details["name"]
# for emp,details in employee.items():
#     if details["salary"]==second_highest:
#         second_highest_employees.append(details["name"])



# print("Second highest salary:", second_highest)
# print("Employee(s) with the second highest salary:", second_highest_employees)
# highest_salary = 0
# highest_employee = ""

# for emp, details in employee.items():
#     if details["salary"] > highest_salary:
#         highest_salary=details["salary"]
#         highest_employee=details["name"]

# print("Employee with the highest salary:", highest_employee)   
# print("highest salary:",highest_salary)








# department_count={}


# for emp,details in employee.items():
#     if details["department"]=="IT":
#         print("Name:",details["name"])

#     department = details["department"]
#     if department in department_count:
#         department_count[department]+=1
#     else:
#         department_count[department]=1

# print("Total salary of IT employees only:", sum(details["salary"] for emp,details in employee.items() if details["department"]=="IT"))
# print("Employee with the highest_salary:",max(details["salary"] for emp,details in employee.items() ))
# print("Count of employees in each department:", department_count)
# employees = {
#     "emp1": {"name": "Priya", "age": 24, "salary": 30000},
#     "emp2": {"name": "Arun", "age": 25, "salary": 35000},
#     "emp3": {"name": "Kumar", "age": 23, "salary": 22000},
#     "emp4": {"name": "Divya", "age": 26, "salary": 40000},
#     "emp5": {"name": "Ravi", "age": 28, "salary": 28000}
# }
# count=0
# for emp,details in employees.items():
#     if details["age"]>24:
#         print("name:",details["name"])

#     if details["salary"]>=25000 and details["salary"]<=35000:
#         print("name:",details["name"])

#     if details["age"]>24 and details["salary"]>30000:
#         count+=1
# print(count)

# employee = {
#     "emp1": {"name": "Priya", "age": 24, "salary": 30000},
#     "emp2": {"name": "Arun", "age": 25, "salary": 35000},
#     "emp3": {"name": "Kumar", "age": 23, "salary": 22000},
#     "emp4": {"name": "Divya", "age": 26, "salary": 40000}
# }
# found=False
# name=input("Enter the employee name to search:").strip()
# for emp,details in employee.items():
#     if details["name"]==name:
#         print("Employee ID:", emp)
#         print("Age:", details["age"])
#         print("Salary:", details["salary"])
#         found=True
# if not found:
#     print("Employee not found")

# for emp,details in employees.items():
#     if details["name"] =="Kumar":
#         print("Employee ID:", emp)
#         print("Salary:", details["salary"])
#         found=True

# if not found:
#     print("Employee not found")


# employees = {
#     "emp1": {"name": "Priya", "age": 24, "salary": 30000},
#     "emp2": {"name": "Arun", "age": 25, "salary": 35000},
#     "emp3": {"name": "Kumar", "age": 23, "salary": 22000}
# }
# employees["emp1"]["salary"]=35000
# employees["emp2"]["age"]=26
# employees["emp4"]={
#     "name": "Divya",
#     "age": 26,
#     "salary": 40000
# }
# print(employees)
# employees = {
#     "emp1": {"name": "Priya", "age": 24, "salary": 30000},
#     "emp2": {"name": "Arun", "age": 25, "salary": 35000},
#     "emp3": {"name": "Kumar", "age": 23, "salary": 22000},
#     "emp4": {"name": "Divya", "age": 26, "salary": 40000}
# }
# count=0
# for emp , details in employees.items():
#     if details["salary"]> 30000:
#         print("Employee ID:", emp)
#         print("Name:", details["name"])
#         count+=1
# print("Total employees with salary greater than 30000:", count)
# print("total salary of all empoyees:", sum(details["salary"] for details in employees.values()))
# employees = {
#     "emp1": {
#         "name": "Priya",
#         "age": 24,
#         "salary": 30000
#     },
#     "emp2": {
#         "name": "Arun",
#         "age": 25,
#         "salary": 35000
#     }
# }
# for emp,details in employees.items():
#     print("Employee ID:", emp)
#     print("Name:", details["name"])
#     print("Age:", details["age"])
#     print("Salary:", details["salary"])


# for emp_id, details in employees.items():
#     print(emp_id)
#     print(details)


# employees = {
#     "emp1": {
#         "name": "Priya",
#         "age": 24,
#         "salary": 30000
#     },
#     "emp2": {
#         "name": "Arun",
#         "age": 25,
#         "salary": 35000
#     }
# }

# print(employees["emp1"]["age"])
# print(employees["emp2"]["name"])
# print(employees["emp1"]["salary"])
# print(employees["emp2"]["age"])