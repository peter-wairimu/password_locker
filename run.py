#!/usr/bin/env python3.6

import random
import json
from locker import Password

print("welcome to password manager,\n\tplease login..")


class credentials:
    '''
    These class accepts account name,username, password.
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


def gen(x):
    chars = "wairimu254"
    pas = ""
    for i in range(x):
        pas += chars[random.randint(0,36)]
    return pas


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

def add():
    account = input("Enter the name of the account.(ie, Facebook,twitter,email)\n>>")
    username =input("Enter your username.\n>>")
    password = input("Enter your password.\n>>")
    details = credentials(account,username,password)
    details.save()
    choose("")

def create():
    account = input("Enter the name of the account(ie,facebook,twitter,email.\n>>>)")
    username =input("Enter your username.\n>>>")
    password = input("Do you want to create a password?(Yes, No)")
    if password == "Yes" or password == "No":
        if password =="Yes":
            length = int(input("How long do you want your password"))
            pas = gen(length)
            print("Your password is:",pas)

        else:
            pas = input("Enter password.\n>>>")

    else:
        print("Invalid")
        create()

    
            








    