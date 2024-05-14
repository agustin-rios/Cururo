import unittest
from cururo.lib.env_modes import EnvModes 

class TestEnvModes(unittest.TestCase):

    def setUp(self):
        self.env_modes = EnvModes(mode='development')

    def test_instance(self):
        self.assertIsInstance(self.env_modes, EnvModes)

    def test_valid_mode(self):
        self.assertEqual(self.env_modes.mode, 'development')
        self.env_modes('testing')
        self.assertEqual(self.env_modes.mode, 'testing')

    def test_invalid_mode(self):
        with self.assertRaises(AssertionError):
            self.env_modes('invalid_mode')

    def test_str_representation(self):
        self.assertEqual(str(self.env_modes), "EnvModes(mode=development)")

    def test_repr_representation(self):
        self.assertEqual(repr(self.env_modes), "EnvModes(mode=development)")

    # def test_non_production_handler(self):
    #     pass # to complete

if __name__ == '__main__':
    unittest.main()
