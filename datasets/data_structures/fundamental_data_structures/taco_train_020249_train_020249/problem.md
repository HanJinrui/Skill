You get a new job working for Eggman Movers.  Your first task is to write a method that will allow the admin staff to enter a person’s name and return what that person's role is in the company.

You will be given an array of object literals holding the current employees of the company.  You code must find the employee with the matching firstName and lastName and then return the role for that employee or if no employee is not found it should return "Does not work here!"

The array is preloaded and can be referenced using the variable `employees` (`$employees` in Ruby). It uses the following structure.

```python
employees = [ {'first_name': "Dipper", 'last_name': "Pines", 'role': "Boss"}, ...... ]
```

There are no duplicate names in the array and the name passed in will be a single string with a space between the first and last name i.e. Jane Doe or just a name.

Starter code:
```python
employees = [{'first_name': 'Ollie', 'last_name': 'Hepburn', 'role': 'Boss'}, {'first_name': 'Morty', 'last_name': 'Smith', 'role': 'Truck Driver'}, {'first_name': 'Peter', 'last_name': 'Ross', 'role': 'Warehouse Manager'}, {'first_name': 'Cal', 'last_name': 'Neil', 'role': 'Sales Assistant'}, {'first_name': 'Jesse', 'last_name': 'Saunders', 'role': 'Admin'}, {'first_name': 'Anna', 'last_name': 'Jones', 'role': 'Sales Assistant'}, {'first_name': 'Carmel', 'last_name': 'Hamm', 'role': 'Admin'}, {'first_name': 'Tori', 'last_name': 'Sparks', 'role': 'Sales Manager'}, {'first_name': 'Peter', 'last_name': 'Jones', 'role': 'Warehouse Picker'}, {'first_name': 'Mort', 'last_name': 'Smith', 'role': 'Warehouse Picker'}, {'first_name': 'Anna', 'last_name': 'Bell', 'role': 'Admin'}, {'first_name': 'Jewel', 'last_name': 'Bell', 'role': 'Receptionist'}, {'first_name': 'Colin', 'last_name': 'Brown', 'role': 'Trainee'}]

def find_employees_role(name):
```
