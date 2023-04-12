#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    # Open the file in write mode, creating it if it doesn't exist
    with open(filename, 'w', encoding='utf8') as file:
        # Write the text to the file
        nb_characters = file.write(text)
    # Return the number of characters written
    return nb_characters

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        text = sys.argv[2]
        nb_characters = write_file(filename, text)
        print(f"{nb_characters} characters written to {filename}")
    else:
        print("Usage: ./1-write_file.py <filename> <text>")
