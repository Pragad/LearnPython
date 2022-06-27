import unittest  # The test framework

import inc_dec  # The code to test


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        print("TESTING 1.")
        self.assertEqual(inc_dec.increment(3), 4)

    # def test_decrement(self):
    #     self.assertEqual(inc_dec.decrement(3), 4)

    # @mock.patch('__main__.')
    # def test_foo():

if __name__ == '__main__':
    unittest.main()
