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