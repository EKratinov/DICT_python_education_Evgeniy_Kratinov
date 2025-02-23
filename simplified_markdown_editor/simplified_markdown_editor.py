result = []

def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def format_plain(text):
    return text

def format_bold(text):
    return f"**{text}**"

def format_italic(text):
    return f"*{text}*"

def format_inline_code(text):
    return f"`{text}`"

def format_header(level, text):
    return f"{'#' * level} {text}\n"

def format_link(label, url):
    return f"[{label}]({url})"

def format_new_line():
    return "\n"

def apply_formatter(command):
    if command == "plain":
        text = input("Text: ")
        return text
    elif command == "bold":
        text = input("Text: ")
        return f"**{text}**"
    elif command == "italic":
        text = input("Text: ")
        return f"*{text}*"
    elif command == "inline-code":
        text = input("Text: ")
        return f"`{text}`"
    elif command == "header":
        level = int(input("Level: "))
        if 1 <= level <= 6:
            text = input("Text: ")
            return f"{'#' * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6")
            return None
    elif command == "link":
        label = input("Label: ")
        url = input("URL: ")
        return f"[{label}]({url})"
    elif command == "new-line":
        return "\n"
    elif command in ["ordered-list", "unordered-list"]:
        num_rows = int(input("Number of rows: "))
        if num_rows > 0:
            rows = [input(f"Row #{i + 1}: ") for i in range(num_rows)]
            if command == "ordered-list":
                return "\n".join(f"{i + 1}. {row}" for i, row in enumerate(rows)) + "\n"
            else:
                return "\n".join(f"* {row}" for row in rows) + "\n"
        else:
            print("The number of rows should be greater than zero")
            return None
    else:
        print("Unknown formatting type or command")
        return None

def main():
    print("Choose a formatter or type !help for help")
    while True:
        command = input("Choose a formatter: ")
        if command == "!help":
            print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
            print("Special commands: !help !done")
        elif command == "!done":
            with open("output.md", "w") as file:
                file.write("".join(result))
            print("Result saved to output.md")
            break
        elif command in ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]:
            formatted_text = apply_formatter(command)
            if formatted_text is not None:
                result.append(formatted_text)
                print("".join(result))
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()
