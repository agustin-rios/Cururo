import unittest


class LinterTest(unittest.TestCase):

    def asssertWarning(self, warningsA, warningsB):
        self.assertEqual(len(warningsA), len(warningsB), 'The number of warnings do not match')
        for x, y in zip(warningsA, warningsB):
            self.assertEqual(x.__str__(), y.__str__())
