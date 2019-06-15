
class User:
    """  Class that generates new instances of users."""
    user = []

    def __init__(self, sir_name, other_name, phone, email):
        """ helps define properties of our objects"""
        self.first_name = sir_name
        self.other_name = other_name
        self.phone = phone
        self.email = email


class Credentials:
    """Class that generates new instances of credentials."""

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
