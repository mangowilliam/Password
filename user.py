
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
        save_user method saves user objects into use
        '''

        User.user.append(self)

# class Credentials:
#    """Class that generates new instances of credentials."""
