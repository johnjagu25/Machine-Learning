def find_palindrome(val):
    return val if val == val[::-1] else -1

print(find_palindrome('malayalam'))