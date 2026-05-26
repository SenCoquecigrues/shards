# TEST1 : parsing works and we get the right kind of dict list
# TEST2 : block and return if header is incorrect
# TEST3 : block if json entry already exists
# TEST3-2 (later?): block if data check fails regarding fields
# TEST4 : otherwise, we do get a filled json
# TEST5 :

# get header
# compare to self.header
# from header, set attribute
# return dict to main
# from main: check if dict is in json
# if not, then save it THEN add it to json
# If not: log the error and the object name (ideally the file number?)
# Log success as well
# Rename file to avoid re-import
# This should be extensively tested

import unittest

class TestImportCsv(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')