#!/bin/bash

SCRIPT_PATH="./ip_validator.py"
ERROR_MSG="The IP address is invalid. Please provide a valid IP address."

# Check if exactly one argument was passed
if [ "$#" -ne 1 ]; then
    echo $ERROR_MSG
    exit 1
fi

# Run the Python script and save the result
result=$(python3 $SCRIPT_PATH $1)

# If the result is "True", ping the server
if [ "$result" == "True" ]; then
    ping -c 4 $1
else
    echo $ERROR_MSG
fi
