def is_palindrome(s):
    return s == s[::-1]
string = input('Enter your words :')
if is_palindrome(string):
    print('The String is palindrome')
else:
    print('The string is not palindrome')