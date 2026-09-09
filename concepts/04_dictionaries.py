"""
Concept 04: Dictionaries in Python
==================================
A Python dictionary (`dict`) is an unordered, mutable collection of key-value pairs.
Starting in Python 3.7+, dictionaries are guaranteed to maintain insertion order.
Keys must be unique and hashable (immutable types like strings, numbers, or tuples).
Values can be of any type, can repeat, and can be nested arbitrarily.
Under the hood, dictionaries use hash tables, giving average O(1) time complexity
for lookup, insertion, update, and deletion operations.
"""

import copy
from collections import Counter, defaultdict


def demo_creation():
    print("--- 1. Creation & Initialization ---")
    # Empty dictionaries
    empty_1 = {}
    empty_2 = dict()

    # Literal key-value pairs
    user = {"name": "Alice", "age": 30, "role": "Engineer"}

    # Using dict() constructor with keyword arguments (keys must be valid identifiers)
    config = dict(host="localhost", port=8080, debug=True)

    # Creating from a list of (key, value) tuples
    pairs = [("python", 1991), ("java", 1995), ("rust", 2010)]
    languages = dict(pairs)

    # Creating using zip() combining two sequences
    keys = ["id", "username", "email"]
    values = [101, "alicedev", "alice@example.com"]
    account = dict(zip(keys, values))

    # Using dict.fromkeys() with an immutable default value
    initial_scores = dict.fromkeys(["math", "science", "english"], 0)

    # Heterogeneous hashable keys (int, float, str, tuple)
    hetero_dict = {
        1: "integer key",
        "name": "string key",
        3.14: "float key",
        (10, 20): "tuple coordinate key",
    }

    print(f"Empty: {empty_1}, Empty (dict()): {empty_2}")
    print(f"Literal user: {user}")
    print(f"dict() kwargs: {config}")
    print(f"From pairs: {languages}")
    print(f"From zip(): {account}")
    print(f"fromkeys(): {initial_scores}")
    print(f"Heterogeneous keys: {hetero_dict}\n")


def demo_accessing():
    print("--- 2. Accessing Elements & Safe Lookups ---")
    student = {"name": "Bob", "grade": "A", "age": 16}

    # Direct indexing with brackets
    print(f"Direct access student['name']: {student['name']}")

    # KeyError on missing key
    try:
        _ = student["gpa"]
    except KeyError as e:
        print(f"Direct access missing key student['gpa'] raises KeyError: {e}")

    # Safe lookup with .get(key, default)
    # Returns None if key doesn't exist and default is not provided
    print(f"student.get('grade'):          {student.get('grade')}")
    print(f"student.get('gpa'):            {student.get('gpa')}")
    print(f"student.get('gpa', 4.0):       {student.get('gpa', 4.0)} (with fallback default)")

    # .setdefault(key, default): returns existing value, OR inserts key: default if missing
    inventory = {"apples": 10, "bananas": 5}
    apples_count = inventory.setdefault("apples", 0)   # Key exists: returns 10, no change
    oranges_count = inventory.setdefault("oranges", 20) # Key missing: inserts 'oranges': 20
    print(f"inventory after setdefault: {inventory}")
    print(f"apples: {apples_count}, oranges: {oranges_count}")

    # Membership testing with 'in' and 'not in' (checks KEYS, not values!)
    print(f"'name' in student:     {'name' in student} (O(1) hash check)")
    print(f"'Bob' in student:      {'Bob' in student} (False! 'Bob' is a value, not a key)")
    print(f"'Bob' in student.values(): {'Bob' in student.values()} (Searches values in O(n))\n")


def demo_modification():
    print("--- 3. Modifying, Adding & Removing Elements ---")
    profile = {"user": "charlie", "followers": 150}
    print(f"Initial: {profile}")

    # Adding a new key-value pair / Reassigning an existing key
    profile["email"] = "charlie@web.org"  # Add new
    profile["followers"] = 151            # Update existing
    print(f"After adding/updating: {profile}")

    # .update() with dict or kwargs
    profile.update({"location": "Berlin", "verified": True})
    profile.update(status="active")
    print(f"After .update(): {profile}")

    # Python 3.9+ Merge (|) and In-place Update (|=) operators
    extras = {"theme": "dark", "status": "busy"}  # 'status' conflicts with profile
    # Union operator | returns a new dict (right operand overrides left)
    merged = profile | extras
    print(f"Union (profile | extras): {merged}")

    # In-place merge |=
    profile |= {"theme": "dark"}
    print(f"After profile |= {{'theme': 'dark'}}: {profile}")

    # Removing elements:
    # 1. del: deletes key, raises KeyError if absent
    del profile["theme"]
    print(f"After del profile['theme']: {profile}")

    # 2. .pop(key, default): removes and returns value, handles default safely
    followers = profile.pop("followers")
    missing_val = profile.pop("non_existent", "N/A")
    print(f"Popped 'followers': {followers}, Popped missing with default: {missing_val}")
    print(f"Profile after pop: {profile}")

    # 3. .popitem(): removes and returns last (key, value) in LIFO order
    last_item = profile.popitem()
    print(f"Popped last item (.popitem()): {last_item}")
    print(f"Profile after popitem: {profile}")

    # 4. .clear(): removes all items
    profile_copy = profile.copy()
    profile_copy.clear()
    print(f"After .clear(): {profile_copy}\n")


def demo_views_and_iteration():
    print("--- 4. Views and Iteration ---")
    salaries = {"Alice": 95000, "Bob": 80000, "Charlie": 87000}

    # Dictionary views: dynamic windows into keys, values, and items
    keys_view = salaries.keys()
    values_view = salaries.values()
    items_view = salaries.items()

    print(f"keys():   {keys_view}")
    print(f"values(): {values_view}")
    print(f"items():  {items_view}")

    # Views are dynamic: updates to the dict immediately reflect in the view
    salaries["Diana"] = 92000
    print(f"keys() after adding Diana: {keys_view} (reflects dynamically!)")
    del salaries["Diana"]

    # Iteration patterns:
    # A. Iterating over keys (default)
    print("Iterating over keys:")
    for name in salaries:
        print(f"  Key: {name} -> Value: {salaries[name]}")

    # B. Iterating over values
    print("Iterating over values:")
    for salary in salaries.values():
        print(f"  Salary: {salary}")

    # C. Idiomatic unpacking iteration over (key, value) pairs
    print("Iterating over key-value pairs with .items():")
    for name, salary in salaries.items():
        print(f"  {name}: ${salary:,}")

    # Set-like operations supported by dict_keys and dict_items
    tech_team = {"Alice": "Dev", "Bob": "QA", "Eve": "Dev"}
    mgmt_team = {"Bob": "Lead", "Frank": "PM", "Eve": "Dev"}

    common_people = tech_team.keys() & mgmt_team.keys()
    only_tech = tech_team.keys() - mgmt_team.keys()
    common_pairs = tech_team.items() & mgmt_team.items()  # Same key AND same value

    print(f"Common keys (tech & mgmt):       {common_people}")
    print(f"Keys only in tech (tech - mgmt): {only_tech}")
    print(f"Identical (key, value) pairs:    {common_pairs}\n")


def demo_merging_and_copying():
    print("--- 5. Shallow Copy vs Deep Copy ---")
    original = {
        "title": "Python Guide",
        "tags": ["programming", "python"],
        "metadata": {"views": 100, "likes": 20},
    }

    # Shallow copy methods
    shallow_1 = original.copy()
    shallow_2 = dict(original)

    # Deep copy
    deep = copy.deepcopy(original)

    # Mutate top-level vs nested elements
    original["title"] = "Advanced Python Guide"  # Rebinds top-level immutable value
    original["tags"].append("backend")           # Mutates nested mutable list
    original["metadata"]["views"] = 500          # Mutates nested mutable dict

    print(f"Original after mutations: {original}")
    print(f"Shallow copy (nested mutated!): tags={shallow_1['tags']}, views={shallow_1['metadata']['views']}")
    print(f"Deep copy (isolated!):          tags={deep['tags']}, views={deep['metadata']['views']}\n")


def demo_collections_specializations():
    print("--- 6. Collections Specializations (defaultdict & Counter) ---")

    # 1. defaultdict: supplies a factory for missing keys without throwing KeyError
    # Grouping words by their first letter
    words = ["apple", "banana", "apricot", "blueberry", "avocado", "cherry"]
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)

    print("defaultdict(list) grouping by first letter:")
    for letter, word_list in sorted(grouped.items()):
        print(f"  '{letter}': {word_list}")

    # Counting with defaultdict(int)
    counts = defaultdict(int)
    for word in ["apple", "banana", "apple", "apple", "banana"]:
        counts[word] += 1
    print(f"defaultdict(int) counts: {dict(counts)}")

    # 2. Counter: purpose-built dictionary for counting hashable objects
    letter_counts = Counter("mississippi")
    print(f"Counter('mississippi'): {letter_counts}")
    print(f"Most common 2 elements:  {letter_counts.most_common(2)}\n")


def demo_common_pitfalls():
    print("--- 7. Common Pitfalls / Gotchas ---")

    # Pitfall A: Unhashable types as dictionary keys
    try:
        invalid_key_dict = {[1, 2]: "value"}  # type: ignore
    except TypeError as e:
        print(f"List as key error: {e}")

    try:
        invalid_tuple_key = {(1, [2, 3]): "value"}  # type: ignore
    except TypeError as e:
        print(f"Tuple with list as key error: {e}")

    # Pitfall B: dict.fromkeys() with a mutable default object (CRITICAL GOTCHA)
    # All keys reference the SAME list instance!
    keys = ["group_a", "group_b"]
    bad_dict = dict.fromkeys(keys, [])
    bad_dict["group_a"].append(100)
    print(f"Bad fromkeys with []: {bad_dict} (Both keys mutated!)")

    # Correct way: Dict comprehension to create distinct lists
    good_dict = {k: [] for k in keys}
    good_dict["group_a"].append(100)
    print(f"Good dict comprehension: {good_dict} (Only group_a affected)")

    # Pitfall C: Modifying dictionary size during iteration
    sample = {"a": 1, "b": 2, "c": 3, "d": 4}
    try:
        for k in sample:
            if k == "b":
                del sample[k]
    except RuntimeError as e:
        print(f"Mutating dict during iteration error: {e}")

    # Solution: Iterate over list(sample.keys()) or a copy
    sample = {"a": 1, "b": 2, "c": 3, "d": 4}
    for k in list(sample.keys()):
        if sample[k] % 2 == 0:
            del sample[k]
    print(f"Safely pruned dict (removed evens): {sample}")

    # Pitfall D: Using if dict.get(key) when value might be falsy (0, False, "")
    settings = {"timeout": 0, "enabled": False}
    # Bad check: 0 is falsy, so this branch won't execute even though key exists!
    if not settings.get("timeout"):
        print("Gotcha: settings.get('timeout') is 0, which is falsy!")

    # Proper check for key existence:
    if "timeout" in settings:
        print(f"Correct check ('timeout' in settings): timeout={settings['timeout']}\n")


def main():
    print("========================================")
    print(" PYTHON LEARNING: 04 - DICTIONARIES ")
    print("========================================\n")
    demo_creation()
    demo_accessing()
    demo_modification()
    demo_views_and_iteration()
    demo_merging_and_copying()
    demo_collections_specializations()
    demo_common_pitfalls()
    print("Dictionary concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
