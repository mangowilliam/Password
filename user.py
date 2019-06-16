import random
class User:
    """  Class that generates new instances of users."""
    user = []

    def __init__(self, sir_name, other_name, phone, email):
        """ helps define properties of our objects"""
        self.sir_name = sir_name
        self.other_name = other_name
        self.phone = phone
        self.email = email

    def save_user(self):
        '''
        save_user method saves user objects into user
        '''

        User.user.append(self)

    def delete_user(self):

        User.user.remove(self)

    @classmethod
    def user_exist(cls, email):
        '''
        Method that checks if a user exists from the user.
        Args:
            sir_nae: sir_name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user:
            if user.email == email:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user

    @classmethod
    def find_by_email(cls, email):
        '''
        Method that takes in an email and returns a user that matches that email.
        Returns :
            user that matches the number.
        '''

        for user in cls.user:
            if user.email == email:
                return user


class Login:
    """  Class that generates new instances of logins."""
    login_details = []

    def __init__(self, login_name, login_password):

        self.login_name = login_name
        self.login_password = login_password
    
