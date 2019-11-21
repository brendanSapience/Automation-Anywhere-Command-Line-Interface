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

import argparse
import sys
sys.path.insert(1, './logics')
import UsersLogics

#Allowed Operations - should be lower case
SupportedOperations = ['create']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Operation should be available in all modules
    parser.add_argument("-o","--operation", type=str,default = "create", help = "<create>: Create a user", dest = "OPERATION")

    parser.add_argument("-u","--username", type=str, help = "<create>: Username", dest = "USERNAME")
    parser.add_argument("-p","--password", type=str, help = "<create>: Password", dest = "PASSWORD")
    parser.add_argument("-d","--description", type=str, help = "<create>: Description", dest = "DESC")
    parser.add_argument("-f","--firstname", type=str, help = "<create>: First Name", dest = "FIRSTNAME")
    parser.add_argument("-l","--lastname", type=str, help = "<create>: Last Name", dest = "LASTNAME")
    parser.add_argument("-e","--email", type=str,default = "aa@aa.com", help = "<create>: User Email", dest = "EMAIL")
    parser.add_argument("-r","--roles", type=str,default = "", help = "<create>: list of role IDs to assign (ex: \"1,3,4\")", dest = "ROLES")

    OPTIONS = parser.parse_args()

    #Check that operation is Supported
    if OPTIONS.OPERATION.lower() not in SupportedOperations:
        parser.error('Operation passed (-o) is not supported: '+OPTIONS.OPERATION)

    ###
    # create operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[0]: #list
        if not OPTIONS.USERNAME:
            parser.error('You need to pass parameter -u (--username)')
        if not OPTIONS.PASSWORD:
            parser.error('You need to pass parameter -p (--password)')
        if not OPTIONS.EMAIL:
            parser.error('You need to pass parameter -e (--email)')

        UsersLogics.create(OPTIONS.USERNAME,OPTIONS.PASSWORD,OPTIONS.EMAIL,OPTIONS.ROLES,OPTIONS.DESC,OPTIONS.FIRSTNAME,OPTIONS.LASTNAME)
