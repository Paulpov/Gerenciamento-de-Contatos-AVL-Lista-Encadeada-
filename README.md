# Sistema de Gerenciamento de Contatos 📖

## Descrição do Projeto
Este sistema de gerenciamento de contatos é projetado para armazenar informações (nomes e números de telefone) de forma organizada e eficiente. Utiliza uma combinação de Árvore AVL e listas encadeadas para garantir inserções rápidas, busca eficiente e listagem em ordem alfabética.

### Estrutura do Sistema

#### Árvore AVL 🌳
A **Árvore AVL** é usada para organizar os contatos pelas iniciais dos seus nomes. Cada nó na árvore representa uma letra do alfabeto, permitindo operações eficientes com tempo logarítmico:
- **Inserção**: Adiciona novos contatos no nó correspondente à primeira letra do nome. Se necessário, realiza rotações para manter a árvore balanceada.
- **Busca**: Inicia procurando pelo nó que corresponde à inicial do nome do contato, depois busca na lista encadeada.
- **Listagem**: Realiza uma travessia in-order para listar todos os contatos em ordem alfabética.

#### Listas Encadeadas 🔗
Cada nó na Árvore AVL possui uma lista encadeada para armazenar contatos com a mesma inicial:
- **Inserção Ordenada**: Insere contatos de forma ordenada dentro da lista para manter a ordem alfabética.
- **Busca Eficiente**: Permite a busca rápida por contatos dentro da mesma inicial.

### Conclusão
A combinação de **árvores AVL** com **listas encadeadas** oferece uma solução robusta e escalável para o gerenciamento de contatos, ideal para lidar com um grande volume de dados de maneira eficiente. Este sistema é perfeito para quem busca rapidez e organização no gerenciamento de suas informações de contato.

---

Espero que você encontre este sistema útil! Se tiver sugestões ou contribuições, sinta-se livre para colaborar. 🌟
