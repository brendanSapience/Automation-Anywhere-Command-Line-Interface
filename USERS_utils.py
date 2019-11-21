##############################################################
#
# Author: Bren Sapience
# Date: Nov 2019
# Scope: Provide functions around RPA User Management
#
# Call Examples:
#
#   python3 ./USERS_utils.py -o create -u test4 -p mylongpassword -e aa@aa.com -r "10,11"
#
#
##############################################################
#!/usr/bin/env python3

import argparse
import sys
sys.path.insert(1, './logics')
import UsersLogics

#Allowed Operations - should be lower case
SupportedOperations = ['create','setlogin','list','delete']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Operation should be available in all modules
    parser.add_argument("-o","--operation", type=str,default = "list", help = "<list>: List existing Users, <create>: Create a user, <setlogin>: set OS Credentials", dest = "OPERATION")

    parser.add_argument("-u","--username", type=str, help = "<create & setlogin & delete>: Username (ex: \"linus\") or list of Usernames (ex: \"linus,carly,yli\")", dest = "USERNAME")
    parser.add_argument("-p","--password", type=str, help = "<create>: Password", dest = "PASSWORD")
    parser.add_argument("-d","--description", type=str, help = "<create>: Description", dest = "DESC")
    parser.add_argument("-f","--firstname", type=str, help = "<create>: First Name", dest = "FIRSTNAME")
    parser.add_argument("-l","--lastname", type=str, help = "<create>: Last Name", dest = "LASTNAME")
    parser.add_argument("-e","--email", type=str,default = "aa@aa.com", help = "<create>: User Email", dest = "EMAIL")
    parser.add_argument("-r","--roles", type=str,default = "", help = "<create>: list of role IDs to assign (ex: \"1,3,4\")", dest = "ROLES")
    parser.add_argument("-s","--session",type=str,default="", help = "<all> Session Name", dest = "sessionname")

    parser.add_argument("-n","--loginusername", type=str,default = "", help = "<setlogin>: OS Login to register under username", dest = "LOGINUSER")
    parser.add_argument("-w","--loginpassword", type=str,default = "", help = "<setlogin>: OS Password to register under username", dest = "LOGINPWD")

    parser.add_argument("-c","--csv",default = False, help = "<list>: Return results in csv format (Default: False)", dest = "CsvOutput")

    OPTIONS = parser.parse_args()
    if not OPTIONS.sessionname:
        parser.error('You need to pass parameter -s (--session)')

    #Check that operation is Supported
    if OPTIONS.OPERATION.lower() not in SupportedOperations:
        parser.error('Operation passed (-o) is not supported: '+OPTIONS.OPERATION)

    ###
    # delete operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[3]: #delete
        if not OPTIONS.USERNAME:
            parser.error('You need to pass parameter -u (--username)')

        UsersLogics.delete(OPTIONS.sessionname,OPTIONS.USERNAME)


    ###
    # list operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[2]: #list
        UsersLogics.list(OPTIONS.sessionname,OPTIONS.CsvOutput)

    ###
    # create operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[0]: #create
        if not OPTIONS.USERNAME:
            parser.error('You need to pass parameter -u (--username)')
        if not OPTIONS.PASSWORD:
            parser.error('You need to pass parameter -p (--password)')
        if not OPTIONS.EMAIL:
            parser.error('You need to pass parameter -e (--email)')

        UsersLogics.create(OPTIONS.sessionname,OPTIONS.USERNAME,OPTIONS.PASSWORD,OPTIONS.EMAIL,OPTIONS.ROLES,OPTIONS.DESC,OPTIONS.FIRSTNAME,OPTIONS.LASTNAME)

    ###
    # setlogin operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[1]: #setlogin
        if not OPTIONS.USERNAME:
            parser.error('You need to pass parameter -u (--username)')
        if not OPTIONS.LOGINUSER:
            parser.error('You need to pass parameter -n (--loginusername)')
        if not OPTIONS.LOGINPWD:
            parser.error('You need to pass parameter -w (--loginpassword)')

        UsersLogics.setlogin(OPTIONS.sessionname,OPTIONS.USERNAME,OPTIONS.LOGINUSER,OPTIONS.LOGINPWD)
