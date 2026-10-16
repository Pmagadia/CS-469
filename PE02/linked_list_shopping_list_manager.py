"""linked_list_shopping_list_manager.py

Contains the LinkedListShoppingListManagerClass, which stores shopping
items in a singly linked list and supports insert, delete, lookup,
print, find smallest, and selection sort operations.
"""


class LinkedListShoppingListManagerClass:
    """Manage a shopping list stored in a singly linked list.

    Attributes:
        head (_Node): The first node in the list, or None if the list is empty.
        tail (_Node): The last node in the list, or None if the list is empty.
        size (int): The number of items currently in the list.
    """

    class _Node:
        """A single node in the linked list (nonpublic inner class).

        The leading underscore marks it as an internal detail of the
        manager class. __slots__ saves memory, since a list can hold
        many nodes.

        Attributes:
            data (str): The item name stored in this node.
            next (_Node): The next node, or None if this is the last node.
        """

        __slots__ = "data", "next"

        def __init__(self, data):
            """Create a node holding an item name.

            Args:
                data (str): The item name to store.
            """
            self.data = data
            self.next = None

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """Return the number of items in O(1) time, using the stored size."""
        return self.size

    def insert_item(self, item):
        """Insert an item at the front of the linked list.

        Only the head pointer changes and nothing has to shift, so this is O(1).

        Args:
            item (str): The name of the item to add.
        """
        new_node = self._Node(item)
        # Order matters: link the new node to the old head BEFORE moving
        # the head, or the rest of the list would be lost.
        new_node.next = self.head
        self.head = new_node
        # If the list was empty, the new node is also the last node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def print_items(self):
        """Print all items in the format [ item1 item2 ... ]."""
        print("[", end=" ")
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print("]")

    def delete_item(self, item):
        """Delete the first node that holds the given item.

        Finding the item means walking from the head, so this is O(n).
        Once found, removing it is a single pointer change, which is O(1).

        Args:
            item (str): The name of the item to delete.

        Returns:
            bool: True if the item was found and deleted, False otherwise.
        """
        prev = None
        cur = self.head

        while cur is not None:
            if cur.data == item:
                if prev is None:
                    # Deleting the head: the next node becomes the new head
                    self.head = cur.next
                else:
                    # Skip over the current node to remove it from the chain
                    prev.next = cur.next
                # If we deleted the last node, the previous node is the new tail
                # (or None if the list is now empty)
                if cur is self.tail:
                    self.tail = prev
                self.size -= 1
                return True
            prev, cur = cur, cur.next

        return False

    def get_last_item(self):
        """Return the last item in the linked list.

        Without a tail pointer, this would have to follow every pointer
        from the head to the end, which is O(n). Because the list keeps a
        tail reference, it can return the last item directly in O(1).

        Returns:
            str: The last item, or None if the list is empty.
        """
        if self.tail is None:
            return None
        return self.tail.data

    def find_smallest(self, linked_list=None):
        """Return the smallest (alphabetically first) item in a linked list.

        Args:
            linked_list (LinkedListShoppingListManagerClass, optional):
                The linked list to search. Defaults to this list, so
                ll.find_smallest() searches ll itself.

        Returns:
            str: The smallest item, or None if the list is empty.
        """
        if linked_list is None:
            linked_list = self
        smallest_node = self._find_smallest_node(linked_list.head)
        if smallest_node is None:
            return None
        return smallest_node.data

    def _find_smallest_node(self, node):
        """Return the node holding the smallest item from node to the end.

        Helper method used by find_smallest() and selection_sort().

        Args:
            node (_Node): The node to start searching from.

        Returns:
            _Node: The node with the smallest item, or None if node is None.
        """
        if node is None:
            return None
        smallest_node = node
        cur = node.next
        while cur is not None:
            if cur.data < smallest_node.data:
                smallest_node = cur
            cur = cur.next
        return smallest_node

    def selection_sort(self):
        """Sort the linked list alphabetically (a to z) using selection sort.

        (Challenge question.) For each node, find the smallest node from
        there to the end and swap their data in place. The nodes themselves
        never move, so head and tail stay valid. Time complexity is O(n^2).
        """
        cur = self.head
        while cur is not None:
            smallest_node = self._find_smallest_node(cur)
            # Swap the data so the smallest item moves into the current node
            cur.data, smallest_node.data = smallest_node.data, cur.data
            cur = cur.next
