class ListNode:
    """Classe para os nós da lista encadeada que armazena cada contato."""
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class AVLNode:
    """Classe para os nós da Árvore AVL. Cada nó armazena uma letra e uma lista de contatos."""
    def __init__(self, initial):
        self.initial = initial
        self.contacts = None  # Ponteiro inicial para a lista encadeada
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """Classe para a Árvore AVL que organiza os AVLNodes."""
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, name, phone):
        if not root:
            node = AVLNode(name[0].upper())
            node.contacts = ListNode(name, phone)  # Criar a lista encadeada com o primeiro contato
            return node

        if name[0].upper() < root.initial:
            root.left = self.insert(root.left, name, phone)
        elif name[0].upper() > root.initial:
            root.right = self.insert(root.right, name, phone)
        else:
            self.insert_in_linked_list(root, name, phone)

        root = self.balance(root)
        return root

    def insert_in_linked_list(self, root, name, phone):
        current = root.contacts
        prev = None
        while current and current.name < name:
            prev = current
            current = current.next
        new_node = ListNode(name, phone)
        if prev:
            prev.next = new_node
        else:
            root.contacts = new_node
        new_node.next = current

    def balance(self, node):
        self.update_height(node)
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def find(self, root, name):
        if not root:
            return None
        if name[0].upper() < root.initial:
            return self.find(root.left, name)
        elif name[0].upper() > root.initial:
            return self.find(root.right, name)
        else:
            return self.search_in_linked_list(root.contacts, name)

    def search_in_linked_list(self, contacts, name):
        current = contacts
        while current:
            if current.name == name:
                return current.phone
            current = current.next
        return None

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            contact = node.contacts
            while contact:
                result.append((contact.name, contact.phone))
                contact = contact.next
            self.inorder_traversal(node.right, result)

    def list_contacts(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result

def main_menu(avl):
    while True:
        print("\n📖 Sistema de Gerenciamento de Contatos")
        print("1. Inserir novo contato")
        print("2. Buscar contato")
        print("3. Listar todos os contatos")
        print("4. Exibir informações do sistema")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Digite o nome do contato: ")
            phone = input("Digite o telefone do contato: ")
            avl.root = avl.insert(avl.root, name, phone)
            print("Contato inserido com sucesso!")
        elif choice == '2':
            name = input("Digite o nome do contato para buscar: ")
            result = avl.find(avl.root, name)
            if result:
                print(f"Telefone: {result}")
            else:
                print("Contato não encontrado.")
        elif choice == '3':
            print("Todos os contatos:")
            for nome, telefone in avl.list_contacts():
                print(f"{nome}: {telefone}")
        elif choice == '4':
            print("\n🌳 Informações do Sistema 🌳")
            print("""
Este sistema utiliza uma Árvore AVL para organizar os contatos pelas iniciais dos seus nomes,
permitindo operações eficientes com tempo logarítmico. Cada nó na árvore representa uma letra do alfabeto,
e as listas encadeadas associadas armazenam os contatos que compartilham a mesma inicial.

Funcionalidades:
- Inserção: Adiciona contatos de maneira ordenada e balanceada.
- Busca: Procura contatos pelo nome, começando pela inicial na árvore.
- Listagem: Exibe todos os contatos em ordem alfabética através de uma travessia in-order.
""")
        elif choice == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    avl = AVLTree()
    main_menu(avl)
