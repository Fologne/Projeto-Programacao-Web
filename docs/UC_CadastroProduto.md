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

# Dicionário de Dados

| Nome do Campo | Descrição | Obrigatório | Tipo | Tamanho | Máscara | Valor Default | Regex |
|---------------|-----------|-------------|------|---------|---------|--------------|-------|
| ID| ID do produto no banco de dados |Obrigatório |INT |1 | | |```^\d{1,120}$```|
|Nome |Nome do produto |Obrigatório |Texto |80 | | |```^.{1,80}$```|
| Descrição|Descrição do produto |Opcional |Texto |250 | | |```^.{0,250}$```|
| Preco|Preço do produto |Obrigatório |Decimal | | | |```^\d+(\.\d{2})?$```|
| Imagem| Imagem do produto | Opcional |Imagem | | | |```^.+\.(jpg\|jpeg\|png\|gif)$```|
| Estoque|Estoque do produto | Obrigatório|INT |3 | | |```^\d{3}$```|
| Esta_disponivel|Disponibilidade do produto |Obrigatório |Boolean | | | |```^(true\|false)$```|
|Criado_em |Data de criação do produto |Obrigatório |Data| | | |```^(0[1-9]\|[12][0-9]\|3[01])\/(0[1-9]\|1[0-2])\/(19\|20)\d{2}$```|
|Modificado_em |Data de modificação do produto | Obrigatório|Data | | | |```^(0[1-9]\|[12][0-9]\|3[01])\/(0[1-9]\|1[0-2])\/(19\|20)\d{2}$```|
| Slug| Slug do produto |Obrigatório | SlugField| | | |```^[a-z0-9-]{1,80}$```|
| Categoria| Categoria do produto | Obrigatório| Texto | | | |```^.{0,50}$```|
|Tipo |Tipo do produto |Opcional |Texto | | | |```^.{0,50}$```|
| Qtd_vendida|Quantidade vendida do produto |Obrigatório | INT| 4| | |```^\d{1,120}$```|
