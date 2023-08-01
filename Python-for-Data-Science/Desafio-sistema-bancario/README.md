<center>

### Desafio Criando Sistema Bancario 

---

O desafio consiste em criar um sistama bancario simples para:

</center>

- SAQUE
    - Permitir apenas 3 saque diario.
    - Cada saque com limite de 500R$
    - Mensagem para saldo insuficiente
- DEPOSITO
    - Permitir apenas depositos de valores maiores que '0'
- EXTRATO
    - Todas as operaçoes devem ser armazenadas
    - Listar todas as movimentaçoes
    - Mensagem de que nao houve movimentações

<center>

### Parte 2

---

</center>

- Criar Funçoes para:
    - Saque
    - Deposito
    - Extrato
    - Novo usuario
    - conta
- Regras
    - Saque:
        - Os argumentos tem que ser passado de forma 'nominal'
    - Deposito:
        - Os argumentos tem que ser passdo de forma 'posicional'
    - Extrato:
        - Os argumentos tem que ser passdo de forma 'posicional' e 'nominal'
    - Novo usuario:
        - Dever ter "nome", "data nascimento", "CPF", "endereço"
        - Endereço no formato "log, n, bairro, cidade/sigla estado"
        - Nao pode cadastra 2 usuarios com mesmo 'CPF'
    - Conta:
        - Numero da agencia fixo '0001'
        - Numero da conta por usuario sequencia começando em 1
        - Nome do usuario  
        - Usuario pode ter varias conta
        - Conta deve pertencer apenas a 1 usuario