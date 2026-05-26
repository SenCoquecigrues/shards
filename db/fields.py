from functools import partial

from .validators import *

class Field:
    def __init__(self, field_name:str, value: any):
        self.value = value
        self.field_name = field_name
        self.validators = []

    def has_errors(self) -> bool:
        error_msgs = {}
        for step in self.validators:
            is_valid = step()
            if not is_valid:
                error_msgs.update({self.field_name: f"Failed {step.func.__name__} validation."})
        return error_msgs

class ReferenceField(Field):
    def __init__(self, value: any):
        super().__init__("reference", value)
        self.validators = [
            partial(is_proper_reference, value=value),
            partial(
                max_length, value=value, max_length=30,
            )
        ]

class StringField(Field):
    def __init__(self, value: any, field_name="string", size=30):
        super().__init__(field_name, value)
        self.validators = [
            partial(
                max_length, value=value, max_length=size,
            )
        ]
