"""
Concept 02: Tuples in Python
============================
A Python tuple is an ordered, immutable sequence of elements.
Tuples are commonly used for heterogeneous data collections (records),
while lists are typically used for homogeneous collections.
Because tuples are immutable, they are hashable (if their items are hashable)
and can be used as dictionary keys and set elements.
"""

import sys
from collections import namedtuple


def demo_creation():
    print("--- 1. Creation & Initialization ---")
    # Empty tuples
    empty_1 = ()
    empty_2 = tuple()

    # The Single-Element Gotcha: Comma is required!
    not_a_tuple = (42)      # int, parentheses are just grouping
    single_tuple = (42,)    # tuple with one element

    # Multi-element tuples (parentheses are optional, comma creates the tuple)
    with_parens = (1, 2, 3)
    without_parens = 1, 2, 3  # Tuple packing syntax
    mixed = ("Alice", 30, True, 3.14)

    # Converting other iterables to tuple
    from_list = tuple([10, 20, 30])
    from_string = tuple("Python")
    from_range = tuple(range(1, 6))

    # Repetition and Concatenation
    repeated = (1, 2) * 3
    concatenated = (1, 2) + (3, 4)

    print(f"Empty: {empty_1}, Empty (tuple()): {empty_2}")
    print(f"type((42)): {type(not_a_tuple).__name__} vs type((42,)): {type(single_tuple).__name__}")
    print(f"With parens: {with_parens}")
    print(f"Without parens: {without_parens}")
    print(f"Mixed types: {mixed}")
    print(f"From list: {from_list}")
    print(f"From string: {from_string}")
    print(f"From range: {from_range}")
    print(f"Repeated: {repeated}")
    print(f"Concatenated: {concatenated}\n")


def demo_indexing_and_slicing():
    print("--- 2. Indexing and Slicing ---")
    letters = ("a", "b", "c", "d", "e", "f", "g")

    # Positive and negative indexing
    first = letters[0]              # 'a'
    last = letters[-1]              # 'g'
    second_last = letters[-2]       # 'f'

    # Slicing: tuple[start:stop:step] (stop is exclusive)
    slice_first_three = letters[:3]  # ('a', 'b', 'c')
    slice_middle = letters[2:5]      # ('c', 'd', 'e')
    slice_step = letters[::2]        # ('a', 'c', 'e', 'g')
    reversed_tuple = letters[::-1]   # ('g', 'f', 'e', 'd', 'c', 'b', 'a')

    print(f"Original: {letters}")
    print(f"First: {first}, Last: {last}, Second to last: {second_last}")
    print(f"letters[:3]  -> {slice_first_three}")
    print(f"letters[2:5] -> {slice_middle}")
    print(f"letters[::2] -> {slice_step}")
    print(f"letters[::-1] (reversed) -> {reversed_tuple}\n")


def demo_immutability():
    print("--- 3. Immutability & Nested Mutability ---")
    point = (10, 20)

    # Immutability: Elements cannot be reassigned or deleted
    try:
        point[0] = 99  # type: ignore
    except TypeError as e:
        print(f"Cannot reassign element: {e}")

    try:
        del point[0]  # type: ignore
    except TypeError as e:
        print(f"Cannot delete element: {e}")

    # Nuance: A tuple is immutable, but it can contain mutable objects!
    # The reference stored inside the tuple cannot change, but the object itself can.
    record = ("Alice", [90, 85, 92])
    print(f"Before mutating inner list: {record}")
    record[1].append(98)
    print(f"After mutating inner list:  {record}\n")


def demo_methods_and_operations():
    print("--- 4. Methods and Built-in Operations ---")
    numbers = (1, 2, 3, 2, 4, 2, 5)

    # Tuples only have 2 methods: count() and index()
    print(f"numbers.count(2): {numbers.count(2)}")
    print(f"numbers.index(3): {numbers.index(3)}")
    print(f"numbers.index(2, 2): {numbers.index(2, 2)}  # Search starting from index 2")

    # Membership testing
    print(f"Is 4 in numbers? {4 in numbers}")
    print(f"Is 99 in numbers? {99 in numbers}")

    # Built-in sequence functions
    print(f"len(numbers): {len(numbers)}")
    print(f"min(numbers): {min(numbers)}, max(numbers): {max(numbers)}, sum(numbers): {sum(numbers)}")

    # sorted() on a tuple returns a new list (not a tuple)
    sorted_as_list = sorted(numbers)
    print(f"sorted(numbers): {sorted_as_list} (type: {type(sorted_as_list).__name__})\n")


def demo_packing_and_unpacking():
    print("--- 5. Packing, Unpacking & Swapping ---")

    # Tuple packing
    user_info = "Alice", 28, "Engineer"
    print(f"Packed tuple: {user_info}")

    # Basic unpacking (number of variables must match number of items)
    name, age, profession = user_info
    print(f"Unpacked -> Name: {name}, Age: {age}, Profession: {profession}")

    # Extended unpacking with the starred expression (*)
    numbers = (1, 2, 3, 4, 5, 6)
    first, *middle, last = numbers
    print(f"first: {first}, middle: {middle} (type: {type(middle).__name__}), last: {last}")

    head, *tail = numbers
    print(f"head: {head}, tail: {tail}")

    # Ignoring elements with underscore (_)
    first_name, _, role = ("Bob", "Smith", "Manager")
    print(f"First: {first_name}, Role: {role} (middle name ignored)")

    # Swapping variables without a temp variable (uses tuple packing/unpacking)
    x, y = 100, 200
    print(f"Before swap: x={x}, y={y}")
    x, y = y, x
    print(f"After swap:  x={x}, y={y}")

    # Multiple return values from functions are actually tuples
    def get_min_max(values):
        return min(values), max(values)

    low, high = get_min_max((4, 8, 2, 9, 1))
    print(f"Function returning tuple: low={low}, high={high}\n")


def demo_tuples_vs_lists():
    print("--- 6. Tuples vs. Lists (Hashability & Memory) ---")

    # 1. Hashability: Tuples can be dictionary keys or set elements (if items are hashable)
    location_names = {
        (40.7128, -74.0060): "New York",
        (37.7749, -122.4194): "San Francisco",
    }
    coords = (40.7128, -74.0060)
    print(f"Dict lookup with tuple key {coords}: {location_names[coords]}")

    # Lists CANNOT be used as dict keys or set items
    try:
        invalid_dict = {[1, 2]: "value"}  # type: ignore
    except TypeError as e:
        print(f"List as dict key error: {e}")

    # A tuple with a mutable item is NOT hashable
    unhashable_tuple = (1, [2, 3])
    try:
        hash(unhashable_tuple)
    except TypeError as e:
        print(f"Tuple with list inside is unhashable: {e}")

    # 2. Memory efficiency
    list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tuple_example = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    list_size = sys.getsizeof(list_example)
    tuple_size = sys.getsizeof(tuple_example)

    print(f"Memory size of list (10 items):  {list_size} bytes")
    print(f"Memory size of tuple (10 items): {tuple_size} bytes ({list_size - tuple_size} bytes saved)\n")


def demo_namedtuples():
    print("--- 7. Namedtuples (collections.namedtuple) ---")

    # Define a namedtuple schema
    Point = namedtuple("Point", ["x", "y"])
    p1 = Point(10, 20)

    # Access by name AND index
    print(f"Point: {p1}")
    print(f"Access by attribute: p1.x = {p1.x}, p1.y = {p1.y}")
    print(f"Access by index:     p1[0] = {p1[0]}, p1[1] = {p1[1]}")

    # Unpacking works identical to standard tuples
    px, py = p1
    print(f"Unpacked namedtuple: px={px}, py={py}")

    # Useful namedtuple methods
    as_dict = p1._asdict()
    print(f"Converted to dict via _asdict(): {as_dict}")

    p2 = p1._replace(x=99)
    print(f"Modified copy via _replace(x=99): {p2}\n")


def demo_common_pitfalls():
    print("--- 8. Common Pitfalls / Gotchas ---")

    # Pitfall A: Single-item tuple without comma
    not_a_tuple = ("apple")
    is_a_tuple = ("apple",)
    print(f"('apple') is type:  {type(not_a_tuple).__name__} (Value: {not_a_tuple})")
    print(f"('apple',) is type: {type(is_a_tuple).__name__} (Value: {is_a_tuple})")

    # Pitfall B: Generator expression vs Tuple comprehension
    # Python has list comprehensions [x for x in ...] and dict comprehensions {k: v for ...}
    # Parentheses create a GENERATOR, NOT a tuple!
    gen_expr = (x * 2 for x in range(4))
    tuple_created = tuple(x * 2 for x in range(4))
    print(f"(x * 2 for x in ...): {gen_expr} (type: {type(gen_expr).__name__})")
    print(f"tuple(x * 2 for x in ...): {tuple_created} (type: {type(tuple_created).__name__})")

    # Pitfall C: Augmented assignment with nested mutable object in a tuple
    # Classic Python puzzle: The list IS mutated, BUT an exception is raised!
    t = (1, [10, 20])
    print(f"Tuple before t[1] += [30]: {t}")
    try:
        t[1] += [30]
    except TypeError as e:
        print(f"Raised TypeError: {e}")
    print(f"Tuple after exception:    {t} (Notice: [30] was appended!)\n")


def main():
    print("========================================")
    print(" PYTHON LEARNING: 02 - TUPLES ")
    print("========================================\n")
    demo_creation()
    demo_indexing_and_slicing()
    demo_immutability()
    demo_methods_and_operations()
    demo_packing_and_unpacking()
    demo_tuples_vs_lists()
    demo_namedtuples()
    demo_common_pitfalls()
    print("Tuple concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
