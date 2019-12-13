import pytest

from fixed_queue import FixedQueue, FixedQueueLinkedList

@pytest.fixture
def empty_queue():
    q = FixedQueue(0)

    return q

@pytest.fixture
def new_queue():
    q = FixedQueue(2)

    return q

def test_size(empty_queue, new_queue):
    
    assert(len(new_queue) == 0)
    assert(len(empty_queue) == 0)

    assert(new_queue.getElems() == [None, None])
    assert(empty_queue.getElems() == [])

def test_enqueue():

    q = FixedQueue(3)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert(len(q) == 3)

    with pytest.raises(Exception):
        q.enqueue(4)

def test_dequeue():

    q = FixedQueue(3)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert(q.dequeue() == 1)
    q.enqueue(4)
    assert(q.dequeue() == 2)
    q.enqueue(5)
    assert(q.dequeue() == 3)
    q.enqueue(6)
    assert(q.dequeue() == 4)
    q.enqueue(7)
    assert(q.dequeue() == 5)
    
    assert(len(q) == 2)
    q.dequeue()
    assert(len(q) == 1)
    q.dequeue()
    assert(len(q) == 0)

    with pytest.raises(IndexError):
        q.dequeue()




@pytest.fixture
def empty_queue_linked():
    q = FixedQueueLinkedList(0)

    return q

@pytest.fixture
def new_queue_linked():
    q = FixedQueueLinkedList(2)

    return q

def test_size_linked(empty_queue_linked, new_queue_linked):
    
    assert(len(new_queue_linked) == 0)
    assert(len(empty_queue_linked) == 0)

    # assert(new_queue_linked.getElems() == [None, None])
    # assert(empty_queue_linked.getElems() == [])

def test_enqueue_linked():

    q = FixedQueueLinkedList(3)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert(len(q) == 3)

    with pytest.raises(Exception):
        q.enqueue(4)

def test_dequeue_linked():

    q = FixedQueueLinkedList(3)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert(q.dequeue() == 1)
    q.enqueue(4)
    assert(q.dequeue() == 2)
    q.enqueue(5)
    assert(q.dequeue() == 3)
    q.enqueue(6)
    assert(q.dequeue() == 4)
    q.enqueue(7)
    assert(q.dequeue() == 5)
    
    assert(len(q) == 2)
    q.dequeue()
    assert(len(q) == 1)
    q.dequeue()
    assert(len(q) == 0)

    with pytest.raises(IndexError):
        q.dequeue()



