from .fields import EntryOfListField, IntField, ReferenceField, StringField
from utils.global_constants import GlobalConstants

class Serialiser:
    def __init__(self, reference: str):
        self.reference = ReferenceField(reference)

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


class DomainSerialiser(Serialiser):
    def __init__(self, reference: str, name: str, element: str, level: int):
        super().__init__(reference=reference)
        self.name = StringField(value=name, field_name="name", max_size=40)
        self.element = EntryOfListField(value=element, field_name="element", values_list=GlobalConstants.ELEMENTS)
        self.level = IntField(value=level, field_name="level", max_amount=5)