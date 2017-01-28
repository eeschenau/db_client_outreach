
#!/usr/bin/env python
# ------------
# Esther Schenau
# Start Date: 28Jan2016
# Database Interface for user outreach. Function document.
# ------------
"""
Requesting search methodology.
"""
def req_info ():
    s = int(input("Do you want to search for users to reach out to via:\n[1] ticker\n[2] name\n[3] quit \nPlease type selection and hit enter. \n"))
    if s not in (1,2,3):
        return req_info()
