from collections import defaultdict
import json
import weakref

from logger import logger

has_loaded = False
products_dict = {}


class AbstractProducts:

    __refs__ = defaultdict(list)

    def __init__(
        self, product: str,
        price: float,
        qtty: int,
        dict_key: str,
        product_id=None
    ) -> bool:
        global has_loaded, products_dict
        id = self.generate_id(dict_key) if not product_id else int(product_id)

        if has_loaded:
            for value in products_dict[dict_key].values():
                if product == value['product']:
                    print(f'ERRO: [{product}] já está cadastrado no sistema.')
                    return False
            products_dict[dict_key].update(
                {
                    str(id): {
                        'product': product,
                        'price': price,
                        'qtty': qtty,
                    }
                }
            )
            logger.log_message({'ADD_PRODUCT_JSON': products_dict})
            with open('products.json', 'w') as f:
                json.dump(products_dict, f,  indent=4)

        self.__product = product
        self.__id = int(id)
        self.__price = price
        self.__qtty = qtty
        self.__refs__[self.__class__].append(weakref.ref(self))
        return True

    def generate_id(self, dict_key: str):
        new_id = 0
        for key in products_dict[dict_key].keys():
            new_id = int(key)
        logger.log_message({'NEWLY_GEN_PRODUCT_ID': new_id + 1})
        return new_id + 1

    def edit_product(self, dict_key: str, product: str = None, price: float = None, qtty: int = None):
        global products_dict
        if price:
            self.__price = price
        if product:
            self.__product = product
        if qtty:
            self.__qtty
        products_dict[dict_key].update(
            {
                str(self.__id): {
                    'product': self.__product,
                    'price': self.__price,
                    'qtty': self.__qtty,
                }
            }
        )
        logger.log_message({'EDIT_PRODUCT_JSON': products_dict})
        with open('products.json', 'w') as f:
            json.dump(products_dict, f,  indent=4)

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

    @classmethod
    def get_instance(cls, product_id: int):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None and inst.id == product_id:
                return inst
        raise LookupError

    @property
    def id(self):
        return self.__id

    @property
    def product(self):
        return self.__product

    @property
    def price(self):
        return self.__price

    @property
    def qtty(self):
        return self.__qtty

    def __del__(self):
        pass

    def cascade_deletion(self, dict_key: str):
        global products_dict
        products_dict[dict_key].pop(str(self.__id), None)
        with open('products.json', 'w') as f:
            json.dump(products_dict, f,  indent=4)
        print(f'{self.product} removido.')
        self.__refs__[self.__class__].remove(weakref.ref(self))
        logger.log_message({'CASCADE_DELETION': 'finish'})
        self.__del__()
