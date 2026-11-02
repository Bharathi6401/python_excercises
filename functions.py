def calculate_employee_salary(name,basic_salary,*args,**kwargs):
    total_salary=basic_salary + sum(args)
    return {
        "name":name,
        "total_salary":total_salary,
        "additional_details": kwargs,
    }

result = calculate_employee_salary(
    "Priya",
    30000,
    2000,
    3000,
    department="IT",
    role="Python Developer"
)

print(result)
def create_employee(name,age,**kwargs):
    print(f"Employee Name:{name}")
    print(f"Employee Age:{age}")
    print("Additional details:",kwargs)

create_employee(
    "Priya",
    24,
    department="IT",
    role="Python Developer",
    experience=2
)



def employee_details(**kwargs):
    print(kwargs["name"])

employee_details(name="Priya", department="Developer")

def employee_details(**kwargs):
    name = kwargs.get("name", "Name not provided")
    department=kwargs.get("department","Department not provided")
    print(name)
    print(department)
    print(kwargs)
employee_details(name="Priya", department="Developer")




def calculate_average(*args):
    
    if len(args)==0 :
        print("Please provide at least one number")

    average=sum(args)/len(args)
    return average

print(calculate_average(10, 20, 30))
print(calculate_average(10, 20, 30, 40, 50))
print(calculate_average())

def calculate_discount(price,discount_percentage=10):
    final_price=price -(price * (discount_percentage / 100))
    return final_price


print(calculate_discount(1000))
print(calculate_discount(2000,20))

def calculate_net_salary(basic_salary,allowance):
    net_salary=basic_salary+allowance
    return net_salary

annual_salary= calculate_net_salary(60000,6000)

print(calculate_net_salary(50000,5000))
print(calculate_net_salary(basic_salary=62000,allowance=3000))
print(annual_salary)