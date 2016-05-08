from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from lambda_examples.example_2 import lambda_handler


class TestExample1(unittest.TestCase):

    def test_valid(self):
        """
        -> Pass matching number and code arguments
        <- Should return true
        """

        arguments = dict(
            number='(541) 555-4842',
            code='ZS'
        )
        self.assertTrue(lambda_handler(arguments, None)['result'])

    def test_invalid(self):
        """
        -> Pass mismatched number and code arguments
        <- Should return false
        """

        arguments = dict(
            number='612.555.0123',
            code='ABCDEFG'
        )
        self.assertFalse(lambda_handler(arguments, None)['result'])

    def test_illegal_character(self):
        """
        -> Pass code with illegal character
        <- Should return false
        """

        arguments = dict(
            number='612.555.0123',
            code='A@B'
        )

        self.assertFalse(lambda_handler(arguments, None)['result'])


################################################################################
################################################################################

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExample1)
    unittest.TextTestRunner(verbosity=2).run(suite)




