from string_utils import reverse_string
from string_utils import capitalize_string
from string_utils import is_capitalized
import unittest

class TestStringUtils(unittest.TestCase):
  def test_reverse_string(self):
    result = reverse_string('Adrian')
    self.assertEqual(result, 'nairdA')

  def test_capitalize_string(self):
    output = capitalize_string('adrian')
    self.assertEqual(output, 'Adrian')

  def test_is_capitalized(self):
    check = is_capitalized('Adrian')
    self.assertTrue(check)


if __name__ == '__main__':
  unittest.main()