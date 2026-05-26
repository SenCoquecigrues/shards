import re

# NOTE: we put these in alphabetical order

def is_float(value):
    if type(value) == bool:
        return False 
    try:
        return float(value)
    except: False

# Group must be made of values of the same type
def is_in_group(value: any, values_list: list[any], strict_mode=False):
    if type(value) == str and strict_mode == False:
        return value.lower() in [entry.lower() for entry in values_list]
    return value in values_list

def is_int(value):
    if type(value) == bool:
        return False 

    try:
        return str(value).isdigit()
    except:
        return False

def is_proper_reference(value):
    pattern = r'[^A-Z|_]'
    match = re.search(pattern, value)
    if match:
        return False
    return True

def max_amount(value, max_amount):
    try:
        return float(value) <= max_amount
    except:
        return False

def max_length(value, max_length):
    return len(value) <= max_length

def min_amount(value, min_amount):
    try:
        return float(value) >= min_amount
    except:
        return False

def min_length(value, min_length):
    return len(value) >= min_length
