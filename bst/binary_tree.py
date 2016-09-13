'''This is the code for balanced binary search tree using AVL trees
This code is inspired by interactivepython website with some modifications
This implementation does not have delete option.'''


class node:
    def __init__(self,key,data,left=None,right=None,parent=None,hfactor=0):
        self.key=key
        self.data=data
        self.hfactor=hfactor
        self.left=left
        self.right=right
        self.parent=parent

    def hasleft(self):
        return self.left

    def hasright(self):
        return self.right

    def isleft(self):
        return self.parent and self.parent.left == self

    def isright(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def __iter__(self):
        if self:
            if self.hasleft():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.hasright():
                for elem in self.right:
                    yield elem



class binary_search_tree:

    def construct_binary_tree(self,array):
        for element,value in array:
            self.insert(element,value)

    def __init__(self,array):
        self.root=None
        self.size=0
        self.construct_binary_tree(array)

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def __iter__(self):
        return  self.root.__iter__()

    def insert(self,key,data):
        if self.root:
            self._insert(key, data, self.root)
            self.size = self.size + 1
        else:
            self.root = node(key, data)
            self.size = self.size + 1



    def _insert(self,key,data,currentNode):
        if key < currentNode.key:
            if currentNode.hasleft():
                self._insert(key, data, currentNode.left)
            else:
                currentNode.left = node(key, data, parent=currentNode)
                self.updateBalance(currentNode.left)
        else:
            if currentNode.hasright():
                self._insert(key, data, currentNode.right)
            else:
                currentNode.right = node(key, data, parent=currentNode)
                self.updateBalance(currentNode.right)

    def updateBalance(self, node):
        if node.hfactor > 1 or node.hfactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isleft():
                node.parent.hfactor += 1
            elif node.isright():
                node.parent.hfactor -= 1

            if node.parent.hfactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.right
        rotRoot.right = newRoot.left
        if newRoot.left != None:
            newRoot.left.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isleft():
                rotRoot.parent.left = newRoot
            else:
                rotRoot.parent.right = newRoot
        newRoot.left = rotRoot
        rotRoot.parent = newRoot
        rotRoot.hfactor = rotRoot.hfactor + 1 - min(newRoot.hfactor, 0)
        newRoot.hfactor = newRoot.hfactor + 1 + max(rotRoot.hfactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.left
        rotRoot.left = newRoot.right
        if newRoot.right != None:
            newRoot.right.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isleft():
                rotRoot.parent.left = newRoot
            else:
                rotRoot.parent.right = newRoot
        newRoot.right = rotRoot
        rotRoot.parent = newRoot
        rotRoot.hfactor = rotRoot.hfactor - 1 - max(newRoot.hfactor, 0)
        newRoot.hfactor = newRoot.hfactor + 1 - min(rotRoot.hfactor, 0)

    def rebalance(self, node):
        if node.hfactor < 0:
            if node.right.hfactor > 0:
                self.rotateRight(node.right)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.hfactor > 0:
            if node.left.hfactor < 0:
                self.rotateLeft(node.left)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def __setitem__(self, k, v):
        self.insert(k, v)

    def __getitem__(self, item):
        return self.search(self,item)



    def findSuccessor(self,currentNode):
        succ = None
        if currentNode.hasright():
            succ = self.findMin(currentNode.right)
            return succ
        else:
            parent = currentNode.parent
            while parent != None:
                if parent.left == node:
                        break
                currentNode = parent
                parent = currentNode.parent
                return parent

    def findMin(self,current):
        while current.hasleft():
            current = current.left
        return current

    def search(self,key):
        if self.root:
            res = self._search(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _search(self,key,current_node):
        if current_node.key==key:
            return current_node
        if key < current_node.key:
            if current_node.hasleft():
                return self._search(key,current_node.left)
            else:
                return None

        else:
            if current_node.hasright():
                return self._search(key,current_node.right)
            else:
                return  None

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False


mytree = binary_search_tree([(-1,10),(-3,11),(2,5),(3,7),(1,8),(5,10),(11,22),(22,33)])


print mytree.root.key
sorted_list=[]
for x in mytree.root:
    sorted_list.append(x)
print sorted_list







