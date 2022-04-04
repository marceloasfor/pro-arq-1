from abstractuser import AbstractUser


class Employee(AbstractUser):
    def __init__(self, username: str, user_id=None):
        super().__init__(username, 'employees', user_id)

    @classmethod
    def list_users(cls):
        employees_list = []
        for employee in cls.get_instances():
            employees_list.append(employee)
        return employees_list
