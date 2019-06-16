#!/usr/bin/env python3.6
from user import User
def create_user(sname,oname,phone,email):
    '''
    Function to create a new user
    '''
    new_user =User(sname,oname,phone,email)
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
