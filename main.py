#!/usr/bin/env python3
import json

import abstractuser
from customer import Customer
from employee import Employee


if __name__ == "__main__":
    # Open users json file
    f = open('users.json')
    # Load json file with all users information
    abstractuser.users_dict = json.load(f)
    f.close()

    customers = []
    employees = []
    for key, value in abstractuser.users_dict['customers'].items():
        # Import customers from json
        customers.append(Customer(username=value['username'], name=value['name'], user_id=int(key)))
    for key, value in abstractuser.users_dict['employees'].items():
        # Import employees from json
        employees.append(Employee(username=value['username'], name=value['name'], user_id=int(key)))
    abstractuser.has_loaded = True

    customer1 = Customer(username='marcelo', name='Marcelo')
    customer2 = Customer(username='marcelo', name='Marcelo')
    customer3 = Customer(username='tomas', name='Tomas')
    customer4 = Customer(username='john', name='John')
    customer5 = Customer(username='pedro', name='Pedro')
    employee1 = Employee(username='joao', name='Joao')
    employee2 = Employee(username='marcos', name='Marcos')

    emp = Employee.list_users()
    cust = Customer.list_users()

    print('Clientes')
    for c in cust:
        print(f'{c.id} : {c.username}')

    print('Funcionarios')
    for e in emp:
        print(f'{e.id} : {e.username}')

    cus = Customer.get_instance(3)
    print(cus, cus.username, cus.id)