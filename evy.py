class Node():
    """The node class instantiates a new node.
    """

    def __init__(self, value):
        self.value = value
        self._next = None


class Queue:

    front = None
    rear = None

    def enqueue(self, value):
        """
        """
        node = Node(value)

        if not self.front:
            self.head = node
            self.front = node
            self.rear = node
        else:
            # self.rear = current
            current = self.front
            while current._next:
                current = current._next

            current._next = node
            self.rear = current._next

    def dequeue(self):
        """
        """

        if not self.front:
            return 'Queue is empty'
        else:
            temp = self.front
            self.front = temp._next
            temp._next = None

        return temp.value

# ================Tests===================
def test_enqueue_one():
    line = Queue()
    line.enqueue('Pam')

    assert line.rear.value == 'Pam'


def test_enqueue_two():
    """Can successfully enqueue items.
    """
    line = Queue()
    line.enqueue('Pam')
    line.enqueue('Jim')

    assert line.rear.value == 'Jim'


def test_one_dequeue():
    """Can successfully dequeue an item.
    """
    import pdb; pdb.set_trace()
    line = Queue()
    line.enqueue('Pam')
    line.enqueue('Jim')
    line.enqueue('Dwight')

    expected = 'Pam'
    actual = line.dequeue()

    assert expected == actual