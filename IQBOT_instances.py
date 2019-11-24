##############################################################
#
# Author: Bren Sapience
# Date: Nov 2019
# Scope: Provide functions around IQ Bot Management
#
# Call Examples:
#
#   python3 ./IQBOT_instances.py -s MySession -o list
#   python3 ./IQBOT_instances.py -s MySession  -o list_files -t VALIDATION -c True -n "_ Invoices - ML"
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
import IQBotLILogics

#Allowed Operations - should be lower case

SupportedOperations = ['list','list_files','list_groups','show']

# list_groups (LI Name or ID), list_domains, list_files (in success, invalid, unclassified, untrained - LI Name or ID),
# export_lis (list of LI Names or IDs), export_domains (list of names),
# change_group_state (staging or  prod, list of group IDs or Numbers), change_li_state (LI Name or ID),
# get_li_details (LI Name or ID), update_desc (LI Name or ID, Group number of ID),
# download_files (LI Name or ID)

# MIGHT NEED TO SPLIT THIS INTO:
# IQBOT_domains, IQBOT_learninginstances, IQBOT_utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Operation should be available in all modules
    parser.add_argument("-o","--operation", type=str,default = "list", help = "<list>: List LIs, <list_files>: List Files in LI, <list_groups> list Groups in LI, <show> show LI details", dest = "OPERATION")

    parser.add_argument("-i","--id",type=str,default="", help = "<all> Learning Instance ID", dest = "LIID")
    parser.add_argument("-n","--name",type=str,default="", help = "<all> Learning Instance Name", dest = "LINAME")

    parser.add_argument("-t","--status",type=str,default="", help = "<list_files> [''|'VALIDATION','UNCLASSIFIED','INVALID','SUCCESS','UNTRAINED']", dest = "FILESTATUS")

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
        Err = IQBotLILogics.list_learning_instances(OPTIONS.sessionname,OPTIONS.CsvOutput)
        exit(0)

    ###
    # LI Group list operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[2]: #list Files in Learning Instance
        if not OPTIONS.LIID and not OPTIONS.LINAME:
            parser.error('You need to pass parameter -i or -n (--id or --name)')

        if OPTIONS.LINAME:
            IQBotLILogics.list_learning_instance_groups(learningInstanceName=OPTIONS.LINAME,learningInstanceID="",sessionname=OPTIONS.sessionname,CsvOutput=OPTIONS.CsvOutput)

        if OPTIONS.LIID:
            IQBotLILogics.list_learning_instance_groups(learningInstanceName="",learningInstanceID=OPTIONS.LIID,sessionname=OPTIONS.sessionname,CsvOutput=OPTIONS.CsvOutput)


    ###
    # LI File list operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[1]: #list Files in Learning Instance
        if not OPTIONS.LIID and not OPTIONS.LINAME:
            parser.error('You need to pass parameter -i or -n (--id or --name)')
        if not OPTIONS.FILESTATUS:
            OPTIONS.FILESTATUS = ""

        if OPTIONS.LINAME:
            IQBotLILogics.list_learning_instance_files(learningInstanceName=OPTIONS.LINAME,learningInstanceID="",status=OPTIONS.FILESTATUS,sessionname=OPTIONS.sessionname,CsvOutput=OPTIONS.CsvOutput)

        if OPTIONS.LIID:
            IQBotLILogics.list_learning_instance_files(learningInstanceName="",learningInstanceID=OPTIONS.LIID,status=OPTIONS.FILESTATUS,sessionname=OPTIONS.sessionname,CsvOutput=OPTIONS.CsvOutput)


    ###
    # LI Detail operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[3]: #list Files in Learning Instance
        if not OPTIONS.LIID and not OPTIONS.LINAME:
            parser.error('You need to pass parameter -i or -n (--id or --name)')

        if OPTIONS.LINAME:
            IQBotLILogics.get_learning_instance_detail(learningInstanceName=OPTIONS.LINAME,learningInstanceID="",sessionname=OPTIONS.sessionname,CsvOutput=OPTIONS.CsvOutput)

        if OPTIONS.LIID:
            IQBotLILogics.get_learning_instance_detail(learningInstanceName="",learningInstanceID=OPTIONS.LIID,sessionname=OPTIONS.sessionname,CsvOutput=OPTIONS.CsvOutput)
