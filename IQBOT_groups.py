##############################################################
#
# Author: Bren Sapience
# Date: Nov 2019
# Scope: Provide functions around IQ Bot Management
#
# Call Examples:
#
#   python3 ./IQBOT_instances.py -s MySession -o list
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

SupportedOperations = ['list']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Operation should be available in all modules
    parser.add_argument("-o","--operation", type=str,default = "list", help = "<list>: List LIs", dest = "OPERATION")

    parser.add_argument("-s","--session",type=str,default="", help = "<all> Session Name", dest = "sessionname")
    parser.add_argument("-c","--csv",default = False, help = "<list>: Return results in csv format (Default: False)", dest = "CsvOutput")

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
