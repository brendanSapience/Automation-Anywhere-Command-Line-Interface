# Automation-Anywhere-Command-Line-Interface
A simple command line interface for Automation Anywhere's RPA and Cognitive Solutions

## How to use it

1. Clone this repository
2. Run any of the utilities:

```
python3 ./USERS_utils.py -o create -u "test4" -p "mylongpassword" -e "aa@aa.com" -r "10,11"
```

3. Get help and list available parameters using the **-h** option:

```
python3 ./AUTH_utils.py -h
```

## Things to know:

Before you can run any of the commands, you need to **authenticate** using *AUTH_utils.py -o login*:

```
./AUTH_utils.py -o login -l "iqbot" -p "myPassword" -u "http://100.1.2.3"
```

The **authentication token** along with the **URL** passed in the authentication call are **stored locally** and **do not need to be passed as parameters beyond the first authentication call**.

Each Utility contains **at least 1 option**: **-o**. **-o** is used to specify the **operation to run** (ex: create, list, delete, update, etc.)


## TO DO

add a list of python dependencies
