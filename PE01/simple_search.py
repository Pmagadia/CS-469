"""simple_search.py

Contains the SimpleSearchClass, which finds an item in a list by
checking each element one at a time from the start (simple / linear search).
"""


class SimpleSearchClass:
    """Search a list of names using simple (linear) search.

    Attributes:
        array (list): The list of names to search through.
    """

    def __init__(self, array):
        """Initialize the search object with a list of names.

        Args:
            array (list): The list of names (name_list) to search.
        """
        self.array = array

    def simple_search(self, searching_item):
        """Find the index of searching_item by checking every element in order.

        Python's built-in index() method is intentionally not used so the
        search logic is written out by hand.

        Args:
            searching_item (str): The name to look for.

        Returns:
            int: The index of searching_item in the list,
            or None if the name is not in the list.

        Time complexity: O(n), since in the worst case every element is checked.
        """
        # Walk through the list from the first element to the last
        for i in range(len(self.array)):
            # Stop as soon as the current element matches the name
            if self.array[i] == searching_item:
                return i
        # The name was not found anywhere in the list
        return None