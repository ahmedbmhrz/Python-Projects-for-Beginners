import os

def main():
    filename = input('Enter the filename to open or create: ').strip()
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        else:
            with open(filename, 'w') as file:
                pass
    except OSError:
        print(f"Error opening {filename}")
        return

    print('Enter the content to save (type "SAVE" to exit):')
    content = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        content.append(line)
    
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(content))
            print(f"Content saved to {filename}")
    except OSError:
        print(f"Error saving {filename}")
        return

if __name__ == "__main__":
    main()