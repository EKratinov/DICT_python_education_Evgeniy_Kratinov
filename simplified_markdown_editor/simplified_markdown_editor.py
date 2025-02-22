def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def main():
    print("Choose a formatter or type !help for help")
    while True:
        command = input("Choose a formatter: ")


        if command == "!help":
            print_help()
        elif command == "!done":
            print("Exiting...")
            break
        elif command in ["plain", "bold", "italic", "header", "link", "inline-code",
                         "ordered-list", "unordered-list", "new-line"]:
            print(f"Formatter '{command}' selected (not yet implemented).")
        else:

            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()
