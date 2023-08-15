import queue

class BST:
    class Node:
        def __init__(self, data = None, left = None, right = None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            curr = self.root
            inserted = False

            while not inserted:
                if data < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = self.Node(data)
                        inserted = True
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = self.Node(data)
                        inserted = True

    def search(self, data):
        curr = self.root
        while curr is not None:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr
        return None

    def r_search(self, data, subtree):
        if subtree is None:
            return None
        else:
            if data < subtree.data:
                return self.r_search(data, subtree.left)
            elif data > subtree.data:
                return self.r_search(data, subtree.right)
            else:
                return subtree

    def search_recursive(self, data):
        return self.r_search(data, self.root)

    def r_insert(self, data, subtree):
        if subtree is None:
            return self.Node(data)
        else:
            if data < subtree.data:
                subtree.left = self.r_insert(data, subtree.left)
                return subtree
            else:
                subtree.right = self.r_insert(data, subtree.right)
                return subtree

    def insert_recursive(self, data):
        self.r_insert(data, self.root)

    def inorder_print(self, subtree):
        if subtree is not None:
            self.inorder_print(subtree.left)
            print(subtree.data, end=" ")
            self.inorder_print(subtree.right)

    def pre_order_print(self, subtree):
        if subtree is not None:
            print(subtree.data, end=" ")
            self.pre_order_print(subtree.left)
            self.pre_order_print(subtree.right)

    def post_order_print(self, subtree):
        if subtree is not None:
            self.post_order_print(subtree.left)
            self.post_order_print(subtree.right)
            print(subtree.data, end=" ")

    def iterative_in_order_print(self):
        stack = []
        curr = self.root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.data, end = " ")
            curr = curr.right

    def iterative_pre_order_print(self):
        stack = [self.root]
        while stack:
            curr = stack.pop()
            if curr:
                print(curr.data, end = " ")
                stack.append(curr.right)
                stack.append(curr.left)

    def iterative_post_order_print(self):
        stack1 = [self.root]
        stack2 = []
        while stack1:
            curr = stack1.pop()
            if curr:
                stack2.append(curr)
                stack1.append(curr.left)
                stack1.append(curr.right)
        while stack2:
            print(stack2.pop().data, end = " ")

    def print(self):
        print("In order")
        self.inorder_print(self.root)
        print()
        self.iterative_in_order_print()
        print()
        print("Pre order")
        self.pre_order_print(self.root)
        print()
        self.iterative_pre_order_print()
        print()
        print("Post order")
        self.post_order_print(self.root)
        print()
        self.iterative_post_order_print()
        print()

    def breadthfirst_print(self):
        nodes_to_visit = queue.Queue()
        nodes_to_visit.put(self.root)
        while not nodes_to_visit.empty():
            curr_node = nodes_to_visit.get()
            if curr_node.left:
                nodes_to_visit.put(curr_node.left)
            if curr_node.right:
                nodes_to_visit.put(curr_node.right)
            print(curr_node.data, end=" ")

# Create an instance of the BST class
bst = BST()

# Insert elements into the BST
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)
bst.insert_recursive(20)
bst.insert_recursive(2)
bst.insert_recursive(14)

# Test the breadthfirst_print method
print("Breadth-First Traversal:")
bst.breadthfirst_print()
print()
print(bst.search(15))
print(bst.search_recursive(15))
bst.print()