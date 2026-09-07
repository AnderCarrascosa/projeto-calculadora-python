# Projeto Calculadora Python

## Descrição

Este projeto consiste em uma calculadora desenvolvida em Python.

O programa solicita dois números ao usuário e permite escolher entre cinco operações matemáticas:

- Soma (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Potência (**)

## Tecnologias utilizadas

- Python 3
- Bash
- Git
- GitHub

## Arquivos do projeto

- `calculadora.py` - contém o código principal da calculadora.
- `executar.sh` - script Bash utilizado para executar o programa Python.
- `README.md` - documentação do projeto.

## Como executar o programa

### Executando diretamente pelo Python

No terminal, dentro da pasta do projeto, execute:

```bash
python3 calculadora.py
```

### Executando pelo arquivo .sh

O arquivo `executar.sh` foi criado para facilitar a execução do programa.

Para executar o arquivo `.sh`, primeiro dê permissão de execução:

```bash
chmod +x executar.sh
```

Depois execute:

```bash
./executar.sh
```

O script irá iniciar automaticamente o programa `calculadora.py`.

## Explicação do código Python

O programa começa solicitando ao usuário dois números.

Os valores digitados são convertidos para o tipo `float`, permitindo trabalhar com números inteiros e decimais.

Em seguida, o programa apresenta as opções de operação:

- `+` - Soma
- `-` - Subtração
- `*` - Multiplicação
- `/` - Divisão
- `**` - Potência

O usuário escolhe uma operação, que é armazenada na variável `operacao`.

O programa utiliza estruturas condicionais `if` e `elif` para identificar a operação escolhida e realizar o cálculo correspondente.

Na divisão, o programa verifica se o segundo número é diferente de zero. Caso seja zero, apresenta uma mensagem informando que não é possível realizar a divisão.

Na operação de potência, o programa calcula o primeiro número elevado ao segundo número.

Caso o usuário escolha uma operação que não esteja entre as opções disponíveis, o programa informa que a operação é inválida.

Após realizar o cálculo, o resultado é apresentado na tela.

## Funcionamento do arquivo executar.sh

O arquivo `executar.sh` é um script Bash utilizado para iniciar o programa Python.

Seu conteúdo executa o seguinte comando:

```bash
python3 calculadora.py
```

Assim, ao executar:

```bash
./executar.sh
```

o programa `calculadora.py` é iniciado automaticamente.
