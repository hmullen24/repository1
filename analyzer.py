import time
import stringdata

def main() :
    data_set = stringdata.get_data()

    # linear search for "not_here"
    start_time = time.time()
    index_found = Searches.linear_search(data_set, "not_here")
    end_time = time.time()
    print(f"Linear search for 'not_here': \nIndex = {index_found} \nTime: {end_time - start_time}\n")

    # binary search for "not_here"
    start_time = time.time()
    index_found = Searches.binary_search(data_set, "not_here")
    end_time = time.time()
    print(f"Binary search for 'not_here': \nIndex = {index_found} \nTime: {end_time - start_time}\n")

    # linear search for "mzzzz"
    start_time = time.time()
    index_found = Searches.linear_search(data_set, "mzzzz")
    end_time = time.time()
    print(f"Linear search for 'mzzzz': \nIndex = {index_found} \nTime: {end_time - start_time}\n")

    # binary search for "mzzzz"
    start_time = time.time()
    index_found = Searches.binary_search(data_set, "mzzzz")
    end_time = time.time()
    print(f"Binary search for 'mzzzz': \nIndex = {index_found} \nTime: {end_time - start_time}\n")

    # linear search for "aaaaa"
    start_time = time.time()
    index_found = Searches.linear_search(data_set, "aaaaa")
    end_time = time.time()
    print(f"Linear search for 'aaaaa': \nIndex = {index_found} \nTime: {end_time - start_time}\n")

    # binary search for "aaaaa"
    start_time = time.time()
    index_found = Searches.binary_search(data_set,"aaaaa")
    end_time = time.time()
    print(f"Binary search for 'aaaaa': \nIndex = {index_found} \nTime: {end_time - start_time}\n")


# the search methods below in the Searches class are based on the methods included in the following textbook

# /**************************************************************************************
# Title: Programming in Python / C++
# Author: Frank Vahid and Roman Lysecky
# Date:
# Code version:
# Availability: Sections 9.7, 9.8; Figures 9.7.1, 9.8.1
# **************************************************************************************/

class Searches :
    def linear_search(container, element) -> int :
        index_result = -1
        for index, val in enumerate(container) : # compare elements one-by-one
            if val == element :
                index_result = index
                break
            else :
                continue
        return index_result

    def binary_search(container, element) -> int :
        index_result = -1
        low_index = 0
        high_index = len(container) - 1
        while high_index >= low_index : # compare elements until a match is found or until a full search is completed with no match found
            split = (high_index + low_index) // 2 # integer division in case of dividing an odd
            if container[split] > element :
                high_index = split - 1
            elif container[split] < element :
                low_index = split + 1
            elif container[split] == element :
                index_result = split
                break
            else :
                return -1
        return index_result


if __name__ == "__main__" :
    main()