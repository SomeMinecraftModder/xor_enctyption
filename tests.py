import unittest
from xor_encryption import xor


class TestXor(unittest.TestCase):
    def test_xor_encryption(self):
        message = "test".encode()
        a = xor(message, b"key!")
        b = xor(a, b"key!")
        self.assertEqual(message, b)


if __name__ == '__main__':
    unittest.main()
