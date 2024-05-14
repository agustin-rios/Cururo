import unittest
from .linter_test import LinterTest
from cururo.util.publisher import Publisher

class TestPublisher(LinterTest):

    def setUp(self):
        self.publisher = Publisher()

    def test_publisher(self):
        self.assertIsInstance(self.publisher, Publisher)
    
    def test_has_publish(self):
        self.assertTrue(hasattr(self.publisher, 'publish'))

    def test_publish(self):
        self.assertTrue(hasattr(self.publisher.publish, '__call__'))

if __name__ == '__main__':
    unittest.main()