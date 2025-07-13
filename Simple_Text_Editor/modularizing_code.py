import os

def read_file(filename):
  with open(filename, 'r') as file:           
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def get_user_input():
    print('Enter the content to save (type "SAVE" to exit):')
    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)
    return '\n'.join(lines)

def main():
    filename = input('Enter the filename to open or create: ').strip()
    try:
        if os.path.exists(filename):
                print(read_file(filename))
        else:
            write_file(filename, '')

        content = get_user_input()
        write_file(filename, content)
        print(f"Content saved to {filename}")
    except OSError:
        print(f"Error, file could not be open: {filename}")
        return

if __name__ == "__main__":
    main()