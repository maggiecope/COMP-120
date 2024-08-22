
from agenda import StackAgenda, QueueAgenda, AgendaEmpty
# Write your pytest test case functions for your StackAgenda and QueueAgenda
# classes below this line.

def test_stack_agenda():
    test = StackAgenda()
    assert test.is_empty() == True

    test.add(6)
    assert test.size() == 1

    test.remove()
    assert test.size == 0 

    test.add(3)
    test.add(5)
    assert test.next() == 5

def test_queue_agenda():
    test = QueueAgenda()
    assert test.is_empty() == True

    test.add(6)
    assert test.size() == 1
    assert test.is_empty == False

    test.remove()
    assert test.size == 0 

    test.add(3)
    test.add(5)
    assert test.next() == 5