# namedtuple

# class Employee:
#     def __init__(self,id,name,lastname,age,email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
# employees = [
#     (1,"toxir","toxirov",25,"toxir@gmail.com"),
#     (1,"akmal","sobirov",30,"akmal@gmail.com")
# ]
# em = Employee(employees[0][0],employees[0][1],employees[0][2],employees[0][3],employees[0][4])
# print(em)


# class Employee:
#     def __init__(self,id,name,lastname,age,email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
# employees = [
#     (1,"toxir","toxirov",25,"toxir@gmail.com"),
#     (1,"akmal","sobirov",30,"akmal@gmail.com")
# ]
#
# for employee in employees:
#     em = Employee(*employee)
#     print(em.name,em.id,em.lastname,em.email,em.age)

#############################################
# from collections import namedtuple
# Employees = namedtuple('Employees','id name,lastname,age,email')
# employees = [
#     (1,"toxir","toxirov",25,"toxir@gmail.com"),
#     (1,"akmal","sobirov",30,"akmal@gmail.com")
# ]
#
# for employee in employees:
#     em = Employees(*employee)
#     print(em.name,em.id,em.lastname,em.email,em.age)
