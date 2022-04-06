# Trabalho Proj Arquitetura de Sistemas
-----------

**Equipe:**

Lucas Sales Carvalho Carioca (matrícula: 2020813)

Marcelo Asfor Pinheiro (matrícula: 2123441)

## CRUD Com Padrões

Esse sistema consiste de um CRUD de diferentes tipos de usuários e produtos. Os usuários tem os métodos básicos para CRUD além de ter o seu resultado de execução salvo em um JSON. Criamos também uma classe singleton de Logging, que é utilizada como forma de auditar as ações executadas além de facilitar no debugging.
A classe de produtos tem os mesmos métodos de CRUD dos usuários. Além disso, nela é possível efetuar ordem de compras, o que significa ser possível reduzir a quantidade de itens do estoque baseado nessas ordens de compra.

### Pré-requisitos

Pré-requisitos do projeto:

1. Python 3.10.4 (recomendado) (mínimo: 3.8.13)
2. Arquivo json na raíz do projeto chamado `users.json`.

O arquivo `users.json` deve ser do seguinte formato:

```
{
    "customers": {
    },
    "employees": {
    }
}
```

### Build inicial

Como o projeto não tem nenhuma dependência em bibliotecas externas, bastar utilizar o python padrão do computador.
No terminal:

```
# Se python3 não for o padrão
python3 main.py

# Se python3 for o padrão
python main.py

# Para saber sua versão de python
python --version
# ou
python3 --version
```

### User

É da classe abstrata User que as classes Customer e Employee herdam.
Os métodos e atributos em comum entre as classes Employee e Customer são gerenciados na classe User.
Além disso, existe um problema que é resolvido pela classe User:

- Toda criação, alteração ou remoção nos dados dos usuários é repassado para um arquivo Json. No fim das contas, esse Json que é a fonte confiável dos dados. Essa funcionalidade permite nos dar persistência nos dados (quase que um banco de dados simplificado).
- A classe User apresenta características do método GRASP High Cohesion. Ela trata exclusivamente de gerenciar dados em comum dos diversos tipos de usuário, mantendo a base de dados sempre sincronizada/atualizada.

### Customer e Employee

Customer e Employee são duas classes que herdam da classe base User. Toda atividade padrão para buscar, criar, editar, listar e destruir objetos foi toda implementada em User. As classes Customer e Employee herdam, e tem a possibilidade de incrementar de acordo com sua necessidade.

### Logger

Aqui é um singleton. Sempre só existirá no máximo 1 instância dessa classe. Isso acaba tornando a atividade de logging muito simples. O objeto é criado no próprio `logger.py`, e depois disso é só importar ele onde deseja ser feito o logging. Ao fim da execução do programa chamamos o método que irá salvar todos os dados de logging num arquivo externo.

### Abstract Product

A classe AbstractProduct é aquela da qual a classe Products herda. A classe gerencia também a criação, alteração oou remoção de dados do arquivo JSON "products.json". Permitindo a persistência dos dados.
Assim como a classe User, AbstractProduct também apresenta características do método GRASP High Cohesion, gerenciando dados comum da classe Products e outras que venham a herdar.

### Products

A classe Products herda da classe AbstractProduct e nela é possível utilizar-se dos métodos herdados para adicionar, atualizar, consultar e remover produtos do sistema.

### ProductManager

A classe ProductManager apresenta características do padrão estrutural GoF Facade, oferecendo métodos de mais alto nível para facilitar a utilização dos métodos existentes nas classes de produtos. Nela é possível aplicar descontos em determinados produtos, atualizando o valor no banco (arquivo json) e realizar ordens de compra, decrementando a quantidade de produtos no estoque e detalhando funcionário, cliente, produto e quantidade da compra.
