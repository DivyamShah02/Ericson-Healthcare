def append_to_file(text):
    with open('log.txt', 'a') as file:
        file.write(text + '\n')

# Example usage:
# append_to_file('path/to/your/file.txt', 'Your text to append')