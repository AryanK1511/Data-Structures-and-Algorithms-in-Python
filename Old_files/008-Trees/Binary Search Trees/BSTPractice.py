import queue

class BST:
    class Node:
        def __init__(self, value, left = None, right = None):
            self.value = value
            self.left = left
            self.right = right
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self.r_insert(value, self.root)

    def r_insert(self, value, node):
        if node is None:
           return self.Node(value)
        elif value < node.value:
            node.left = self.r_insert(value, node.left)
            return node
        elif value > node.value:
            node.right = self.r_insert(value, node.right)
            return node
        return
    
    def bfs_print(self):
        if self.root is None:
            print([])
            return 
        #BFS Traversal
        popList = []
        nodeList = queue.Queue()
        nodeList.put(self.root)

        while not nodeList.empty():
            currentNode = nodeList.get()
            popList.append(currentNode.value)
            if currentNode.left:
                nodeList.put(currentNode.left)
            if currentNode.right:
                nodeList.put(currentNode.right)

        print(popList)
        
    def inorder_print(self):
        self.rio(self.root)

    def rio(self, node):
        if node:
            self.rio(node.left)
            self.rio(node.right)
            print(node.value)  

    def delete_rec(self, value):
        self.root = self.r_delete(value, self.root)

    def r_delete(self, value, node):
        if node is None:
            return None
        
        # Recursive Binary Search to find the node to be deleted
        if value < node.value:
            node.left = self.r_delete(value, node.left)
        elif value > node.value:
            node.right = self.r_delete(value, node.right)
        else:

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.value = self.min_value_node(node.right).value
            node.right = self.r_delete(node.value, node.right)
            
        return node
    
    def min_value_node(self, node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    # ChatGPT delete
    def delete(self, value):
        # Search value
        curr_node = self.root
        parent_node = None
        found = False
        
        while curr_node and not found:
            if value < curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.left
            elif value > curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.right
            else:
                found = True
        
        if curr_node is None:
            return
        
        # Case 1: Node has no children
        if curr_node.left is None and curr_node.right is None:
            if parent_node is None:
                self.root = None
            elif parent_node.left == curr_node:
                parent_node.left = None
            else:
                parent_node.right = None
            del curr_node
        
        # Case 2: Node has only left child
        elif curr_node.right is None:
            if parent_node is None:
                self.root = curr_node.left
            elif parent_node.left == curr_node:
                parent_node.left = curr_node.left
            else:
                parent_node.right = curr_node.left
            del curr_node
        
        # Case 3: Node has only right child
        elif curr_node.left is None:
            if parent_node is None:
                self.root = curr_node.right
            elif parent_node.left == curr_node:
                parent_node.left = curr_node.right
            else:
                parent_node.right = curr_node.right
            del curr_node
        
        # Case 4: Node has both children
        else:
            parent_successor = curr_node
            successor = curr_node.right
            while successor.left:
                parent_successor = successor
                successor = successor.left

            curr_node.value = successor.value

            if parent_successor.left == successor:
                parent_successor.left = successor.right
            else:
                parent_successor.right = successor.right

            del successor

    def search(self, value):
        return self.r_search(value, self.root)

    def r_search(self, value, node):
        if node is None:
            return None
        
        if value == node.value:
            return node
        elif value < node.value:
            return self.r_search(value, node.left)
        elif value > node.value:
            return self.r_search(value, node.right)

bst = BST()
bst.insert(8)
bst.insert(5)
bst.insert(16)
bst.insert(7)
bst.insert(3)
bst.insert(11)
bst.insert(20)
bst.insert(4)
bst.insert(14)
bst.insert(6)
bst.bfs_print()
bst.delete_rec(5)
bst.delete_rec(8)
bst.delete_rec(7)
bst.delete_rec(20)
bst.delete_rec(11)
bst.delete_rec(14)
bst.delete_rec(6)
bst.delete_rec(3)
bst.delete_rec(16)
bst.delete_rec(4)

print("+++++++++++")
bst.bfs_print()
print("----------------")
