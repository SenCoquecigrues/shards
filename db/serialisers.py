from .fields import EntryOfListField, IntField, ReferenceField, StringField
from utils.global_constants import GlobalConstants

"""
    Serialisers are collection of fields, mapping
    datas to a fixed model. They are used to interact
    with the database: check if datas can be be made 
    into a new table row, initialise the table itself... 
"""
class Serialiser:
    table_name = ""
    def __init__(self, reference: str):
        self.reference = ReferenceField(reference)

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


class DomainSerialiser(Serialiser):
    table_name = "domain"
    def __init__(self, reference: str, name: str, element: str, level: int):
        super().__init__(reference=reference)
        self.name = StringField(value=name, field_name="name", max_size=40)
        self.element = EntryOfListField(
            value=element,
            field_name="element",
            values_list=GlobalConstants.ELEMENTS
        )
        self.level = IntField(value=level, field_name="level", max_amount=5)