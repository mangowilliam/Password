import unittest

from user import Login, User


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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user = []

    def test_init(self):
        """
        test_init test case to test if each object is initialized correctly
        """
        self.assertEqual(self.new_user.sir_name, "Mango")
        self.assertEqual(self.new_user.other_name, "William")
        self.assertEqual(self.new_user.phone, "0770771045")
        self.assertEqual(self.new_user.email, "juniormango@yahoo.com")

    def test_save_user(self):
        '''
        test_save_contact test case to test if the  object is saved into
         the user
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "0712345678",
                         "test@user.com")  # new contact
        test_user.save_user()
        self.assertEqual(len(User.user), 2)

    def test_delete_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "0712345678",
                         "test@user.com")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user), 1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test", "user", "0711223344", "test@user.com")
        test_user.save_user()

        user_exist = User.user_exist("test@user.com")

        self.assertTrue(user_exist)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(), User.user)

    def test_find_user_by_email(self):
        '''
        test to check if we can find a user by email and display information
        '''

        self.new_user.save_user()
        test_user = User("Test", "user", "0711223344",
                         "test@user.com")  # new contact
        test_user.save_user()

        found_user = User.find_by_email("test@user.com")

        self.assertEqual(found_user.phone, test_user.phone)

    class TestLogin(unittest.TestCase):
        '''
        Test class that defines test cases for the login class behaviours.

        Args:
        unittest.TestCase: TestCase class that helps in creating test login
        '''

        def setUp(self):
            """
            set up method to run before each test case
            """
            self.new_login = Login("changaa", "mbogi")

        def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Login.login_details = []

        def test_init(self):
            """
            test_init test case to test if each object is initialized correctly
            """
            self.assertEqual(self.new_login.login_name, "changaa")
            self.assertEqual(self.new_login.login_password, "mbogi")
            

        def test_save_login(self):
            '''
            test_save_contact test case to test if the  object is saved 
            '''
            self.new_login.save_login() 
            self.assertEqual(len(Login.login_details), 1)
        


if __name__ == '__main__':
    unittest.main()
