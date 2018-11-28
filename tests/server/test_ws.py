#!/usr/bin/env python3
# runs tests of all of the server functionalities
import os

#test bottles
print("Testing bottles controller...")
os.system('python3.6 test_bottles.py')

#test users
print("Testing users controller...")
os.system('python3.6 test_users.py')

#test reviews
print("Testing reviews controller...")
os.system('python3.6 test_reviews.py')

#test reset
print("Testing reset controller...")
os.system('python3.6 test_reset.py')
