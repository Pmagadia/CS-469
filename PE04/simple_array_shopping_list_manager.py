"""Shopping list stored in a plain Python list.

Python lists act like arrays, so that's what I'm using for the "array"
side. Every new item goes in at the front. For sorting I went with the
quicksort from this week's reading, the version that splits the list
into two new lists around a pivot.
"""


class SimpleArrayShoppingListManagerClass:
    """Keeps track of shopping items in a list.

    Attributes:
        items (list): the shopping items, newest one first
    """

    def __init__(self) -> None:
        """Set up an empty list for the items."""
        self.items = []

    def insert_item(self, item: str) -> None:
        """Put a new item at the front of the list.

        insert(0, ...) makes every item behind it shift down one spot, so
        the bigger the list gets, the more work this takes. That's O(n).

        Args:
            item (str): the item to add
        """
        self.items.insert(0, item)

    def print_items(self) -> None:
        """Show everything in the list."""
        print(self.items)

    def quick_sort_helper(self, array: list) -> list:
        """Recursive quicksort that hands back a sorted copy of the list.

        The first item is the pivot. Everything that comes before it
        alphabetically (or matches it) goes in one list, and everything
        after it goes in another. Then I call this same method on both
        lists and glue the results back together with the pivot in the
        middle.

        This is O(n log n) most of the time. The catch is a list that's
        already in order. Then the pivot is always the smallest item, one
        side is always empty, and it drops to O(n^2). I saw that happen
        with the quicksort in HOS04.

        Args:
            array (list): the items that still need sorting

        Returns:
            list: the same items, in alphabetical order
        """
        # 0 or 1 items means there's nothing left to sort
        if len(array) < 2:
            return array

        pivot = array[0]
        smaller = [item for item in array[1:] if item <= pivot]
        bigger = [item for item in array[1:] if item > pivot]

        return self.quick_sort_helper(smaller) + [pivot] + self.quick_sort_helper(bigger)

    def quick_sort(self) -> None:
        """Sort the shopping list and swap in the sorted version."""
        self.items = self.quick_sort_helper(self.items)
