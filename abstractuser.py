from abc import ABC, abstractmethod
from collections import defaultdict
import json
import weakref

has_loaded = False
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


class AbstractUser(ABC):
    """
    Base class User
    """

    __refs__ = defaultdict(list)

    @abstractmethod
    def __init__(self, username: str, dict_key: str, user_id=None) -> bool:
        global has_loaded, users_dict
        id = self.generate_id(dict_key) if not user_id else user_id

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

        self.__username = username
        self.__id = id
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

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username
