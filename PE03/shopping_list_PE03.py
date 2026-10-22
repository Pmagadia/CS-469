"""shopping_list_PE03.py

Stacks and recursion with a shopping list.

I'm storing the same shopping items two ways, once in a simple array and
once in a stack built on a linked list. The array code is in
simple_array_shopping_list_manager.py and the stack code is in
linked_list_stack_shopping_list_manager.py. This file runs both and times
the insert so I can compare them.
"""

import time

from simple_array_shopping_list_manager import SimpleArrayShoppingListManagerClass
from linked_list_stack_shopping_list_manager import LinkedListStackShoppingListManagerClass

item_list = [
    "apple", "banana", "milk", "bread", "butter", "cheese",
    "carrot", "pork", "beef", "mushroom", "fish",
]


def main() -> None:
    """Test the array and the stack, then print how long the inserts took."""

    # ---------- Simple array ----------
    print("------ Simple array ------")
    shopping_array = SimpleArrayShoppingListManagerClass()

    # Time how long it takes to add every item to the array
    start = time.perf_counter()
    for item in item_list:
        shopping_array.insert_item(item)
    array_insert_time = time.perf_counter() - start

    print("current list:\t", end=" ")
    shopping_array.print_items()
    print("-insert operation: %s\n\n" % array_insert_time)

    # ---------- Linked-list stack ----------
    print("------ Linked-List-Stack ------")
    shopping_stack = LinkedListStackShoppingListManagerClass()

    # Same thing for the stack: push every item and time it
    start = time.perf_counter()
    for item in item_list:
        shopping_stack.insert_item(item)
    stack_insert_time = time.perf_counter() - start

    print("current list:\t", end=" ")
    shopping_stack.print_items_from_bottom()

    # Peek at the top, the stack shouldn't change
    print("last inserted item:\t%s" % shopping_stack.getLastItem())
    print("current list:\t", end=" ")
    shopping_stack.print_items_from_bottom()

    # Pop the top, fish should be gone after this
    print("last removed item:\t%s" % shopping_stack.removeLastItem())
    print("current list:\t", end=" ")
    shopping_stack.print_items_from_bottom()

    # Print it the other way around, starting from the top
    print("current list from top:\t", end=" ")
    shopping_stack.print_items_from_top()

    print("-insert operation: %s" % stack_insert_time)


if __name__ == "__main__":
    main()
