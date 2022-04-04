from abstractuser import AbstractUser


class Customer(AbstractUser):
    def __init__(self, username: str, name:str, user_id=None):
        super().__init__(
            username=username, 
            name=name, 
            dict_key='customers', 
            user_id=user_id,
        )

    @classmethod
    def list_users(cls):
        customers_list = []
        for customer in cls.get_instances():
            customers_list.append(customer)
        return customers_list

    @classmethod
    def get_instance(cls, user_id: int):
        return super().get_instance(user_id)

    def edit_user(self, username: str = None, name: str = None):
        super().edit_user('customers', username, name)

    @classmethod
    def delete_user(cls, user_id: int):
        obj = cls.get_instance(user_id)
        obj.cascade_deletion()

    def cascade_deletion(self):
        super().cascade_deletion('customers')
