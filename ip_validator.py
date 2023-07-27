#!/bin/python3
import sys

def split_numbers(ip_address):
    # Split the IP address at the dots
    numbers = ip_address.split('.')
    # Convert each number from string to integer
    numbers = [int(number) for number in numbers]
    return numbers

def check_numbers(numbers):
    # Check if the list has exactly 4 elements
    if len(numbers) != 4:
        return False

    # Check if each element is a number between 0 and 255
    for number in numbers:
        if not 0 <= number <= 255:
            return False

    return True

def main():
    # The first argument is always the script name itself,
    # so we use the second argument (index 1)
    ip_address = sys.argv[1]
    numbers = split_numbers(ip_address)
    is_valid = check_numbers(numbers)
    print(is_valid)

main()
