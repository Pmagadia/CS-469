"""shopping_list.py

This assignment is to gain knowledge on Linked List and Selection Sort.
As implementation scenario, shopping list have been selected.
The program stores shopping items in both of simple array or linked list.
Each storing mechanism are separated to different files such as “simple_array_shopping_list_manager.py”
or “linked_list_shopping_list_manager.py” each file contains FileNameClass classes with essential methods
for data manipulation. Note that “shopping_list.py” with the “main” method have been already implemented,
and you are assigned to implement other classes/methods. As part of assignment, compare actual runtime of
insert/delete/lookup operation between two lists and justify in a short paragraph on how and their performance. 
"""

from simple_array_shopping_list_manager import SimpleArrayShoppingListManagerClass
from linked_list_shopping_list_manager import LinkedListShoppingListManagerClass
import time

item_list = ["apple", "banana", "milk", "bread", "butter", "cheese", "carrot", "pork", "beef", "mushroom", "fish"]

def main():
        print("------ Simple array ------")
        sa = SimpleArrayShoppingListManagerClass()

        #insert operation
        simple_array_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
                sa.insert_item(item_list[i])
        simple_array_insert_end_time = time.perf_counter()
        print("current list:\t", end = " ")
        sa.print_items()

        #delete operation
        simple_array_delete_start_time = time.perf_counter()
        sa.delete_item("milk")
        simple_array_delete_end_time = time.perf_counter()
        print("delete milk:\t", end = " ")
        sa.print_items()

        #look up operation(last element)
        simple_array_lookup_start_time = time.perf_counter()
        sa_lastElement = sa.get_last_item()
        simple_array_lookup_end_time = time.perf_counter()
        print("last element:\t%s" % sa_lastElement)
        
        #sort operation
        sa.selection_sort()
        print("Sorted(a to z):\t", end = " ")
        sa.print_items()

        #time summary:
        saInsertOp = simple_array_insert_end_time - simple_array_insert_start_time
        saDeleteOp = simple_array_delete_end_time - simple_array_delete_start_time
        saLookupOp = simple_array_lookup_end_time - simple_array_lookup_start_time
        print("-insert: %s\n-delete: %s\n-lookup: %s\n" %(saInsertOp, saDeleteOp, saLookupOp))

        print("------ Linked list ------")
        ll = LinkedListShoppingListManagerClass()
        #insert operation
        linked_list_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
                ll.insert_item(item_list[i])
        linked_list_insert_end_time = time.perf_counter()
        print("current list:\t", end = " ")
        ll.print_items()

        #delete operation
        linked_list_delete_start_time = time.perf_counter()
        ll.delete_item("milk")
        linked_list_delete_end_time = time.perf_counter()
        print("delete milk:\t", end = " ")
        ll.print_items()
        
        #look up operation(last element)
        linked_list_lookup_start_time = time.perf_counter()
        ll_lastElement = ll.get_last_item()
        linked_list_lookup_end_time = time.perf_counter()
        print("last element:\t%s" % ll_lastElement)
        
        #find smallest
        print("smallest element:\t%s" % ll.find_smallest() )

        #sort operation
        ll.selection_sort()
        print("Sorted(a to z):\t", end = " ")
        ll.print_items()

        #time summary:
        llInsertOp= linked_list_insert_end_time - linked_list_insert_start_time
        llDeleteOp= linked_list_delete_end_time - linked_list_delete_start_time
        llLookupOp= linked_list_lookup_end_time - linked_list_lookup_start_time
        print("-insert: %s\n-delete: %s\n-lookup: %s\n" %(llInsertOp, llDeleteOp, llLookupOp))

if __name__ == "__main__":
        main()

