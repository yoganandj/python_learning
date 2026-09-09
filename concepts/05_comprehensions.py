"""
Concept 05: Comprehensions in Python
=====================================
Comprehensions provide a concise, expressive, and declarative syntax for constructing
new collections (lists, dictionaries, sets) or generators from existing iterables.

Key Advantages:
1. Readability: Expresses "what" you want to construct rather than the procedural "how".
2. Performance: Executed at C-speed in CPython via specialized bytecodes (LIST_APPEND,
   MAP_ADD, SET_ADD), avoiding Python-level attribute lookups and method call overhead.
3. Scope Isolation: In Python 3, comprehensions have their own local scope, preventing
   loop variables from leaking into the enclosing namespace (with a specific nuance for
   the walrus operator `:=`).
"""

import itertools
import sys


def demo_list_comprehensions():
    print("--- 1. List Comprehensions ---")

    # Basic mapping syntax: [expression for item in iterable]
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]
    print(f"Original numbers: {numbers}")
    print(f"Squares:          {squares}")

    # Comparison: Traditional for-loop vs list comprehension
    # Loop approach:
    doubled_loop = []
    for n in numbers:
        doubled_loop.append(n * 2)

    # Comprehension approach (more concise and faster):
    doubled_comp = [n * 2 for n in numbers]
    print(f"Doubled (loop):   {doubled_loop}")
    print(f"Doubled (comp):   {doubled_comp}")

    # Filtering with 'if': [expression for item in iterable if condition]
    raw_scores = [88, 42, 95, 70, 59, 100, 63]
    passing_scores = [score for score in raw_scores if score >= 70]
    print(f"All scores:       {raw_scores}")
    print(f"Passing (>=70):   {passing_scores}")

    # Combining transformation + filtering
    words = ["  apple ", "BANANA", "  cherry  ", "date", "FIG "]
    cleaned_long_words = [
        word.strip().lower()
        for word in words
        if len(word.strip()) > 4
    ]
    print(f"Cleaned words (>4 chars): {cleaned_long_words}")

    # CRITICAL DISTINCTION: Filter 'if' vs Ternary 'if-else'
    # 1. Filter 'if' (goes AFTER 'for'): decides WHETHER an element is included.
    evens_only = [x for x in range(10) if x % 2 == 0]
    print(f"Filter if (evens only):             {evens_only}")

    # 2. Ternary 'if-else' (goes BEFORE 'for'): decides WHAT VALUE is produced.
    labels = ["Even" if x % 2 == 0 else "Odd" for x in range(6)]
    print(f"Ternary if-else (value selection):   {labels}")

    # 3. Combining BOTH ternary transform AND filtering:
    # Transform numbers 0..9, but filter out multiples of 3, labeling the rest
    parity_of_non_threes = [
        "even" if x % 2 == 0 else "odd"
        for x in range(10)
        if x % 3 != 0
    ]
    print(f"Combined ternary + filter:          {parity_of_non_threes}")

    # Comprehension vs map() and filter()
    # While map/filter with lambda work, comprehensions are widely preferred in Python:
    nums = [1, 2, 3, 4, 5, 6]
    via_map_filter = list(map(lambda x: x * 10, filter(lambda x: x % 2 == 0, nums)))
    via_comprehension = [x * 10 for x in nums if x % 2 == 0]
    print(f"Via map() & filter():               {via_map_filter}")
    print(f"Via comprehension (Pythonic!):      {via_comprehension}\n")


def demo_dict_comprehensions():
    print("--- 2. Dictionary Comprehensions ---")

    # Basic syntax: {key_expr: value_expr for item in iterable}
    numbers = [1, 2, 3, 4, 5]
    squares_map = {n: n**2 for n in numbers}
    print(f"Squares dictionary: {squares_map}")

    # Transforming existing dictionary keys/values
    prices_usd = {"laptop": 1200, "mouse": 25, "monitor": 300, "keyboard": 75}
    eur_rate = 0.92
    prices_eur = {item: round(price * eur_rate, 2) for item, price in prices_usd.items()}
    print(f"Prices in USD: {prices_usd}")
    print(f"Prices in EUR: {prices_eur}")

    # Inverting / Swapping keys and values: {value: key for key, value in d.items()}
    status_codes = {200: "OK", 404: "Not Found", 500: "Internal Error"}
    name_to_code = {name: code for code, name in status_codes.items()}
    print(f"Code to name: {status_codes}")
    print(f"Name to code: {name_to_code}")

    # Filtering dictionary items
    expensive_items = {
        item: price
        for item, price in prices_usd.items()
        if price >= 100
    }
    print(f"Expensive items (>= $100): {expensive_items}")

    # Zipping two sequences into a dictionary with conditions
    keys = ["id", "username", "email", "nickname", "bio"]
    values = [101, "alicedev", "alice@example.com", None, ""]
    # Filter out None and empty string values
    cleaned_profile = {
        k: v
        for k, v in zip(keys, values)
        if v is not None and v != ""
    }
    print(f"Cleaned profile from zipped lists: {cleaned_profile}")

    # Creating lookup indexes from a list of records
    users = [
        {"id": 1, "name": "Alice", "dept": "Engineering"},
        {"id": 2, "name": "Bob", "dept": "Design"},
        {"id": 3, "name": "Charlie", "dept": "Engineering"},
    ]
    user_by_id = {u["id"]: u for u in users}
    name_by_id = {u["id"]: u["name"] for u in users}
    print(f"User indexed by ID: {user_by_id[1]}")
    print(f"Names mapped to IDs: {name_by_id}")

    # Avoiding mutable default aliasing (solving dict.fromkeys gotcha)
    categories = ["electronics", "books", "clothing"]
    # Safe: each key gets its own unique list instance
    safe_catalog = {category: [] for category in categories}
    safe_catalog["books"].append("Fluent Python")
    print(f"Distinct list per key: {safe_catalog}\n")


def demo_set_comprehensions():
    print("--- 3. Set Comprehensions ---")

    # Basic syntax: {expression for item in iterable}
    # Automatic deduplication during collection
    numbers = [-3, -2, -1, 0, 1, 2, 3]
    unique_squares = {x**2 for x in numbers}
    print(f"Original numbers: {numbers}")
    print(f"Unique squares set: {unique_squares}")

    # Extracting unique file extensions
    filenames = [
        "main.py", "test_app.py", "styles.css", "index.html",
        "script.js", "utils.py", "README.md", "app.js",
    ]
    extensions = {
        file.split(".")[-1]
        for file in filenames
        if "." in file
    }
    print(f"File list: {filenames}")
    print(f"Unique extensions: {extensions}")

    # Extracting unique word lengths
    sentence = "The quick brown fox jumps over the lazy dog"
    word_lengths = {len(word) for word in sentence.split()}
    print(f"Sentence: '{sentence}'")
    print(f"Unique word lengths: {sorted(word_lengths)}")

    # Set comprehension with filtering
    vowels = {"a", "e", "i", "o", "u"}
    text = "comprehensions are extraordinarily elegant"
    unique_vowels_in_text = {char.lower() for char in text if char.lower() in vowels}
    print(f"Unique vowels in text: {sorted(unique_vowels_in_text)}\n")


def demo_generator_expressions():
    print("--- 4. Generator Expressions ---")

    # Syntax: (expression for item in iterable)
    # Notice: Parentheses instead of square brackets!
    # Generator expressions evaluate lazily on-demand rather than eagerly creating the full list.
    numbers = [1, 2, 3, 4, 5]
    gen = (x**2 for x in numbers)
    print(f"Generator expression object: {gen}")
    print(f"First value via next():     {next(gen)}")
    print(f"Remaining values via list(): {list(gen)}")

    # Memory Efficiency Comparison: sys.getsizeof()
    # List comprehension creates all elements in RAM up front.
    # Generator expression generates one item at a time.
    n = 1_000_000
    list_comp = [x for x in range(n)]
    gen_expr = (x for x in range(n))

    list_size = sys.getsizeof(list_comp)
    gen_size = sys.getsizeof(gen_expr)
    print(f"Memory for {n:,} items:")
    print(f"  List comprehension:   {list_size:,} bytes (~{list_size / (1024 * 1024):.2f} MB)")
    print(f"  Generator expression: {gen_size:,} bytes (~{gen_size / 1024:.2f} KB)")
    print(f"  Memory savings:       {list_size / gen_size:.1f}x less memory!")

    # Inline syntax: Passing directly into reductions without double parentheses
    # When a generator expression is the ONLY argument to a function, outer parens can be omitted!
    total_squares = sum(x**2 for x in range(1, 11))
    has_negative = any(x < 0 for x in [3, 7, -2, 9, 4])
    all_positive = all(x > 0 for x in [3, 7, 12, 9, 4])
    max_word_len = max(len(w) for w in ["python", "comprehension", "iterator"])
    joined_str = ", ".join(str(x) for x in range(5))

    print(f"sum(x**2 for x in 1..10):       {total_squares}")
    print(f"any(x < 0 for x in values):      {has_negative}")
    print(f"all(x > 0 for x in values):      {all_positive}")
    print(f"max(len(w) for w in words):      {max_word_len}")
    print(f"', '.join(str(x) for x in 0..4): {joined_str}")

    # Generator Exhaustion Gotcha
    # Generators are one-time use iterators!
    single_use_gen = (x * 10 for x in range(3))
    first_sum = sum(single_use_gen)
    second_sum = sum(single_use_gen)  # Already exhausted, yields nothing
    print(f"First sum of generator:          {first_sum}")
    print(f"Second sum after exhaustion:     {second_sum} (Exhausted!)\n")


def demo_nested_comprehensions():
    print("--- 5. Nested Comprehensions & Multi-Loop Flattening ---")

    # Multi-loop list comprehension (flattening a 2D matrix)
    # The Golden Rule: The order of 'for' clauses in the comprehension MATCHES
    # the order of standard nested 'for' loops!
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    # Equivalent nested loops:
    # flattened = []
    # for row in matrix:          <- 1st for
    #     for item in row:        <- 2nd for
    #         flattened.append(item)
    flattened = [item for row in matrix for item in row]
    print(f"Original matrix: {matrix}")
    print(f"Flattened list:  {flattened}")

    # Multi-loop with filtering (e.g. Cartesian product with conditions)
    ranks = ["A", "K", "Q"]
    suits = ["Spades", "Hearts"]
    deck = [f"{r} of {s}" for s in suits for r in ranks]
    print(f"Cartesian product (deck sample): {deck}")

    # Coordinates excluding diagonal (r == c)
    off_diagonal_coords = [(r, c) for r in range(3) for c in range(3) if r != c]
    print(f"Off-diagonal coordinates (r != c): {off_diagonal_coords}")

    # Constructing 2D structures (Comprehension inside a Comprehension)
    # 3x3 Identity Matrix (1 on diagonal, 0 elsewhere)
    identity_matrix = [
        [1 if row == col else 0 for col in range(3)]
        for row in range(3)
    ]
    print("3x3 Identity Matrix:")
    for row in identity_matrix:
        print(f"  {row}")

    # Matrix Transposition: swap rows and columns
    rect_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    num_cols = len(rect_matrix[0])
    transposed = [
        [row[col_idx] for row in rect_matrix]
        for col_idx in range(num_cols)
    ]
    print(f"Original rect matrix ({len(rect_matrix)}x{num_cols}):")
    for r in rect_matrix:
        print(f"  {r}")
    print(f"Transposed matrix ({len(transposed)}x{len(transposed[0])}):")
    for r in transposed:
        print(f"  {r}")

    # Nested dictionary comprehension
    # Multiplication table mapping: outer dict maps factor_a, inner dict maps factor_b -> product
    mult_table = {
        i: {j: i * j for j in range(1, 4)}
        for i in range(1, 4)
    }
    print(f"Nested multiplication table: {mult_table}\n")


def demo_walrus_operator():
    print("--- 6. The Walrus Operator (:=) in Comprehensions ---")

    # Introduced in Python 3.8 (PEP 572).
    # Problem: Avoiding expensive recalculation when you need to both FILTER and TRANSFORM.

    def expensive_transform(n: int) -> int:
        """Simulates an expensive calculation."""
        return (n**3) - (n**2) + 7

    numbers = [1, 2, 3, 4, 5, 6]

    # Without walrus operator:
    # Option A: Call expensive_transform(x) TWICE (wasteful CPU cycles)
    # [expensive_transform(x) for x in numbers if expensive_transform(x) > 50]

    # Option B: Clunky nested single-element iteration
    # [y for x in numbers for y in [expensive_transform(x)] if y > 50]

    # With walrus operator: Assign to 'y' in the if-clause, then use 'y' in the expression!
    filtered_and_computed = [
        y
        for x in numbers
        if (y := expensive_transform(x)) > 50
    ]
    print(f"Values where expensive_transform(x) > 50: {filtered_and_computed}")

    # Another practical example: parsing and reusing regex/string operations
    logs = [
        "ERROR: Disk full",
        "INFO: Service started",
        "WARN: Low memory",
        "ERROR: Connection timed out",
        "DEBUG: Ping 20ms",
    ]
    # Extract only error messages stripped of prefix
    error_messages = [
        msg
        for line in logs
        if line.startswith("ERROR:") and (msg := line.removeprefix("ERROR:").strip())
    ]
    print(f"Extracted error messages: {error_messages}")

    # Scope Behavior Gotcha with Walrus Operator:
    # Regular comprehension variables DO NOT leak to the outer scope in Python 3.
    # HOWEVER, variables bound by the walrus operator (:=) DO leak into the enclosing scope!
    data = [10, 20, 30]
    _ = [val * 2 for val in data]
    print(f"Is 'val' in locals()? {'val' in locals()} (Comprehension variable was isolated)")

    _ = [(leak := item) for item in data]
    print(f"Is 'leak' in locals()? {'leak' in locals()} (Walrus target leaked! Value: {leak})\n")


def demo_common_pitfalls_and_best_practices():
    print("--- 7. Common Pitfalls & Best Practices ---")

    # Pitfall A: Readability & Over-engineering
    # Comprehensions should clarify, not obfuscate.
    # PEP 20: "Readability counts" and "Flat is better than nested".
    # BAD (overly complex, hard to debug):
    # [x.strip() for sublist in data for item in sublist for x in item.split(",") if x.strip().isdigit() and int(x.strip()) > 0]
    # GOOD: Use a clear generator function or traditional loop when complexity grows.

    # Pitfall B: Using comprehensions purely for side effects
    # Comprehensions are designed to CONSTRUCT collections.
    # BAD (allocates an unnecessary list of [None, None, None] in RAM):
    items = ["task_a", "task_b", "task_c"]
    # [print(f"Processing {item}") for item in items]  # Anti-pattern!

    # GOOD: Use a standard for-loop for side effects:
    print("Processing items via idiomatic for-loop (no garbage list created):")
    for item in items:
        print(f"  Processed: {item}")

    # Pitfall C: Late Binding Closures in Comprehensions (Classic Interview Puzzle)
    # Functions created inside comprehensions bind loop variables by REFERENCE, not by value!
    # BAD: All lambdas reference the FINAL value of i (which is 3):
    bad_multipliers = [lambda x: x * i for i in range(4)]
    bad_results = [m(2) for m in bad_multipliers]
    print(f"Late-binding lambdas result with input 2: {bad_results} (All 6s, not [0, 2, 4, 6]!)")

    # FIX: Use default argument binding (i=i) to capture the value at definition time:
    good_multipliers = [lambda x, i=i: x * i for i in range(4)]
    good_results = [m(2) for m in good_multipliers]
    print(f"Fixed lambdas with i=i default argument:  {good_results} (Correct!)")

    # Pitfall D: Modifying the collection being iterated
    # Never mutate the list/dict you are iterating over within the comprehension!
    nums_to_filter = [1, 2, 3, 4, 5]
    # Creating a new list via comprehension is safe because the original is unchanged:
    filtered = [x for x in nums_to_filter if x % 2 != 0]
    print(f"Filtered copy (safe): {filtered}")

    # Pitfall E: Generator slicing
    # Generators cannot be indexed or sliced with [start:stop]
    gen = (x for x in range(10))
    try:
        _ = gen[2:5]  # type: ignore
    except TypeError as e:
        print(f"Direct slicing on generator raises TypeError: {e}")

    # Solution: Use itertools.islice for generator slicing without creating a list
    gen = (x * 10 for x in range(10))
    sliced_gen = list(itertools.islice(gen, 2, 5))
    print(f"Sliced generator via itertools.islice(gen, 2, 5): {sliced_gen}\n")


def main():
    print("========================================")
    print(" PYTHON LEARNING: 05 - COMPREHENSIONS ")
    print("========================================\n")
    demo_list_comprehensions()
    demo_dict_comprehensions()
    demo_set_comprehensions()
    demo_generator_expressions()
    demo_nested_comprehensions()
    demo_walrus_operator()
    demo_common_pitfalls_and_best_practices()
    print("Comprehension concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
