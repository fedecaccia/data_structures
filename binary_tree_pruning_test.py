import pytest

from binary_tree import Node
from binary_tree_pruning import BinaryTreePruning


@pytest.fixture
def tree0():
    t = BinaryTreePruning(0)
    t.root.left = Node(0)
    t.root.right = Node(1)

    return t

@pytest.fixture
def tree1():
    t = BinaryTreePruning(0)
    t.root.left = Node(0)
    t.root.left.left = Node(1)
    t.root.left.right = Node(1)
    t.root.right = Node(0)
    t.root.right.left = Node(1)
    t.root.right.right = Node(1)

    return t

@pytest.fixture
def tree2():
    t = BinaryTreePruning(0)
    t.root.left = Node(0)
    t.root.left.left = Node(0)
    t.root.left.right = Node(1)
    t.root.right = Node(0)
    t.root.right.left = Node(0)
    t.root.right.right = Node(0)

    return t

@pytest.fixture
def tree3():
    t = BinaryTreePruning(0)
    t.root.left = Node(0)
    t.root.left.left = Node(0)
    t.root.left.right = Node(0)
    t.root.right = Node(0)
    t.root.right.left = Node(0)
    t.root.right.right = Node(0)

    return t

def test_tree_with_wrong_values():
    with pytest.raises(ValueError):
        BinaryTreePruning(8)

def test_pruning(tree0, tree1, tree2, tree3):
    
    tree0.prune()
    assert(tree0.print_tree("levelorder") == "0 - 1 - ")
    assert(tree0.size() == 2)

    tree1.prune()
    assert(tree1.print_tree("levelorder") == "0 - 0 - 0 - 1 - 1 - 1 - 1 - ")
    assert(tree1.size() == 7)

    tree2.prune()
    assert(tree2.print_tree("levelorder") == "0 - 0 - 1 - ")
    assert(tree2.size() == 3)

    tree3.prune()
    assert(tree3.print_tree("levelorder") == "")
    assert(tree3.size() == 0)