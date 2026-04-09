# Especificação de Caso de Uso

## Informações Gerais

| Campo | Descrição |
|------|-----------|
| **Nome do Caso de Uso** | Cadastrar/alterar usuário|
| **Descrição** | O cliente pode cadastrar um usuário de comprador para ele |
| **Ator Envolvido** | Cliente|

---

## Interação entre Ator e Sistema

| Funcionário (Ator) | Sistema |
|--------------------|---------|
| O cliente seleciona para cadastrar um usuário| O sistema abre uma tela com os campos para o cadastro de usuário  |
| O cliente seleciona para alterar seu usuário | O sistema abre uma tela com os campos que podem ser alterados |
| O cliente seleciona para finalizar a alteração/cadastro do usuário | O sistema abre uma tela dizendo que a ação foi bem sucedida |

---

## Exceções
- Nenhuma exceção definida

---

## Alternativas
- Nenhuma alternativa definida

---

## Regras de Negócio
- RN01 - Cada usuário deve possuir um código de identificação.
- RN02 - Não pode existir dois cadastros com o mesmo CPF.
- RN03 - Data de nascimento deve ser válida e o usuário cadastrado deve possuir mais de 18 anos.
- RN04 - O telefone deve seguir o padrão DD999999999 ou DD99999999.
- RN05 - O código deve ser selecionado pelo sistema seguindo uma sequência numérica.

---

## Requisitos de Interface com o Usuário
- RI01 - O sistema deve exibir uma tela para selecionar se deseja cadastrar o usuário caso ele não esteja logado.
- RI02 - O sistema deve exibir uma tela para selecionar se deseja alterar o usuário caso ele esteja logado.

---
