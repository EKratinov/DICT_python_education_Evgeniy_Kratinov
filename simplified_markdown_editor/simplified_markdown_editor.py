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
        return format_plain(text)
    elif command == "bold":
        text = input("Text: ")
        return format_bold(text)
    elif command == "italic":
        text = input("Text: ")
        return format_italic(text)
    elif command == "inline-code":
        text = input("Text: ")
        return format_inline_code(text)
    elif command == "header":
        level = int(input("Level: "))
        if 1 <= level <= 6:
            text = input("Text: ")
            return format_header(level, text)
        else:
            print("The level should be within the range of 1 to 6")
    elif command == "link":
        label = input("Label: ")
        url = input("URL: ")
        return format_link(label, url)
    elif command == "new-line":
        return format_new_line()
    else:
        print("Unknown formatting type or command")
        return None

def main():
    print("Choose a formatter or type !help for help")
    while True:
        command = input("Choose a formatter: ")
        if command == "!help":
            print_help()
        elif command == "!done":
            print("".join(result))
            break
        elif command in ["plain", "bold", "italic", "header", "link", "inline-code", "new-line"]:
            formatted_text = apply_formatter(command)
            if formatted_text is not None:
                result.append(formatted_text)
                print("".join(result))
        else:
            print("Unknown formatting type or command")

if __name__ == "__main__":
    main()
