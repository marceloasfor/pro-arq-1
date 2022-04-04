from user import User


class Employee(User):
    def __init__(self, username: str, name: str, user_id=None):
        super().__init__(
            username=username, 
            name=name,
            dict_key='employees',
            user_id=user_id,
        )

    @classmethod
    def list_users(cls):
        employees_list = []
        for employee in cls.get_instances():
            employees_list.append(employee)
        return employees_list

    @classmethod
    def get_instance(cls, user_id: int):
        return super().get_instance(user_id)

    def edit_user(self, username: str = None, name: str = None):
        super().edit_user('employees', username, name)

    @classmethod
    def delete_user(cls, user_id: int):
        obj = cls.get_instance(user_id)
        obj.cascade_deletion()

    def cascade_deletion(self):
        super().cascade_deletion('employees')
