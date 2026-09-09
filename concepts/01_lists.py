"""
Concept 01: Lists in Python
===========================
A Python list is a mutable, ordered sequence of elements.
Lists can hold items of different types, allow duplicates, and support dynamic resizing.
"""

import copy


def demo_creation():
    print("--- 1. Creation & Initialization ---")    
    # Empty lists
    empty_1 = []
    empty_2 = list()

    # Literals with homogeneous and heterogeneous types
    numbers = [1, 2, 3, 4, 5]
    mixed = ["Alice", 42, 3.14, True, [10, 20]]

    # Converting other iterables to list
    from_string = list("Python")       # ['P', 'y', 't', 'h', 'o', 'n']
    from_range = list(range(1, 6))      # [1, 2, 3, 4, 5]

    # Repetition
    zeros = [0] * 4                     # [0, 0, 0, 0]

    print(f"Empty: {empty_1}")
    print(f"Empty (list()): {empty_2}")
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed}")
    print(f"From string: {from_string}")
    print(f"From range: {from_range}")
    print(f"Repeated zeros: {zeros}\n")


def demo_indexing_and_slicing():
    print("/n--- 2. Indexing and Slicing ---")
    letters = ["a", "b", "c", "d", "e", "f", "g"]

    # Positive and negative indexing
    first = letters[0]                  # 'a'
    last = letters[-1]                  # 'g'
    second_last = letters[-2]           # 'f'

    # Slicing: list[start:stop:step]
    # Note: 'stop' is exclusive
    slice_first_three = letters[:3]     # ['a', 'b', 'c']
    slice_middle = letters[2:5]         # ['c', 'd', 'e']
    slice_step = letters[::2]           # ['a', 'c', 'e', 'g']
    reversed_list = letters[::-1]       # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

    print(f"Original: {letters}")
    print(f"First element: {first}, Last element: {last}, Second to last: {second_last}")
    print(f"letters[:3]  -> {slice_first_three}")
    print(f"letters[2:5] -> {slice_middle}")
    print(f"letters[::2] -> {slice_step}")
    print(f"letters[::-1] (reversed) -> {reversed_list}\n")
    
    print(f"letters[:-1] (all but last) -> {letters[:-1]}")
    print(f"letters[:-2] (all but last two) -> {letters[:-2]}")


def demo_modification():
    print("--- 3. Mutation and Modifying Elements ---")
    items = [10, 20, 30, 40, 50]

    # Reassigning single element
    items[1] = 999                      # [10, 999, 30, 40, 50]

    # Slice assignment (can replace, shrink, or expand)
    items[2:4] = [300, 400, 450]        # Replaces 2 elements with 3: [10, 999, 300, 400, 450, 50]

    print(f"After modifications: {items}\n")


def demo_methods():
    print("--- 4. Common List Methods ---")
    fruits = ["apple", "banana"]

    # Adding elements
    fruits.append("cherry")             # Appends single element to end: ['apple', 'banana', 'cherry']
    fruits.insert(1, "blueberry")       # Inserts at index 1: ['apple', 'blueberry', 'banana', 'cherry']
    fruits.extend(["date", "elderberry"]) # Appends multiple items: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

    print(f"After adding: {fruits}")

    # Removing elements
    removed_item = fruits.pop()         # Removes & returns last item ('elderberry')
    popped_idx = fruits.pop(1)          # Removes & returns item at index 1 ('blueberry')
    fruits.remove("banana")             # Removes first occurrence of value 'banana'
    print(f"Popped last: {removed_item}, Popped index 1: {popped_idx}")
    print(f"After removals: {fruits}")

    # Searching & Counting
    print(f"Index of 'cherry': {fruits.index('cherry')}")
    print(f"Count of 'apple': {fruits.count('apple')}")
    print(f"Is 'kiwi' in fruits? {'kiwi' in fruits}")

    # Sorting
    numbers = [5, 2, 9, 1, 7]
    sorted_copy = sorted(numbers)       # Returns new sorted list, leaves original untouched
    numbers.sort(reverse=True)          # In-place sort (modifies original)
    print(f"sorted(numbers) copy: {sorted_copy}")
    print(f"In-place sorted descending: {numbers}\n")


def demo_copying():
    print("--- 5. Shallow Copy vs Deep Copy ---")
    original = [1, [2, 3], 4]

    # Shallow copies
    shallow_1 = original.copy()
    shallow_2 = original[:]
    shallow_3 = list(original)

    # Deep copy
    deep = copy.deepcopy(original)

    # Modify nested list in original
    original[1][0] = 999

    print(f"Original after modifying nested list: {original}")
    print(f"Shallow copy (affected!):            {shallow_1}")
    print(f"Deep copy (unaffected):               {deep}\n")


def demo_common_pitfalls():
    print("--- 6. Common Pitfalls / Gotchas ---")

    # Pitfall A: Nested list creation with multiplication
    # BAD: creates 3 references to the SAME inner list
    bad_grid = [[0] * 3] * 3
    bad_grid[0][0] = 1
    print(f"Bad grid ([[0]*3]*3) after setting [0][0]=1: {bad_grid}")

    # GOOD: creates independent inner lists
    good_grid = [[0] * 3 for _ in range(3)]
    good_grid[0][0] = 1
    print(f"Good grid after setting [0][0]=1:            {good_grid}")

    # Pitfall B: Default mutable argument in functions
    def append_to(item, target=None):
        # Best Practice: Avoid target=[] in parameter list
        if target is None:
            target = []
        target.append(item)
        return target

    print(f"Append call 1: {append_to('first')}")
    print(f"Append call 2: {append_to('second')}\n")


def main():
    print("========================================")
    print(" PYTHON LEARNING: 01 - LISTS ")
    print("========================================\n")
    demo_creation()
    demo_indexing_and_slicing()
    # demo_modification()
    # demo_methods()
    # demo_copying()
    # demo_common_pitfalls()
    print("List concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
