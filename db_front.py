#!/usr/bin/env python
# ------------
# Esther Schenau
# Start Date: 28Jan2016
# Database Interface for user outreach.
# ------------
from db_func import *
#-------------
print ("\n\n\nWelcome to the outreach tool! The purpose is to create an easy, actionable list of users based on their coverage for outreach purposes.\n")
#SETUP
    #import entries in file to array which will be the WHERE clause
    #entries should take the form of the firm's SFDC, a unique ID
    #will hardcode for now, might be able to tie to a userID later on

#FILE LOADED? Y - proceed, N - error, prompt again

#REQUEST INFO

req_info()

#RETURN INFORMATION
    #list of clientID, clientFIRM, clientType, clientPhone, clientEmail
    #do you want to downloaad? YES - return a .csv file
