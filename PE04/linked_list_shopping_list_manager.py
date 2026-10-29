"""Shopping list stored as a singly linked list.

New items go on the front, same as the array version. The difference is
in the sort. Instead of building new lists of item names, I move the
actual nodes around and relink them, so nothing gets copied.
"""


class LinkedListShoppingListManagerClass:
    """Keeps track of shopping items with linked nodes.

    Attributes:
        head (_Node): first node in the list, or None if it's empty
        tail (_Node): last node in the list, or None if it's empty.
            Same tail trick I used in PE02. Here it makes joining lists fast.
    """

    class _Node:
        """Holds one item and a link to the next node.

        Attributes:
            data (str): the item
            next (_Node): the next node, or None if this is the last one
        """

        def __init__(self, data: str) -> None:
            """Create a node for one item.

            Args:
                data (str): the item to store
            """
            self.data = data
            self.next = None

    def __init__(self) -> None:
        """Start out with nothing in the list."""
        self.head = None
        self.tail = None

    def insert_item(self, item: str) -> None:
        """Put a new item at the front of the list.

        Nothing has to shift like it does in the array. The new node just
        points at the old first node and becomes the head. That's O(1).

        Args:
            item (str): the item to add
        """
        new_node = self._Node(item)
        # Hook the new node up to the list before moving head,
        # otherwise the rest of the list gets lost
        new_node.next = self.head
        self.head = new_node
        # First item in an empty list is also the last item
        if self.tail is None:
            self.tail = new_node

    def print_items(self) -> None:
        """Show everything in the list like [ item1 item2 ... ]."""
        print("[", end=" ")
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("]")

    def _add_node_to_end(self, node) -> None:
        """Tack an existing node onto the end of this list.

        Only used by the sort. Having the tail means I don't have to walk
        the whole list to find the end.

        Args:
            node (_Node): the node to move here
        """
        node.next = None  # cut it off from wherever it was before
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def _join(self, other) -> None:
        """Attach another list to the end of this one.

        Just one link to change and a new tail, so it's O(1).

        Args:
            other (LinkedListShoppingListManagerClass): the list to attach
        """
        if other.head is None:
            return
        if self.head is None:
            self.head = other.head
        else:
            self.tail.next = other.head
        self.tail = other.tail

    def quick_sort_helper(self, linked_list):
        """Recursive quicksort for a linked list.

        The first item is the pivot. I go through the list one time and
        drop every node into one of three lists: smaller than the pivot,
        the same as the pivot, or bigger. Smaller and bigger get sorted the
        same way, and then the three lists get joined back together.

        I used three lists here instead of two so items that match the
        pivot are done right away and don't get sorted again.

        Like the array version, it's O(n log n) on average, but a list
        that's already in order makes it O(n^2).

        Args:
            linked_list (LinkedListShoppingListManagerClass): the list to sort

        Returns:
            LinkedListShoppingListManagerClass: the same nodes, now in
                alphabetical order
        """
        # 0 or 1 nodes means there's nothing left to sort
        if linked_list.head is None or linked_list.head.next is None:
            return linked_list

        pivot = linked_list.head.data
        smaller = LinkedListShoppingListManagerClass()
        equal = LinkedListShoppingListManagerClass()
        bigger = LinkedListShoppingListManagerClass()

        current = linked_list.head
        while current is not None:
            # Grab the next node first, since moving this one clears its link
            next_node = current.next
            if current.data < pivot:
                smaller._add_node_to_end(current)
            elif current.data == pivot:
                equal._add_node_to_end(current)
            else:
                bigger._add_node_to_end(current)
            current = next_node

        # Sort both sides, then line everything back up: smaller, equal, bigger
        result = self.quick_sort_helper(smaller)
        result._join(equal)
        result._join(self.quick_sort_helper(bigger))
        return result

    def quick_sort(self) -> None:
        """Sort the shopping list and point head and tail at the sorted nodes."""
        sorted_list = self.quick_sort_helper(self)
        self.head = sorted_list.head
        self.tail = sorted_list.tail
