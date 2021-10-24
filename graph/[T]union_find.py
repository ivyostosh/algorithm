"""
Union Find

- Use Cases:
    - Check the connectivity of a graph
    - Find quick merge of two sets ?

- Complexity:
    - Time: union O(1), find O(1) ?
    - Space: O(n)

"""

class UnionFind:

    def __init__(self):
        self.father = {}
        self.size_of_set = {}
        self.num_of_set = 0

    def add(self, x):
        # If the point has appeared, return
        if x in self.father:
            return
        
        # Initialize the father to be none, and increment counters by 1
        self.father[x] = None
        self.num_of_set += 1
        self.size_of_set += 1

    def find(self, x):

        # Find the source root
        root = x
        while self.father[root]:
            root = self.father[root]

        # Point all nodes from x to root to root directly
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root

    def merge(self, x, y):
        # Find the root of two nodes
        root_x, root_y = self.find(x), self.find(y)

        # If the roots are not the same, connect them.
        if root_x != root_y:
            # Convert one root to the new root, decrease set by 1, and merge sets.
            self.father[root_x] = root_y
            self.num_of_set -= 1
            self.size_of_set[y] += self.size_of_set[x]
    
    def is_connected(self, x, y):
        # If the roots are the same, they are connected
        return self.find(x) == self.find(y)

    def get_num_of_set(self):
        return self.num_of_set

    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]
    
