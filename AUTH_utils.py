##############################################################
#
# Author: Bren Sapience
# Date: Nov 2019
# Scope: Provide Authentication functions to AAE
#
# Call Examples:
#
#   python3 ./AUTH_utils.py -o login -l "iqbot" -p "Un1ver\$e" -u "http://100.21.186.147" -s aNewSession
#   python3 ./AUTH_utils.py -o token -s aNewSession -t "sdfgjkh23rjkh3245hjk345jkh324l5jewbrm23kl45jredfk;ewlkthr3jk54" 
#
##############################################################

import argparse
import sys
sys.path.insert(1, './logics')
sys.path.insert(1, './libs')
import AuthLogics
import DataUtils

#Allowed Operations - should be lower case
SupportedOperations = ['login','token','logout','clear','list']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Operation should be available in all modules
    parser.add_argument("-o","--operation", type=str,default = "login", help = "<login>:Perform a Login Request,<token>: get token status,<logout>: logout,<clear>: delete all sessions, <list>: list sessions", dest = "OPERATION")

    # Options for login
    parser.add_argument("-l","--login",type=str,default="", help = "<login> Control Room login", dest = "login")
    parser.add_argument("-p","--password",type=str, default="", help = "<login> Control Room password", dest = "password")
    parser.add_argument("-u","--url",type=str, default="", help = "<login> Base URL to Control Room. Ex: http://100.1.2.3", dest = "url")
    parser.add_argument("-s","--session",type=str,default="", help = "<login> Session Name", dest = "sessionname")

    # Options for token
    parser.add_argument("-t","--token",type=str,default="", help = "<token> authentication token to verify", dest = "token")

    OPTIONS = parser.parse_args()

    #Check that operation is Supported
    if OPTIONS.OPERATION.lower() not in SupportedOperations:
        parser.error('Operation passed (-o) is not supported: '+OPTIONS.OPERATION)

    ###
    # login operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[0]: #login
        if not OPTIONS.login:
            parser.error('You need to pass parameter -l (--login)')
        if not OPTIONS.password:
            parser.error('You need to pass parameter -p (--password)')
        if not OPTIONS.url:
            parser.error('You need to pass parameter -u (--url)')
        if not OPTIONS.sessionname:
            OPTIONS.sessionname = DataUtils.RandomSessionNameGenerator()

        AuthLogics.login(OPTIONS.url,OPTIONS.login,OPTIONS.password,OPTIONS.sessionname)

    ###
    # token check operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[1]: #token
        if not OPTIONS.token:
            parser.error('You need to pass parameter -t (--token)')
        if not OPTIONS.sessionname:
            parser.error('You need to pass parameter -s (--session)')

        AuthLogics.checktoken(OPTIONS.token,OPTIONS.sessionname)

    ###
    # logout operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[2]: #logout
        if not OPTIONS.sessionname:
            parser.error('You need to pass parameter -s (--session)')
        AuthLogics.logout(OPTIONS.sessionname)

    ###
    # clear operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[3]: #clear
        isError = DataUtils.clearSessions()
        if(not isError):
            print("Sessions cleared.")
        else:
            print("An error occured..")

    ###
    # list operation
    ###

    if OPTIONS.OPERATION.lower() == SupportedOperations[4]: #list
        sessionList,isError = DataUtils.listSessions()
        if(not isError):
            print(sessionList)
        else:
            print("An error occured..: "+str(sessionList))
