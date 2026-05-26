
import unittest

from db.serialisers import DomainSerialiser
from db.fields import EntryOfListField, FloatField, IntField, ReferenceField, StringField

class TestFields(unittest.TestCase):
    def test_field_name(self):
        with self.assertRaises(ValueError):
            StringField(value="value", field_name="no space allowed")

        with self.assertRaises(ValueError):
            StringField(value="value", field_name="NO_UPPERCASE_ALLOWED")

        with self.assertRaises(ValueError):
            StringField(value="value", field_name="N0_numb3r_4110w3d")

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

        str_field = StringField(
            "This field is too long and has a name):",
            field_name="name_can_be_anything",
            max_size=5
        )
        self.assertEqual(
            str_field.has_errors(),
            {'name_can_be_anything': 'Failed max_length validation.'}
        )

        str_field = StringField("This field's too short ):", min_size=40)
        self.assertEqual(
            str_field.has_errors(),
            {'string': 'Failed min_length validation.'}
        )

    def test_number_fields(self):
        int_field = IntField('1')
        self.assertEqual(
            int_field.has_errors(), {}
        )

        int_field = IntField(-1)
        self.assertEqual(
            int_field.has_errors(), {"int": 'Failed min_amount validation.'}
        )

        int_field = IntField(10, max_amount=5)
        self.assertEqual(
            int_field.has_errors(), {"int": 'Failed max_amount validation.'}
        )

        int_field = IntField(10.5)
        self.assertEqual(
            int_field.has_errors(), {"int": 'Failed is_int validation.'}
        )

        float_field = FloatField(10.5)
        self.assertEqual(
            float_field.has_errors(), {}
        )

        float_field = FloatField(-1, min_amount=-10)
        self.assertEqual(
            float_field.has_errors(), {}
        )

    def test_entry_of_list_field(self):
        test_field = EntryOfListField(value="value", values_list=["Value", "not", "this", "vALue"])
        self.assertEqual(test_field.has_errors(), {})

        test_field = EntryOfListField(
            value="value",
            field_name="another_name",
            values_list=["Value", "not", "this", "vALue"],
            strict_mode=True
        )
        self.assertEqual(test_field.has_errors(), {'another_name': 'Failed is_in_group validation.'})