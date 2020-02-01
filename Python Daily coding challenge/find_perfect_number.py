# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.
def perfect_number(n):
    sum_of_digit = 0
    total_val = ""
    for character in str(n):
        digit = int(character)
        sum_of_digit += digit
        total_val += character
    last_digit =  abs(10 - sum_of_digit)
    return None if sum_of_digit > 10 else total_val + str(last_digit)




print(perfect_number(1))
print(perfect_number(5))
print(perfect_number(19))
print(perfect_number(26))
print(perfect_number(49))