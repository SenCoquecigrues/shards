from functools import partial

from .validators import *

# TODO: later: implement a validator for None value
class BaseField:
    sql_datatype = "" # indicate the data type in SQL
    def __init__(self, field_name:str, value: any, is_unique=False):
        self.value = value
        if not is_proper_field_name(field_name):
            error_msg = f"Field name {field_name} is not proper field name"
            raise ValueError(error_msg)
        self.field_name = field_name
        self.validators = []
        self.is_unique = is_unique

    def has_errors(self) -> dict:
        error_msgs = {}
        for step in self.validators:
            is_valid = step()
            if not is_valid:
                error_msgs.update({self.field_name: f"Failed {step.func.__name__} validation."})
        return error_msgs

    def __repr__(self):
        return f"Field {self.field_name}: {self.value}"

class ReferenceField(BaseField):
    sql_datatype = "STR"
    def __init__(self, value: any):
        super().__init__("reference", value, is_unique=True)
        self.validators = [
            partial(is_proper_reference, value=value),
            partial(
                max_length, value=value, max_length=30,
            )
        ]

class StringField(BaseField):
    sql_datatype = "STR"
    def __init__(self, value: any, field_name="string", min_size=0, max_size=30):
        super().__init__(field_name, value)
        self.validators = [
            partial(
                max_length,
                value=value, max_length=max_size,
            ),
            partial(
                min_length,
                value=value, min_length=min_size,
            )
        ]

class NumberField(BaseField):
    def __init__(self, value: any, field_name="number", floor=0, ceiling=100):
        super().__init__(field_name, value)
        self.validators = [
            partial(
                max_amount,
                value=value,
                max_amount=ceiling,
            ),
            partial(
                min_amount,
                value=value,
                min_amount=floor,
            )
        ]

class IntField(NumberField):
    sql_datatype = "INT"

    def __init__(self, value: any, field_name="int", min_amount=0, max_amount=100):
        super().__init__(value, field_name, min_amount, max_amount)
        self.validators.insert(0, 
            partial(
                is_int,
                value=value
            ),
        )

class FloatField(NumberField):
    sql_datatype = "FLOAT"

    def __init__(self, value: any, field_name="float", min_amount=0, max_amount=100):
        super().__init__(value, field_name, min_amount, max_amount)
        self.validators.insert(0, 
            partial(
                is_float,
                value=value
            ),
        )

"""
    Check that value is also inside a chosen group
"""
class EntryOfListField(BaseField):
    sql_datatype = "STR"

    def __init__(self,
         value: any,
         field_name="entry_of_list",
         values_list=[],
         strict_mode=False
     ):
        super().__init__(field_name, value)
        self.validators = [ 
            partial(
                is_in_group,
                value=value,
                values_list=values_list,
                strict_mode=strict_mode
            ),
        ]