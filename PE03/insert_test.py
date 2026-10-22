"""insert_test.py

Quick test to see how insert holds up on a big list (50,000 items).
"""

import time

from simple_array_shopping_list_manager import SimpleArrayShoppingListManagerClass
from linked_list_stack_shopping_list_manager import LinkedListStackShoppingListManagerClass

for manager_class in (SimpleArrayShoppingListManagerClass, LinkedListStackShoppingListManagerClass):
    shopping_list = manager_class()
    start = time.perf_counter()
    for i in range(50000):
        shopping_list.insert_item("x")
    print(manager_class.__name__, round(time.perf_counter() - start, 4), "seconds")