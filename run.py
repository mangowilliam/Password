#!/usr/bin/env python3.6
from user import User


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


def main():
    print("Hello Welcome. What is your name?")
    sir_name = input()

    print(f"Hello {sir_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a new user, du - display user, ex -exit the user ")

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
                print("You dont seem to have any contacts saved yet")
                print('\n')

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("you can start again")
if __name__ == '__main__':

    main()