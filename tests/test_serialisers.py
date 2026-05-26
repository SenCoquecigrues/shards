
# TODO
# TEST3 : block if entry already exists
# TEST3-2 (later?): block if data check fails regarding fields

# if not, then save it
# If not: log the error and the object name (ideally the file number?)
# Log success as well
# Rename file to avoid re-import
# This should be extensively tested
import csv, os, unittest

from db.serialisers import DomainSerialiser
from db.fields import ReferenceField, StringField

class TestSerialisers(unittest.TestCase):
    def test_reference_field(self):
        ref_field = ReferenceField("CORRECT_REFERENCE")
        self.assertEqual(
            ref_field.has_errors(), {}
        )

        ref_field = ReferenceField("FORBIDDEN CHARACTers 3")
        has_errors = ref_field.has_errors()
        self.assertEqual(
            has_errors, {'reference': 'Failed is_proper_reference validation.'}
        )

        ref_field = ReferenceField(
            "THIS_REFERENCE_HAS_NO_FORBIDDEN_CHARACTERS_BUT_IT_IS_FAR_TOO_LONG"
        )
        has_errors = ref_field.has_errors()
        self.assertEqual(
            has_errors, {'reference': 'Failed max_length validation.'}
        )

    def test_string_field(self):
        str_field = StringField('Here! A string :)')
        self.assertEqual(
            str_field.has_errors(), {}
        )

        str_field = StringField("This field is too long ):", size=5)        
        self.assertEqual(
            str_field.has_errors(),
            {'string': 'Failed max_length validation.'}
        )

        str_field = StringField("This field has a name", field_name="name", size=5)        
        self.assertEqual(
            str_field.has_errors(),
            {'name': 'Failed max_length validation.'}
        )