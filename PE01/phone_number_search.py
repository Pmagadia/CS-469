"""phone_number_search.py

This assignment is to practice python language (ex. class, method, Object-Oriented Programming concept,
and syntaxes) and implement simple and binary search for looking up the phone number of a given name. 
"""

from binary_search import BinarySearchClass
from simple_search import SimpleSearchClass
import time

name_list = ["Alice", 
        "Bob", 
        "Charlie", 
        "Daisy", 
        "Emily", 
        "Fred", 
        "George", 
        "Harry",
        "Iris", 
        "Jenny", 
        "Kenny", 
        "Lucas", 
        "Mary", 
        "Nancy", 
        "Oliver", 
        "Phillip", 
        "Quinn", 
        "Rose", 
        "Sophia", 
        "Thomas"]
phone_number = ["000-230-2491",
               "000-203-1274",
               "000-211-2394",
               "000-212-1183",
               "000-204-1237",
               "000-271-2394",
               "000-231-0183",
               "000-213-3233",
               "000-251-2395",
               "000-211-0183",
               "000-283-1214",
               "000-221-2314",
               "000-261-0243",
               "000-253-1334",
               "000-229-2183",
               "000-238-2283",
               "000-255-2133",
               "000-243-2243",
               "000-282-2386",
               "000-231-2143"]

def main():
        person_name = "Thomas"
        print("look up %s's phone number..." % person_name)

        # Note that name_list and phone_number array indexes are synced
        ss = SimpleSearchClass(name_list)
        simple_search_start_time = time.perf_counter()
        sim_result = ss.simple_search(person_name)
        simple_search_end_time = time.perf_counter()
        print("phone number(simple search): " + phone_number[sim_result])
        print("--- simple search: %s seconds ---" % (simple_search_end_time - simple_search_start_time))

        # Note that name_list and phone_number array indexes are synced
        bs = BinarySearchClass(name_list)
        binary_search_start_time = time.perf_counter()
        bin_result = bs.binary_search(person_name)
        binary_search_end_time = time.perf_counter()
        print("phone number(binary search): " + phone_number[bin_result])
        print("--- binary search: %s seconds ---" % (binary_search_end_time - binary_search_start_time))

if __name__ == "__main__":
    main()

