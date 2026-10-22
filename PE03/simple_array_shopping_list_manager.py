"""simple_array_shopping_list_manager.py

Array version of the shopping list. Python doesn't really have a classic
array for strings, so I'm using a regular list, which works like an array
under the hood. This one only needs to insert and print.
"""


class SimpleArrayShoppingListManagerClass:
    """Shopping list that keeps its items in a Python list.

    Attributes:
        items (list): the shopping items. The newest one is always at index 0.
    """

    def __init__(self) -> None:
        """Start with an empty list."""
        self.items = []

    def insert_item(self, item: str) -> None:
        """Add an item to the front of the list.

        Everything already in the list has to slide over one spot to make
        room, so this gets slower as the list grows. That's O(n).

        Args:
            item (str): name of the item to add
        """
        self.items.insert(0, item)

    def print_items(self) -> None:
        """Print the whole list."""
        print(self.items)
