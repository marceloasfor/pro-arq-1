from employee import Employee
from products import Products
from employee import Employee
from customer import Customer


class ProductManager:
    # Product Management methods
    @classmethod
    def applyDiscount(cls, productID: int, percent: float):
        # retrieve another user
        try:
            prod = Products.get_instance(productID)
            newPrice = prod.price - ((percent/100)*prod.price)
            prod.edit_product(price=newPrice)
        except:
            pass

    @classmethod
    def buyOrder(cls, productID: int, employeeID: int, customerID: int, qtty: int):
        try:
            prod = Products.get_instance(productID)
            emp = Employee.get_instance(employeeID)
            cust = Customer.get_instance(customerID)

            newQtd = prod.qtty - qtty
            prod.edit_product(qtty=newQtd)

            print(
                f'Compra de {qtty} {prod.product}(s), pelo valor de R${prod.price}\nVendedor:{emp.username}\nComprador:{cust.username}')
        except:
            pass
