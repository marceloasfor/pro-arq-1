import json

import user
import abstractProducts
from customer import Customer
from employee import Employee
from products import Products
from productManager import ProductManager
from logger import logger


if __name__ == "__main__":
    # Open users json file
    f = open('users.json')
    # Load json file with all users information
    user.users_dict = json.load(f)
    f.close()

    productsJson = open('products.json')
    abstractProducts.products_dict = json.load(productsJson)
    productsJson.close()

    customers = []
    employees = []
    productsList = []
    for key, value in user.users_dict['customers'].items():
        # Import customers from json
        customers.append(
            Customer(username=value['username'], name=value['name'], user_id=int(key)))
    for key, value in user.users_dict['employees'].items():
        # Import employees from json
        employees.append(
            Employee(username=value['username'], name=value['name'], user_id=int(key)))
    user.has_loaded = True

    for key, value in abstractProducts.products_dict['products'].items():
        productsList.append(
            Products(product=value['product'], price=value['price'], qtty=value['qtty'], product_id=int(key)))
    abstractProducts.has_loaded = True

    customer1 = Customer(username='marcelo', name='Marcelo')
    customer2 = Customer(username='marcelo', name='Marcelo')
    customer3 = Customer(username='tomas', name='Tomas')
    customer4 = Customer(username='john', name='John')
    customer5 = Customer(username='pedro', name='Pedro')
    employee1 = Employee(username='joao', name='Joao')
    employee2 = Employee(username='marcos', name='Marcos')

    product1 = Products(product='Carro1', price=15000.00, qtty=5)
    product2 = Products(product='Carro2', price=25000.00, qtty=10)
    product3 = Products(product='Carro3', price=35000.00, qtty=15)
    product4 = Products(product='Carro4', price=45000.00, qtty=20)

    emp = Employee.list_users()
    cust = Customer.list_users()
    prod = Products.list_products()

    print('Clientes')
    for c in cust:
        print(f'{c.id} : {c.username} - {c.name}')

    print('Funcionarios')
    for e in emp:
        print(f'{e.id} : {e.username} - {e.name}')

    print('Produtos')
    for p in prod:
        print(f'{p.id} : {p.product} - {p.price} - {p.qtty}')

    try:
        cus = Customer.get_instance(3)
        print(cus, cus.username, cus.id)
    except LookupError:
        pass

    # Customer methods
    # add a customer
    print('Criando um novo usuário:')
    new_customer = Customer(username='james', name='James Bond')
    # edit customer
    print(
        f'new_customer: [{new_customer.id}:{new_customer.username}] - {new_customer.name}')
    print('Alterando dados do usuário:')
    new_customer.edit_user(username='daniel', name='Daniel Craig')
    print(
        f'new_customer: [{new_customer.id}:{new_customer.username}] - {new_customer.name}')
    # list all customers
    print('Todos os usuários:')
    for cust in Customer.list_users():
        print(f'[{cust.id}:{cust.username}] - {cust.name}')
    # retrieve another user
    print('GET outro usuário:')
    try:
        another_user = Customer.get_instance(1)
        print(
            f'another_user: [{another_user.id}:{another_user.username}] - {another_user.name}')
    except:
        pass
    # delete new_customer
    print('Deletando o new_customer:')
    Customer.delete_user(new_customer.id)
    for cust in Customer.list_users():
        print(f'[{cust.id}:{cust.username}] - {cust.name}')

    
    # Employee methods:
    # add a employee
    print('Criando um novo funcionário:')
    new_employee = Employee(username='Jackie', name='Jackie Chan')
    # edit employee
    # TODO

    # Products methods:
    print('Adicionando um novo produto:')
    new_product = Products(product='Moto', price=1000.00, qtty=12)
    
    # edit products
    # TODO

    # Management methods
    ProductManager.applyDiscount(8, 20)
    ProductManager.buyOrder(productID=8, employeeID=3, customerID=4, qtty=10)

    logger.log_save()
