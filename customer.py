from abstractuser import AbstractUser


class Customer(AbstractUser):
    def __init__(self, username: str, user_id=None):
        super().__init__(username, 'customers', user_id)

    @classmethod
    def list_users(cls):
        customers_list = []
        for customer in cls.get_instances():
            customers_list.append(customer)
        return customers_list
