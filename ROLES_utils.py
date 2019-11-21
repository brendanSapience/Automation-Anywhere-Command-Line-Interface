##############################################################
#
# Author: Bren Sapience
# Date: Nov 2019
# Scope: Provide functions around RPA User Management
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
import RolesLogics

#Allowed Operations - should be lower case
SupportedOperations = ['list']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Operation should be available in all modules
    parser.add_argument("-o","--operation", type=str,default = "list", help = "<list>: list roles", dest = "OPERATION")
    parser.add_argument("-c","--csv",default = False, help = "Return results in csv format (Default: False)", dest = "CsvOutput")

    OPTIONS = parser.parse_args()

    #Check that operation is Supported
    if OPTIONS.OPERATION.lower() not in SupportedOperations:
        parser.error('Operation passed (-o) is not supported: '+OPTIONS.OPERATION)

    ###
    # list operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[0]: #list

        RolesLogics.list(OPTIONS.CsvOutput)
