#! /usr/bin/env python3
import argparse
import os
import random
import string
from src import utils

print(file_service.create_file)


def read_file():
    filename = input("Enter file name : ")
    with open(filename, "r") as f:
        data = f.read()
        print(data)


def create_file():
    filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    content = input("Enter file content : ")
    with open(f"{filename}.txt", "w") as f:
        f.write(content)


def delete_file():
    filename = input("Enter file name : ")
    filename = os.path.abspath(filename)
    os.remove(filename)


def list_dir():
    list_directory = os.listdir()
    print(list_directory)


def change_dir():
    directory = input("Enter dir name : ")
    os.chdir(directory)
    print(f'Working directory is {directory} now')


def get_file_permissions():
    filename = input("Enter file name: ")
    permissions = oct(os.stat(filename).st_mode)
    print(f"File {filename} permissions: {permissions}")


def set_file_permissions():
    filename = input("Enter file name : ")
    permissions = input("Input UNIX permissions in oct format :")
    os.chmod(filename, int(permissions))
    print(f"Set {permissions} to {filename}")


def main():
    parser = argparse.ArgumentParser(description='Restfull file server')
    parser.add_argument('-d', '--directory', help='Working directory', default='./')
    args = parser.parse_args()
    os.chdir(args.directory)
    print(f'Working directory is {os.getcwd()}')
    commands = {
        "read": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir,
        "getperm": get_file_permissions,
        "setperm": set_file_permissions
    }
    while True:
        command = input("Enter command: ")
        if command == "exit":
            return
        if command not in commands:
            print("Unknown command")
            continue
        command = commands[command]
        try:
            command()
        except Exception as ex:
            print(f"Error on {command} execution: {ex} ")


if __name__ == "__main__":
    main()