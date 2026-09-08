"""
Concept 03: Sets in Python
==========================
A Python set is an unordered collection of unique, hashable elements.
Sets are mutable (you can add and remove elements), but the elements
themselves must be immutable (hashable).
Under the hood, sets use hash tables, giving them average O(1) time
complexity for lookups, insertions, and deletions.
"""


def demo_creation():
    print("--- 1. Creation & Deduplication ---")
    # Empty set: Must use set(), NOT {}
    empty_set = set()
    empty_dict = {}  # Gotcha: This is a dict, not a set!

    # Literal creation with braces
    numbers = {1, 2, 3, 4, 5}

    # Automatic deduplication
    duplicates = {1, 2, 2, 3, 3, 3, 4}

    # Converting iterables to sets
    from_list = set([10, 20, 20, 30])
    from_string = set("mississippi")  # Unique characters
    from_range = set(range(1, 6))

    # Heterogeneous types (as long as each element is hashable)
    mixed = {42, "Python", 3.14, (1, 2)}

    print(f"Empty set: {empty_set} (type: {type(empty_set).__name__})")
    print(f"empty_dict = {{}} is type: {type(empty_dict).__name__} (NOT a set!)")
    print(f"Numbers: {numbers}")
    print(f"Deduplicated from {1, 2, 2, 3, 3, 3, 4}: {duplicates}")
    print(f"From list with duplicates: {from_list}")
    print(f"From string 'mississippi': {from_string}")
    print(f"From range(1, 6): {from_range}")
    print(f"Mixed hashable types: {mixed}\n")


def demo_modification():
    print("--- 2. Adding and Removing Elements ---")
    fruits = {"apple", "banana"}
    print(f"Initial set: {fruits}")

    # Adding a single element
    fruits.add("cherry")
    fruits.add("apple")  # Duplicate: no effect, no error
    print(f"After .add('cherry') and .add('apple'): {fruits}")

    # Adding multiple elements from an iterable
    fruits.update(["date", "elderberry", "banana"])
    print(f"After .update(['date', 'elderberry', 'banana']): {fruits}")

    # Removing elements: remove() vs discard()
    # remove() raises KeyError if element is not found
    fruits.remove("banana")
    print(f"After .remove('banana'): {fruits}")
    try:
        fruits.remove("non_existent")
    except KeyError as e:
        print(f"fruits.remove('non_existent') raised KeyError: {e}")

    # discard() safely removes element without raising an error if missing
    fruits.discard("date")
    fruits.discard("non_existent")  # Silently ignored!
    print(f"After .discard('date') and .discard('non_existent'): {fruits}")

    # pop(): Removes and returns an arbitrary element
    popped = fruits.pop()
    print(f"Popped element: '{popped}', Remaining: {fruits}")

    # clear(): Empties the set
    fruits_copy = fruits.copy()
    fruits_copy.clear()
    print(f"After .clear(): {fruits_copy}\n")


def demo_set_operations():
    print("--- 3. Mathematical Set Operations ---")
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(f"Set A: {a}")
    print(f"Set B: {b}\n")

    # 1. Union: Elements in either A or B
    # Operator | requires a set; method .union() accepts any iterable
    print(f"Union (A | B):               {a | b}")
    print(f"Union method A.union(b):     {a.union(b)}")

    # 2. Intersection: Elements in both A and B
    print(f"Intersection (A & B):        {a & b}")
    print(f"Intersection A.intersection: {a.intersection(b)}")

    # 3. Difference: Elements in A but NOT in B
    print(f"Difference (A - B):          {a - b}")
    print(f"Difference (B - A):          {b - a}")

    # 4. Symmetric Difference: Elements in A or B, but NOT both
    print(f"Symmetric Difference (A ^ B): {a ^ b}")
    print(f"A.symmetric_difference(B):    {a.symmetric_difference(b)}")

    # In-place operation variants (mutates the set)
    tracker = {1, 2, 3}
    tracker |= {3, 4, 5}  # Equivalent to tracker.update({3, 4, 5})
    print(f"After tracker |= {{3, 4, 5}}:  {tracker}")
    tracker &= {2, 3, 4}  # Equivalent to tracker.intersection_update({2, 3, 4})
    print(f"After tracker &= {{2, 3, 4}}:  {tracker}\n")


def demo_relationships():
    print("--- 4. Set Relationships & Comparisons ---")
    small = {1, 2}
    medium = {1, 2, 3}
    other = {4, 5}

    print(f"small: {small}, medium: {medium}, other: {other}")

    # Subset tests
    print(f"small <= medium (subset):        {small <= medium} (method: {small.issubset(medium)})")
    print(f"small <  medium (proper subset): {small < medium}")
    print(f"small <  small  (proper subset): {small < small}")

    # Superset tests
    print(f"medium >= small (superset):        {medium >= small} (method: {medium.issuperset(small)})")
    print(f"medium >  small (proper superset): {medium > small}")

    # Disjoint test (no elements in common)
    print(f"small.isdisjoint(other):  {small.isdisjoint(other)}")
    print(f"small.isdisjoint(medium): {small.isdisjoint(medium)}")

    # Set equality (ignores element order)
    print(f"{{1, 2, 3}} == {{3, 2, 1}}: {{1, 2, 3}} == {{3, 2, 1}} -> {{1, 2, 3}} == {{3, 2, 1}}\n")


def demo_performance():
    print("--- 5. Membership Testing & Fast Deduplication ---")
    # Lookup performance: O(1) for sets vs O(n) for lists
    items_list = [10, 20, 30, 40, 50]
    items_set = {10, 20, 30, 40, 50}

    print(f"30 in items_set:  {30 in items_set}  # O(1) hash lookup")
    print(f"30 in items_list: {30 in items_list} # O(n) linear scan")

    # Fast list deduplication
    raw_data = ["apple", "orange", "apple", "banana", "orange", "pear"]
    unique_items = list(set(raw_data))
    print(f"Original list:       {raw_data}")
    print(f"list(set(raw_data)): {unique_items} (Notice: order may not be preserved)")

    # If insertion order MUST be preserved while deduplicating (Python 3.7+):
    order_preserved = list(dict.fromkeys(raw_data))
    print(f"Order-preserved:     {order_preserved}\n")


def demo_frozenset():
    print("--- 6. Frozensets (Immutable Sets) ---")
    # frozenset is an immutable, hashable set
    frozen = frozenset([1, 2, 3, 4])
    print(f"frozenset: {frozen} (type: {type(frozen).__name__})")

    # Cannot mutate a frozenset
    try:
        frozen.add(5)  # type: ignore
    except AttributeError as e:
        print(f"Cannot call .add() on frozenset: {e}")

    # Because frozenset is hashable:
    # 1. It CAN be stored as an element in another set (sets of sets)
    set_of_sets = {frozenset({1, 2}), frozenset({3, 4})}
    print(f"Set of frozensets: {set_of_sets}")

    # 2. It CAN be used as a dictionary key
    group_permissions = {
        frozenset({"read", "write"}): "Editor",
        frozenset({"read"}): "Viewer",
    }
    user_perms = frozenset({"read", "write"})
    print(f"Dict lookup with frozenset key: {group_permissions[user_perms]}\n")


def demo_common_pitfalls():
    print("--- 7. Common Pitfalls / Gotchas ---")

    # Pitfall A: The empty set literal trap
    not_a_set = {}
    is_a_set = set()
    print(f"{{}} is type:    {type(not_a_set).__name__} (Empty dict, NOT empty set!)")
    print(f"set() is type: {type(is_a_set).__name__}")

    # Pitfall B: Unhashable elements (lists, dicts, mutable sets)
    try:
        invalid_set = {1, 2, [3, 4]}  # type: ignore
    except TypeError as e:
        print(f"Cannot put list in set: {e}")

    # Tuples containing mutable elements are also unhashable!
    try:
        invalid_set = {1, (2, [3, 4])}  # type: ignore
    except TypeError as e:
        print(f"Cannot put tuple with inner list in set: {e}")

    # Pitfall C: Sets are NOT subscriptable (no indexing or slicing)
    sample_set = {"a", "b", "c"}
    try:
        _ = sample_set[0]  # type: ignore
    except TypeError as e:
        print(f"Indexing sample_set[0] fails: {e}")

    # Pitfall D: Mutating a set while iterating over it
    active_tokens = {"token1", "token2", "token3"}
    try:
        for token in active_tokens:
            if token == "token2":
                active_tokens.remove(token)
    except RuntimeError as e:
        print(f"Mutating set during iteration raises: {e}")

    # Correct way: iterate over a copy of the set
    active_tokens = {"token1", "token2", "token3"}
    for token in set(active_tokens):
        if token == "token2":
            active_tokens.remove(token)
    print(f"Safe removal by iterating over set copy: {active_tokens}\n")


def main():
    print("========================================")
    print(" PYTHON LEARNING: 03 - SETS ")
    print("========================================\n")
    demo_creation()
    demo_modification()
    demo_set_operations()
    demo_relationships()
    demo_performance()
    demo_frozenset()
    demo_common_pitfalls()
    print("Set concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
