#!/usr/bin/env python3.6
from user import User
from user import Login


def create_user(sname, oname, phone, email):
    '''
    Function to create a new user
    '''
    new_user = User(sname, oname, phone, email)
    return new_user


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def delete_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()


def check_existing_user(email):
    '''
    Function that check if a contact exists with that email and return a Boolean
    '''
    return User.user_exist(email)


def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()


def find_user(email):
    '''
    Function that finds a user by email and returns the user
    '''
    return User.find_by_email(email)

def create_login(login_name, login_password):
    '''
    Function to create a login account
    '''

    new_login = Login(login_name,login_password)

    return new_login

def save_login(login):
    '''
    Function to save a login account
    '''
    login.save_login()
def log_in(login_name, login_password):
    '''
    Function that allows a user to log into their credential account

    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = Login.log_in(login_name, login_password)
    if log_in != False:
        return Login.log_in(login_name, login_password)
def create_generated_password(name):
    '''
    Function that generates a password for the user 

    Args:
        name : the name of the account
    '''
    password = Login.generate_password()

    return password



def main():
    print("Hello Welcome. What is your name?")
    sir_name = input()

    print(f"Hello {sir_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a new user, du - display user, dus - delete a user, ex -exit the user, fu - find user")

        short_code = input().lower()

        if short_code == 'cu':
            print("new user")
            print("-" * 10)

            print("sir name....")
            sir_name = input()

            print("other name...")
            other_name = input()

            print("Phone number ...")
            phone = input()

            print("Email address ...")
            email = input()

            # create and save new user.
            save_user(create_user(
                sir_name, other_name, phone, email))
            print('\n')
            print(f"New Contact {sir_name} {other_name} created")
            print('\n')

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all your contact users")
                print('\n')

                for user in display_users():
                    print(
                        f"{user.sir_name} {user.other_name} .....{user.phone} {user.email}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')

        elif short_code == 'fu':

            print("Enter the email of the user")

            search_user = input()
            if check_existing_user(search_user):
                search_user = find_user(search_user)
                print(f"{search_user.sir_name} {search_user.other_name}")
                print('-' * 20)

                print(f"Phone....{search_user.phone}")
                print(f"email ...{search_user.email}")
            else:
                print("user not saved")

        elif short_code == 'dus':
            print("Enter the email for the user you want to delete")
            search_user = input()
            if check_existing_user(email):
                search_user = find_user(email)
                delete_user(search_user)
                print("user deleted")
            else:
                print('no such user')
                print('\t')

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("you can start again")


if __name__ == '__main__':

    main()
