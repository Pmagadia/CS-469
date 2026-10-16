"""simple_array_shopping_list_manager.py

Contains the SimpleArrayShoppingListManagerClass, which stores shopping
items in a simple array and supports insert, delete, lookup, print, and
selection sort operations.

Python does not have a classic fixed-size array for strings. Its built-in
list works as a dynamic array, so it is used here.
"""


class SimpleArrayShoppingListManagerClass:
    """Manage a shopping list stored in a simple array (Python list).

    Attributes:
        items (list): The shopping items, with the newest item at the front.
    """

    def __init__(self):
        """Initialize an empty array to hold shopping items."""
        self.items = []

    def __len__(self):
        """Return the number of items in the array."""
        return len(self.items)

    def insert_item(self, item):
        """Insert an item at the front of the array.

        Every existing item has to shift one position to the right,
        so this is O(n).

        Args:
            item (str): The name of the item to add.
        """
        self.items.insert(0, item)

    def print_items(self):
        """Print all items in the array."""
        print(self.items)

    def delete_item(self, item):
        """Delete the first occurrence of an item from the array.

        Uses index() to find the position and pop() to remove it, instead
        of remove(). index() scans the list once; checking "item in list"
        first would scan it twice. Every item after the deleted one shifts
        left, so this is O(n).

        Args:
            item (str): The name of the item to delete.

        Returns:
            bool: True if the item was found and deleted, False otherwise.
        """
        try:
            position = self.items.index(item)
        except ValueError:
            # index() raises ValueError when the item is not in the list
            return False
        self.items.pop(position)
        return True

    def get_last_item(self):
        """Return the last item in the array.

        An array can jump straight to any index, so this is O(1).

        Returns:
            str: The last item, or None if the array is empty.
        """
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def selection_sort(self):
        """Sort the items alphabetically (a to z) using selection sort.

        For each position, find the smallest item in the unsorted part and
        swap it into that position. Sorting happens in place by swapping,
        rather than building a new list with pop(), so the original array is
        replaced by the sorted result. Time complexity is O(n^2); space is O(1).
        """
        for i in range(len(self.items)):
            # Assume the first unsorted item is the smallest
            smallest_index = i
            # Look through the rest of the unsorted part for a smaller item
            for j in range(i + 1, len(self.items)):
                if self.items[j] < self.items[smallest_index]:
                    smallest_index = j
            # Swap the smallest item into position i (always safe, even if
            # i == smallest_index, so no "if" check is needed)
            self.items[i], self.items[smallest_index] = (
                self.items[smallest_index],
                self.items[i],
            )
