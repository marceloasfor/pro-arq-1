from abstractProducts import AbstractProducts


class Products(AbstractProducts):
    def __init__(self, product: str, price: float, qtty: int, product_id: int=None):
        super().__init__(
            product=product,
            price=price,
            qtty=qtty,
            dict_key='products',
            product_id=product_id,
        )

    @classmethod
    def list_products(cls):
        products_list = []
        for product in cls.get_instances():
            products_list.append(product)
        return products_list

    @classmethod
    def get_instance(cls, product_id: int):
        return super().get_instance(product_id)

    def edit_product(self, product: str = None, price: float = 0, qtty: int = 0):
        super().edit_product('products', product, price, qtty)

    @classmethod
    def delete_product(cls, product_id: int):
        obj = cls.get_instance(product_id)
        obj.cascade_deletion()

    def cascade_deletion(self):
        super().cascade_deletion('products')
