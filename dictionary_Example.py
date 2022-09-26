# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:28:35 2022

@author: Vincent Medrano
"""

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# can also be like

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# to iterate through a dictionary

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
# to remove a value

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
# del keyword used to remove Johns entry
del phonebook["John"]
print(phonebook)

# or you can pop it off

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
# use the pop keyword
phonebook.pop("John")
print(phonebook)

# Exercise

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

# add Jake to phonebook
phonebook["Jake"] = 938273443
# delete Jill from phonebook  
del phonebook["Jill"]  

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  

