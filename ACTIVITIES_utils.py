##############################################################
#
# Author: Bren Sapience
# Date: Nov 2019
# Scope: Provide functions around RPA Activity Management
#
# Call Examples:
#
#   python3 ./
#   python3 ./
#
##############################################################

import argparse
import sys
sys.path.insert(1, './logics')
import ActivitiesLogics

#Allowed Operations - should be lower case
SupportedOperations = ['list']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Operation should be available in all modules
    parser.add_argument("-o","--operation", type=str,default = "list", help = "<list>:list existing activities", dest = "OPERATION")
    parser.add_argument("-c","--csv",default = False, help = "Return results in csv format (Default: False)", dest = "CsvOutput")
    parser.add_argument("-s","--session",type=str,default="", help = "<all> Session Name", dest = "sessionname")

    OPTIONS = parser.parse_args()
    if not OPTIONS.sessionname:
        parser.error('You need to pass parameter -s (--session)')

    #Check that operation is Supported
    if OPTIONS.OPERATION.lower() not in SupportedOperations:
        parser.error('Operation passed (-o) is not supported: '+OPTIONS.OPERATION)

    ###
    # list operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[0]: #list

        ActivitiesLogics.list(OPTIONS.sessionname,OPTIONS.CsvOutput)
