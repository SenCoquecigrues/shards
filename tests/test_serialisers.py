# TODO
# TEST3 : block if entry already exists

# if not, then save it
# If not: log the error and the object name (ideally the file number?)
# Log success as well
# Rename file to avoid re-import
# This should be extensively tested
import unittest

from db.serialisers import DomainSerialiser
from db.fields import EntryOfListField, FloatField, IntField, ReferenceField, StringField

class TestSerialisers(unittest.TestCase):
    def test_good_instance(self):
        test_domain = DomainSerialiser(
            "GOOD_REFERENCE", "my_domain", "FORBIDDEN", 1
        )

        is_valid = test_domain.is_valid()
        self.assertEqual(is_valid, {'status': True, 'errorMsgs': []})

    def test_bad_instance(self):
        test_domain = DomainSerialiser(
            "WRONG REFERENCE", "my_domain", "FORBIDDEN", 1
        )

        is_valid = test_domain.is_valid()
        self.assertEqual(
            is_valid,
            {'status': False, 'errorMsgs': {'reference': 'Failed is_proper_reference validation.'}}
        )