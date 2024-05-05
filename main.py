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
        self.contacts = None  # Head da lista encadeada
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
            root = AVLNode(name[0].upper())
            root.contacts = ListNode(name, phone)
            return root

        if name[0].upper() < root.initial:
            root.left = self.insert(root.left, name, phone)
        elif name[0].upper() > root.initial:
            root.right = self.insert(root.right, name, phone)
        else:
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
            return root

        self.update_height(root)
        balance = self.get_balance(root)

        # Balance the node if necessary
        if balance > 1 and name[0].upper() < root.left.initial:
            return self.rotate_right(root)
        if balance < -1 and name[0].upper() > root.right.initial:
            return self.rotate_left(root)
        if balance > 1 and name[0].upper() > root.left.initial:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and name[0].upper() < root.right.initial:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

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

# Exemplo de uso:
avl = AVLTree()
contatos = [
    ("Amanda Ferreira", "(11) 99234-5678"),
    ("Ana Souza", "(85) 54321-9876"),
    ("Pedro Alves", "(21) 23456-7890"),
    ("Paulo Lima", "(47) 98765-4321"),
    ("Beatriz Santos", "(31) 87654-3210"),
    ("Beto Gonçalves", "(11) 56789-0123"),
    ("Carlos Prado", "(47) 23456-7890"),
    ("Daniela Moraes", "(85) 34567-8901"),
    ("Eduardo Campos", "(21) 45678-9123"),
    ("Elisa Soares", "(31) 12345-6789")
]

for nome, telefone in contatos:
    avl.root = avl.insert(avl.root, nome, telefone)

print("Todos os contatos:")
for nome, telefone in avl.list_contacts():
    print(f"{nome}: {telefone}")
