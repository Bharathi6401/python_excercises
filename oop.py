class BankAccount:
    def __init__(self,account_holder,balance):

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_holder=account_holder
        self.__balance=balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.__balance+=amount

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance-=amount
    def get_balance(self):
        return self.__balance

b1=BankAccount("Jaya",-10000)
b1.deposit(2000)
b1.withdraw(3000)
try:
    b1.withdraw(20000)
except ValueError as e:
    print(e)
print(b1.get_balance())





# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self,salary):
#         if  salary <= 0:
#             raise ValueError("Salary must be greater than or equal to zero")
#         else:
#             self.__salary=salary


# emp1=Employee(50000)
# print(emp1.get_salary())

# emp1.set_salary(48000)
# print(emp1.get_salary())
# print(emp1._Employee__salary)



# class Developer:
#     def work(self):
#         return "Developer writes code"

# class Manager:
#     def work(self):
#         return "Manager manages the team"
    
# employees=[Developer(),Manager()]
# for employee in employees:
#     print(employee.work()) 

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def get_details(self):
#         return f"{self.name} earns {self.salary}"

# class Developer(Employee):
#     def __init__(self,name,salary,language):
#         super().__init__(name,salary)
#         self.language=language
#     def get_developer_details(self):
#         return f"{self.name} works with {self.language} and earns {self.salary}"
    
#     def get_details(self):
#         print(super().get_details())
#         return f"{self.name} is a Developer, works with {self.language} and earns {self.salary}"
    

# dev=Developer("Jaya",5000,"Python AI engineer")
# print(dev.get_details())
# print(dev.get_developer_details())



# class Employee:
#     def __init__(self,name,salary,experience):
#         self.name=name
#         self.salary=salary
#         self.experience=experience

#     def get_details(self):
#         return f"Name: {self.name}, Salary: {self.salary}, Experience: {self.experience}"
#     def is_eligible_for_promotion(self):
#         return self.experience >= 2
    
# emp1=Employee("Saran",50000,3)
# emp2=Employee("Jaya",65000,2)

# print(emp1.get_details())
# print(emp1.is_eligible_for_promotion())
# print(emp2.get_details())
# print(emp2.is_eligible_for_promotion())

# def validate_age(age):
#     age = int(age)
#     if age<0:
#         raise ValueError("Age cannot be negative")
#     if age >120:
#         raise ValueError("Invalid age")
#     else:
#         return "Valid age"

# def calculate_discount(price, discount_percentage):
#     try:
#         price = float(price)
#         discount_percentage = float(discount_percentage)
#     except(ValueError,TypeError):
#         return "Invalid input"
    
#     if price <=0:
#         return "Invalid price"
    
#     if discount_percentage<0 or discount_percentage>100:
#         return "Invalid discount"
    
#     final_price = price - (price * (discount_percentage / 100))
#     return final_price


# print(calculate_discount(1000, 10))
# print(calculate_discount("500", "20"))
# print(calculate_discount("abc", 10))
# print(calculate_discount(-100, 10))
# print(calculate_discount(1000, 0))
# print(calculate_discount(1000, 120))
# def validate_salary(salary):
#     try:
#         salary = float(salary)

#         if salary > 0:
#             return "Valid salary"
#         else:
#             return "Invalid salary"

#     except (ValueError, TypeError):
#         return "Please enter a number"


# print(validate_salary("25000"))
# print(validate_salary(-5000))
# print(validate_salary("abc"))
# print(validate_salary(0))

# class Rectangle:
#  def __init__(self,width,height):
#   self.width=width
#   self.height=height
#  def area(self):
#   return self.width*self.height

# r1=Rectangle(5,3)
# print(r1.area() )
# class Student:
#  def __init__(self,name,grade):
#   self.name=name
#   self.grade=grade

# s1=Student("Anna","A")
# print(s1.grade)	
# s1.grade="B"
# print(s1.grade)

# class Car:
#  def __init__(self,brand):
#   self.brand=brand
#  def show(self):
#   print(self.brand)
# c1=Car("Ford")
# c1.show()

# class Dog:
#  def __init__(self,name,age):
#   self.name=name
#   self.age=age
#  def bark(self):
#   return self.name,"says Woof!"

# d1=Dog("Buddy",3)
# print(d1.bark())

# class Person:
#  def __init__(self,name,age):
#   self.name=name
#   self.age=age
#  def greet(self):
#   return "Hello, my name is", self.name

# p1=Person("John",36)
# print(p1.greet())


# class Employee:
#     def __init__(self,name,salary,experience):
#         self.name=name
#         self.salary=salary
#         self.experience=experience

#     def get_details(self):
#         return{
#             "name":self.name,"salary":self.salary,"experience":self.experience
#         }
#     def _is_eligible_for_promotion(self):
#         return self.experience>=2

# emp1=Employee("Saran",50000,1)
# emp2=Employee("Jaya",25000,3)

# print(emp1.get_details())
# print("is eligible?", emp1._is_eligible_for_promotion())

# print(emp2.get_details())
# print("is eligible?", emp2._is_eligible_for_promotion())
