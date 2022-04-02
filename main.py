from abc import ABC, abstractmethod
from collections import defaultdict
import json
import weakref

# users_dict = {'customers': dict(), 'employees': dict()}
users_dict = {}
'''
customers: {
    users:
    1:{
        'username': marcelo,
    },
employees:
    1: {
        'username': joao,
    },
}
'''
has_loaded = False


class AbstractUser(ABC):
    """
    Base class User
    """

    __refs__ = defaultdict(list)

    @abstractmethod
    def __init__(self, username: str, dict_key: str, user_id=None) -> bool:
        id = self.generate_id(dict_key) if not user_id else user_id

        global has_loaded
        if has_loaded:
            for value in users_dict[dict_key].values():
                if username == value['username']:
                    print(f'ERRO: [{username}] já está cadastrado no sistema.')
                    return False
            users_dict[dict_key].update(
                {
                    id: {
                        'username': username,
                    }
                }
            )
            with open('users.json', 'w') as f:
                json.dump(users_dict, f,  indent=4)
        
        self.username = username
        self.id = id
        self.__refs__[self.__class__].append(weakref.ref(self))
        return True

    def generate_id(self, dict_key: str):
        new_id = 0
        for key in users_dict[dict_key].keys():
            new_id = int(key)
        return new_id + 1

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst


class Customer(AbstractUser):
    def __init__(self, username: str, user_id=None):
        super().__init__(username, 'customers', user_id)

    @classmethod
    def list_users(cls):
        customers_list = []
        for customer in cls.get_instances():
            customers_list.append(customer)
        return customers_list


class Employee(AbstractUser):
    def __init__(self, username: str, user_id=None):
        super().__init__(username, 'employees', user_id)
    
    @classmethod
    def list_users(cls):
        employees_list = []
        for employee in cls.get_instances():
            employees_list.append(employee)
        return employees_list


if __name__ == "__main__":
    # Open users json file
    f = open('users.json')
    # Load json file with all users information
    users_dict = json.load(f)
    f.close()

    customers = []
    employees = []
    for key, value in users_dict['customers'].items():
        # Import customers from json
        customers.append(Customer(username=value['username'], user_id=int(key)))
    for key, value in users_dict['employees'].items():
        # Import employees from json
        employees.append(Employee(username=value['username'], user_id=int(key)))
    has_loaded = True

    customer1 = Customer(username='marcelo')
    customer2 = Customer(username='marcelo')
    customer2 = Customer(username='tomas')
    customer2 = Customer(username='john')
    customer3 = Customer(username='pedro')
    employee1 = Employee(username='joao')
    employee2 = Employee(username='marcos')

    emp = Employee.list_users()
    cust = Customer.list_users()

    print('Clientes')
    for c in cust:
        print(f'{c.id} : {c.username}')

    print('Funcionarios')
    for e in emp:
        print(f'{e.id} : {e.username}')
