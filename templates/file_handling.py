'''file_path = "amazon_kinesis.txt"
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print('File content:\n', content)
except FileNotFoundError:
    print("The file does not exist")'''




f = open("amazon_kinesis.txt","r")
#print(f.read())
print(f.readline())
print(f.readline())


'''file_handle = open("new_file.txt","x")
file_handle.write("hello you can write something")
file_handle.close()'''

file_handle = open("new_file.txt","r")
print(file_handle.read())

file_handle = open("new_file.txt","a")
file_handle.write("python is a simple but is less useful comparison to java")
file_handle.close()
file_handle = open("new_file.txt","r")
print(file_handle.read())