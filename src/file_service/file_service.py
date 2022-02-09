#! /usr/bin/env python3
import argparse
import os.path


def read_file():
    filename = input("Enter file name : ")
    print(f"read file : {filename}")
    # TODO read file and print result


def create_file():
    content = input("Enter file content : ")
    print(f"create_file : {content}")
    # TODO write content to file


def delete_file():
    filename = input("Enter file name : ")
    print(f"delete file : {filename}")
    # TODO delete file


def list_dir():
    print(f"list dir")
    pass
    # Print content of current working directory

def get_file_meta_data(filename):
    """
    Read file creation date, edit date, filesize

    :param filename: filename to read
    :return: tuple (create_date, modification_date, filesize)
    :raises Exception if file not found
    """
    #os.path.getctime - create file time
    #os.path.getmtime - modify file time
    #os.path.getsize()

def change_dir():
    directory = input("Enter dir name : ")
    print(f"change dir : {directory}")
    # Change current working directory


def main():
    # Create argument parser that will retrieve working directory
    commands = {
        "get": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir
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
            print(f"Error on {command} execution : {ex}")


if __name__ == "__main__":
    main()