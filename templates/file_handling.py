file_path = "amazon_kinesis.txt"
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print('File content:\n', content)
except FileNotFoundError:
    print("The file does not exist")