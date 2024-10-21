from db import connect_db
from get_records import (get_all_author_quotes, get_quotes_by_all_tags,
                         get_quotes_by_tag)


def main():
    while True:
        user_input = input("Enter 'command: value' ")
        command, *value = user_input.split(":")
        match command:
            case "exit":
                break
            case "name":
                get_all_author_quotes(value[0].lstrip())
            case "tag":
                get_quotes_by_tag(value[0].lstrip())
            case "tags":
                get_quotes_by_all_tags(value[0].lstrip().split(","))
            case _:
                print("Invalid command")


if __name__ == "__main__":
    connect_db()
    main()
