## CRUD Com Padrões

Esse projeto consite de um CRUD de dois tipos de usuários: Cliente e Funcionário. O objetivo é praticar os conceitos de padrões GRASP e GoF.

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

Classe base User da qual as classes Customer e Employee herdam.
Os métodos e atributos em comum entre as classes Employee e Customer são gerenciados na classe User.
Além disso, existe um problema que é resolvido pela classe User:

- Toda criação, alteração ou remoção nos dados dos usuários é repassado para um arquivo Json. No fim das contas, é esse Json a fonte confiável dos dados. Essa funcionalidade permite nos dar persistência nos dados (quase que um banco de dados simplificado).
- A classe User apresenta características do método GRASP High Cohesion. Ela trata exclusivamente de gerenciar dados em comum dos diversos tipos de usuário, mantendo a base de dados sempre sincronizada/atualizada.

### Customer

Customer é uma classe que herda da classe User. O construtor chama o construtor da classe User. A maioria dos métodos também estão implementados na classe User. A ideia da classe Customer é poder ter características próprias, que a distinguam de Employee. E a classe User seria então a gerenciadora das atividades em comum das classes Customer e Employee.

### Logger

Aqui é um singleton. Sempre só existirá no máximo 1 instância dessa classe. Isso acaba tornando a atividade de logging muito simples. O objeto é criado no próprio `logger.py`, e depois disso é só importar ele onde deseja ser feito o logging. Ao fim da execução do programa, chamamos o método que irá salvar todos os dados de logging num arquivo externo.

### Employee

Definir a classe Employee aqui.
