"""
Concept 06: Unpacking in Python
===============================
Unpacking (also known as destructuring in other languages) is an expressive and
idiomatic Python feature that allows extracting values from iterables or mappings
directly into variables or function arguments without manual indexing or slicing.

Key Mechanisms Covered:
1. Basic Sequence / Iterable Unpacking (1-to-1 variable assignment)
2. Extended Iterable Unpacking (PEP 3132: Starred `*` expressions)
3. Deep / Nested Structural Unpacking
4. Loop & Comprehension Unpacking
5. Function Argument Unpacking (`*args` and `**kwargs`)
6. Collection Literal Unpacking & Merging (PEP 448)
7. Structural Pattern Matching Unpacking (PEP 634: `match / case`)
8. Common Pitfalls, Edge Cases & Best Practices
"""

import itertools
import sys


def demo_basic_iterable_unpacking():
    print("--- 1. Basic Iterable Unpacking (1-to-1 Binding) ---")

    # Unpacking works with ANY iterable on the right-hand side (RHS),
    # matching variables on the left-hand side (LHS) positionally.

    # 1. Tuples and Lists
    point_tuple = (10, 20)
    x, y = point_tuple
    print(f"From tuple (10, 20)       -> x={x}, y={y}")

    colors_list = ["red", "green", "blue"]
    c1, c2, c3 = colors_list
    print(f"From list ['red'...]      -> c1={c1}, c2={c2}, c3={c3}")

    # 2. Strings (each character is an element)
    first_char, second_char, third_char = "XYZ"
    print(f"From string 'XYZ'         -> first={first_char}, second={second_char}, third={third_char}")

    # 3. Ranges and Generators
    r_start, r_mid, r_end = range(3)
    print(f"From range(3)             -> start={r_start}, mid={r_mid}, end={r_end}")

    gen = (n * 10 for n in range(1, 4))
    g1, g2, g3 = gen
    print(f"From generator (1..3 *10) -> g1={g1}, g2={g2}, g3={g3}")

    # 4. Target Syntax Nuance: LHS parentheses and brackets
    # Parentheses or brackets on the LHS are optional syntactic grouping for targets;
    # they unpack the exact same way.
    a, b = [100, 200]
    (t1, t2) = [100, 200]
    [l1, l2] = [100, 200]
    print(f"Syntaxes equivalent       -> a,b: ({a},{b}), (t1,t2): ({t1},{t2}), [l1,l2]: [{l1},{l2}]")

    # 5. The Classic Variable Swap Idiom
    # Python evaluates the ENTIRE right-hand side first (building a temporary tuple),
    # and only then performs assignments from left to right.
    val_a = "Alpha"
    val_b = "Beta"
    print(f"Before swap: val_a={val_a}, val_b={val_b}")
    val_a, val_b = val_b, val_a
    print(f"After swap:  val_a={val_a}, val_b={val_b}")

    # Cyclic rotation of 3 variables
    x1, x2, x3 = 1, 2, 3
    x1, x2, x3 = x2, x3, x1
    print(f"Rotated (1, 2, 3) -> ({x1}, {x2}, {x3})")

    # 6. Unpacking Function Return Values
    def get_user_coordinates():
        # Returning multiple comma-separated values returns a tuple
        return 37.7749, -122.4194

    latitude, longitude = get_user_coordinates()
    print(f"Unpacked return values    -> lat={latitude}, lon={longitude}")

    # 7. Ignoring Values with Underscore (_)
    # By convention, `_` signals a throwaway variable
    name, _, role = ("Alice", "SecretSaltValue", "Admin")
    print(f"Ignoring middle value     -> Name: {name}, Role: {role} (password hash discarded)")

    # 8. ValueError: Mismatched Element Count
    # Exact count matching is enforced if no starred expression is present:
    try:
        n1, n2 = [1, 2, 3]  # Too many values
    except ValueError as e:
        print(f"Too many values error     -> ValueError: {e}")

    try:
        n1, n2, n3 = [1, 2]  # Not enough values
    except ValueError as e:
        print(f"Not enough values error   -> ValueError: {e}\n")


def demo_extended_unpacking():
    print("--- 2. Extended Iterable Unpacking (PEP 3132 - Starred '*') ---")

    # Introduced in Python 3.0 (PEP 3132):
    # A single starred expression `*target` on the LHS can capture any remaining items
    # as a Python LIST.

    # 1. Capturing the tail: head, *tail
    numbers = [10, 20, 30, 40, 50]
    head, *tail = numbers
    print(f"Original: {numbers}")
    print(f"head: {head}, *tail: {tail} (tail type: {type(tail).__name__})")

    # 2. Capturing the lead: *lead, last
    *lead, last = numbers
    print(f"*lead: {lead}, last: {last}")

    # 3. Capturing the middle: first, *middle, last
    first, *middle, last = numbers
    print(f"first: {first}, *middle: {middle}, last: {last}")

    # 4. Multiple fixed targets around star
    first, second, *body, second_to_last, final = range(10)
    print(f"From range(10): first={first}, second={second}, body={body}, second_last={second_to_last}, final={final}")

    # 5. Starred targets ALWAYS produce a list!
    # Even when unpacking a tuple, set, string, or generator:
    text = "Python"
    char_start, *char_mid, char_end = text
    print(f"Unpacking string '{text}':")
    print(f"  char_start: {char_start!r}, *char_mid: {char_mid}, char_end: {char_end!r}")

    # 6. Starred target captures EMPTY LIST when elements match exact counts
    a, *b, c = [1, 2]
    print(f"Unpacking 2 items into a, *b, c: a={a}, *b={b}, c={c} (b is empty list)")

    # 7. Unpacking all elements into a single list with trailing comma
    *all_items, = (1, 2, 3, 4)
    print(f"*all_items, = (1, 2, 3, 4) -> {all_items} (type: {type(all_items).__name__})")

    # 8. Constraint: Only ONE starred expression allowed in assignment target list!
    try:
        compile("*a, *b = [1, 2, 3, 4]", "<string>", "exec")
    except SyntaxError as e:
        print(f"Multiple starred targets -> SyntaxError: {e.msg}")

    # 9. Constraint: Starred assignment target must be in a list or tuple
    try:
        compile("*a = [1, 2, 3]", "<string>", "exec")
    except SyntaxError as e:
        print(f"Lone starred target      -> SyntaxError: {e.msg}")

    # 10. Idiomatic use: Ignoring arbitrary middle items with `*_`
    data_row = ["2026-09-09", "12:34:56", "192.168.1.1", "GET", "/api/v1/status", "200", "412ms"]
    date, time, *_, status, latency = data_row
    print(f"Log parsing with `*_`    -> Date: {date} {time}, Status: {status}, Latency: {latency}\n")


def demo_nested_and_deep_unpacking():
    print("--- 3. Nested & Deep Structural Unpacking ---")

    # Unpacking patterns can mirror arbitrarily nested sequence hierarchies.
    # The structure on the LHS must match the nesting depth on the RHS.

    # 1. Nested Tuples / Lists
    user_record = ("Alice", (37.7749, -122.4194), ("Engineering", "Staff Architect"))
    name, (lat, lon), (department, role) = user_record
    print(f"User Record: {user_record}")
    print(f"  Name: {name}")
    print(f"  Coordinates: Lat={lat}, Lon={lon}")
    print(f"  Organization: {department} / {role}")

    # 2. Combining Nested Unpacking with Starred Expressions
    student_profile = ("Bob", [88, 92, 79, 95, 100], "A")
    name, (*homework_grades, final_exam), grade = student_profile
    print(f"\nStudent Profile: {student_profile}")
    print(f"  Name: {name}")
    print(f"  Homework grades: {homework_grades}")
    print(f"  Final exam score: {final_exam}")
    print(f"  Letter grade: {grade}")

    # 3. Multiple Nested Starred Expressions (at distinct nesting levels)
    # While you cannot have two stars at the same level, you CAN have stars in separate sub-structures!
    nested_batches = ([1, 2, 3, 4], ["a", "b", "c", "d", "e"])
    (first_num, *rest_nums), (first_char, *rest_chars) = nested_batches
    print(f"\nNested batches unpacking:")
    print(f"  first_num: {first_num}, rest_nums: {rest_nums}")
    print(f"  first_char: {first_char}, rest_chars: {rest_chars}")

    # 4. Real-world example: Parsing structured command messages
    incoming_packet = ("CMD_UPLOAD", ("user_42", "session_99"), ("/uploads/report.pdf", 2048, "application/pdf"))
    cmd, (user_id, session_id), (file_path, file_size, mime_type) = incoming_packet
    print(f"\nPacket parsed -> Command: {cmd}, User: {user_id}, File: {file_path} ({file_size} bytes, {mime_type})\n")


def demo_loop_and_comprehension_unpacking():
    print("--- 4. Unpacking in Loops & Comprehensions ---")

    # 1. Unpacking in standard `for` loops
    points = [(0, 0), (2, 3), (5, 8), (10, 12)]
    print("Coordinates iteration:")
    for x, y in points:
        distance_squared = x**2 + y**2
        print(f"  Point ({x}, {y}) -> x^2 + y^2 = {distance_squared}")

    # 2. Dictionary .items() unpacking
    app_settings = {"host": "0.0.0.0", "port": 8080, "workers": 4, "reload": True}
    print("\nDictionary items iteration:")
    for key, val in app_settings.items():
        print(f"  Config '{key}' => {val}")

    # 3. enumerate() unpacking: index + value
    fruits = ["apple", "banana", "cherry"]
    print("\nenumerate() unpacking:")
    for idx, fruit in enumerate(fruits, start=1):
        print(f"  Rank #{idx}: {fruit}")

    # 4. zip() unpacking: multiple simultaneous iterables
    names = ["Alice", "Bob", "Charlie"]
    roles = ["Developer", "Designer", "Manager"]
    levels = ["Senior", "Mid", "Lead"]
    print("\nzip() multi-sequence unpacking:")
    for name, role, level in zip(names, roles, levels):
        print(f"  {name} is a {level} {role}")

    # 5. Starred unpacking directly in `for` loops
    # Useful for jagged or variable-length records
    team_projects = [
        ("Alpha Team", "Alice", "Bob", "Charlie"),
        ("Beta Team", "Dave"),
        ("Gamma Team", "Eve", "Frank"),
    ]
    print("\nStarred unpacking in for-loop header (team, *members):")
    for team, *members in team_projects:
        print(f"  {team} ({len(members)} member{'s' if len(members) != 1 else ''}): {', '.join(members)}")

    # 6. Nested unpacking in `for` loops
    annotated_locations = [
        ("Office", (37.789, -122.401)),
        ("Home", (37.755, -122.443)),
    ]
    print("\nNested unpacking in for-loop header:")
    for label, (lat, lon) in annotated_locations:
        print(f"  {label} located at [{lat:.3f}, {lon:.3f}]")

    # 7. Unpacking in Comprehensions
    users_data = [(1, "alice", "active"), (2, "bob", "suspended"), (3, "carol", "active")]
    active_usernames = [username.upper() for user_id, username, status in users_data if status == "active"]
    user_status_map = {username: status for _, username, status in users_data}
    print(f"\nComprehension unpacking:")
    print(f"  Active usernames: {active_usernames}")
    print(f"  User status map:  {user_status_map}\n")


def demo_function_argument_unpacking():
    print("--- 5. Function Argument Unpacking (*args & **kwargs at Call Sites) ---")

    # Difference between DEFINING and CALLING:
    # `def f(*args, **kwargs):`  -> PACKS multiple arguments into tuple/dict inside function.
    # `f(*iterable, **mapping):` -> UNPACKS elements of iterable/dict into function parameters.

    # 1. Unpacking iterables into positional arguments with `*`
    def calculate_box_volume(length: float, width: float, height: float) -> float:
        return length * width * height

    dimensions_list = [10.0, 5.0, 2.0]
    volume_from_list = calculate_box_volume(*dimensions_list)
    print(f"Dimensions: {dimensions_list}")
    print(f"calculate_box_volume(*dimensions_list) -> {volume_from_list}")

    # Unpacking into built-ins (e.g. range, print, divmod)
    step_params = (1, 10, 2)
    evens_range = list(range(*step_params))
    print(f"range(*{step_params}) -> {evens_range}")

    # The famous zip(*matrix) "unzipping" / transposition idiom
    matrix = [
        (1, "a", True),
        (2, "b", False),
        (3, "c", True),
    ]
    col1, col2, col3 = zip(*matrix)
    print(f"Original matrix: {matrix}")
    print(f"Unzipped with zip(*matrix): col1={col1}, col2={col2}, col3={col3}")

    # 2. Unpacking dictionaries into keyword arguments with `**`
    def create_database_connection(host: str, port: int, database: str, ssl: bool = False) -> str:
        return f"postgresql://{host}:{port}/{database}?ssl={ssl}"

    db_config = {"host": "db.internal.net", "port": 5432, "database": "analytics", "ssl": True}
    conn_str = create_database_connection(**db_config)
    print(f"\nDatabase config dict: {db_config}")
    print(f"create_database_connection(**db_config):")
    print(f"  -> {conn_str}")

    # 3. Combining positional, `*args`, explicit kwargs, and `**kwargs`
    def format_event(category: str, *tags: str, priority: str = "NORMAL", **metadata: str) -> str:
        tag_str = f"[{', '.join(tags)}]" if tags else "[]"
        meta_str = ", ".join(f"{k}={v}" for k, v in metadata.items())
        return f"[{priority}] {category} {tag_str} -> {meta_str}"

    extra_tags = ["security", "auth"]
    context = {"ip": "10.0.0.1", "attempts": "3"}
    event_output = format_event("LOGIN_FAILURE", *extra_tags, priority="HIGH", **context)
    print(f"\nCombined call unpacking:\n  {event_output}")

    # 4. Universal Decorator / Forwarder Pattern
    def inspect_call(func):
        """A simple wrapper demonstrating transparent argument forwarding."""
        def wrapper(*args, **kwargs):
            print(f"  [LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"  [LOG] {func.__name__} returned {result}")
            return result
        return wrapper

    @inspect_call
    def add(a: int, b: int, debug: bool = False) -> int:
        return a + b

    print("\nTransparent forwarding via *args and **kwargs in decorators:")
    add(15, 27, debug=True)

    # 5. Argument Unpacking Gotchas
    # Gotcha A: Non-string keys cannot be unpacked into kwargs
    try:
        def sample_fn(**kwargs): pass
        sample_fn(**{100: "not a string key"})  # type: ignore
    except TypeError as e:
        print(f"\nNon-string key in **kwargs -> TypeError: {e}")

    # Gotcha B: Duplicate parameter collision (keyword provided explicitly AND via **kwargs)
    try:
        def greet(name, greeting="Hello"): return f"{greeting}, {name}"
        greet("Alice", greeting="Hi", **{"greeting": "Hey"})
    except TypeError as e:
        print(f"Duplicate kwarg collision -> TypeError: {e}\n")


def demo_collection_literal_unpacking():
    print("--- 6. Collection Literal Unpacking & Merging (PEP 448) ---")

    # Introduced in Python 3.5 (PEP 448):
    # Allows multiple `*` unpacking inside list/tuple/set literals
    # and multiple `**` unpacking inside dictionary literals.

    # 1. Merging Lists
    list_a = [1, 2, 3]
    list_b = [4, 5]
    merged_list = [*list_a, 999, *list_b, 1000]
    print(f"List A: {list_a}, List B: {list_b}")
    print(f"Merged list [*a, 999, *b, 1000] -> {merged_list}")

    # 2. Merging Tuples
    tup_a = ("a", "b")
    tup_b = ("c", "d")
    merged_tuple = (*tup_a, "x", *tup_b)
    print(f"Merged tuple (*tup_a, 'x', *tup_b) -> {merged_tuple}")

    # 3. Merging Sets (automatic deduplication)
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    merged_set = {*set_a, *set_b, 6}
    print(f"Merged set {{*set_a, *set_b, 6}} -> {sorted(merged_set)}")

    # 4. Converting arbitrary iterables / generators inside literals
    range_elements = [*range(5)]
    generator_chars = {*(ch.upper() for ch in "banana")}
    print(f"[*range(5)] -> {range_elements}")
    print(f"{{*(ch.upper() for ch in 'banana')}} -> {sorted(generator_chars)}")

    # 5. Merging Dictionaries with `**`
    # Golden Rule: Left-to-right evaluation! Later keys OVERWRITE earlier keys.
    base_config = {
        "theme": "light",
        "font_size": 14,
        "show_line_numbers": True,
        "tab_size": 4,
    }

    user_overrides = {
        "theme": "dark",
        "font_size": 16,
    }

    environment_overrides = {
        "tab_size": 2,
    }

    final_config = {
        **base_config,
        **user_overrides,
        **environment_overrides,
        "autosave": True,  # Additional inline setting
    }
    print(f"\nDictionary merging with **:")
    print(f"  Base config:        {base_config}")
    print(f"  User overrides:     {user_overrides}")
    print(f"  Env overrides:      {environment_overrides}")
    print(f"  Merged final config:{final_config}")

    # Comparison: PEP 448 (`{**d1, **d2}`) vs PEP 584 (`d1 | d2` in Python 3.9+)
    via_union_operator = base_config | user_overrides | environment_overrides | {"autosave": True}
    print(f"  Identical via Python 3.9+ '|' union: {final_config == via_union_operator}\n")


def demo_structural_pattern_matching_unpacking():
    print("--- 7. Structural Pattern Matching Unpacking (PEP 634 - Python 3.10+) ---")

    # Structural Pattern Matching (`match / case`) elevates unpacking to declarative
    # data validation and destructuring.

    # 1. Sequence Patterns with exact shapes and wildcards
    def handle_command(command: list[str]) -> str:
        match command:
            case ["quit"]:
                return "Exiting application..."
            case ["help"]:
                return "Showing available commands..."
            case ["load", filename]:
                return f"Loading file: {filename}"
            case ["save", filename, ("--force" | "-f")]:
                return f"Force-saving file: {filename}"
            case ["save", filename]:
                return f"Standard save: {filename}"
            # Starred pattern inside case: matches variable rest of sequence
            case ["filter", column, *values]:
                return f"Filtering '{column}' matching values: {values}"
            case _:
                return f"Unknown command syntax: {command}"

    commands_to_test = [
        ["quit"],
        ["load", "data.csv"],
        ["save", "model.pt", "-f"],
        ["filter", "category", "electronics", "appliances", "books"],
        ["unknown", "foo", "bar"],
    ]
    print("Handling command sequences via match/case:")
    for cmd in commands_to_test:
        print(f"  {cmd} -> {handle_command(cmd)}")

    # 2. Mapping Patterns (destructuring dictionaries) with `**rest`
    def process_api_response(response: dict) -> str:
        match response:
            case {"status": 200, "data": [*records], **extra}:
                return f"Success with {len(records)} records. Extra metadata: {extra}"
            case {"status": 404, "error": msg}:
                return f"Resource Not Found: {msg}"
            case {"status": 500, **details}:
                return f"Server Error encountered: {details}"
            case _:
                return "Unrecognized response format"

    responses = [
        {"status": 200, "data": ["item1", "item2", "item3"], "cached": True, "server": "us-east"},
        {"status": 404, "error": "User with ID 42 does not exist"},
        {"status": 500, "trace_id": "tx_99812", "retries": 3},
    ]
    print("\nHandling API response mappings via match/case:")
    for res in responses:
        print(f"  {res} -> {process_api_response(res)}")

    # 3. Sub-pattern binding with the `as` keyword
    def analyze_geo_shape(shape: tuple) -> str:
        match shape:
            case ("rect", (x, y) as origin, (w, h)):
                return f"Rectangle with origin {origin} and dimensions {w}x{h}"
            case ("circle", (x, y), r) if r > 0:
                return f"Circle at ({x}, {y}) with radius {r}"
            case _:
                return "Invalid geometry"

    print("\nSub-pattern binding with 'as':")
    print(f"  {analyze_geo_shape(('rect', (10, 20), (100, 50)))}")
    print(f"  {analyze_geo_shape(('circle', (0, 0), 15))}\n")


def demo_common_pitfalls_and_best_practices():
    print("--- 8. Common Pitfalls & Best Practices ---")

    # Pitfall A: Unpacking a dictionary directly yields its KEYS, not (key, value) pairs!
    config = {"port": 8080, "host": "localhost"}
    key1, key2 = config
    print(f"Unpacking dict directly: key1={key1!r}, key2={key2!r} (Yielded keys, NOT values!)")
    # Correct approach:
    (k1, v1), (k2, v2) = config.items()
    print(f"Unpacking config.items(): ({k1}={v1}), ({k2}={v2})")

    # Pitfall B: Eager consumption of infinite or massive generators
    # Starred unpacking eagerly exhausts the iterable into a list in RAM!
    def count_from(start: int):
        n = start
        while True:
            yield n
            n += 1

    # DANGEROUS: `first, *rest = count_from(1)` will HANG forever / run out of RAM!
    # Correct approach for streaming / unbounded iterables: use itertools.islice() or next()
    gen = count_from(1)
    first_val = next(gen)
    next_three = list(itertools.islice(gen, 3))
    print(f"\nSafe generator consumption via next() and islice():")
    print(f"  First: {first_val}, Next 3: {next_three}")

    # Pitfall C: Shallow copy semantics in collection unpacking
    # Unpacking into a new literal `[*matrix]` creates a NEW outer list,
    # but nested mutable objects are still references to the SAME objects!
    original_grid = [[1, 2], [3, 4]]
    unpacked_copy = [*original_grid]
    # Mutating an inner element mutates both:
    unpacked_copy[0].append(99)
    print(f"\nShallow unpacking mutation:")
    print(f"  Original grid:  {original_grid} (inner list modified!)")
    print(f"  Unpacked copy:  {unpacked_copy}")

    # Pitfall D: The missing comma in single-starred assignment
    # `*a = [1, 2]` is a SyntaxError.
    # Must be `*a, = [1, 2]` or `[*a] = [1, 2]`.
    *valid_single_starred, = [10, 20, 30]
    print(f"\nSingle starred assignment requires trailing comma: *a, = ... -> {valid_single_starred}")

    # Pitfall E: Readability & Excessive Destructuring
    # While Python allows deep nesting like `a, ((b, *c), d), *e = data`,
    # exceeding 2 levels of nesting is often unreadable and brittle to schema changes.
    # BEST PRACTICE: For deeply nested records, prefer typing.NamedTuple, dataclasses,
    # or clear sequential unpacking with descriptive variable names.
    print("Best practice: Keep unpacking flat and declarative for maximum readability.\n")


def main():
    print("========================================")
    print("   PYTHON LEARNING: 06 - UNPACKING      ")
    print("========================================\n")
    demo_basic_iterable_unpacking()
    demo_extended_unpacking()
    demo_nested_and_deep_unpacking()
    demo_loop_and_comprehension_unpacking()
    demo_function_argument_unpacking()
    demo_collection_literal_unpacking()
    demo_structural_pattern_matching_unpacking()
    demo_common_pitfalls_and_best_practices()
    print("All unpacking concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
