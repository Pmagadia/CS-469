"""linked_list_stack_shopping_list_manager.py

Stack version of the shopping list, built on a singly linked list.
I'm treating the head of the list as the top of the stack. That way the
last item I add is always the first one I can get back out (LIFO), and
both adding and removing stay O(1) since I never have to walk the list.
Printing is done with recursion, either from the top down or from the
bottom up.
"""


class LinkedListStackShoppingListManagerClass:
    """Shopping list stored as a stack made out of linked nodes.

    Attributes:
        head (_Node): the node on top of the stack, or None when it's empty
    """

    class _Node:
        """One item in the stack.

        I kept this inside the manager class since nothing else needs to
        use it. The underscore is just a reminder that it's internal.

        Attributes:
            data (str): the item name
            next (_Node): the node right below this one, or None at the bottom
        """

        def __init__(self, data: str) -> None:
            """Make a new node for an item.

            Args:
                data (str): the item name to store
            """
            self.data = data
            self.next = None

    def __init__(self) -> None:
        """Start with an empty stack. Nothing on top yet."""
        self.head = None

    def insert_item(self, item: str) -> None:
        """Push an item onto the top of the stack.

        Only the head changes here and nothing has to move, so this is O(1)
        no matter how big the stack gets.

        Args:
            item (str): name of the item to add
        """
        new_node = self._Node(item)
        # Point the new node at the current top first. If I moved head
        # first, I'd lose track of everything underneath.
        new_node.next = self.head
        self.head = new_node

    def is_list_empty(self) -> bool:
        """Check if there's anything in the stack.

        Returns:
            bool: True if it's empty, False if there's at least one item
        """
        return self.head is None

    def print_item_recursive_from_top(self, currentNode) -> None:
        """Helper that prints the stack from the top down, using recursion.

        I print the current item first and then call myself on the next
        node. Since I start at the top, the top item shows up first.

        Every call waits on the call stack until the one after it finishes,
        so a stack with n items uses n calls. That's fine for a shopping
        list, but Python stops at around 1,000 calls with a RecursionError,
        the same error I hit with Fibonacci in HOS03.

        Args:
            currentNode (_Node): the node I'm on right now
        """
        # Base case: I've gone past the bottom, so stop
        if currentNode is None:
            return
        print(currentNode.data, end=" ")
        self.print_item_recursive_from_top(currentNode.next)

    def print_items_from_top(self) -> None:
        """Print the stack as [ top ... bottom ]."""
        print("[", end=" ")
        self.print_item_recursive_from_top(self.head)
        print("]")

    def print_item_recursive_from_bottom(self, currentNode) -> None:
        """Helper that prints the stack from the bottom up, using recursion.

        Same as the top version, except I make the recursive call before
        printing. The calls dive all the way to the bottom first, then each
        one prints on its way back up. So the bottom item comes out first.
        Same limit applies here, around 1,000 items before Python stops it.

        Args:
            currentNode (_Node): the node I'm on right now
        """
        # Base case: I've gone past the bottom, so stop
        if currentNode is None:
            return
        self.print_item_recursive_from_bottom(currentNode.next)
        print(currentNode.data, end=" ")

    def print_items_from_bottom(self) -> None:
        """Print the stack as [ bottom ... top ]."""
        print("[", end=" ")
        self.print_item_recursive_from_bottom(self.head)
        print("]")

    def getLastItem(self):
        """Look at the last item I added without taking it off (peek).

        Returns:
            str: the item on top, or None if the stack is empty
        """
        if self.is_list_empty():
            return None
        return self.head.data

    def removeLastItem(self):
        """Take the last item I added off the stack and return it (pop).

        Returns:
            str: the item that was on top, or None if the stack is empty
        """
        if self.is_list_empty():
            return None
        removed_node = self.head
        self.head = removed_node.next
        # Cut the old top loose so it's not still pointing into the stack
        removed_node.next = None
        return removed_node.data
