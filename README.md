# Automation-Anywhere-Command-Line-Interface
A simple command line interface for Automation Anywhere's RPA and Cognitive Solutions

## How to use it

1. Clone this repository
2. Authenticate (you can pass a Session Name or let it generate one at random):

```
python3 ./AUTH_utils.py -l "admin" -p "myPassword" -u "http://100.1.2.3" -s DevelopmentEnv
```

3. Use any Utility (dont forget to pass the Session Name):

```
python3 ./USERS_utils.py -s DevelopmentEnv -o create -u "test4" -p "mylongpassword" -e "aa@aa.com" -r "10,11"
```

4. Get help and list available parameters using the **-h** option:

```
python3 ./AUTH_utils.py -h
```

## Things to know:

Before you can run any of the commands, you need to **authenticate** using *AUTH_utils.py -o login*:

```
python3 ./AUTH_utils.py -s MySessionName -o login -l "iqbot" -p "myPassword" -u "http://100.1.2.3"
```

The **authentication token** along with the **URL** passed in the authentication call are **stored locally** and **do not need to be passed as parameters beyond the first authentication call**.

The **Session Name** needs to be passed in all calls (it serves to retrieve the URL and Authentication Token dynamically)

Each Utility contains **at least 2 options**: **-s** and **-o**. **-o** is used to specify the **operation to run** (ex: create, list, delete, update, etc.). **-s** is used to specify the **Session Name**.

## Utilities Currently Available:

* AUTH_utils.py: Authentication commands (login, logout, get token info, list sessions, clear sessions)
* ROLES_utils.py: Roles management commands (list)
* DEVICES_utils.py: Devices management commands (list)
* USERS_utils.py: Users management commands (create,set login, list, delete)


## TO DO

add a list of python dependencies
