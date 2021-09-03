#!/usr/bin/env python3.6

import random
import json
from sys import pycache_prefix
from locker import Password

print("welcome to password manager,\n\tplease login..")


class credentials:
    '''
    These class accepts account_name,username, password.
    It stores them as a dictionary.

    '''
    def __init__(self,account,username,password):

        self.account = account
        self.username = username
        self.password = password
    
    def save(self):
        f=open("account.text","a")
        f.write(self.account+ "\n")
        f.write(self.username + "\n")
        f.write(self.password + "\n")
        f.close()

class user:
    '''
    These class holds information about the user

    '''
    def __init__(self,data):
        self.data = data 

    def user(self):
        return self.data["user"]

    def password(self):
        return self.data["password"]

def main():
    '''
    These is the main function of the application

    '''
    login("")
    choose("")

def login(a):
    '''
    These is the login function that verifies each and every user

    '''
    if a!= "":
        print(a)
    username = input("username>>> ")
    password = input("password>>> ")
    with open("locker.json","r") as f:
        data = f.read()
        data = json.loads(data)
    user_data = user(data)
    if username == user_data.user():
        if password == user_data.password():
            print("Login successful.\n\tWelcome..")
        else:
            print("Incorrect password")
            login("please try again")

    else:
        print("Incorrect username")
        login("Please try again..")


def choose(a):
    '''
    These function allows the user choose from available option

    '''

    if a!= "":
        print(a)
    x = int(input("What do you want to do:\n\t1. Add an existing account. \n\t2. Create a new account.\n\t3. Delete an account.\n\42.View your accounts.\n>>> "))
    print(x)
    if x == 1:
        add()
    elif x == 2:
        create()
    elif x == 3:
        delete()
    elif x == 4:
        view()
        choose("")
    else:
        choose("Invalid")




    