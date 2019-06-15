import unittest
from user import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        """
        set up method to run before each test case
        """
        self.new_user = User("Mango", "William", "0770771045",
                             "juniormango@yahoo.com")  # new user objects

    def test_init_new_user(self):
        """
        test_init test case to test if each object is initialized correctly
        """
        self.assertEqual(self.new_user.sir_name, "Mango")
        self.assertEqual(self.new_user.other_name, "William")
        self.assertEqual(self.new_user.phone, "0770771045")
        self.assertEqual(self.new_user.email, "juniormango@yahoo.com")

    de


if __name__ == '__main__':
    unittest.main()
