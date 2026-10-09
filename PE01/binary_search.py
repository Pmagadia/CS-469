"""binary_search.py

Contains the BinarySearchClass, which finds an item in a sorted list by
repeatedly checking the middle element and discarding half of the list.
"""


class BinarySearchClass:
    """Search an alphabetically sorted list of names using binary search.

    Attributes:
        array (list): The sorted list of names to search through.
    """

    def __init__(self, array):
        """Initialize the search object with a sorted list of names.

        Args:
            array (list): The alphabetically sorted list of names (name_list).
        """
        self.array = array

    def binary_search(self, searching_item):
        """Find the index of searching_item by halving the search range each step.

        The list must already be sorted alphabetically for this to work.

        Args:
            searching_item (str): The name to look for.

        Returns:
            int: The index of searching_item in the list,
            or None if the name is not in the list.

        Time complexity: O(log n), since each comparison removes half
        of the remaining elements.
        """
        # Start with the whole list: low is the first index, high is the last
        low = 0
        high = len(self.array) - 1

        # Keep searching while there is at least one element left in range
        while low <= high:
            # Find the middle index (floor division keeps it an integer)
            mid = (low + high) // 2
            guess = self.array[mid]

            if guess == searching_item:
                # Found the name
                return mid
            if guess > searching_item:
                # The middle name comes after the target alphabetically,
                # so the target must be in the left half
                high = mid - 1
            else:
                # The middle name comes before the target alphabetically,
                # so the target must be in the right half
                low = mid + 1

        # The range is empty, so the name is not in the list
        return None