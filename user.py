from abc import ABC
from collections import defaultdict
import json
import weakref

from logger import logger

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


class User(ABC):
    """
    Base class User
    """

    __refs__ = defaultdict(list)

    def __init__(
        self, username: str,
        name: str,
        dict_key: str,
        user_id=None
    ) -> bool:
        global has_loaded, users_dict
        id = self.generate_id(dict_key) if not user_id else int(user_id)

        if has_loaded:
            for value in users_dict[dict_key].values():
                if username == value['username']:
                    print(f'ERRO: [{username}] já está cadastrado no sistema.')
                    return False
            users_dict[dict_key].update(
                {
                    str(id): {
                        'username': username,
                        'name': name,
                    }
                }
            )
            logger.log_message({'ADD_USER_JSON': users_dict})
            with open('users.json', 'w') as f:
                json.dump(users_dict, f,  indent=4)

        self.__username = username
        self.__id = int(id)
        self.__name = name
        self.__refs__[self.__class__].append(weakref.ref(self))
        return True

    def generate_id(self, dict_key: str):
        new_id = 0
        for key in users_dict[dict_key].keys():
            new_id = int(key)
        logger.log_message({'NEWLY_GEN_USER_ID': new_id + 1})
        return new_id + 1

    def edit_user(self, dict_key: str, username: str = None, name: str = None):
        global users_dict
        if name:
            self.__name = name
        if username:
            self.__username = username
        users_dict[dict_key].update(
                {
                    str(self.__id): {
                        'username': self.__username,
                        'name': self.__name,
                    }
                }
            )
        logger.log_message({'EDIT_USER_JSON': users_dict})
        with open('users.json', 'w') as f:
                json.dump(users_dict, f,  indent=4)

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

    @classmethod
    def get_instance(cls, user_id: int):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None and inst.id == user_id:
                return inst
        raise LookupError

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def name(self):
        return self.__name

    def __del__(self):
        pass

    def cascade_deletion(self, dict_key: str):
        global users_dict
        users_dict[dict_key].pop(str(self.__id), None)
        with open('users.json', 'w') as f:
            json.dump(users_dict, f,  indent=4)
        print(f'{self.username} removido.')
        self.__refs__[self.__class__].remove(weakref.ref(self))
        logger.log_message({'CASCADE_DELETION': 'finish'})
        self.__del__()
