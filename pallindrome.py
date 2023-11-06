def is_palindrome(string):
    string = string.lower().replace(" ", "")
    
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return False
    
    return True

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")