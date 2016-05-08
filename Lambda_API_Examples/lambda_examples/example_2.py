from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import string


def to_integer(character):
    """ Converts an ascii character to its alphabetical index integer """

    if character in string.digits:
        return int(character)

    return string.ascii_lowercase.index(character.lower())


def lambda_handler(event, context):
    """ AWS Lambda function call """

    try:
        # Remove any characters that are not digits 0-9
        phone_number = re.sub(
            r'[^0-9]+',
            '',
            event['number']
        )

        phone_total = sum(map(to_integer, phone_number))
        code_total = sum(map(to_integer, event['code']))

        print('PHONE:', event['number'], '->', phone_total)
        print('CODE:', event['code'], '->', code_total)

        result = bool(phone_total == code_total)
    except Exception:
        result = False

    return {'result': result}


