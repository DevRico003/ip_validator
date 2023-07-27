# IP Address Validator

## Overview
This repository contains two scripts for validating an IP address and pinging it if it's valid. It consists of:

1. `ip_validator.py`: A Python script that validates if the provided IP address is within the valid range (0.0.0.0 to 255.255.255.255). 

2. `ip_validator.sh`: A Bash script that uses `ip_validator.py` to check the validity of an IP address, and pings it if it's valid. 

## Requirements
- Python 3
- Bash Shell

## Usage
### Python script
To use the Python script, you should pass the IP address as an argument when you call the script. For example:

```
python3 ip_validator.py 192.168.1.1
```

This will print `True` if the IP address is valid, and `False` otherwise.

### Bash script
The Bash script should also be called with an IP address as an argument:

```
bash ip_validator.sh 192.168.1.1
```

This script will check if the IP address is valid. If it's valid, it will attempt to ping the IP address. If it's not valid, it will print an error message.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.