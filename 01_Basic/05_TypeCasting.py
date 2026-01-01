# Type Casting in python 

# Implicit casting (automatic)
x = 5       # int
y = 2.5     # float
result = x + y  # Python automatically converts int to float
print(f"5 + 2.5 = {result} (type: {type(result).__name__})")

# Explicit casting (manual)
a = int(3.14)
print(f"int(3.14) = {a}")

print("\n" + "=" * 60)
print("2. CONVERTING TO INT")
print("=" * 60)

print(f"int(3.14) = {int(3.14)}")           # Truncates, doesn't round!
print(f"int(3.99) = {int(3.99)}")           # Still 3, not 4!
print(f"int('42') = {int('42')}")           # String to int
print(f"int(True) = {int(True)}")           # True = 1
print(f"int(False) = {int(False)}")         # False = 0

# This will cause an error:
try:
    print(int("3.14"))
except ValueError as e:
    print(f"int('3.14') → Error: {e}")

# Workaround: convert to float first
print(f"int(float('3.14')) = {int(float('3.14'))}")

print("\n" + "=" * 60)
print("3. CONVERTING TO FLOAT")
print("=" * 60)

print(f"float(5) = {float(5)}")
print(f"float('3.14') = {float('3.14')}")
print(f"float(True) = {float(True)}")
print(f"float('inf') = {float('inf')}")     # Infinity

print("\n" + "=" * 60)
print("4. CONVERTING TO STRING (works with almost anything)")
print("=" * 60)

print(f"str(42) = '{str(42)}'")
print(f"str(3.14) = '{str(3.14)}'")
print(f"str([1, 2, 3]) = '{str([1, 2, 3])}'")
print(f"str({{'a': 1}}) = '{str({'a': 1})}'")
print(f"str(None) = '{str(None)}'")

print("\n" + "=" * 60)
print("5. CONVERTING TO BOOL")
print("=" * 60)

print(f"bool(1) = {bool(1)}")               # True
print(f"bool(0) = {bool(0)}")               # False (only 0 is False)
print(f"bool(-1) = {bool(-1)}")             # True (any non-zero)
print(f"bool('') = {bool('')}")             # False (empty string)
print(f"bool('hello') = {bool('hello')}")   # True (non-empty)
print(f"bool([]) = {bool([])}")             # False (empty list)
print(f"bool([1, 2]) = {bool([1, 2])}")     # True (non-empty)
print(f"bool(None) = {bool(None)}")         # False

print("\n" + "=" * 60)
print("6. COLLECTION CONVERSIONS")
print("=" * 60)

# String to list
print(f"list('hello') = {list('hello')}")

# List to tuple
print(f"tuple([1, 2, 3]) = {tuple([1, 2, 3])}")

# List to set (removes duplicates)
print(f"set([1, 2, 2, 3]) = {set([1, 2, 2, 3])}")

# List of tuples to dict
print(f"dict([('a', 1), ('b', 2)]) = {dict([('a', 1), ('b', 2)])}")

# Tuple to list
print(f"list((1, 2, 3)) = {list((1, 2, 3))}")

print("\n" + "=" * 60)
print("7. HANDLING CONVERSION ERRORS")
print("=" * 60)

def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        return f"Cannot convert '{value}' to int"
    except TypeError:
        return f"Invalid type for conversion: {type(value).__name__}"

print(f"safe_int_convert('42') = {safe_int_convert('42')}")
print(f"safe_int_convert('abc') = {safe_int_convert('abc')}")
print(f"safe_int_convert([1, 2]) = {safe_int_convert([1, 2])}")

print("\n" + "=" * 60)
print("8. DATA LOSS IN CONVERSIONS")
print("=" * 60)

original = 3.99
converted = int(original)
print(f"float {original} → int {converted} (lost .99)")

original_list = [1, 1, 2, 2, 3]
converted_set = set(original_list)
print(f"list {original_list} → set {converted_set} (lost duplicates)")

print("\n" + "=" * 60)
print("9. ROUNDING vs TRUNCATING")
print("=" * 60)

value = 3.7
print(f"int({value}) = {int(value)} (truncates)")
print(f"round({value}) = {round(value)} (rounds)")
print(f"int(round({value})) = {int(round(value))} (round then convert)")

print("\n" + "=" * 60)
print("10. SPECIAL CASES")
print("=" * 60)

# Binary, octal, hex to int
print(f"int('1010', 2) = {int('1010', 2)} (binary to int)")
print(f"int('FF', 16) = {int('FF', 16)} (hex to int)")
print(f"int('77', 8) = {int('77', 8)} (octal to int)")

# Int to binary, octal, hex strings
print(f"bin(10) = '{bin(10)}'")
print(f"oct(10) = '{oct(10)}'")
print(f"hex(255) = '{hex(255)}'")