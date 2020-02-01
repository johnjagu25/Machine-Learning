# Kaprekar's Constant is the number 6174. 
# This number is special because it has the property where for any 4-digit number 
# that has 2 or more unique digits, 
# if you repeatedly apply a certain function it always reaches the number 6174.

# This certain function is as follows:
# - Order the number in ascending form and descending form to create 2 numbers.
# - Pad the descending number with zeros until it is 4 digits in length.
# - Subtract the ascending number from the descending number.
# - Repeat.

# Given a number n, find the number of times the function needs to be applied to reach 
# Kaprekar's constant. Here's some starter code:

kaprekar_constant = 6174
def find_kaprekar(val, n = 0):
    if val == kaprekar_constant:
        return n
    string_val = str(val)
    string_val = ((4 - len(string_val)) * "0" ) + string_val
    asc_val = "".join(sorted(string_val))
    dec_val = int(asc_val[::-1])
    asc_val = int(asc_val)
    value = dec_val - asc_val
    return find_kaprekar(value,n+1)


print(find_kaprekar(1000))
print(find_kaprekar(191))
print(find_kaprekar(123))
print(find_kaprekar(78))
