from .fields import ReferenceField

class Serialiser:
    def __init__(self, reference):
        self.reference = ReferenceField(reference)

    def is_valid(self):
        print("true")


class DomainSerialiser(Serialiser):
    def __init__(self, reference):
        super().__init__(reference=reference)

#"reference", "name", "element", level