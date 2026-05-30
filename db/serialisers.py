import inspect, sys

from db import fields

from utils.global_constants import GlobalConstants

"""
    Serialisers are collection of fields, mapping
    datas to a fixed model. They are used to interact
    with the database: check if datas can be be made 
    into a new table row, initialise the table itself... 
"""
class BaseSerialiser:
    table_name = ""
    def __init__(self, reference: str):
        self.reference = fields.ReferenceField(reference)

    @classmethod
    def init(cls):
        pass


    def is_valid(self):
        errorMsgs = {}
        for key, value in self.__dict__.items():
            errors = value.has_errors()
            if errors != {}:
                errorMsgs.update(errors)

        if len(errorMsgs.keys()) == 0:
            return {
                "status": True, "errorMsgs": []}
        else:
            return {
                "status": False,
                "errorMsgs": errorMsgs
            }

    def create_new_sql_entry(self):
        if self.is_valid():
            for key, value in self.__dict__.items():
                pass


class DomainSerialiser(BaseSerialiser):
    table_name = "domain"
    def __init__(self, reference: str, name: str, element: str, level: int):
        super().__init__(reference=reference)
        self.name = fields.StringField(value=name, field_name="name", max_size=40)
        self.element = fields.EntryOfListField(
            value=element,
            field_name="element",
            values_list=GlobalConstants.ELEMENTS
        )
        self.level = fields.IntField(value=level, field_name="level", max_amount=5)


def get_all_serialisers():
    current_module = sys.modules[__name__]
    all_used_serialisers = []

    for name, obj in inspect.getmembers(current_module):
#    for name, obj in inspect.getmembers(serialisers):
        if (
            inspect.isclass(obj) and
            obj.__name__.endswith("Serialiser") and
            not obj == BaseSerialiser
        ):
            all_used_serialisers.append(obj)

    return all_used_serialisers