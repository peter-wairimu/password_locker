#!/usr/bin/env python3.6
import random
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
    if a! = "":
        print(a)
    username = input("username>>> ")
    password = input("password>>> ")
    with open("locker.py","r") as f:
        data = f.read()
        data = py.loads(data)
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

    if a != "":
        print(a)




    