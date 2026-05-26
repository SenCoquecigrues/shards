import re

# NOTE: we put these in alphabetical order

def is_proper_reference(value):
    pattern = r'[^A-Z|_]'
    match = re.search(pattern, value)
    if match:
        return False
    return True

def max_length(value, max_length):
    return len(value) <= max_length

def min_length(value, min_length):
    return len(value) >= min_length