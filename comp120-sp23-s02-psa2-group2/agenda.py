from abc import ABC, abstractmethod
from typing import Any
from comp120 import Stack, Queue


class AgendaEmpty(Exception):
    """Error to indicate that an item has been requested when a structure
    (e.g. stack or queue) is empty."""
    
    pass

class Agenda(ABC):
    """Parent/base class for all classes that will implement the Agenda ADT.

    DO NOT MODIFY THIS CLASS IN ANY WAY."""

    @abstractmethod
    def add(self, item: Any) -> None:
        """Adds an item to the agenda."""
        return

    @abstractmethod
    def remove(self) -> Any:
        """Removes and returns an next item on the agenda."""
        return

    @abstractmethod
    def next(self) -> Any:
        """Returns an next item on the agenda."""
        return

    @abstractmethod
    def size(self) -> int:
        """Returns the number of items on the agenda."""
        return 0

    @abstractmethod
    def is_empty(self) -> bool:
        """Returns True if the agenda has no items, and False otherwise."""
        return False


# Write your StackAgenda and QueueAgenda classes below this line.
# Both of these classes should inherit from the Agenda class, which
# is defined above.
 
class StackAgenda(Agenda):

    _items: list[Any]

    def __init__(self):
        self._items = Stack()
    
    def add(self,item):
        self._items.push(item)

    def remove(self):
        if self.is_empty():
            raise AgendaEmpty()
        
        return self._items.pop()

    def next(self):
        if self.is_empty():
                raise AgendaEmpty()

        return self._items.peek()
    
    def size(self):
        return self._items.size()

    def is_empty(self):
        return self._items.is_empty() 



class QueueAgenda(Agenda):


    def __init__(self):
        self._items= Queue()

    def add(self,item):
        self._items.enqueue(item)
    
    def remove(self):
        if self.is_empty():
            raise AgendaEmpty()
            
        return self._items.dequeue()

    def next(self):
        if self.is_empty() == True:
            raise AgendaEmpty()

        return self._items.first()

    def size(self):
        return self._items.size()

    def is_empty(self):
        return self._items.size()==0

     

