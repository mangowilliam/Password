import random
import string
class User:
    """  Class that generates new instances of users."""
    user = []

    def __init__(self, sir_name, other_name, phone, email,login_name,login_password):
        """ helps define properties of our objects"""
        self.sir_name = sir_name
        self.other_name = other_name
        self.phone = phone
        self.email = email
        self.login_name=login_name
        self.login_password=login_password

    def save_user(self):
        '''
        save_user method saves user objects into user
        '''

        User.user.append(self)

    def delete_user(self):
        '''
        method that deletes user
        '''

        User.user.remove(self)

    @classmethod
    def user_exist(cls, email):
        '''
        Method that checks if a user exists from the users.
        Args:
            email: uses user email to search if it exists
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
        method that returns all the users
        '''
        return cls.user

    @classmethod
    def find_by_email(cls, email):
        '''
        Method that takes in an email and returns a user that matches that email.
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
    
    def save_login(self):
        '''
        Method that saves a user's login details 
        '''
        Login.login_details.append(self)
    @classmethod
    def generate_password(size = 9, chars=string.ascii_letters + string.digits + string.punctuation):
        '''
        Method that generates a random password
        '''
        # Length of the generated password == 9
        return ''.join( random.choice(chars) for _ in range(9) )
        
    @classmethod
    def log_in(cls, login_name, login_password):
        '''
        Method that allows a user to log into their details
        Args:
            login name : username of the user
            password : password for the user
        '''
        for user in cls.login_details:
            if user.login_name == login_name and user.login_password == login_password:
                return Login.login_details

        return False
