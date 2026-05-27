import re

# NOTE: we put these in alphabetical order

def is_float(value: any) -> bool:
    if type(value) == bool:
        return False 
    try:
        return type(float(value)) == float
    except:
        return False

# Group must be made of values of the same type
def is_in_group(
        value: any,
        values_list: list[any],
        strict_mode=False
    ) -> bool:
    if type(value) == str and strict_mode == False:
        return value.lower() in [entry.lower() for entry in values_list]
    return value in values_list

def is_int(value: any) -> bool:
    if type(value) == bool:
        return False 

    try:
        return str(value).isdigit()
    except:
        return False

def is_proper_field_name(value: str) -> bool:
    pattern = r'[^a-z|_]'
    match = re.search(pattern, value)
    if match:
        return False
    return True

def is_proper_reference(value: str) -> bool:
    pattern = r'[^A-Z|_]'
    match = re.search(pattern, value)
    if match:
        return False
    return True

def max_amount(value: any, max_amount: int) -> bool:
    try:
        return float(value) <= max_amount
    except:
        return False

def max_length(value: any, max_length: int) -> bool:
    return len(value) <= max_length

def min_amount(value: any, min_amount: int) -> bool:
    try:
        return float(value) >= min_amount
    except:
        return False

def min_length(value: any, min_length: int) -> bool:
    return len(value) >= min_length
