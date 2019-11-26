##############################################################
#
# Author: Bren Sapience
# Date: Nov 2019
# Scope: Provide functions around IQ Bot Group Management
#
# Call Examples:
#
#   python3 ./IQBOT_groups.py -s MySession  -o activate -l "_Invoices - Standard - 1" -i "ALL"
#   python3 ./IQBOT_groups.py -s MySession  -o deactivate -l "_Invoices - Standard - 1" -i "2,3"
#   python3 ./IQBOT_groups.py -s MySession  -o deactivate -l "_Invoices - Standard - 1" -i "4"
#
# List Learning instances and related info
# Get learning instance statistics
# Get List of files in validation
#
##############################################################
#!/usr/bin/env python3

import argparse
import sys
sys.path.insert(1, './logics')
import IQBotGroupsLogics

#Allowed Operations - should be lower case

SupportedOperations = ['list','activate','deactivate']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Operation should be available in all modules
    parser.add_argument("-o","--operation", type=str,default = "list", help = "<list>: List Groups,<activate>: activate Groups,<deactivate>: deactivate Groups", dest = "OPERATION")

    parser.add_argument("-s","--session",type=str,default="", help = "<all> Session Name", dest = "sessionname")
    parser.add_argument("-c","--csv",default = False, help = "<list>: Return results in csv format (Default: False)", dest = "CsvOutput")

    parser.add_argument("-i","--grp", type=str,default = "", help = "<activate,deactivate>: \"ALL\" or one Group Number or a list of Groups separated by commas, ex: \"ALL\" or \"4\" or \"2,3\")", dest = "GROUPNUM")
    parser.add_argument("-l","--li", type=str,default = "", help = "<activate,deactivate>: LI Name", dest = "LINAME")

    OPTIONS = parser.parse_args()
    if not OPTIONS.sessionname:
        parser.error('You need to pass parameter -s (--session)')

    #Check that operation is Supported
    if OPTIONS.OPERATION.lower() not in SupportedOperations:
        parser.error('Operation passed (-o) is not supported: '+OPTIONS.OPERATION)

    ###
    # LI list operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[0]: #list Learning Instances
        Err = IQBotGroupsLogics.list_groups(OPTIONS.sessionname,OPTIONS.CsvOutput)
        exit(0)

    ###
    # Activate or deactivate Group operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[1] or OPTIONS.OPERATION.lower() == SupportedOperations[2]:
        Err = IQBotGroupsLogics.change_group(OPTIONS.GROUPNUM,OPTIONS.LINAME,OPTIONS.OPERATION,OPTIONS.sessionname,OPTIONS.CsvOutput)
        exit(0)
