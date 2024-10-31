
  # PROJETO EXTENSIONISTA


# Requisitos do Sistema de Controle de Cestas Básicas

## Requisitos Funcionais

1. **Cadastro de Beneficiários**:
   - O sistema deve permitir o cadastro de beneficiários com os seguintes dados: nome, CPF, endereço, quantidade de membros da família e data de nascimento.

2. **Registro de Retiradas**:
   - O sistema deve permitir o registro de retiradas de cestas básicas associadas a cada beneficiário, incluindo a data da retirada.
   - O sistema deve verificar se o beneficiário já retirou uma cesta no último mês e impedir novas retiradas se este for o caso.

3. **Visualização de Beneficiários**:
   - O sistema deve exibir uma lista de todos os beneficiários cadastrados, com a opção de visualizar detalhes específicos de cada beneficiário.

4. **Visualização de Retiradas**:
   - O sistema deve permitir visualizar todas as retiradas realizadas por um beneficiário específico.

5. **Busca e Filtros**:
   - O sistema deve incluir funcionalidade de busca para encontrar beneficiários pelo nome ou CPF.
   - Deve haver filtros para visualizar retiradas por data ou beneficiário.

6. **Interface de Administração**:
   - O sistema deve ter uma interface administrativa que permita gerenciar beneficiários e retiradas, incluindo a capacidade de editar e excluir registros.

## Requisitos Não Funcionais

1. **Usabilidade**:
   - O sistema deve ser intuitivo e fácil de usar para administradores e operadores.

2. **Desempenho**:
   - O sistema deve ser capaz de processar requisições rapidamente, permitindo o cadastro e consulta de beneficiários e retiradas sem atrasos significativos.

3. **Segurança**:
   - O sistema deve garantir a segurança dos dados pessoais dos beneficiários, utilizando criptografia e proteção contra acesso não autorizado.

4. **Manutenibilidade**:
   - O código do sistema deve ser bem documentado e organizado para facilitar futuras manutenções e atualizações.

5. **Escalabilidade**:
   - O sistema deve ser projetado para suportar um aumento no número de beneficiários e retiradas sem comprometer o desempenho.

6. **Compatibilidade**:
   - O sistema deve ser compatível com os principais navegadores e dispositivos, incluindo desktops e dispositivos móveis.


  # CONTROLE BENEFICIÁRIOS CESTAS BÁSICAS</strong>


<p align="center">
  Projeto extensionista realizado em Django para a Graduação em Engenharia de Software - Anhanguera. 
  Utilizando o framework Django Admin, o projeto foi desenvolvido com o intuito de ajudar a assistência social de uma Paróquia no fornecimento, controle e distribuição de cestas básicas.
</p>


# Diagrama de Casos de Uso

![diagrama de caso de uso](https://github.com/user-attachments/assets/ec07ebb2-c7e2-4ebf-bfc6-50868debd36f)


# Diagrama de Classes


![diagramadeclasse](https://github.com/user-attachments/assets/f797587e-b749-431b-8db8-3b0303efc4b0)
