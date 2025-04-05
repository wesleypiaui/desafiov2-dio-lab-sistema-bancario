# 🏦 Sistema Bancário 

Bem-vindo à documentação do **Sistema Bancário Modularizado**! Este sistema foi desenvolvido para gerenciar usuários, contas correntes e operações bancárias de forma eficiente e modular. Abaixo, você encontrará todas as funcionalidades disponíveis e instruções para uso.

---

## 📋 Funcionalidades

1. **Criar Usuário**  
   - Cadastra um novo cliente no sistema.  
   - Cada usuário é composto por:
     - Nome
     - Data de nascimento
     - CPF (apenas números)
     - Endereço (formato: `logradouro, número - bairro - cidade/sigla estado`)
   - ⚠️ **Regra**: Não é permitido cadastrar dois usuários com o mesmo CPF.

2. **Criar Conta Corrente**  
   - Vincula uma conta a um cliente existente.  
   - Cada conta é composta por:
     - Agência (fixa: `0001`)
     - Número da conta (sequencial, começando em 1)
     - Usuário vinculado
   - ⚠️ **Regra**: Um usuário pode ter várias contas, mas uma conta pertence a apenas um usuário.

3. **Depositar**  
   - Adiciona dinheiro à conta.  
   - ✅ Aceita valores positivos.  
   - Retorna o saldo atualizado e registra a transação no extrato.

4. **Sacar**  
   - Permite retirar dinheiro da conta, respeitando:
     - Limite máximo por saque.
     - Limite diário de saques.  
   - Retorna o saldo atualizado e registra a transação no extrato.

5. **Exibir Extrato**  
   - Mostra todas as transações realizadas, com data e hora.  
   - Exibe o saldo atual.

6. **Listar Contas**  
   - Exibe todas as contas cadastradas no sistema, incluindo:
     - Agência
     - Número da conta
     - Nome do usuário vinculado

7. **Sair**  
   - Encerra o programa.

---

## 🚀 Como Usar

### 1️⃣ Execução do Sistema
1. Copie o código para um arquivo chamado `sistema_bancario.py`.
2. Execute o arquivo no terminal:
   ```bash
   python sistema_bancario.py
   ```

---

### 2️⃣ Menu Principal

Ao iniciar o sistema, você verá o seguinte menu:

```
===========================================
🏦  Bem-vindo ao Sistema Bancário!
===========================================

Por favor, escolha uma das opções abaixo:

1️⃣  Criar Usuário         ➡️  Cadastrar um novo cliente no sistema.
2️⃣  Criar Conta Corrente  ➡️  Vincular uma conta a um cliente existente.
3️⃣  Depositar             ➡️  Adicionar dinheiro à sua conta.
4️⃣  Sacar                 ➡️  Retirar dinheiro da sua conta (respeitando limites).
5️⃣  Exibir Extrato        ➡️  Visualizar suas transações e saldo atual.
6️⃣  Listar Contas         ➡️  Ver todas as contas cadastradas no sistema.
7️⃣  Sair                  ➡️  Encerrar o programa.

===========================================
💡 Dica: Certifique-se de criar um usuário antes de criar uma conta!
===========================================
```

---

## 📚 Detalhes Técnicos

### Estrutura do Código
O sistema foi projetado com **funções independentes** para cada operação, garantindo modularidade e clareza. Abaixo, estão as principais funções:

#### 1. **Criar Usuário**
```python
def criar_usuario(nome, data_nascimento, cpf, endereco):
    ...
```
- **Argumentos**:
  - `nome` (str): Nome do usuário.
  - `data_nascimento` (str): Data de nascimento no formato `dd/mm/yyyy`.
  - `cpf` (str): CPF do usuário (somente números).
  - `endereco` (str): Endereço completo.
- **Retorno**: Mensagem de sucesso ou erro.

#### 2. **Criar Conta Corrente**
```python
def criar_conta_corrente(cpf):
    ...
```
- **Argumentos**:
  - `cpf` (str): CPF do usuário a ser vinculado.
- **Retorno**: Mensagem de sucesso ou erro.

#### 3. **Depósito**
```python
def deposito(saldo, valor, extrato, /):
    ...
```
- **Argumentos (apenas por posição)**:
  - `saldo` (float): Saldo atual da conta.
  - `valor` (float): Valor do depósito.
  - `extrato` (list): Lista de transações.
- **Retorno**: Saldo atualizado e extrato.

#### 4. **Saque**
```python
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    ...
```
- **Argumentos (apenas por nome)**:
  - `saldo` (float): Saldo atual da conta.
  - `valor` (float): Valor do saque.
  - `extrato` (list): Lista de transações.
  - `limite` (float): Limite máximo por saque.
  - `numero_saques` (int): Número de saques realizados hoje.
  - `limite_saques` (int): Limite diário de saques.
- **Retorno**: Saldo atualizado e extrato.

#### 5. **Exibir Extrato**
```python
def exibir_extrato(saldo, /, *, extrato):
    ...
```
- **Argumentos**:
  - `saldo` (float, por posição): Saldo atual da conta.
  - `extrato` (list, por nome): Lista de transações.
- **Retorno**: Nenhum (apenas exibe o extrato no console).

#### 6. **Listar Contas**
```python
def listar_contas():
    ...
```
- **Retorno**: Nenhum (apenas exibe as contas no console).

---

## 🛠 Regras e Restrições

1. **CPF Único**: Não é permitido cadastrar dois usuários com o mesmo CPF.
2. **Limite de Saques**: Cada conta tem um limite diário de saques e valor máximo por saque.
3. **Conta Vinculada ao Usuário**: É necessário criar um usuário antes de criar uma conta.

---

## 📝 Exemplo de Uso

### Criando um Usuário
1. Escolha a opção `1️⃣ Criar Usuário`.
2. Insira os dados solicitados:
   - Nome: `João Silva`
   - Data de nascimento: `01/01/1990`
   - CPF: `12345678900`
   - Endereço: `Rua das Flores, 123 - Centro - São Paulo/SP`

### Criando uma Conta Corrente
1. Escolha a opção `2️⃣ Criar Conta Corrente`.
2. Insira o CPF do usuário: `12345678900`.

### Realizando um Depósito
1. Escolha a opção `3️⃣ Depositar`.
2. Insira o valor do depósito: `500`.

### Realizando um Saque
1. Escolha a opção `4️⃣ Sacar`.
2. Insira o valor do saque: `200`.

### Exibindo o Extrato
1. Escolha a opção `5️⃣ Exibir Extrato`.

---

## 👨‍💻 Contribuição

Se você deseja contribuir com melhorias para este sistema, sinta-se à vontade para enviar sugestões ou implementar novas funcionalidades.

---

## 📜 Licença

Este projeto é de uso livre e foi desenvolvido para fins educacionais. 🚀
