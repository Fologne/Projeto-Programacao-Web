# Especificação de Caso de Uso

## Informações Gerais

| Campo | Descrição |
|------|-----------|
| **Nome do Caso de Uso** | Cadastro de produto |
| **Descrição** | O administrador pode cadastrar/alterar um produto |
| **Ator Envolvido** | Administrador |

---

## Interação entre Ator e Sistema

| Funcionário (Ator) | Sistema |
|--------------------|---------|
| O administrador seleciona para cadastrar um novo produto | O sistema deve exibir uma tela para cadastro do produto |
| O administrador preenche todos os campos e seleciona cadastrar| O sistema deve colocar o produto em seu banco de dados |
| O administrador seleciona para alterar o produto| O sistema deve exibir uma tela para alterar campos pré-definidos |

---

## Exceções
- Nenhuma exceção definida.

---

## Alternativas
- Nenhuma alternativa definida.

---

## Regras de Negócio
- RN01 - Cada produto deve ter um id.
- RN02 - Cada produto deve ter um preço e estoque.
- RN03 - Os campos criado_em e modificado_em devem ser preenchidos automaticamente.
- RN04 - O campo de qtd_vendida deve ser inicializado em 0 e aumentado conforme vendas.

---

## Requisitos de Interface com o Usuário
- RI01 - O sistema deve exibir uma tela para o cadastro/alteração do produto.
- RI02 - O sistema deve exibir uma tela quando o produto for cadastrado/alterado com sucesso.

---
