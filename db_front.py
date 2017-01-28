#!/usr/bin/env python
# ------------
# Esther Schenau
# Start Date: 28Jan2016
# Database Interface for user outreach.
# ------------

"""

Welcome to the outreach tool! The purpose is to create an easy, actionable list of users based on their coverage for outreach purposes.

"""


#SETUP
    #import entries in file to array which will be the WHERE clause
    #entries should take the form of the firm's SFDC, a unique ID
    #will hardcode for now, might be able to tie to a userID later on

#FILE LOADED? Y - proceed, N - error, prompt again

#REQUEST INFO

    #Search by company / ticker for now. (Therapeutic area for later.)

    # What company are you interested in? Enter ticker or name.
    # SELECT clientID, clientFirm, ticker FROM table1, table2 WHERE firmnames in LIST GROUP by firmType HAVING (optional) ORDER DESC contractValue
    # IF nothing found, prompt user to check spelling or shorten to a commonly used version of the company name.
