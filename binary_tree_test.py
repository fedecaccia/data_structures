import pytest

from binary_tree import Node, Queue, Stack, BinaryTree


def test_queue():

    q = Queue()

    assert(q.is_empty() == True)    
    assert(len(q) == 0)

    q.enqueue(Node(0))
    q.enqueue(Node(1))
    q.enqueue(Node(2))
    q.enqueue(Node(3))

    assert(q.is_empty() == False)
    assert(len(q) == 4)
    assert(q.peek() == 0)

    v = q.dequeue()

    assert(v.value == 0)
    assert(len(q) == 3)

def test_stack():

    s = Stack()

    assert(s.is_empty() == True)    
    assert(len(s) == 0)

    s.push(Node(0))
    s.push(Node(1))
    s.push(Node(2))
    s.push(Node(3))

    assert(s.is_empty() == False)
    assert(len(s) == 4)
    assert(s.peek() == 3)

    v = s.pop()

    assert(v.value == 3)
    assert(len(s) == 3)

@pytest.fixture
def tree():
    """
            1
        2      3
    4     5  6    7
                    8
    """

    t = BinaryTree(1)
    t.root.left = Node(2)
    t.root.right = Node(3)
    t.root.left.left = Node(4)
    t.root.left.right = Node(5)
    t.root.right.left = Node(6)
    t.root.right.right = Node(7)
    t.root.right.right.right = Node(8)

    return t

@pytest.fixture
def another_tree():
    """
            1
        2      3
    4     5       6
        7   8   9
    """

    t = BinaryTree(1)
    t.root.left = Node(2)
    t.root.right = Node(3)
    t.root.left.left = Node(4)
    t.root.left.right = Node(5)
    t.root.right.right = Node(6)
    t.root.left.right.left = Node(7)
    t.root.left.right.right = Node(8)
    t.root.right.right.left = Node(9)

    return t


def test_preorder_traversal(tree, another_tree):    
    assert(tree.print_tree("preorder") == "1 - 2 - 4 - 5 - 3 - 6 - 7 - 8 - ")
    assert(another_tree.print_tree("preorder") == "1 - 2 - 4 - 5 - 7 - 8 - 3 - 6 - 9 - ")

def test_inorder_traversal(tree, another_tree):    
    assert(tree.print_tree("inorder") == "4 - 2 - 5 - 1 - 6 - 3 - 7 - 8 - ")
    assert(another_tree.print_tree("inorder") == "4 - 2 - 7 - 5 - 8 - 1 - 3 - 9 - 6 - ")

def test_postorder_traversal(tree, another_tree):    
    assert(tree.print_tree("postorder") == "4 - 5 - 2 - 6 - 8 - 7 - 3 - 1 - ")
    assert(another_tree.print_tree("postorder") == "4 - 7 - 8 - 5 - 2 - 9 - 6 - 3 - 1 - ")

def test_levelorder_traversal(tree, another_tree):    
    assert(tree.print_tree("levelorder") == "1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - ")
    assert(another_tree.print_tree("levelorder") == "1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - ")

def test_reverse_levelorder_traversal(tree, another_tree):    
    assert(tree.print_tree("reverse levelorder") == "8 - 4 - 5 - 6 - 7 - 2 - 3 - 1 - ")
    assert(another_tree.print_tree("reverse levelorder") == "7 - 8 - 9 - 4 - 5 - 6 - 2 - 3 - 1 - ")

def test_root_height(tree, another_tree):    
    assert(tree.height(tree.root) == 4)
    assert(another_tree.height(another_tree.root) == 4)

def test_node_height(tree, another_tree):    
    assert(tree.height(tree.root) == 4)
    assert(tree.height(tree.root.right) == 3)
    assert(another_tree.height(another_tree.root.left.left) == 1)
    assert(another_tree.height(another_tree.root.left.right) == 2)

def test_node_height_recursive(tree, another_tree):    
    assert(tree.height_recursive(tree.root) == 4)
    assert(tree.height_recursive(tree.root.right) == 3)
    assert(another_tree.height_recursive(another_tree.root.left.left) == 1)
    assert(another_tree.height_recursive(another_tree.root.left.right) == 2)


def test_size(tree, another_tree):
    assert(tree.size() == 8)
    assert(another_tree.size() == 9)

def test_size_recursive(tree, another_tree):
    assert(tree.size_recursive(tree.root) == 8)
    assert(another_tree.size_recursive(another_tree.root) == 9)

