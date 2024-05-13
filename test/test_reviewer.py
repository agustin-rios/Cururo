import unittest
from .linter_test import LinterTest
from cururo.reviewer import Reviewer

class TestReviewer(LinterTest):
     def setUp(self):
         self.reviewer = Reviewer("api_key", "assistant_id")
         self.reviewer.assisant = None

if __name__ == '__main__':
    unittest.main()