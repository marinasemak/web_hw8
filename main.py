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
                name_value = value[0].lstrip()
                result = get_all_author_quotes(name_value)
                print(f"Quotes for name '{name_value}':")
                print(result)
            case "tag":
                tag_value = value[0].lstrip()
                result = get_quotes_by_tag(tag_value)
                print(f"Quotes for tag '{tag_value}':")
                print(result)
            case "tags":
                tags_value = value[0].lstrip().split(",")
                result = get_quotes_by_all_tags(tags_value)
                print(f"Quotes for tags {tags_value}:")
                print(result)
            case _:
                print("Invalid command")


if __name__ == "__main__":
    connect_db()
    main()
